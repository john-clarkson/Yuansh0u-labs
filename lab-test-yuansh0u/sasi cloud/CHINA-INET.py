CHINA-INET#sh run 
Building configuration...

Current configuration : 2686 bytes
!
! Last configuration change at 03:51:27 UTC Sun Jul 23 2017
!
version 15.2
service timestamps debug datetime msec
service timestamps log datetime msec
!
hostname CHINA-INET
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
 ip address 1.0.8.1 255.255.255.255
!
interface Loopback1
 ip address 1.0.1.1 255.255.255.255
!
interface Loopback2
 ip address 1.0.9.1 255.255.255.255
!
interface Loopback3
 ip address 1.0.10.1 255.255.255.255
!
interface Loopback4
 ip address 1.0.11.1 255.255.255.255
!
interface FastEthernet0/0
 no ip address
 shutdown
 duplex full
!         
interface Ethernet1/0
 ip address 114.248.1.254 255.255.255.0
 duplex full
!
interface Ethernet1/1
 ip address 219.235.229.254 255.255.255.0
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
router bgp 4808
 bgp log-neighbor-changes
 neighbor 219.235.229.249 remote-as 9809
 !
 address-family ipv4
  network 1.0.8.1 mask 255.255.255.255
  network 1.0.9.1 mask 255.255.255.255
  network 1.0.10.1 mask 255.255.255.255
  network 1.0.11.1 mask 255.255.255.255
  neighbor 219.235.229.249 activate
 exit-address-family
!
ip nat inside source static tcp 192.168.1.15 80 221.238.131.253 80 extendable
ip nat inside source static tcp 192.168.1.11 81 221.238.131.253 81 extendable
ip nat inside source static tcp 192.168.1.12 82 221.238.131.253 82 extendable
ip nat inside source static tcp 192.168.1.13 83 221.238.131.253 83 extendable
ip nat inside source static tcp 192.168.1.15 84 221.238.131.253 84 extendable
ip nat inside source static tcp 192.168.1.16 85 221.238.131.253 85 extendable
ip nat inside source static tcp 192.168.1.15 86 221.238.131.253 86 extendable
ip nat inside source static tcp 192.168.1.14 88 221.238.131.253 88 extendable
ip nat inside source static tcp 192.168.1.16 89 221.238.131.253 89 extendable
ip nat inside source static tcp 192.168.1.15 91 221.238.131.253 91 extendable
ip forward-protocol nd
!
!
ip http server
ip http authentication local
no ip http secure-server
ip route 58.113.1.0 255.255.255.252 114.248.1.1 name PUBLIC-IP
!
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

