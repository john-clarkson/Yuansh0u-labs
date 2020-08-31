CE2#sh run
CE2#sh running-config 
Building configuration...

Current configuration : 1857 bytes
!
! Last configuration change at 09:39:44 UTC Thu Jul 20 2017
!
version 15.2
service timestamps debug datetime msec
service timestamps log datetime msec
!
hostname CE2
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
ip dhcp pool LAN
 network 192.168.1.0 255.255.255.0
 default-router 192.168.1.254 
 dns-server 8.8.8.8 
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
interface FastEthernet0/0
 no ip address
 shutdown
 duplex full
!
interface Ethernet1/0
 description LAN
 ip address 192.168.1.254 255.255.255.0
 ip nat inside
 duplex full
!
interface Ethernet1/1
 ip address 172.16.1.1 255.255.0.0
 ip nat outside
 duplex full
!
interface Ethernet1/2
 description MPLS-VPN
 ip address 10.254.200.1 255.255.255.252
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
router bgp 65133
 bgp log-neighbor-changes
 neighbor 10.254.200.2 remote-as 65511
 !
 address-family ipv4
  network 192.168.1.0
  neighbor 10.254.200.2 activate
 exit-address-family
!
ip nat inside source route-map NAT interface Ethernet1/1 overload
ip forward-protocol nd
!
!
ip http server
ip http authentication local
no ip http secure-server
ip route 0.0.0.0 0.0.0.0 172.16.1.254
!
ip access-list extended LAN
 permit ip 192.168.1.0 0.0.0.255 any
!
no cdp advertise-v2
!
route-map NAT permit 10
 match ip address LAN
 match interface Ethernet1/1
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

