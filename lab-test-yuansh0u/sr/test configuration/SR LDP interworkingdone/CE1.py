CE1#sh run
CE1#sh running-config 
Building configuration...

Current configuration : 2108 bytes
!
! Last configuration change at 15:15:47 UTC Sat Nov 18 2017
!
version 15.5
service timestamps debug datetime msec
service timestamps log datetime msec
no platform punt-keepalive disable-kernel-core
platform console serial
!
hostname CE1
!
boot-start-marker
boot-end-marker
!
!
vrf definition A
 rd 1:1
 !
 address-family ipv4
 exit-address-family
!
vrf definition B
 rd 2:2
 !
 address-family ipv4
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
license udi pid CSR1000V sn 9VVTGTA61V7
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
 vrf forwarding A
 ip address 1.1.1.1 255.255.255.255
!
interface Loopback1
 vrf forwarding B
 ip address 1.1.1.1 255.255.255.255
!
interface GigabitEthernet1
 no ip address
 negotiation auto
!         
interface GigabitEthernet1.100
 encapsulation dot1Q 100
 vrf forwarding A
 ip address 169.254.100.1 255.255.255.0
!
interface GigabitEthernet1.101
 encapsulation dot1Q 101
 vrf forwarding B
 ip address 169.254.100.1 255.255.255.0
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
 no ip address
 shutdown 
 negotiation auto
!
router bgp 65511
 bgp router-id 1.1.1.1
 bgp log-neighbor-changes
 neighbor 169.254.100.254 remote-as 9000
 !
 address-family ipv4 vrf A
  bgp router-id 1.1.1.1
  redistribute connected
  neighbor 169.254.100.254 remote-as 9000
  neighbor 169.254.100.254 activate
 exit-address-family
 !
 address-family ipv4 vrf B
  bgp router-id 1.1.1.1
  redistribute connected
  neighbor 169.254.100.254 remote-as 9000
  neighbor 169.254.100.254 activate
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
 exec-timeout 0 0
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

