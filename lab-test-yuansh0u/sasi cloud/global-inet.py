GLOBAL-INET#
GLOBAL-INET#sh run
GLOBAL-INET#sh running-config 
Building configuration...

Current configuration : 2042 bytes
!
! Last configuration change at 17:21:05 UTC Thu Jul 20 2017
!
version 15.5
service timestamps debug datetime msec
service timestamps log datetime msec
no platform punt-keepalive disable-kernel-core
platform console serial
!
hostname GLOBAL-INET
!
boot-start-marker
boot-end-marker
!
!
vrf definition GLOBAL-INET
 rd 9809:45
 !
 address-family ipv4
  route-target export 9809:45
  route-target import 9809:45
 exit-address-family
!
!
no aaa new-model
!
!
!
!
!
!
!
!
!
!
!



!
!
!
!
!
!         
!
!
!
!
subscriber templating
!
multilink bundle-name authenticated
!
!
!
!
!
!
!
!
!
!
!
!
!
license udi pid CSR1000V sn 9FVVSBNTSXF
!
spanning-tree extend system-id
!
username cisco privilege 15 password 0 cisco
!
redundancy
!
!
!
!
!
!
! 
!
!
!
!
!
!
!
!
!
!
!
!         
! 
! 
! 
! 
! 
! 
!
!
interface Loopback0
 ip address 4.4.4.4 255.255.255.255
 ip ospf 9809 area 0
!
interface Loopback84
 vrf forwarding GLOBAL-INET
 ip address 8.8.4.4 255.255.255.255
!
interface Loopback88
 vrf forwarding GLOBAL-INET
 ip address 8.8.8.8 255.255.255.255
!
interface GigabitEthernet1
 no ip address
 shutdown 
 negotiation auto
!
interface GigabitEthernet2
 no ip address
 shutdown
 negotiation auto
!
interface GigabitEthernet3
 no ip address
 shutdown
 negotiation auto
!
interface GigabitEthernet4
 ip address 169.254.200.10 255.255.255.252
 ip ospf 9809 area 0
 negotiation auto
!
router ospf 9809
 router-id 4.4.4.4
 mpls ldp autoconfig
!
router bgp 9809
 bgp log-neighbor-changes
 neighbor 3.3.3.3 remote-as 9809
 neighbor 3.3.3.3 update-source Loopback0
 !
 address-family vpnv4
  neighbor 3.3.3.3 activate
  neighbor 3.3.3.3 send-community extended
 exit-address-family
 !
 address-family ipv4 vrf GLOBAL-INET
  network 0.0.0.0
 exit-address-family
!
!
virtual-service csr_mgmt
!
ip forward-protocol nd
!
ip http server
ip http authentication local
no ip http secure-server
ip route vrf GLOBAL-INET 0.0.0.0 0.0.0.0 Null0
!
!         
!
!
control-plane
!
 !
 !
 !
 !
!
!
!
!
!
line con 0
 stopbits 1
line vty 0 4
 password cisco
 login local
 transport input all
!
!
end
          
