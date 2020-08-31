ASR-1K#SH RUN
Building configuration...

Current configuration : 4450 bytes
!
! Last configuration change at 00:27:27 UTC Fri Jul 21 2017
!
version 15.5
service timestamps debug datetime msec
service timestamps log datetime msec
no platform punt-keepalive disable-kernel-core
platform console serial
!
hostname ASR-1K
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



no ip domain lookup
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
license udi pid CSR1000V sn 91MSSU3BVIT
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
 description ROUTER-ID
 ip address 169.254.254.255 255.255.255.255
!
interface Loopback45
 description GLOBAL-IP
 ip address 45.117.99.254 255.255.255.255
!
interface Tunnel0
 description CHINA-BGP
 ip address 100.64.1.1 255.255.255.252
 tunnel source 114.248.1.1
 tunnel destination 219.235.229.249
!
interface GigabitEthernet1
 no ip address
 negotiation auto
!
interface GigabitEthernet1.10
 description CEA
 encapsulation dot1Q 10
 vrf forwarding CEA
 ip address 169.254.254.1 255.255.255.252
!
interface GigabitEthernet1.20
 description CEB
 encapsulation dot1Q 20
 vrf forwarding CEB
 ip address 169.254.254.1 255.255.255.252
!
interface GigabitEthernet1.45
 encapsulation dot1Q 45
 ip address 169.254.254.1 255.255.255.252
 ip nat outside
!
interface GigabitEthernet2
 ip address 114.248.1.1 255.255.255.0
 ip nat outside
 negotiation auto
!
interface GigabitEthernet3
 no ip address
 negotiation auto
!         
interface GigabitEthernet3.45
!
interface GigabitEthernet3.58
 description CHINA-INET-PUBLIC-IP
 encapsulation dot1Q 58
 ip address 58.113.1.2 255.255.255.252
 ip nat inside
!
interface GigabitEthernet3.100
 description MPLS-CEA-GW
 encapsulation dot1Q 100
 vrf forwarding CEA
 ip address 10.254.100.2 255.255.255.252
!
interface GigabitEthernet3.172
 description INET-CUSTOMER-PRIVATE-SUBNETS
 encapsulation dot1Q 172
 ip address 172.16.1.254 255.255.0.0
 ip nat inside
!
interface GigabitEthernet3.200
 description MPLS-CEB-GW
 encapsulation dot1Q 200
 vrf forwarding CEB
 ip address 10.254.200.2 255.255.255.252
!
interface GigabitEthernet4
 no ip address
 shutdown
 negotiation auto
!
router bgp 65511
 bgp router-id 169.254.254.255
 bgp log-neighbor-changes
 neighbor 100.64.1.2 remote-as 9809
 !
 address-family ipv4
  neighbor 100.64.1.2 activate
  neighbor 100.64.1.2 route-map SET-NEXT-HOP-LOCAL-ISP in
 exit-address-family
 !
 address-family rtfilter unicast
 exit-address-family
 !
 address-family ipv4 vrf CEA
  neighbor 10.254.100.1 remote-as 65122
  neighbor 10.254.100.1 activate
  neighbor 169.254.254.2 remote-as 9809
  neighbor 169.254.254.2 activate
 exit-address-family
 !
 address-family ipv4 vrf CEB
  neighbor 10.254.200.1 remote-as 65133
  neighbor 10.254.200.1 activate
  neighbor 169.254.254.2 remote-as 9809
  neighbor 169.254.254.2 activate
 exit-address-family
!
!
virtual-service csr_mgmt
!
ip nat inside source route-map CHINA interface GigabitEthernet2 overload
ip nat inside source route-map GLOBAL interface Loopback45 overload
ip forward-protocol nd
!
ip http server
ip http authentication local
no ip http secure-server
ip route 0.0.0.0 0.0.0.0 169.254.254.2 name GLOBAL-INET
ip route 219.235.229.249 255.255.255.255 114.248.1.254 name CHINA-PE
!
ip access-list extended PRIVATE-CUSTOMER
 permit ip 172.16.0.0 0.0.255.255 any
ip access-list extended PUBLIC-IP-CUSTOMER
 permit ip 58.113.1.0 0.0.0.3 any
!
!
route-map GLOBAL permit 10
 match ip address PRIVATE-CUSTOMER
 match interface GigabitEthernet1.45
!
route-map GLOBAL permit 20
 match ip address PUBLIC-IP-CUSTOMER
 match interface GigabitEthernet1.45
!
route-map SET-NEXT-HOP-LOCAL-ISP permit 10
 set ip next-hop 114.248.1.254
!
route-map CHINA permit 10
 match ip address PRIVATE-CUSTOMER
 match interface GigabitEthernet2
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
          
