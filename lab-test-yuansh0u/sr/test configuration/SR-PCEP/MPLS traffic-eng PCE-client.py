mpls traffic-eng
auto-tunnel pcc
 tunnel-id min 1 max 99
 reoptimize timers delay install 0
 commit

XR-PE1
 router isis fuck
    address-family ipv4 unicast
     mpls traffic-eng router-id loopback0
     mpls traffic-eng level-2-only
     commit
     !

ipv4 unnumbered mpls traffic-eng loopback 0
mpls traffic-eng
interface GigabitEthernet0/0/0/0.12 
interface GigabitEthernet0/0/0/0.15 
interface GigabitEthernet0/0/0/0.100
interface GigabitEthernet0/0/0/0.111
interface GigabitEthernet0/0/0/0.113
exit
 pce
  peer source ipv4 100.64.11.1
  peer ipv4 150.1.255.253
  !
  segment-routing
  logging events peer-status
  stateful-client
   instantiation
   commit
   !
ALL IOS XR
   router isis fuck
    address-family ipv4 unicast
     mpls traffic-eng router-id loopback0
     mpls traffic-eng level-2-only
     commit
     !
XR-P1
ipv4 unnumbered mpls traffic-eng loopback 0
 router isis fuck
    address-family ipv4 unicast
     mpls traffic-eng router-id loopback0
     mpls traffic-eng level-2-only
     commit
     !

ipv4 unnumbered mpls traffic-eng loopback 0
mpls traffic-eng
interface GigabitEthernet0/0/0/0.12 
interface GigabitEthernet0/0/0/0.13 
interface GigabitEthernet0/0/0/0.14
interface GigabitEthernet0/0/0/0.16
interface GigabitEthernet0/0/0/0.111
interface GigabitEthernet0/0/0/0.112
exit
 pce
  peer source ipv4 100.64.1.1
  peer ipv4 150.1.255.253
  !
  segment-routing
  logging events peer-status
  stateful-client
   instantiation
   commit

 !!
 XR-P3
ipv4 unnumbered mpls traffic-eng loopback 0
 router isis fuck
    address-family ipv4 unicast
     mpls traffic-eng router-id loopback0
     mpls traffic-eng level-2-only
     commit
     !


mpls traffic-eng
interface GigabitEthernet0/0/0/0.13
interface GigabitEthernet0/0/0/0.14
interface GigabitEthernet0/0/0/0.113
exit
 pce
  peer source ipv4 100.64.1.3
  peer ipv4 150.1.255.253
  !
  segment-routing
  logging events peer-status
  stateful-client
   instantiation
   commit

 !!
 XR-P5
ipv4 unnumbered mpls traffic-eng loopback 0
 router isis fuck
    address-family ipv4 unicast
     mpls traffic-eng router-id loopback0
     mpls traffic-eng level-2-only
     commit
     !


mpls traffic-eng
interface GigabitEthernet0/0/0/0.11
interface GigabitEthernet0/0/0/0.56
interface GigabitEthernet0/0/0/0.15
exit
 pce
  peer source ipv4 100.64.1.5
  peer ipv4 150.1.255.253
  !
  segment-routing
  logging events peer-status
  stateful-client
   instantiation
   commit
 !!  
XR-P6
ipv4 unnumbered mpls traffic-eng loopback 0
 router isis fuck
    address-family ipv4 unicast
     mpls traffic-eng router-id loopback0
     mpls traffic-eng level-2-only
     commit
     !


mpls traffic-eng
interface GigabitEthernet0/0/0/0.16
interface GigabitEthernet0/0/0/0.56
exit
 pce
  peer source ipv4 100.64.1.6
  peer ipv4 150.1.255.253
  !
  segment-routing
  logging events peer-status
  stateful-client
   instantiation
   commit