IPV6 over IPV4 DMVPN
SITE_A(config-if)#ip nhrp redirect 
% NHRP-WARNING: 'ip nhrp redirect' failed to initialise
SITE_A(config-if)#

hub:
interface Tunnel 1234
 ip address 20.169.169.254 255.255.255.0
 no ip redirects
 ip mtu 1400
 ip nhrp map multicast dynamic
 ip nhrp network-id 300
 ip nhrp shortcut
 ip nhrp redirect
 ip tcp adjust-mss 1360
 ip ospf network broadcast
 ip ospf priority 255
 ip ospf 4 area 0
 tunnel source FastEthernet0/0
 tunnel mode gre multipoint
 tunnel key 54321

spoke:
interface Tunnel1234
 ip address 20.169.169.1 255.255.255.0
 no ip redirects
 ip mtu 1400
 ip nhrp map 20.169.169.254 202.100.1.1
 ip nhrp map multicast 202.100.1.1
 ip nhrp network-id 300
 ip nhrp nhs 20.169.169.254
 ip nhrp shortcut
 ip tcp adjust-mss 1360
 ip ospf network broadcast
 ip ospf priority 0
 ip ospf 4 area 0
 tunnel source FastEthernet0/0
 tunnel mode gre multipoint
 tunnel key 54321

interface Tunnel1234
 ip address 20.169.169.2 255.255.255.0
 no ip redirects
 ip mtu 1400
 ip nhrp map 20.169.169.254 202.100.1.1
 ip nhrp map multicast 202.100.1.1
 ip nhrp network-id 300
 ip nhrp nhs 20.169.169.254
 ip nhrp shortcut
 ip tcp adjust-mss 1360
 ip ospf network broadcast
 ip ospf priority 0
 ip ospf 4 area 0
 tunnel source FastEthernet0/0
 tunnel mode gre multipoint
 tunnel key 54321

crypto keyring IPV4-DMVPN	 
  pre-shared-key address  0.0.0.0  key MOTHERFUCKERS
!
crypto isakmp policy 10
 encr aes 256
 authentication pre-share
 group 2
crypto isakmp profile IPV4-DMVPN 
   keyring IPV4-DMVPN
   match identity address  0.0.0.0
!

crypto ipsec transform-set AES256/SHA/TUNNEL/TRANSPORT esp-aes 256 esp-sha-hmac
 mode TRANSPORT 
 
!
crypto ipsec profile IPV4-DMVPN 
 set transform-set AES256/SHA/TUNNEL/TRANSPORT 
 set isakmp-profile IPV4-DMVPN

interface Tunnel1234
 tunnel protection ipsec profile IPV4-DMVPN
 ================================================
 router opsf 4
  router-id x.x.x.x
spoke1:
 interface loopback0
   ip address 1.1.1.1 255.255.255.255
   ip ospf 4 area 0

spoke2:   
 interface loopback0
   ip address 2.2.2.2 255.255.255.255
   ip ospf 4 area 0   
=================================
spoke:
interface tunnel 1234
  ipv6 address FE80::1/2 link-local
  ipv6 address FC00:20:169:169::1/2/64
  ipv6 nhrp map FC00:20:169:169::254/128 202.100.1.1
  ipv6 nhrp network-id 300
  ipv6 nhrp nhs FC00:20:169:169::254

 router eigrp IPV6
 !
 address-family ipv6 unicast autonomous-system 1000
  !
  topology base
  exit-af-topology
  eigrp router-id 123.123.123.1/2/254
 exit-address-family
 =========================================
