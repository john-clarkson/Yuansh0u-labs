CEB-DC#sh run
CEB-DC#sh running-config 
Building configuration...

Current configuration : 1529 bytes
!
! Last configuration change at 04:58:17 UTC Wed Jul 19 2017
!
version 15.2
service timestamps debug datetime msec
service timestamps log datetime msec
!
hostname CEB-DC
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
ip cef    
no ipv6 cef
!         
!         
multilink bundle-name authenticated
!         
!         
!         
!         
!         
!         
!         
username cisco privilege 15 password 0 cisco
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
 ip address 192.168.100.254 255.255.255.255
!
interface FastEthernet0/0
 no ip address
 shutdown
 duplex full
!         
interface Ethernet1/0
 ip address 169.254.2.1 255.255.255.252
 duplex full
!
interface Ethernet1/1
 no ip address
 shutdown
 duplex full
!
interface Ethernet1/2
 no ip address
 shutdown
 duplex full
!
interface Ethernet1/3
 no ip address
 shutdown
 duplex full
!
interface Ethernet1/4
 no ip address
 shutdown
 duplex full
!
interface Ethernet1/5
 no ip address
 shutdown
 duplex full
!
interface Ethernet1/6
 no ip address
 shutdown
 duplex full
!
interface Ethernet1/7
 no ip address
 shutdown
 duplex full
!
router bgp 65533
 bgp router-id 192.168.100.254
 bgp log-neighbor-changes
 neighbor 169.254.2.2 remote-as 9809
 !
 address-family ipv4
  network 192.168.100.254 mask 255.255.255.255
  neighbor 169.254.2.2 activate
 exit-address-family
!
ip forward-protocol nd
!
!
ip http server
ip http authentication local
no ip http secure-server
!
no cdp advertise-v2
!
!
!
control-plane
!
!
line con 0
 stopbits 1
line aux 0
 stopbits 1
line vty 0 4
 password cisco
 login local
 transport input all
!
!
end

