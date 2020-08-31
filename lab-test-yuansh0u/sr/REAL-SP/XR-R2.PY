RP/0/RP0/CPU0:XR-R2#show running-config 
Thu Mar 15 16:16:49.751 UTC
 Building configuration...
!! IOS XR Configuration version = 6.2.25
!! Last configuration change at Thu Mar 15 12:47:48 2018 by cisco
!
hostname XR-R2
username cisco
 group root-lr
 group cisco-support
 secret 5 $1$D2lU$qe7hfQARro7vjvcTdqaDC.
!
ipv4 unnumbered mpls traffic-eng Loopback0
call-home
 service active
 contact smart-licensing
 profile CiscoTAC-1
  active
  destination transport-method http
 !
!
interface Loopback0
 ipv4 address 100.64.1.2 255.255.255.255
!
interface MgmtEth0/RP0/CPU0/0
 ipv4 address 150.1.39.1 255.255.0.0
!         
interface GigabitEthernet0/0/0/0.39
 ipv4 address 39.39.39.9 255.255.255.0
 encapsulation dot1q 39
!
interface GigabitEthernet0/0/0/0.912
 ipv4 address 169.254.12.2 255.255.255.0
 encapsulation dot1q 912
!
interface GigabitEthernet0/0/0/0.923
 ipv4 address 169.254.23.2 255.255.255.0
 encapsulation dot1q 923
!
interface GigabitEthernet0/0/0/0.924
 ipv4 address 169.254.24.2 255.255.255.0
 encapsulation dot1q 924
!
interface GigabitEthernet0/0/0/0.925
 ipv4 address 169.254.25.2 255.255.255.0
 encapsulation dot1q 925
!
interface GigabitEthernet0/0/0/0.926
 ipv4 address 169.254.26.2 255.255.255.0
 encapsulation dot1q 926
!
interface GigabitEthernet0/0/0/1
 shutdown
!
interface GigabitEthernet0/0/0/2
 shutdown
!
interface GigabitEthernet0/0/0/3
 shutdown
!
interface GigabitEthernet0/0/0/4
 shutdown
!
interface GigabitEthernet0/0/0/5
 shutdown
!
interface GigabitEthernet0/0/0/6
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
 interface GigabitEthernet0/0/0/0.912
  point-to-point
  address-family ipv4 unicast
   fast-reroute per-prefix
   fast-reroute per-prefix ti-lfa
  !
 !        
 interface GigabitEthernet0/0/0/0.923
  point-to-point
  address-family ipv4 unicast
   fast-reroute per-prefix
   fast-reroute per-prefix ti-lfa
  !
 !
 interface GigabitEthernet0/0/0/0.924
  point-to-point
  address-family ipv4 unicast
   fast-reroute per-prefix
   fast-reroute per-prefix ti-lfa
  !
 !
 interface GigabitEthernet0/0/0/0.925
  point-to-point
  address-family ipv4 unicast
   fast-reroute per-prefix
   fast-reroute per-prefix ti-lfa
  !
 !
 interface GigabitEthernet0/0/0/0.926
  point-to-point
  address-family ipv4 unicast
   fast-reroute per-prefix
   fast-reroute per-prefix ti-lfa
  !
 !
!
router bgp 1
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
ssh server v2
end

