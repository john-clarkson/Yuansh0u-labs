NOVA-PE2#sh run
NOVA-PE2#sh running-config 
Building configuration...

Current configuration : 2307 bytes
!
! Last configuration change at 21:11:55 UTC Tue Jul 18 2017
!
version 15.5
service timestamps debug datetime msec
service timestamps log datetime msec
no platform punt-keepalive disable-kernel-core
platform console serial
!
hostname NOVA-PE2
!
boot-start-marker
boot-end-marker
!
!
vrf definition CEA
 rd 9809:1
 !
 address-family ipv4
  route-target export 9809:1
  route-target import 9809:1
 exit-address-family
!
vrf definition CEB
 rd 9809:2
 !
 address-family ipv4
  route-target export 9809:2
  route-target import 9809:2
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
license udi pid CSR1000V sn 97IMX7ISR0X
!
spanning-tree extend system-id
!
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
 ip address 2.2.2.2 255.255.255.255
 ip ospf 9809 area 0
!
interface GigabitEthernet1
 no ip address
 negotiation auto
!         
interface GigabitEthernet1.10
 encapsulation dot1Q 10
 vrf forwarding CEA
 ip address 169.254.1.2 255.255.255.252
!
interface GigabitEthernet1.20
 encapsulation dot1Q 20
 vrf forwarding CEB
 ip address 169.254.2.2 255.255.255.252
!
interface GigabitEthernet2
 ip address 169.254.200.6 255.255.255.252
 ip ospf 9809 area 0
 negotiation auto
!
interface GigabitEthernet3
 no ip address
 shutdown
 negotiation auto
!
interface GigabitEthernet4
 no ip address
 shutdown 
 negotiation auto
!
router ospf 9809
 router-id 2.2.2.2
 prefix-suppression
 mpls ldp autoconfig
!
router bgp 9809
 bgp router-id 2.2.2.2
 bgp log-neighbor-changes
 neighbor 3.3.3.3 remote-as 9809
 neighbor 3.3.3.3 update-source Loopback0
 !
 address-family vpnv4
  neighbor 3.3.3.3 activate
  neighbor 3.3.3.3 send-community extended
 exit-address-family
 !
 address-family ipv4 vrf CEA
  neighbor 169.254.1.1 remote-as 65522
  neighbor 169.254.1.1 activate
 exit-address-family
 !        
 address-family ipv4 vrf CEB
  neighbor 169.254.2.1 remote-as 65533
  neighbor 169.254.2.1 activate
 exit-address-family
!
!
virtual-service csr_mgmt
!
ip forward-protocol nd
!
no ip http server
no ip http secure-server
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
line vty 0
 login
line vty 1
 login
 length 0
line vty 2 4
 login
!
!
end

