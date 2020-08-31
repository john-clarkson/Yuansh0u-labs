RP/0/0/CPU0:XR-P2#sh running-config 
Tue Nov 28 12:59:16.397 UTC
Building configuration...
!! IOS XR Configuration 6.0.1
!! Last configuration change at Tue Nov 28 10:25:33 2017 by cisco
!
hostname XR-P2
vrf B
 address-family ipv4 unicast
  import route-target
   2:2
  !
  export route-target
   2:2
  !
 !
!
ipv4 unnumbered mpls traffic-eng Loopback0
interface Loopback0
 ipv4 address 100.64.1.2 255.255.255.255
!
interface MgmtEth0/0/CPU0/0
 shutdown
!
interface GigabitEthernet0/0/0/0.12
 ipv4 address 169.254.12.2 255.255.255.0
 encapsulation dot1q 12
!
interface GigabitEthernet0/0/0/0.201
 vrf B
 ipv4 address 169.254.200.254 255.255.255.0
 encapsulation dot1q 201
!
interface GigabitEthernet0/0/0/0.222
 ipv4 address 169.254.222.22 255.255.255.0
 encapsulation dot1q 222
!
interface GigabitEthernet0/0/0/1
 shutdown
!
interface GigabitEthernet0/0/0/2
 shutdown
!
route-policy PASS
  pass
end-policy
!
router isis fuck
 is-type level-2-only
 net 49.0001.0000.0002.00
 log adjacency changes
 address-family ipv4 unicast
  metric-style wide
  mpls traffic-eng level-2-only
  mpls traffic-eng router-id Loopback0
  segment-routing mpls
 !
 interface Loopback0
  passive
  address-family ipv4 unicast
   prefix-sid index 2
  !
 !
 interface GigabitEthernet0/0/0/0.12
  point-to-point
  address-family ipv4 unicast
   fast-reroute per-prefix
   fast-reroute per-prefix ti-lfa
  !
 !
 interface GigabitEthernet0/0/0/0.222
  point-to-point
  address-family ipv4 unicast
   fast-reroute per-prefix
   fast-reroute per-prefix ti-lfa
  !
 !
!
router bgp 9000
 bgp router-id 100.64.1.2
 address-family vpnv4 unicast
 !
 neighbor 100.64.1.4
  remote-as 9000
  update-source Loopback0
  address-family vpnv4 unicast
  !
 !
 neighbor 100.64.1.6
  remote-as 9000
  update-source Loopback0
  address-family vpnv4 unicast
  !
 !
 vrf B
  rd 2:2
  address-family ipv4 unicast
  !
  neighbor 169.254.200.1
   remote-as 65522
   address-family ipv4 unicast
    route-policy PASS in
    route-policy PASS out
   !
  !
 !
!
mpls traffic-eng
 pce
  peer source ipv4 100.64.1.2
  peer ipv4 150.1.255.253
  !
  segment-routing
  logging events peer-status
  stateful-client
   instantiation
  !
 !
 auto-tunnel pcc
  tunnel-id min 1 max 99
 !
 reoptimize timers delay installation 0
!
segment-routing
!
end

