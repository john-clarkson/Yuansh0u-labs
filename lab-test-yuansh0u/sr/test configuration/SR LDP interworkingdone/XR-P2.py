

IMPORTANT:  READ CAREFULLY
Welcome to the Demo Version of Cisco IOS XRv (the "Software").
The Software is subject to and governed by the terms and conditions
of the End User License Agreement and the Supplemental End User
License Agreement accompanying the product, made available at the
time of your order, or posted on the Cisco website at
www.cisco.com/go/terms (collectively, the "Agreement").
As set forth more fully in the Agreement, use of the Software is
strictly limited to internal use in a non-production environment
solely for demonstration and evaluation purposes.  Downloading,
installing, or using the Software constitutes acceptance of the
Agreement, and you are binding yourself and the business entity
that you represent to the Agreement.  If you do not agree to all
of the terms of the Agreement, then Cisco is unwilling to license
the Software to you and (a) you may not download, install or use the
Software, and (b) you may return the Software as more fully set forth
in the Agreement.


Please login with any configured user/password, or cisco/cisco


User Access Verification

Username: cisco
Password: 
RP/0/0/CPU0:Nov 18 18:29:45.702 : exec[65700]: %SECURITY-LOGIN-6-AUTHEN_SUCCESS : Successfully authenticated user 'cisco' from 'console' on 'con0_0_CPU0' 


RP/0/0/CPU0:XR-P2#sh running-config 
Sat Nov 18 18:29:49.112 UTC
Building configuration...
!! IOS XR Configuration 6.0.1
!! Last configuration change at Sat Nov 18 16:23:36 2017 by cisco
!
hostname XR-P2
logging console informational
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
interface Loopback0
 ipv4 address 100.64.1.2 255.255.255.255
!
interface MgmtEth0/0/CPU0/0
 shutdown
!
interface GigabitEthernet0/0/0/0.12
 ipv4 address 169.254.12.2 255.255.255.0
 encapsulation dot1q 12
!
interface GigabitEthernet0/0/0/0.201
 vrf B
 ipv4 address 169.254.200.254 255.255.255.0
 encapsulation dot1q 201
!
interface GigabitEthernet0/0/0/0.222
 ipv4 address 169.254.222.22 255.255.255.0
 encapsulation dot1q 222
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
 net 49.0001.0000.0002.00
 address-family ipv4 unicast
  metric-style wide
  mpls ldp auto-config
 !
 interface Loopback0
  passive
  address-family ipv4 unicast
  !
 !
 interface GigabitEthernet0/0/0/0.12
  point-to-point
  address-family ipv4 unicast
  !
 !
 interface GigabitEthernet0/0/0/0.222
  point-to-point
  address-family ipv4 unicast
  !
 !
!
router bgp 9000
 bgp router-id 100.64.1.2
 address-family vpnv4 unicast
 !
 neighbor 100.64.1.4
  remote-as 9000
  update-source Loopback0
  address-family vpnv4 unicast
  !
 !
 vrf B
  rd 2:2
  address-family ipv4 unicast
  !
  neighbor 169.254.200.1
   remote-as 65522
   address-family ipv4 unicast
    route-policy PASS in
    route-policy PASS out
   !
  !
 !
!
mpls ldp
 router-id 100.64.1.2
 address-family ipv4
  label
   local
    allocate for host-routes
   !
  !
 !
!
end

