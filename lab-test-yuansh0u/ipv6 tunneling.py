GRE tunnel : ip protocol 47 (IPV4/6)
IPIP tunnel : ip protocol 4 (IPV4)
ipv6 ip tunnel : ip protocol 41 (IPV6)
======================================
TOKYO#sh run inter tun 64

interface Tunnel64  
 description IPV4 OVER IPV6 GRE Tunnel and IPv6IP tunnel
 ip address 46.46.46.1 255.255.255.0
 shutdown
 tunnel source FastEthernet0/0.2
 tunnel mode gre [gre ipv6|ipv6ip]
 tunnel destination FC00:168:192:2:C82B:21FF:FE70:8
 !
end

interface Tunnel46
 description IPV6 OVER IPV4 GRE Tunnel and IPIP tunnel
 no ip address
 ipv6 address EEEE:EEEE:EEEE::1/64
 tunnel source FastEthernet0/0.2
 tunnel destination 168.192.2.1
 !
end

TOKYO# 


NEET#show run inter tun 64 
Building configuration...

Current configuration : 239 bytes
!
interface Tunnel64
 description IPV4 OVER IPV6 GRE Tunnel and IPv6IP tunnel
 ip address 46.46.46.2 255.255.255.0
 shutdown
 tunnel source FastEthernet0/0.2
 tunnel mode [gre ipv6|ipv6ip]
 tunnel destination FC00:168:192:1:C804:AFF:FED4:8
 !
end

NEET#show run inter tun 46
Building configuration...

Current configuration : 222 bytes
!
interface Tunnel46
 description IPV6 OVER IPV4 GRE Tunnel and IPIP tunnel
 no ip address
 ip virtual-reassembly
 ipv6 address EEEE:EEEE:EEEE::2/64
 tunnel source FastEthernet0/0.2
 tunnel destination 168.192.1.1
 !
end

NEET#
==========================================================================================

TOKYO/NEET:
 ip route 0.0.0.0 0.0.0.0 Tunnel64
 ipv6 route ::/0 Tunnel46

ip dhcp pool [TOKYO|NEET]-IPV4
   network 150.150.X.0 255.255.255.0
   default-router 150.150.X.X 
   dns-server 8.8.8.8 
ipv6 dhcp pool [TOKYO|NEET]-IPV6
 dns-server 2001:FFFF:FFFF:FFFF:FFFF::FFFF


 interface FastEthernet1/1
 description DUAL-STACK-TEST-PC
 ip address 150.150.X.X 255.255.255.0
 ip ospf 100 area 0
 ipv6 address FC00:150:150:X::X/64
 ipv6 nd other-config-flag
 ipv6 dhcp server [TOKYO|NEET]-IPV6
 !
 ========================
 router bgp 65511
 neighbor 168.192.X.X [shutdown] 
 neighbor FC00:168:192:X::X [shutdown]
========================================================================================