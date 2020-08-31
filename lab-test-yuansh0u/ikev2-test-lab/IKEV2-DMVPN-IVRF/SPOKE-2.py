SPOKE-2#sh run
SPOKE-2#sh running-config 
Building configuration...

Current configuration : 2975 bytes
!
! Last configuration change at 17:37:43 UTC Tue Mar 27 2018
!
version 15.5
service timestamps debug datetime msec
service timestamps log datetime msec
no platform punt-keepalive disable-kernel-core
platform console serial
!
hostname SPOKE-2
!
boot-start-marker
boot-end-marker
!
!
vrf definition IWAN-TRANSPORT-1
 rd 1:1
 !
 address-family ipv4
 exit-address-family
!
vrf definition inside-vrf
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
license udi pid CSR1000V sn 9729C6JYOSD
!
spanning-tree extend system-id
!
!
redundancy
!
crypto ikev2 proposal AES/CBC/256 
 encryption aes-cbc-256
 integrity sha512
 group 14
!
!
crypto ikev2 keyring DMVPN-KEYRING-1
 peer ANY
  address 0.0.0.0 0.0.0.0
  pre-shared-key c1sco123
 !
!
!
crypto ikev2 profile FVRF-IKEv2-IWAN-TRANSPORT-1
 match fvrf IWAN-TRANSPORT-1
 match identity remote address 0.0.0.0 
 authentication remote pre-share
 authentication local pre-share
 keyring local DMVPN-KEYRING-1
 ivrf inside-vrf
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
crypto ipsec security-association replay window-size 1024
!
crypto ipsec transform-set AES256/SHA/TRANSPORT esp-aes 256 esp-sha-hmac 
 mode transport
!
crypto ipsec profile DMVPN-PROFILE-TRANSPORT-1
 set transform-set AES256/SHA/TRANSPORT 
 set ikev2-profile FVRF-IKEv2-IWAN-TRANSPORT-1
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
 vrf forwarding inside-vrf
 ip address 192.168.20.1 255.255.255.0
!
interface Tunnel0
 vrf forwarding inside-vrf
 ip address 100.64.1.2 255.255.255.0
 no ip redirects
 ip mtu 1400
 ip nhrp network-id 101
 ip nhrp nhs 100.64.1.100 nbma 202.100.15.1 multicast
 ip nhrp registration no-unique
 ip nhrp shortcut
 ip tcp adjust-mss 1360
 tunnel source GigabitEthernet1.35
 tunnel mode gre multipoint
 tunnel key 101
 tunnel vrf IWAN-TRANSPORT-1
 tunnel protection ipsec profile DMVPN-PROFILE-TRANSPORT-1
!
interface GigabitEthernet1
 no ip address
 negotiation auto
!
interface GigabitEthernet1.35
 description INET-Front-door
 encapsulation dot1Q 35
 vrf forwarding IWAN-TRANSPORT-1
 ip address 202.100.35.1 255.255.255.0
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
router eigrp OVERLAY
 !
 address-family ipv4 unicast vrf inside-vrf autonomous-system 500
  !
  topology base
  exit-af-topology
  network 100.64.1.0 0.0.0.255
  network 192.168.20.0
  eigrp router-id 22.22.22.22
 exit-address-family
!
!
virtual-service csr_mgmt
!
ip forward-protocol nd
!
no ip http server
no ip http secure-server
ip route vrf IWAN-TRANSPORT-1 0.0.0.0 0.0.0.0 202.100.35.5
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

