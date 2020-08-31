INET#SH RUN
INET#SH RUNning-config 
Building configuration...

Current configuration : 1383 bytes
!
! Last configuration change at 17:03:07 UTC Tue Mar 27 2018
!
version 15.5
service timestamps debug datetime msec
service timestamps log datetime msec
no platform punt-keepalive disable-kernel-core
platform console serial
!
hostname INET
!
boot-start-marker
boot-end-marker
!
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
license udi pid CSR1000V sn 9NIT1XWY5VG
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
interface GigabitEthernet1
 no ip address
 negotiation auto
!
interface GigabitEthernet1.15
 encapsulation dot1Q 15
 ip address 202.100.15.5 255.255.255.0
!
interface GigabitEthernet1.25
 encapsulation dot1Q 25
 ip address 202.100.25.5 255.255.255.0
!
interface GigabitEthernet1.35
 encapsulation dot1Q 35
 ip address 202.100.35.5 255.255.255.0
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

