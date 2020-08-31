NAT#sh run
NAT#sh running-config 
Building configuration...

Current configuration : 2037 bytes
!
! Last configuration change at 19:00:30 UTC Tue May 15 2018
!
upgrade fpd auto
version 15.0
service timestamps debug datetime msec
service timestamps log datetime msec
no service password-encryption
!
hostname NAT
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
crypto keyring DMVPN-KEYRING 
  pre-shared-key address 0.0.0.0 0.0.0.0 key MOTHERFUCKERS
!
crypto isakmp policy 10
 encr aes 256
 authentication pre-share
 group 2
crypto isakmp profile DMVPN-PHASE3
   keyring DMVPN-KEYRING
   match identity address 0.0.0.0 
!
crypto ipsec security-association replay window-size 1024
!
crypto ipsec transform-set ESP/NULL/MD5/TUNNEL esp-null esp-sha-hmac 
 mode transport
!
crypto ipsec profile DMVPN-PROFILE
 set transform-set ESP/NULL/MD5/TUNNEL 
 set isakmp-profile DMVPN-PHASE3
!
!
!
!
!         
!
!
interface Tunnel0
 ip address 10.1.1.3 255.255.255.0
 ip ospf network point-to-multipoint
 ip ospf 1 area 0
 tunnel source FastEthernet0/1
 tunnel destination 202.100.1.2
 tunnel protection ipsec profile DMVPN-PROFILE shared
 !
!
interface FastEthernet0/0
 ip address 192.168.1.254 255.255.255.0
 ip nat inside
 ip virtual-reassembly
 duplex auto
 speed auto
 !
!
interface FastEthernet0/1
 ip address 202.100.2.1 255.255.255.0
 ip nat outside
 ip virtual-reassembly
 duplex auto
 speed auto
 !
!
router ospf 1
 log-adjacency-changes
!
ip forward-protocol nd
no ip http server
no ip http secure-server
!
!
ip nat inside source list LAN interface FastEthernet0/1 overload
ip route 0.0.0.0 0.0.0.0 202.100.2.254
!
ip access-list extended LAN
 permit ip 192.168.1.0 0.0.0.255 any
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
 stopbits 1
line aux 0
 exec-timeout 0 0
 privilege level 15
 logging synchronous
 stopbits 1
line vty 0 4
 login
!
end

