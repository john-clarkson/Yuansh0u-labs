
site1:
ip dhcp pool DHCP-IPV4
   network 150.150.1.0 255.255.255.0
   default-router 150.150.1.1 
   dns-server 8.8.8.8 

ipv6 dhcp pool DHCP-IPV6
 address prefix FC00:150:150:1::/64
 dns-server 2001:FFFF:FFFF:FFFF:FFFF::FFFF

interface FastEthernet0/1
 description DUAL-STACK-TEST-PC-1
 ip address 150.150.1.1 255.255.255.0

 ipv6 address FC00:150:150:1::1/64
 ipv6 nd managed-config-flag
 ipv6 dhcp server DHCP-IPV6

site2:
ip dhcp pool DHCP-IPV4
   network 150.150.2.0 255.255.255.0
   default-router 150.150.2.2 
   dns-server 8.8.8.8 

ipv6 dhcp pool DHCP-IPV6
 address prefix FC00:150:150:2::/64
 dns-server 2001:FFFF:FFFF:FFFF:FFFF::FFFF

interface FastEthernet0/1
 description DUAL-STACK-TEST-PC-1
 ip address 150.150.2.2 255.255.255.0
 ipv6 address FC00:150:150:2::2/64
 ipv6 nd managed-config-flag
 ipv6 dhcp server DHCP-IPV6


ip route 0.0.0.0 0.0.0.0 202.100.1.254 name DUAL-STACK-INET-IPV4
!
ipv6 route ::/0 2000:202:100:1::254 name DUAL-STACK-INET-IPV6

ip route 0.0.0.0 0.0.0.0 61.128.1.254 name DUAL-STACK-INET-IPV4
!
ipv6 route ::/0 2000:61:128:1::254 name DUAL-STACK-INET-IPV6


IPV6 VTI;

SITE1

crypto keyring IPV6 
  pre-shared-key address ipv6 2000:61:128:1::1/128 key MOTHERFUCKERS
!
crypto isakmp policy 10
 encr aes 256
 authentication pre-share
 group 2
crypto isakmp profile IPV6
   keyring IPV6 
   match identity address ipv6 2000:61:128:1::1/128 
!

crypto ipsec transform-set AES256/SHA/TUNNEL/TRANSPORT esp-aes 256 esp-sha-hmac 
 
!
crypto ipsec profile IPV6
 set transform-set AES256/SHA/TUNNEL/TRANSPORT 
 set isakmp-profile IPV6

interface Tunnel100
ipv6 address cccc:cccc::/64 eui-64
ipv6 enable
ipv6 cef
tunnel source f0/0
tunnel destination 2000:61:128:1::1
tunnel mode ipsec ipv6
tunnel protection ipsec profile IPV6



site2:
crypto keyring IPV6 
  pre-shared-key address ipv6 2000:202:100:1::1/128 key MOTHERFUCKERS
 
!
crypto isakmp policy 10
 encr aes 256
 authentication pre-share
 group 2
crypto isakmp profile IPV6
   keyring IPV6 
   match identity address ipv6 2000:202:100:1::1/128 
!

crypto ipsec transform-set AES256/SHA/TUNNEL/TRANSPORT esp-aes 256 esp-sha-hmac 
 
!
crypto ipsec profile IPV6
 set transform-set AES256/SHA/TUNNEL/TRANSPORT 
 set isakmp-profile IPV6

interface Tunnel100
ipv6 address cccc:cccc::/64 eui-64
ipv6 enable
tunnel source f0/0
tunnel destination 2000:202:100:1::1
tunnel mode ipsec ipv6
tunnel protection ipsec profile IPV6

=====================================================================
IPV4 VTI

Site1:
crypto keyring IPV4 
  pre-shared-key address  61.128.1.1  key MOTHERFUCKERS
!
crypto isakmp policy 10
 encr aes 256
 authentication pre-share
 group 2
crypto isakmp profile IPV4 
   keyring IPV4 
   match identity address  61.128.1.1 255.255.255.255
!

crypto ipsec transform-set AES256/SHA/TUNNEL/TRANSPORT esp-aes 256 esp-sha-hmac 
 
!
crypto ipsec profile IPV4 
 set transform-set AES256/SHA/TUNNEL/TRANSPORT 
 set isakmp-profile IPV4 

interface Tunnel101
ip address 12.1.1.1 255.255.255.0
tunnel source f0/0
tunnel destination 61.128.1.1
tunnel mode ipsec ipv4
tunnel protection ipsec profile IPV4

Site2:
crypto keyring IPV4 
  pre-shared-key address  202.100.1.1 key MOTHERFUCKERS
!
crypto isakmp policy 10
 encr aes 256
 authentication pre-share
 group 2
crypto isakmp profile IPV4 
   keyring IPV4 
   match identity address  202.100.1.1 255.255.255.255
!

crypto ipsec transform-set AES256/SHA/TUNNEL/TRANSPORT esp-aes 256 esp-sha-hmac 
 
!
crypto ipsec profile IPV4 
 set transform-set AES256/SHA/TUNNEL/TRANSPORT 
 set isakmp-profile IPV4 

interface Tunnel101
ip address 12.1.1.2 255.255.255.0
tunnel source f0/0
tunnel destination 202.100.1.1
tunnel mode ipsec ipv4
tunnel protection ipsec profile IPV4
====================================================================================

VTI does not work between WINDOWS 7. or lan;
GRE OVER ipsec WORK!

inter tunnel X  (ipv4)
 tunnel mode gre ip
inter tunnel X  (ipv6)
 tunnel mode gre ipv6 
======================================================
SITE_A#show cry isa sa
IPv4 Crypto ISAKMP SA
dst             src             state          conn-id status
61.128.1.1      202.100.1.1     QM_IDLE           1002 ACTIVE
202.100.1.1     61.128.1.1      QM_IDLE           1001 ACTIVE

IPv6 Crypto ISAKMP SA

 dst: 2000:61:128:1::1
 src: 2000:202:100:1::1
 state: QM_IDLE         conn-id:   1005 status: ACTIVE

SITE_A#

===================================================


