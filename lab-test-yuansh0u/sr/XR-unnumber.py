hostname XR-PE4
interface Loopback0
 ipv4 address 100.64.11.4 255.255.255.255
!
interface GigabitEthernet0/0/0/0
ipv4 point-to-point
ipv4 unnumbered Loopback0
no shut
 !
interface GigabitEthernet0/0/0/1
ipv4 point-to-point
ipv4 unnumbered Loopback0 
no shut
!
interface GigabitEthernet0/0/0/2
ipv4 point-to-point
ipv4 unnumbered Loopback0
no shut
 router isis fuck
 is-type level-2-only
 net 49.0001.0000.0011.00
 log adjacency changes
 address-family ipv4 unicast
  metric-style wide
  segment-routing mpls sr-prefer
  segment-routing prefix-sid-map advertise-local
 !
 interface Loopback0
  passive
  point-to-point
  address-family ipv4 unicast
   prefix-sid index 11

   !
    interface GigabitEthernet0/0/0/3.67
  point-to-point
  address-family ipv4 unicast
   fast-reroute per-prefix
   fast-reroute per-prefix ti-lfa
   !
      interface GigabitEthernet0/0/0/1
  point-to-point
  address-family ipv4 unicast
   fast-reroute per-prefix
   fast-reroute per-prefix ti-lfa
   ! 
       interface GigabitEthernet0/0/0/2
  point-to-point
  address-family ipv4 unicast
   fast-reroute per-prefix
   fast-reroute per-prefix ti-lfa
   !
 segment-routing
 global-block 16000 23999
 !
 ipv4 unnumbered mpls traffic-eng loopback 0
 !
 router isis fuck
    address-family ipv4 unicast
     mpls traffic-eng router-id loopback0
     mpls traffic-eng level-2-only
     commit
     !

ipv4 unnumbered mpls traffic-eng loopback 0
mpls traffic-eng
interface GigabitEthernet0/0/0/0.67
interface GigabitEthernet0/0/0/1
interface GigabitEthernet0/0/0/2
exit
 pce
  peer source ipv4 100.64.11.4
  peer ipv4 150.1.255.253
  !
  segment-routing
  logging events peer-status
  stateful-client
   instantiation
   commit
