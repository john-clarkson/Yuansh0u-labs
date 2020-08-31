RP/0/0/CPU0:XR-PE2#sh running-config 
Tue Nov 28 12:58:42.369 UTC
Building configuration...
!! IOS XR Configuration 6.0.1
!! Last configuration change at Tue Nov 28 10:24:49 2017 by cisco
!
hostname XR-PE2
vrf A
 address-family ipv4 unicast
  import route-target
   1:1
  !
  export route-target
   1:1
  !
 !
!
line console
 timeout login response 0
!
ipv4 unnumbered mpls traffic-eng Loopback0
interface Loopback0
 ipv4 address 100.64.22.2 255.255.255.255
!
interface MgmtEth0/0/CPU0/0
 shutdown
!
interface GigabitEthernet0/0/0/0.112
 ipv4 address 169.254.112.2 255.255.255.0
 encapsulation dot1q 112
!
interface GigabitEthernet0/0/0/0.200
 vrf A
 ipv4 address 169.254.200.254 255.255.255.0
 encapsulation dot1q 200
!
interface GigabitEthernet0/0/0/0.222
 ipv4 address 169.254.222.2 255.255.255.0
 encapsulation dot1q 222
!
interface GigabitEthernet0/0/0/0.224
 ipv4 address 169.254.224.2 255.255.255.0
 encapsulation dot1q 224
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
 net 49.0001.0000.0022.00
 log adjacency changes
 address-family ipv4 unicast
  metric-style wide
  mpls traffic-eng level-2-only
  mpls traffic-eng router-id Loopback0
  segment-routing mpls
 !
 interface Loopback0
  passive
  point-to-point
  address-family ipv4 unicast
   prefix-sid index 22
  !
 !
 interface GigabitEthernet0/0/0/0.112
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
 interface GigabitEthernet0/0/0/0.224
  point-to-point
  address-family ipv4 unicast
   fast-reroute per-prefix
   fast-reroute per-prefix ti-lfa
  !
 !
!
router bgp 9000
 bgp router-id 100.64.22.2
 address-family vpnv4 unicast
 !
 neighbor 100.64.1.6
  remote-as 9000
  update-source Loopback0
  address-family vpnv4 unicast
  !
 !
 neighbor 169.254.100.1
  remote-as 65511
 !
 vrf A
  rd 1:1
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
mpls oam
!
mpls traffic-eng
 pce
  peer source ipv4 100.64.22.2
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

