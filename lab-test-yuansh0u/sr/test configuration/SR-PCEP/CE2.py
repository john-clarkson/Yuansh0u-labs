CE2#sh run
CE2#sh running-config 
Building configuration...

Current configuration : 2174 bytes
!
! Last configuration change at 15:46:25 UTC Mon Nov 20 2017
!
version 15.5
service timestamps debug datetime msec
service timestamps log datetime msec
no platform punt-keepalive disable-kernel-core
platform console serial
!
hostname CE2
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
license udi pid CSR1000V sn 9VFQSOPYPSW
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
 ip address 2.2.2.2 255.255.255.255
!
interface Loopback1
 vrf forwarding B
 ip address 2.2.2.2 255.255.255.255
!
interface GigabitEthernet1
 no ip address
 negotiation auto
!         
interface GigabitEthernet1.200
 encapsulation dot1Q 200
 vrf forwarding A
 ip address 169.254.200.1 255.255.255.0
!
interface GigabitEthernet1.201
 encapsulation dot1Q 201
 vrf forwarding B
 ip address 169.254.200.1 255.255.255.0
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
router bgp 65522
 bgp router-id 2.2.2.2
 bgp log-neighbor-changes
 neighbor 169.254.200.254 remote-as 9000
 !
 address-family ipv4
  no neighbor 169.254.200.254 activate
 exit-address-family
 !
 address-family ipv4 vrf A
  bgp router-id 2.2.2.2
  redistribute connected
  neighbor 169.254.200.254 remote-as 9000
  neighbor 169.254.200.254 activate
 exit-address-family
 !
 address-family ipv4 vrf B
  bgp router-id 2.2.2.2
  redistribute connected
  neighbor 169.254.200.254 remote-as 9000
  neighbor 169.254.200.254 activate
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

