RP/0/0/CPU0:XR-PE1#sh running-config 
Tue Nov 21 12:47:54.950 UTC
Building configuration...
!! IOS XR Configuration 6.0.1
!! Last configuration change at Tue Nov 21 12:17:52 2017 by cisco
!
hostname XR-PE1
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
interface Loopback0
 ipv4 address 100.64.11.1 255.255.255.255
!
interface MgmtEth0/0/CPU0/0
 shutdown
!
interface GigabitEthernet0/0/0/0.12
!
interface GigabitEthernet0/0/0/0.15
 ipv4 address 169.254.15.1 255.255.255.0
 encapsulation dot1q 15
!
interface GigabitEthernet0/0/0/0.100
 vrf A
 ipv4 address 169.254.100.254 255.255.255.0
 encapsulation dot1q 100
!
interface GigabitEthernet0/0/0/0.111
 ipv4 address 169.254.111.1 255.255.255.0
 encapsulation dot1q 111
!
interface GigabitEthernet0/0/0/0.113
 ipv4 address 169.254.113.1 255.255.255.0
 encapsulation dot1q 113
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
 !
 interface GigabitEthernet0/0/0/0.15
  point-to-point
  address-family ipv4 unicast
   fast-reroute per-prefix
   fast-reroute per-prefix ti-lfa
  !
 !
 interface GigabitEthernet0/0/0/0.111
  point-to-point
  address-family ipv4 unicast
   fast-reroute per-prefix
   fast-reroute per-prefix ti-lfa
  !
 !
 interface GigabitEthernet0/0/0/0.113
  point-to-point
  address-family ipv4 unicast
   fast-reroute per-prefix
   fast-reroute per-prefix ti-lfa
  !
 !
!
router bgp 9000
 bgp router-id 100.64.11.1
 address-family vpnv4 unicast
 !
 neighbor 100.64.1.4
  remote-as 9000
  update-source Loopback0
  address-family vpnv4 unicast
  !
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
  neighbor 169.254.100.1
   remote-as 65511
   address-family ipv4 unicast
    route-policy PASS in
    route-policy PASS out
   !
  !
 !
!
mpls oam
!
segment-routing
 global-block 16000 23999
 mapping-server
  prefix-sid-map
   address-family ipv4
    100.64.1.2/32 8
   !
  !
 !
!
end

