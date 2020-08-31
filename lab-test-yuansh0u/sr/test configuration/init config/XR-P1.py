RP/0/0/CPU0:XR-P1# sh running-config 
Sat Nov 18 11:56:04.981 UTC
Building configuration...
!! IOS XR Configuration 6.0.1
!! Last configuration change at Sat Nov 18 11:01:44 2017 by cisco
!
hostname XR-P1
interface Loopback0
 ipv4 address 100.64.1.1 255.255.255.255
!
interface MgmtEth0/0/CPU0/0
 shutdown
!
interface GigabitEthernet0/0/0/0.12
 ipv4 address 169.254.12.1 255.255.255.0
 encapsulation dot1q 12
!
interface GigabitEthernet0/0/0/0.13
 ipv4 address 169.254.13.1 255.255.255.0
 encapsulation dot1q 13
!
interface GigabitEthernet0/0/0/0.14
 ipv4 address 169.254.14.1 255.255.255.0
 encapsulation dot1q 14
!
interface GigabitEthernet0/0/0/0.111
 ipv4 address 169.254.111.11 255.255.255.0
 encapsulation dot1q 111
!
interface GigabitEthernet0/0/0/0.112
 ipv4 address 169.254.112.1 255.255.255.0
 encapsulation dot1q 112
!
interface GigabitEthernet0/0/0/1
 shutdown
!
interface GigabitEthernet0/0/0/2
 shutdown
!
router isis fuck
 is-type level-2-only
 net 49.0001.0000.0001.00
 address-family ipv4 unicast
  metric-style wide
  segment-routing mpls
 !
 interface Loopback0
  address-family ipv4 unicast
   prefix-sid index 1
  !
 !
 interface GigabitEthernet0/0/0/0.12
  point-to-point
  address-family ipv4 unicast
  !
 !
 interface GigabitEthernet0/0/0/0.13
  point-to-point
  address-family ipv4 unicast
  !
 !
 interface GigabitEthernet0/0/0/0.14
  point-to-point
  address-family ipv4 unicast
  !
 !
 interface GigabitEthernet0/0/0/0.111
  point-to-point
  address-family ipv4 unicast
  !
 !
 interface GigabitEthernet0/0/0/0.112
  point-to-point
  address-family ipv4 unicast
  !
 !
!
segment-routing
!
end

