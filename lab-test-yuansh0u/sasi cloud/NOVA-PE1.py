
NOVA-PE1>
NOVA-PE1>
NOVA-PE1>
NOVA-PE1>
NOVA-PE1>
NOVA-PE1>
NOVA-PE1>en
NOVA-PE1#sh run
NOVA-PE1#sh running-config 
Building configuration...

Current configuration : 3041 bytes
!
! Last configuration change at 00:23:35 UTC Wed Jul 19 2017
!
version 15.5
service timestamps debug datetime msec
service timestamps log datetime msec
no platform punt-keepalive disable-kernel-core
platform console serial
!
hostname NOVA-PE1
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
license udi pid CSR1000V sn 9QDJYJZ8YHD
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
 ip address 1.1.1.1 255.255.255.255
 ip ospf 9809 area 0
!
interface GigabitEthernet1
 no ip address
 negotiation auto
!
interface GigabitEthernet1.10
 description CEA
 encapsulation dot1Q 10
 vrf forwarding CEA
 ip address 169.254.254.2 255.255.255.252
!
interface GigabitEthernet1.20
 description CEB
 encapsulation dot1Q 20
 vrf forwarding CEB
 ip address 169.254.254.2 255.255.255.252
!
interface GigabitEthernet1.45
 description GLOBAL-INET
 encapsulation dot1Q 45
 vrf forwarding GLOBAL-INET
 ip address 169.254.254.2 255.255.255.252
!
interface GigabitEthernet2
 no ip address
 shutdown
 negotiation auto
!
interface GigabitEthernet3
 ip address 169.254.200.2 255.255.255.252
 ip ospf 9809 area 0
 negotiation auto
!
interface GigabitEthernet4
 no ip address
 shutdown
 negotiation auto
!
router ospf 9809
 router-id 1.1.1.1
 prefix-suppression
 mpls ldp autoconfig
!
router bgp 9809
 bgp router-id 1.1.1.1
 bgp log-neighbor-changes
 neighbor 3.3.3.3 remote-as 9809
 neighbor 3.3.3.3 update-source Loopback0
 !
 address-family ipv4
  neighbor 3.3.3.3 activate
 exit-address-family
 !
 address-family vpnv4
  neighbor 3.3.3.3 activate
  neighbor 3.3.3.3 send-community extended
 exit-address-family
 !
 address-family ipv4 vrf CEA
  neighbor 169.254.254.1 remote-as 65511
  neighbor 169.254.254.1 activate
 exit-address-family
 !
 address-family ipv4 vrf CEB
  neighbor 169.254.254.1 remote-as 65511
  neighbor 169.254.254.1 activate
 exit-address-family
 !
 address-family ipv4 vrf GLOBAL-INET
  redistribute static
  neighbor 169.254.254.1 remote-as 65511
  neighbor 169.254.254.1 activate
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
ip route vrf GLOBAL-INET 45.117.99.0 255.255.255.0 169.254.254.1 name ASR1K-VRF-GLOBAL-INET
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

