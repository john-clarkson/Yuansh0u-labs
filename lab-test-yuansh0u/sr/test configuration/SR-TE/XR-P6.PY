RP/0/0/CPU0:XR-P6#sh running-config 
Tue Nov 28 13:00:26.462 UTC
Building configuration...
!! IOS XR Configuration 6.0.1
!! Last configuration change at Tue Nov 28 10:26:44 2017 by cisco
!
hostname XR-P6
ipv4 unnumbered mpls traffic-eng Loopback0
interface Loopback0
 ipv4 address 100.64.1.6 255.255.255.255
!
interface MgmtEth0/0/CPU0/0
 shutdown
!
interface GigabitEthernet0/0/0/0
 ipv4 address 150.1.66.66 255.255.0.0
!
interface GigabitEthernet0/0/0/0.16
 ipv4 address 169.254.16.6 255.255.255.0
 encapsulation dot1q 16
!
interface GigabitEthernet0/0/0/0.56
 ipv4 address 169.254.56.6 255.255.255.0
 encapsulation dot1q 56
!
interface GigabitEthernet0/0/0/0.67
 ipv4 address 169.254.67.6 255.255.255.0
 encapsulation dot1q 67
!
interface GigabitEthernet0/0/0/1
 shutdown
!
interface GigabitEthernet0/0/0/2
 shutdown
!
router isis fuck
 is-type level-2-only
 net 49.0001.0000.0006.00
 distribute bgp-ls level 2
 log adjacency changes
 address-family ipv4 unicast
  metric-style wide
  mpls traffic-eng level-2-only
  mpls traffic-eng router-id Loopback0
  segment-routing mpls
 !
 interface Loopback0
  address-family ipv4 unicast
   prefix-sid index 6
  !
 !
 interface GigabitEthernet0/0/0/0
  address-family ipv4 unicast
  !
 !
 interface GigabitEthernet0/0/0/0.16
  bfd minimum-interval 150
  bfd multiplier 3
  bfd fast-detect ipv4
  point-to-point
  address-family ipv4 unicast
   fast-reroute per-prefix
   fast-reroute per-prefix ti-lfa
  !
 !
 interface GigabitEthernet0/0/0/0.56
  bfd minimum-interval 150
  bfd multiplier 3
  bfd fast-detect ipv4
  point-to-point
  address-family ipv4 unicast
   fast-reroute per-prefix
   fast-reroute per-prefix ti-lfa
  !
 !
 interface GigabitEthernet0/0/0/0.67
  bfd minimum-interval 150
  bfd multiplier 3
  bfd fast-detect ipv4
  point-to-point
  address-family ipv4 unicast
   fast-reroute per-prefix
   fast-reroute per-prefix ti-lfa
  !
 !
!
router bgp 9000
 bgp router-id 100.64.1.6
 bgp cluster-id 9.9.9.9
 address-family ipv4 unicast
  network 66.66.66.66/32
 !
 address-family vpnv4 unicast
 !
 neighbor 100.64.1.2
  remote-as 9000
  update-source Loopback0
  address-family vpnv4 unicast
   route-reflector-client
  !
 !
 neighbor 100.64.1.3
  remote-as 9000
  update-source Loopback0
  address-family vpnv4 unicast
   route-reflector-client
  !
 !
 neighbor 100.64.11.1
  remote-as 9000
  update-source Loopback0
  address-family vpnv4 unicast
   route-reflector-client
  !
 !
 neighbor 100.64.22.2
  remote-as 9000
  update-source Loopback0
  address-family vpnv4 unicast
   route-reflector-client
  !
 !
!
mpls traffic-eng
 pce
  peer source ipv4 100.64.1.6
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

