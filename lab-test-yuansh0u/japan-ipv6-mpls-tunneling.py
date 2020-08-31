JAPAN-P-RR
ipv6 unicast-routing
ipv6 cef
ipv6 multicast-routing
!
interface FastEthernet0/0
 ipv6 address 192:168:198::2/64
 ipv6 router isis 
 !
!
interface FastEthernet0/1
 ipv6 address 192:168:198:5::6/64
 ipv6 router isis
interface Loopback0
 ipv6 address 192:168:253:253::253/128

JAPAN-PE1
ipv6 unicast-routing
ipv6 cef
ipv6 multicast-routing

interface FastEthernet0/1
 ipv6 address 192:168:198::1/64
 ipv6 router isis 
interface Loopback0
 ipv6 address 192:168:251:251::251/128  

JAPAN-PE2
interface FastEthernet0/1 
 ipv6 address 192:168:198:5::5/64
 ipv6 router isis
interface Loopback0
 ipv6 address 192:168:252:252::252/128  

 ===============================================
JAPAN-P-RR#show ipv6 route
IPv6 Routing Table - default - 8 entries
Codes: C - Connected, L - Local, S - Static, U - Per-user Static route
       B - BGP, HA - Home Agent, MR - Mobile Router, R - RIP
       I1 - ISIS L1, I2 - ISIS L2, IA - ISIS interarea, IS - ISIS summary
       D - EIGRP, EX - EIGRP external, ND - Neighbor Discovery
       O - OSPF Intra, OI - OSPF Inter, OE1 - OSPF ext 1, OE2 - OSPF ext 2
       ON1 - OSPF NSSA ext 1, ON2 - OSPF NSSA ext 2
C   192:168:198::/64 [0/0]
     via FastEthernet0/0, directly connected
L   192:168:198::2/128 [0/0]
     via FastEthernet0/0, receive
C   192:168:198:5::/64 [0/0]
     via FastEthernet0/1, directly connected
L   192:168:198:5::6/128 [0/0]
     via FastEthernet0/1, receive
I2  192:168:251:251::251/128 [115/10]
     via FE80::C825:26FF:FECC:6, FastEthernet0/0
I2  192:168:252:252::252/128 [115/10]
     via FE80::C82C:24FF:FE38:6, FastEthernet0/1
LC  192:168:253:253::253/128 [0/0]
     via Loopback0, receive
L   FF00::/8 [0/0]
     via Null0, receive
JAPAN-P-RR# 


JAPAN-P-RR#ping ipv6  192:168:251:251::251

Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 192:168:251:251::251, timeout is 2 seconds:
!!!!!
Success rate is 100 percent (5/5), round-trip min/avg/max = 20/54/164 ms
JAPAN-P-RR#ping ipv6  192:168:252:252::252

Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 192:168:252:252::252, timeout is 2 seconds:
!!!!!
Success rate is 100 percent (5/5), round-trip min/avg/max = 4/40/84 ms
JAPAN-P-RR#
===========================================================================

TOKYO/NEET
 interface f0/0.2
   ipv6 address autoconfig
   ipv6 ns ra suppress
!
router bgp 65511
 address-family ipv4
  redistribute connected
 exit-address-family
 !
 address-family ipv6
  redistribute connected
 exit-address-family   

 PE:
 router bgp 1000
  address-family ipv6 vrf [TOKYO|NEET]]
  neighbor FC00:168:192:X remote-as 65511
  neighbor FC00:168:192:X activate
  neighbor FC00:168:192:X as-override
 exit-address-family
 =========================