RP/0/0/CPU0:XR-P3(config)#SH RUN
Sat Nov 18 11:48:40.411 UTC
Building configuration...
!! IOS XR Configuration 6.0.1
!! Last configuration change at Sat Nov 18 11:47:45 2017 by cisco
!
hostname XR-P3
vrf B
 address-family ipv4 unicast
  import route-target
   2:2
  !
  export route-target
   2:2
  !
 !
!
line console
 timeout login response 0
!
interface Loopback0
 ipv4 address 100.64.1.3 255.255.255.255
!
interface MgmtEth0/0/CPU0/0
 shutdown
!
interface GigabitEthernet0/0/0/0
!
interface GigabitEthernet0/0/0/0.13
 ipv4 address 169.254.13.3 255.255.255.0
 encapsulation dot1q 13
!
interface GigabitEthernet0/0/0/0.34
 ipv4 address 169.254.34.3 255.255.255.0
 encapsulation dot1q 34
!
interface GigabitEthernet0/0/0/0.101
 vrf B
 ipv4 address 169.254.100.254 255.255.255.0
 encapsulation dot1q 101
!
interface GigabitEthernet0/0/0/0.113
 ipv4 address 169.254.113.3 255.255.255.0
 encapsulation dot1q 113
!
interface GigabitEthernet0/0/0/1
 shutdown
!
interface GigabitEthernet0/0/0/2
 shutdown
!
!
route-policy PASS
  pass
end-policy
!
router isis fuck
 is-type level-2-only
 net 49.0001.0000.0003.00
 log adjacency changes
 address-family ipv4 unicast
  metric-style wide
  segment-routing mpls
 !
 interface Loopback0
  passive
  address-family ipv4 unicast
   prefix-sid index 3
  !
 !
 interface GigabitEthernet0/0/0/0.13
  point-to-point
  address-family ipv4 unicast
  !
 !
 interface GigabitEthernet0/0/0/0.34
  point-to-point
  address-family ipv4 unicast
  !
 !
 interface GigabitEthernet0/0/0/0.113
  point-to-point
  address-family ipv4 unicast
  !
 !
!
router bgp 9000
 bgp router-id 100.64.1.3
 address-family vpnv4 unicast
 !
 neighbor 100.64.1.4
  remote-as 9000
  update-source Loopback0
  address-family vpnv4 unicast
  !
 !
 neighbor 169.254.100.1
  remote-as 65511
 !
 vrf B
  rd 2:2
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
segment-routing
!
end

