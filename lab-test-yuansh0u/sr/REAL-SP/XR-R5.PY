RP/0/RP0/CPU0:XR-R5#sh running-config 
Wed Mar 14 21:21:42.330 UTC
 Building configuration...
!! IOS XR Configuration version = 6.2.25
!! Last configuration change at Wed Mar 14 21:01:09 2018 by cisco
!
hostname XR-R5
logging console informational
service timestamps log disable
service timestamps debug disable
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
 ipv4 address 100.64.1.5 255.255.255.255
!         
interface MgmtEth0/RP0/CPU0/0
 ipv4 address 150.1.39.2 255.255.0.0
!
interface GigabitEthernet0/0/0/0.915
 ipv4 address 169.254.15.5 255.255.255.0
 encapsulation dot1q 915
!
interface GigabitEthernet0/0/0/0.925
 ipv4 address 169.254.25.5 255.255.255.0
 encapsulation dot1q 925
!
interface GigabitEthernet0/0/0/0.935
 ipv4 address 169.254.35.5 255.255.255.0
 encapsulation dot1q 935
!
interface GigabitEthernet0/0/0/0.945
 ipv4 address 169.254.45.5 255.255.255.0
 encapsulation dot1q 945
!
interface GigabitEthernet0/0/0/0.956
 !interface GigabitEthernet0/0/0/0.925
 ipv4 address 169.254.56.5 255.255.255.0
 encapsulation dot1q 956
!
interface GigabitEthernet0/0/0/0.957
 ipv4 address 169.254.57.5 255.255.255.0
 encapsulation dot1q 957
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
 net 49.0001.0000.0005.00
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
   prefix-sid index 5
  !
 !
 interface GigabitEthernet0/0/0/0.915
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
 interface GigabitEthernet0/0/0/0.935
  point-to-point
  address-family ipv4 unicast
   fast-reroute per-prefix
   fast-reroute per-prefix ti-lfa
  !
 !
 interface GigabitEthernet0/0/0/0.945
  point-to-point
  address-family ipv4 unicast
   fast-reroute per-prefix
   fast-reroute per-prefix ti-lfa
  !
 !
 interface GigabitEthernet0/0/0/0.956
  point-to-point
  address-family ipv4 unicast
   fast-reroute per-prefix
   fast-reroute per-prefix ti-lfa
  !
 !
 interface GigabitEthernet0/0/0/0.957
  point-to-point
  address-family ipv4 unicast
   fast-reroute per-prefix
   fast-reroute per-prefix ti-lfa
  !
 !
!
router bgp 9000
 address-family l2vpn vpls-vpws
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
ssh server v2
ssh server rate-limit 600
end

