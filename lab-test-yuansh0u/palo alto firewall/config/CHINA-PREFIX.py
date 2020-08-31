CHINA-PREFIX#sh running-config 
Building configuration...

Current configuration : 3272 bytes
!
! Last configuration change at 10:08:34 UTC Mon Jul 10 2017
!
version 15.2
service timestamps debug datetime msec
service timestamps log datetime msec
!
hostname CHINA-PREFIX
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
!
!
!
!
!
! 
crypto keyring SVTI  
  pre-shared-key address 202.20.71.1 key cisco
!
crypto isakmp policy 10
 encr 3des
 hash md5 
 authentication pre-share
 group 2
crypto isakmp profile SVTI
   keyring SVTI
   match identity address 202.20.71.1 255.255.255.255 
!
!
crypto ipsec transform-set ESP/NULL/MD5/TUNNEL esp-null esp-md5-hmac 
 mode tunnel
!
crypto ipsec profile SVTI
 set transform-set ESP/NULL/MD5/TUNNEL 
 set isakmp-profile SVTI
!
!
!
!
!
!
!
interface Tunnel0
 description CHINA-BGP
 ip address 100.64.2.254 255.255.255.0
 ip ospf network point-to-multipoint
 ip ospf 100 area 0
 tunnel source 219.230.229.249
 tunnel destination 202.10.71.1
!
interface Tunnel1
 description CHINA-BGP-Site-B
 ip address 100.64.20.254 255.255.255.0
 ip ospf network point-to-multipoint
 ip ospf 100 area 0
 tunnel source 219.230.229.249
 tunnel destination 202.20.71.1
!
interface Tunnel72
 ip address 172.16.72.1 255.255.255.252
 tunnel source Ethernet1/5
 tunnel mode ipsec ipv4
 tunnel destination 202.20.71.1
 tunnel protection ipsec profile SVTI
!
interface FastEthernet0/0
 no ip address
 shutdown 
 duplex full
!
interface Ethernet1/0
 no ip address
 shutdown
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
 ip address 219.230.229.249 255.255.255.0
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
router ospf 100
!
router bgp 9000
 bgp router-id 2.2.2.2
 bgp log-neighbor-changes
 no bgp default ipv4-unicast
 neighbor 100.64.2.1 remote-as 65555
 neighbor 100.64.20.1 remote-as 65556
 !
 address-family ipv4
  redistribute static
  neighbor 100.64.2.1 activate
  neighbor 100.64.2.1 send-community
  neighbor 100.64.2.1 route-map DENY-ALL-BGP-UPDATES in
  neighbor 100.64.2.1 route-map SET-BGP-NO-ADVERTISE-COMMUITY out
  neighbor 100.64.20.1 activate
  neighbor 100.64.20.1 send-community
  neighbor 100.64.20.1 route-map DENY-ALL-BGP-UPDATES in
  neighbor 100.64.20.1 route-map SET-BGP-NO-ADVERTISE-COMMUITY out
 exit-address-family
!
ip forward-protocol nd
!
!
no ip http server
no ip http secure-server
ip route 0.0.0.0 0.0.0.0 219.230.229.254
ip route 1.0.8.0 255.255.255.0 219.230.229.254 name CHINA-INET
ip route 1.0.9.0 255.255.255.0 219.230.229.254 name CHINA-INET
ip route 1.0.10.0 255.255.255.0 219.230.229.254 name CHINA-INET
ip route 1.0.11.0 255.255.255.0 219.230.229.254 name CHINA-INET
ip route 1.0.12.0 255.255.255.0 219.230.229.254 name CHINA-INET
!
ip access-list extended test
!
!
route-map SET-BGP-NO-ADVERTISE-COMMUITY permit 10
 set community no-advertise
!
route-map DENY-ALL-BGP-UPDATES deny 10
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
 login
!
!
end

CHINA-PREFIX#