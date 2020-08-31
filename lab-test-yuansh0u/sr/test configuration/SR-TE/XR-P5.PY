RP/0/0/CPU0:XR-P5#sh running-config 
Tue Nov 28 13:00:16.603 UTC
Building configuration...
!! IOS XR Configuration 6.0.1
!! Last configuration change at Tue Nov 28 10:26:27 2017 by cisco
!
hostname XR-P5
ipv4 unnumbered mpls traffic-eng Loopback0
interface Loopback0
 ipv4 address 100.64.1.5 255.255.255.255
!
interface MgmtEth0/0/CPU0/0
 shutdown
!
interface GigabitEthernet0/0/0/0.15
 ipv4 address 169.254.15.5 255.255.255.0
 encapsulation dot1q 15
!
interface GigabitEthernet0/0/0/0.56
 ipv4 address 169.254.56.5 255.255.255.0
 encapsulation dot1q 56
!
interface GigabitEthernet0/0/0/1
 shutdown
!
interface GigabitEthernet0/0/0/2
 shutdown
!
router isis fuck
 is-type level-2-only
 net 49.0001.0000.0005.00
 log adjacency changes
 address-family ipv4 unicast
  metric-style wide
  mpls traffic-eng level-2-only
  mpls traffic-eng router-id Loopback0
  segment-routing mpls
 !
 interface Loopback0
  address-family ipv4 unicast
   prefix-sid index 5
  !
 !
 interface GigabitEthernet0/0/0/0.15
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
!
mpls traffic-eng
 pce
  peer source ipv4 100.64.1.5
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

