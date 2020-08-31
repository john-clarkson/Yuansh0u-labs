INET#sh run
INET#sh running-config 
Building configuration...

Current configuration : 1006 bytes
!
! Last configuration change at 19:03:33 UTC Tue May 15 2018
!
upgrade fpd auto
version 15.0
service timestamps debug datetime msec
service timestamps log datetime msec
no service password-encryption
!
hostname INET
!
boot-start-marker
boot-end-marker
!
!
no aaa new-model
!
!
!
ip source-route
no ip icmp rate-limit unreachable
ip cef    
!
!
!
!
no ip domain lookup
no ipv6 cef
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
redundancy
!
!
ip tcp synwait-time 5
! 
!         
!
!
!
!
!
!
interface FastEthernet0/0
 ip address 202.100.1.254 255.255.255.0
 duplex auto
 speed auto
 !
!
interface FastEthernet0/1
 ip address 202.100.2.254 255.255.255.0
 duplex auto
 speed auto
 !
!
ip forward-protocol nd
no ip http server
no ip http secure-server
!
!         
!
!
!
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
gatekeeper
 shutdown
!
!
line con 0
 exec-timeout 0 0
 privilege level 15
 logging synchronous
