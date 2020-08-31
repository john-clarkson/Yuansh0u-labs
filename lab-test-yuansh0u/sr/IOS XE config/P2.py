
!
mpls traffic-eng tunnels
mpls traffic-eng pcc peer 150.1.255.253 source 2.2.2.2
mpls traffic-eng pcc report-all
!
!

!
segment-routing mpls
 !
 connected-prefix-sid-map
  address-family ipv4
   2.2.2.2/32 index 200 range 1 
  exit-address-family
 !

interface Loopback0
 ip address 2.2.2.2 255.255.255.255
 ip router isis fuck
!         
interface GigabitEthernet2
 ip router isis fuck
 negotiation auto
 mpls traffic-eng tunnels

 isis network point-to-point 
!
!
router isis fuck
 net 49.0001.0000.0007.00
 is-type level-2-only
 metric-style wide
 distribute link-state
 segment-routing mpls
 mpls traffic-eng router-id Loopback0
 mpls traffic-eng level-2
!
router bgp 9000
 bgp router-id 2.2.2.2
 bgp log-neighbor-changes
 neighbor 150.1.255.253 remote-as 9000
 neighbor 150.1.255.253 update-source GigabitEthernet2
 !
 address-family ipv4
  redistribute connected
  neighbor 150.1.255.253 activate
 exit-address-family
 !
 address-family link-state link-state
  neighbor 150.1.255.253 activate
  neighbor 150.1.255.253 route-reflector-client
 exit-address-family
!
