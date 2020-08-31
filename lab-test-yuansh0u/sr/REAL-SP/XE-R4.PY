
!
hostname XE-R4

mpls traffic-eng tunnels
mpls traffic-eng pcc peer 150.1.255.253 source 100.64.1.4
mpls traffic-eng pcc report-all
!
segment-routing mpls
 !
 connected-prefix-sid-map
  address-family ipv4
   100.64.1.4/32 index 4 range 1 
  exit-address-family
 !
!
!
interface Loopback0
 ip address 100.64.1.4 255.255.255.255
 ip router isis fuck
!

!
interface GigabitEthernet2
 no ip address
 no shutdown
 negotiation auto
 no mop enabled
 no mop sysid
!
interface GigabitEthernet2.914
 encapsulation dot1Q 914
 ip address 169.254.14.4 255.255.255.0
 ip router isis fuck
 mpls traffic-eng tunnels
 isis network point-to-point 
!
interface GigabitEthernet2.924
 encapsulation dot1Q 924
 ip address 169.254.24.4 255.255.255.0
 ip router isis fuck
 mpls traffic-eng tunnels
 isis network point-to-point 
!
interface GigabitEthernet2.945
 encapsulation dot1Q 945
 ip address 169.254.45.4 255.255.255.0
 ip router isis fuck
 mpls traffic-eng tunnels
 isis network point-to-point 
!
interface GigabitEthernet2.947
 encapsulation dot1Q 947
 ip address 169.254.47.4 255.255.255.0
 ip router isis fuck
 mpls traffic-eng tunnels
 isis network point-to-point 
!
interface GigabitEthernet3
 no ip address
 shutdown
 negotiation auto
 no mop enabled
 no mop sysid
!
router isis fuck
 net 49.0001.0000.0004.00
 is-type level-2-only
 metric-style wide
 segment-routing mpls
 fast-reroute per-prefix level-2 all
 fast-reroute ti-lfa level-2
 mpls traffic-eng router-id Loopback0
 mpls traffic-eng level-2
!


