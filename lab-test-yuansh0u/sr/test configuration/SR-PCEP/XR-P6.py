RP/0/0/CPU0:XR-P6#SH RUN
Tue Nov 21 12:27:52.212 UTC
Building configuration...
!! IOS XR Configuration 6.0.1
!! Last configuration change at Tue Nov 21 12:24:25 2017 by cisco
!
hostname XR-P6
interface Loopback0
 ipv4 address 100.64.1.6 255.255.255.255
!
!
interface Loopback66
 no shutdown
 ipv4 address 66.66.66.66 255.255.255.255
!
interface MgmtEth0/0/CPU0/0
 shutdown
!
interface GigabitEthernet0/0/0/0
 ipv4 address 150.1.66.254 255.255.0.0
!
interface GigabitEthernet0/0/0/0.16
 ipv4 address 169.254.16.6 255.255.255.0
 encapsulation dot1q 16
!
interface GigabitEthernet0/0/0/0.56
 ipv4 address 169.254.56.6 255.255.255.0
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
 net 49.0001.0000.0006.00
 distribute bgp-ls level 2
 log adjacency changes
 address-family ipv4 unicast
  metric-style wide
  segment-routing mpls
 !
 interface Loopback0
  address-family ipv4 unicast
   prefix-sid index 6
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
!
router bgp 9000
 bgp router-id 100.64.1.6
 bgp cluster-id 9.9.9.9
 address-family ipv4 unicast
  network 66.66.66.66/32
 !
 address-family vpnv4 unicast
 !
 address-family link-state link-state
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
 neighbor 150.1.255.253
  remote-as 9000
  update-source GigabitEthernet0/0/0/0
  address-family ipv4 unicast
  !
  address-family link-state link-state
   route-reflector-client
segment-routing
!
end





