6PE:
  UK-GERMANY
0001 0100 1100 0000: 0000 0000 0000 0000: 0000 0000 0000 0000: 0000 0000 0000 0000:0000 0000 0000 0000: 0000 00000000 0000: 0000 0000 0000 0000: 0000 0000 0000 0000
       D                                                                         64
  1   4    


decimal 0123456789
binary 
      1  0 1 1 0 0 =8+4+32
     32-16-8-4-2-1  
hex 0123456789 A  B  C  D  E  F
              10 11 12 13 14 15


UK#show run | sec router bgp
router bgp 65511
 bgp router-id 10.10.10.10
 bgp log-neighbor-changes
 neighbor 100.65.67.173 remote-as 9000
 neighbor 169.169.254.2 remote-as 9000
 neighbor FC00:169:169:254A::2 remote-as 9000
 !
 address-family ipv4
  no synchronization
  bgp dmzlink-bw
  network 1.1.1.0 mask 255.255.255.0
  network 181.11.0.0
  neighbor 100.65.67.173 activate
  neighbor 100.65.67.173 weight 999
  neighbor 100.65.67.173 filter-list 10 out
  neighbor 100.65.67.173 dmzlink-bw
  neighbor 169.169.254.2 activate
  neighbor 169.169.254.2 weight 1000
  neighbor 169.169.254.2 allowas-in
  neighbor 169.169.254.2 filter-list 10 out
  no auto-summary
 exit-address-family
 !        
 address-family ipv6
  network FC00:1:1:1::/64
  neighbor FC00:169:169:254A::2 activate
  neighbor FC00:169:169:254A::2 allowas-in
 exit-address-family
UK# 

=================================================================

GERMANY#sh run | se router bgp
router bgp 65511
 bgp router-id 20.20.20.20
 bgp log-neighbor-changes
 neighbor 169.169.254.6 remote-as 9000
 neighbor FC00:169:169:254B::6 remote-as 9000
 !
 address-family ipv4
  no synchronization
  bgp dmzlink-bw
  network 2.2.2.0 mask 255.255.255.0
  network 182.22.0.0
  neighbor 169.169.254.6 activate
  neighbor 169.169.254.6 allowas-in
  neighbor 169.169.254.6 filter-list 10 out
  neighbor 169.169.254.6 dmzlink-bw
  no neighbor FC00:169:169:254B::6 activate
  no auto-summary
 exit-address-family
 !
 address-family ipv6
  network FC00:2:2:2::/64
  neighbor FC00:169:169:254B::6 activate
  neighbor FC00:169:169:254B::6 allowas-in
 exit-address-family


PE_1:
  router bgp 9000
     address-family ipv6
  
  no synchronization
  neighbor 169.169.253.253 activate
  neighbor 169.169.253.253 send-label
  neighbor 169.169.254.254 activate
  neighbor 169.169.254.254 send-label
  neighbor FC00:169:169:254A::1 activate
 exit-address-family

PE_2:
router bgp 9000
 address-family ipv6
  no synchronization
  neighbor 169.169.253.253 activate
  neighbor 169.169.253.253 send-label
  neighbor 169.169.254.254 activate
  neighbor 169.169.254.254 send-label
  neighbor FC00:169:169:254B::5 activate
 exit-address-family

RR_1:
router bgp 9000
  address-family ipv6
  neighbor 169.169.253.1 activate
  neighbor 169.169.253.1 route-reflector-client
  neighbor 169.169.253.1 send-label
  neighbor 169.169.253.2 activate
  neighbor 169.169.253.2 route-reflector-client
  neighbor 169.169.253.2 send-label
 exit-address-family

RR_2:
router bgp 9000
  address-family ipv6
  neighbor 169.169.253.1 activate
  neighbor 169.169.253.1 route-reflector-client
  neighbor 169.169.253.1 send-label
  neighbor 169.169.253.2 activate
  neighbor 169.169.253.2 route-reflector-client
  neighbor 169.169.253.2 send-label
 exit-address-family

PE_1#show bgp ipv6 unicast 
BGP table version is 22, local router ID is 169.169.253.1
Status codes: s suppressed, d damped, h history, * valid, > best, i - internal,
              r RIB-failure, S Stale
Origin codes: i - IGP, e - EGP, ? - incomplete

   Network          Next Hop            Metric LocPrf Weight Path
*> FC00:1:1:1::/64  FC00:169:169:254A::1
                                             0             0 65511 i
*>iFC00:2:2:2::/64  ::FFFF:169.169.253.2
                                             0    100      0 65511 i
* i                 ::FFFF:169.169.253.2
                                             0    100      0 65511 i


PE_1#show bgp ipv6 unicast fc00:2:2:2::/64
BGP routing table entry for FC00:2:2:2::/64, version 21
Paths: (2 available, best #1, table default)
  Advertised to update-groups:
     9         
  65511
    ::FFFF:169.169.253.2 (metric 3) from 169.169.253.253 (169.169.253.253)
      Origin IGP, metric 0, localpref 100, valid, internal, best
      Originator: 169.169.253.2, Cluster list: 0.0.0.1
      mpls labels in/out nolabel/2004
  65511
    ::FFFF:169.169.253.2 (metric 3) from 169.169.254.254 (169.169.254.254)
      Origin IGP, metric 0, localpref 100, valid, internal
      Originator: 169.169.253.2, Cluster list: 0.0.0.1
      mpls labels in/out nolabel/2004
PE_1# 

RR_1# show bgp ipv6 unicast fc00:2:2:2::/64
BGP routing table entry for FC00:2:2:2::/64, version 18
Paths: (1 available, best #1, table default)
  Advertised to update-groups:
     4         
  65511, (Received from a RR-client)
    ::FFFF:169.169.253.2 (metric 3) from 169.169.253.2 (169.169.253.2)
      Origin IGP, metric 0, localpref 100, valid, internal, best
      mpls labels in/out nolabel/2004
RR_1#

RR_2#show bgp ipv6 unicast fc00:2:2:2::/64
BGP routing table entry for FC00:2:2:2::/64, version 20
Paths: (1 available, best #1, table default)
  Advertised to update-groups:
     5         
  65511, (Received from a RR-client)
    ::FFFF:169.169.253.2 (metric 3) from 169.169.253.2 (169.169.253.2)
      Origin IGP, metric 0, localpref 100, valid, internal, best
      mpls labels in/out nolabel/2004




PE_1#show bgp ipv6 unicast summary 
BGP router identifier 169.169.253.1, local AS number 9000
BGP table version is 22, main routing table version 22
2 network entries using 288 bytes of memory
3 path entries using 228 bytes of memory
2/2 BGP path/bestpath attribute entries using 248 bytes of memory
1 BGP rrinfo entries using 24 bytes of memory
1 BGP AS-PATH entries using 24 bytes of memory
2 BGP extended community entries using 48 bytes of memory
0 BGP route-map cache entries using 0 bytes of memory
0 BGP filter-list cache entries using 0 bytes of memory
BGP using 860 total bytes of memory
BGP activity 88/78 prefixes, 150/136 paths, scan interval 60 secs

Neighbor        V           AS MsgRcvd MsgSent   TblVer  InQ OutQ Up/Down  State/PfxRcd
169.169.253.253 4         9000      61      55       22    0    0 00:38:02        1
169.169.254.254 4         9000      59      55       22    0    0 00:38:04        1
FC00:169:169:254A::1
                4        65511      22      25       22    0    0 00:16:39        1
PE_1#

PE_1#show ipv6 route
IPv6 Routing Table - default - 5 entries
Codes: C - Connected, L - Local, S - Static, U - Per-user Static route
       B - BGP, HA - Home Agent, MR - Mobile Router, R - RIP
       I1 - ISIS L1, I2 - ISIS L2, IA - ISIS interarea, IS - ISIS summary
       D - EIGRP, EX - EIGRP external, ND - Neighbor Discovery
       O - OSPF Intra, OI - OSPF Inter, OE1 - OSPF ext 1, OE2 - OSPF ext 2
       ON1 - OSPF NSSA ext 1, ON2 - OSPF NSSA ext 2
B   FC00:1:1:1::/64 [20/0]
     via FE80::C820:1DFF:FEBC:8, FastEthernet0/0.10
B   FC00:2:2:2::/64 [200/0]
     via 169.169.253.2%default, indirectly connected
C   FC00:169:169:254A::/64 [0/0]
     via FastEthernet0/0.10, directly connected
L   FC00:169:169:254A::2/128 [0/0]
     via FastEthernet0/0.10, receive
L   FF00::/8 [0/0]
     via Null0, receive
PE_1# 


PE_1# show ipv6 cef
::/0
  no route
::/127
  discard
FC00:1:1:1::/64
  nexthop FE80::C820:1DFF:FEBC:8 FastEthernet0/0.10
FC00:2:2:2::/64
  nexthop 169.169.1.2 FastEthernet1/0 label 100 2004
FC00:169:169:254A::/64
  attached to FastEthernet0/0.10
FC00:169:169:254A::1/128
  attached to FastEthernet0/0.10
FC00:169:169:254A::2/128
  receive for FastEthernet0/0.10
FE80::/10
  receive for Null0
FF00::/8
  multicast
PE_1#

PE_1#show bgp all neighbors 
For address family: IPv4 Unicast

For address family: IPv6 Unicast
BGP neighbor is 169.169.253.253,  remote AS 9000, internal link
  BGP version 4, remote router ID 169.169.253.253
  BGP state = Established, up for 00:39:51
  Last read 00:00:30, last write 00:00:20, hold time is 180, keepalive interval is 60 seconds
  Neighbor sessions:
    1 active, is multisession capable
  Neighbor capabilities:
    Route refresh: advertised and received(new)
    Four-octets ASN Capability: advertised and received
    Address family IPv6 Unicast: advertised and received
    ipv6 MPLS Label capability: advertised and received
    Address family IPv4 MDT: advertised and received
    Address family VPNv4 Unicast: advertised and received
    Multisession Capability: advertised and received
  Message statistics, state Established:
    InQ depth is 0
    OutQ depth is 0

PE_1#show bgp ipv6 unicast labels 
   Network          Next Hop      In label/Out label
   FC00:1:1:1::/64  FC00:169:169:254A::1
                                    1006/nolabel
   FC00:2:2:2::/64  ::FFFF:169.169.253.2
                                    nolabel/2004
                    ::FFFF:169.169.253.2
                                    nolabel/2004


IDC-CORE# ping vrf UK FC00:2:2:2::254 SOUrce FC00:1:1:1::254 re 10

Type escape sequence to abort.
Sending 10, 100-byte ICMP Echos to FC00:2:2:2::254, timeout is 2 seconds:
Packet sent with a source address of FC00:1:1:1::254%UK
!!!!!!!!!!
Success rate is 100 percent (10/10), round-trip min/avg/max = 100/144/212 ms
IDC-CORE#


PE_1#show bgp ipv6 unicast  FC00:1:1:1::/64
BGP routing table entry for FC00:1:1:1::/64, version 2
Paths: (1 available, best #1, table default)
  Advertised to update-groups:
     10        
  65511
    FC00:169:169:254A::1 (FE80::C820:1DFF:FEBC:8) from FC00:169:169:254A::1 (10.10.10.10)
      Origin IGP, metric 0, localpref 100, valid, external, best
      mpls labels in/out 1007/nolabel

                     
PE_1#show mpls forwarding-table 
Local      Outgoing   Prefix           Bytes Label   Outgoing   Next Hop    
Label      Label      or Tunnel Id     Switched      interface              
1001       Pop Label  169.169.253.11/32   \
                                       0             Fa1/0      169.169.1.2 
1002       102        169.169.253.253/32   \
                                       0             Fa1/0      169.169.1.2 
1005       No Label   1.1.1.0/24[V]    8496          Fa0/0.10   169.169.254.1
1007       No Label   FC00:1:1:1::/64  10134         Fa0/0.10   FE80::C820:1DFF:FEBC:8
1011       No Label   181.11.0.0/16[V] 0             Fa0/0.10   169.169.254.1
1015       No Label   l2ckt(9000)      202790        Fa0/1      point2point 
1020       104        169.169.254.254/32   \
                                       0             Fa1/0      169.169.1.2 
1022       100        169.169.253.2/32 0             Fa1/0      169.169.1.2 
PE_1#

RR_1# show bgp ipv6 unicast fc00:1:1:1::/64
BGP routing table entry for FC00:1:1:1::/64, version 21
Paths: (1 available, best #1, table default)
  Advertised to update-groups:
     4         
  65511, (Received from a RR-client)
    ::FFFF:169.169.253.1 (metric 3) from 169.169.253.1 (169.169.253.1)
      Origin IGP, metric 0, localpref 100, valid, internal, best
      mpls labels in/out nolabel/1007
RR_1#

PE_2#show bgp ipv6 unicast  FC00:1:1:1::/64
BGP routing table entry for FC00:1:1:1::/64, version 28
Paths: (2 available, best #1, table default)
  Advertised to update-groups:
     8         
  65511
    ::FFFF:169.169.253.1 (metric 3) from 169.169.253.253 (169.169.253.253)
      Origin IGP, metric 0, localpref 100, valid, internal, best
      Originator: 169.169.253.1, Cluster list: 0.0.0.1
      mpls labels in/out nolabel/1007
  65511
    ::FFFF:169.169.253.1 (metric 3) from 169.169.254.254 (169.169.254.254)
      Origin IGP, metric 0, localpref 100, valid, internal
      Originator: 169.169.253.1, Cluster list: 0.0.0.1
      mpls labels in/out nolabel/1007
PE_2#



P1#
*Oct 17 05:15:55.753: MPLS turbo: Fa1/1: rx: Len 60 Stack {102 6 255} - ipv4 data
*Oct 17 05:15:59.625: MPLS turbo: Fa1/0: rx: Len 122 Stack {100 0 62} {2004 0 62} - ipv6 data
*Oct 17 05:15:59.629: MPLS turbo: Fa1/1: tx: Len 118 Stack {2004 0 61} - ipv6 data
*Oct 17 05:15:59.789: MPLS turbo: Fa1/1: rx: Len 122 Stack {101 0 62} {1006 0 62} - ipv6 data
*Oct 17 05:15:59.789: MPLS turbo: Fa1/0: tx: Len 118 Stack {1006 0 61} - ipv6 data

===================================================
6VPE:
CHINA-1#
 router bgp 65533
  address-family ipv6
  redistribute eigrp 300
  no synchronization
  neighbor FC00:169:169:FFAC::10 activate
  neighbor FC00:169:169:FFAC::10 filter-list 10 out
 exit-address-family

CHINA-2#
 router bgp 65533
 address-family ipv6
  redistribute eigrp 300
  no synchronization
  neighbor FC00:169:169:FFBC::14 activate
  neighbor FC00:169:169:FFBC::14 filter-list 10 out
 exit-address-family 

USA-1#
 router bgp 65533
 address-family ipv6
  redistribute ospf 6 match internal external 1 external 2
  no synchronization
  neighbor FC00:169:169:FFAE::22 activate
  neighbor FC00:169:169:FFAE::22 filter-list 10 out
 exit-address-family 

USA-2#
 router bgp 65533
 address-family ipv6
  redistribute ospf 6 match internal external 1 external 2
  no synchronization
  neighbor FC00:169:169:FFBE::26 activate
  neighbor FC00:169:169:FFBE::26 filter-list 10 out
 exit-address-family

PE:
vrf upgrade-cli multi-af-mode non-common-policies [Specify a particular VRF] 
 You are about to upgrade to the multi-AF VRF syntax commands.
You will lose any IPv6 address configured on interfaces
belonging to upgraded VRFs.

Are you sure ? [yes]: yes

interface f0/0.[X]
 ipv6 address fc00:x:x:x::x/64
 ipv6 nd ra suppressed

router bgp 9000
 address-family ipv6 vrf [NAME]
  no synchronization
  neighbor FC00:169:169:XXXX::XX remote-as 6XXXX
  neighbor FC00:169:169:XXXX::XX activate
 exit-address-family
 address-family vpnv6
  neighbor 169.169.253.253 activate
  neighbor 169.169.253.253 send-community extended
  neighbor 169.169.254.254 activate
  neighbor 169.169.254.254 send-community extended
 exit-address-family

RR:
router bgp 9000
 address-family vpnv6
  neighbor 169.169.253.1 activate
  neighbor 169.169.253.1 send-community extended
  neighbor 169.169.253.1 route-reflector-client
  neighbor 169.169.253.2 activate
  neighbor 169.169.253.2 send-community extended
  neighbor 169.169.253.2 route-reflector-client
  neighbor 169.169.253.3 activate
  neighbor 169.169.253.3 send-community extended
  neighbor 169.169.253.3 route-reflector-client
  neighbor 169.169.253.4 activate
  neighbor 169.169.253.4 send-community extended
  neighbor 169.169.253.4 route-reflector-client
 exit-address-family 
========================================
CHINA:
route-map SET_USA_PREFIX_EIGRPv6_BANDWIDTH_HIGHER permit 10
 match ipv6 address prefix-list [NAME] 
 set metric 50000 100 255 1 1500
route-map SET_USA_PREFIX_EIGRPv6_BANDWIDTH_HIGHER permit 20
 set metric 35000 100 255 1 1500

USA:
route-map SET_CHINA_PREFIX_OSPFv3_OE1 permit 10
 match ipv6 address prefix-list [NAME]
 set metric-type type-1
route-map SET_CHINA_PREFIX_OSPFv3_OE1 permit 20 
========================
BGP INTO IGP
CHINA:
ipv6 router eigrp 300
 redistribute bgp 65533 route-map SET_USA_PREFIX_EIGRPv6_BANDWIDTH_HIGHER
USA:
 ipv6 router ospf 6
 redistribute bgp 65556 route-map SET_CHINA_PREFIX_OSPFv3_OE1
=================================================================
US_KS_1#ping fc00:3:3:3::254 source lo0

Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to FC00:3:3:3::254, timeout is 2 seconds:
Packet sent with a source address of FC00:155:155:155::1
!!!!!
Success rate is 100 percent (5/5), round-trip min/avg/max = 180/229/284 ms
US_KS_1#

IDC-CORE#ping vrf CHINA IPV6 FC00:155:155:155::1

Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to FC00:155:155:155::1, timeout is 2 seconds:
!!!!!
Success rate is 100 percent (5/5), round-trip min/avg/max = 228/250/272 ms
IDC-CORE#

US_KS_1#show ipv6 route
IPv6 Routing Table - default - 20 entries
Codes: C - Connected, L - Local, S - Static, U - Per-user Static route
       B - BGP, HA - Home Agent, MR - Mobile Router, R - RIP
       I1 - ISIS L1, I2 - ISIS L2, IA - ISIS interarea, IS - ISIS summary
       D - EIGRP, EX - EIGRP external, ND - Neighbor Discovery
       O - OSPF Intra, OI - OSPF Inter, OE1 - OSPF ext 1, OE2 - OSPF ext 2
       ON1 - OSPF NSSA ext 1, ON2 - OSPF NSSA ext 2
OE1 FC00:3:3:3::/64 [110/2]
     via FE80::C81C:12FF:FE10:38, FastEthernet0/0
     via FE80::C81E:1EFF:FEE4:38, FastEthernet0/1
O   FC00:15:15:15::/64 [110/2]
     via FE80::C81C:12FF:FE10:38, FastEthernet0/0
O   FC00:25:25:25::/64 [110/2]
     via FE80::C81E:1EFF:FEE4:38, FastEthernet0/1
OE1 FC00:30:30:30::30/128 [110/2]
     via FE80::C81C:12FF:FE10:38, FastEthernet0/0
     via FE80::C81E:1EFF:FEE4:38, FastEthernet0/1
OE1 FC00:31:31:31::31/128 [110/2]
     via FE80::C81C:12FF:FE10:38, FastEthernet0/0
     via FE80::C81E:1EFF:FEE4:38, FastEthernet0/1
O   FC00:50:50:50::50/128 [110/1]
     via FE80::C81C:12FF:FE10:38, FastEthernet0/0
O   FC00:51:51:51::51/128 [110/1]
     via FE80::C81E:1EFF:FEE4:38, FastEthernet0/1
C   FC00:52:52:52::/64 [0/0]
     via FastEthernet0/1, directly connected
L   FC00:52:52:52::2/128 [0/0]
     via FastEthernet0/1, receive
C   FC00:55:55:55::/64 [0/0]
     via FastEthernet0/0, directly connected
L   FC00:55:55:55:55::1/128 [0/0]
     via FastEthernet0/0, receive
C   FC00:155:155:155::/64 [0/0]
     via Loopback0, directly connected
L   FC00:155:155:155::1/128 [0/0]
     via Loopback0, receive
O   FC00:155:155:155::2/128 [110/2]
     via FE80::C81E:1EFF:FEE4:38, FastEthernet0/1
     via FE80::C81C:12FF:FE10:38, FastEthernet0/0
OE1 FC00:183:31:3::/64 [110/2]
     via FE80::C81C:12FF:FE10:38, FastEthernet0/0
     via FE80::C81E:1EFF:FEE4:38, FastEthernet0/1
OE1 FC00:183:32:3::/64 [110/2]
     via FE80::C81C:12FF:FE10:38, FastEthernet0/0
     via FE80::C81E:1EFF:FEE4:38, FastEthernet0/1
OE1 FC00:183:33:3::/64 [110/2]
     via FE80::C81C:12FF:FE10:38, FastEthernet0/0
     via FE80::C81E:1EFF:FEE4:38, FastEthernet0/1
OE1 FC00:192:168:3::/64 [110/2]
     via FE80::C81C:12FF:FE10:38, FastEthernet0/0
     via FE80::C81E:1EFF:FEE4:38, FastEthernet0/1
OE1 FC00:192:168:30::/64 [110/2]
     via FE80::C81C:12FF:FE10:38, FastEthernet0/0
     via FE80::C81E:1EFF:FEE4:38, FastEthernet0/1
L   FF00::/8 [0/0]
     via Null0, receive
US_KS_1#

IDC-CORE#show ipv6 route
IPv6 Routing Table - default - 1 entries
Codes: C - Connected, L - Local, S - Static, U - Per-user Static route
       B - BGP, HA - Home Agent, MR - Mobile Router, R - RIP
       I1 - ISIS L1, I2 - ISIS L2, IA - ISIS interarea, IS - ISIS summary
       D - EIGRP, EX - EIGRP external, ND - Neighbor Discovery
       O - OSPF Intra, OI - OSPF Inter, OE1 - OSPF ext 1, OE2 - OSPF ext 2
       ON1 - OSPF NSSA ext 1, ON2 - OSPF NSSA ext 2
L   FF00::/8 [0/0]
     via Null0, receive
IDC-CORE#  show ipv6 route vrf CHINA
IPv6 Routing Table - CHINA - 23 entries
Codes: C - Connected, L - Local, S - Static, U - Per-user Static route
       B - BGP, HA - Home Agent, MR - Mobile Router, R - RIP
       I1 - ISIS L1, I2 - ISIS L2, IA - ISIS interarea, IS - ISIS summary
       D - EIGRP, EX - EIGRP external, ND - Neighbor Discovery
       O - OSPF Intra, OI - OSPF Inter, OE1 - OSPF ext 1, OE2 - OSPF ext 2
       ON1 - OSPF NSSA ext 1, ON2 - OSPF NSSA ext 2
C   FC00:3:3:3::/64 [0/0]
     via GigabitEthernet2/0.3, directly connected
L   FC00:3:3:3::254/128 [0/0]
     via GigabitEthernet2/0.3, receive
EX  FC00:15:15:15::/64 [170/77056]
     via FE80::C822:1DFF:FE40:6, GigabitEthernet1/0.300
     via FE80::C821:1DFF:FE40:6, GigabitEthernet1/0.301
EX  FC00:25:25:25::/64 [170/77056]
     via FE80::C822:1DFF:FE40:6, GigabitEthernet1/0.300
     via FE80::C821:1DFF:FE40:6, GigabitEthernet1/0.301
D   FC00:30:30:30::30/128 [90/130816]
     via FE80::C822:1DFF:FE40:6, GigabitEthernet1/0.300
D   FC00:31:31:31::31/128 [90/130816]
     via FE80::C821:1DFF:FE40:6, GigabitEthernet1/0.301
EX  FC00:50:50:50::50/128 [170/77056]
     via FE80::C822:1DFF:FE40:6, GigabitEthernet1/0.300
     via FE80::C821:1DFF:FE40:6, GigabitEthernet1/0.301
EX  FC00:51:51:51::51/128 [170/77056]
     via FE80::C822:1DFF:FE40:6, GigabitEthernet1/0.300
     via FE80::C821:1DFF:FE40:6, GigabitEthernet1/0.301
EX  FC00:52:52:52::/64 [170/77056]
     via FE80::C822:1DFF:FE40:6, GigabitEthernet1/0.300
     via FE80::C821:1DFF:FE40:6, GigabitEthernet1/0.301
EX  FC00:55:55:55::/64 [170/77056]
     via FE80::C822:1DFF:FE40:6, GigabitEthernet1/0.300
     via FE80::C821:1DFF:FE40:6, GigabitEthernet1/0.301
EX  FC00:155:155:155::1/128 [170/77056]
     via FE80::C822:1DFF:FE40:6, GigabitEthernet1/0.300
     via FE80::C821:1DFF:FE40:6, GigabitEthernet1/0.301
EX  FC00:155:155:155::2/128 [170/77056]
     via FE80::C822:1DFF:FE40:6, GigabitEthernet1/0.300
     via FE80::C821:1DFF:FE40:6, GigabitEthernet1/0.301
C   FC00:183:31:3::/64 [0/0]
     via Loopback31, directly connected
L   FC00:183:31:3::3/128 [0/0]
     via Loopback31, receive
C   FC00:183:32:3::/64 [0/0]
     via Loopback32, directly connected
L   FC00:183:32:3::3/128 [0/0]
     via Loopback32, receive
C   FC00:183:33:3::/64 [0/0]
     via Loopback33, directly connected
L   FC00:183:33:3::3/128 [0/0]
     via Loopback33, receive
C   FC00:192:168:3::/64 [0/0]
     via GigabitEthernet1/0.300, directly connected
L   FC00:192:168:3::1/128 [0/0]
     via GigabitEthernet1/0.300, receive
C   FC00:192:168:30::/64 [0/0]
     via GigabitEthernet1/0.301, directly connected
L   FC00:192:168:30::1/128 [0/0]
     via GigabitEthernet1/0.301, receive
L   FF00::/8 [0/0]
     via Null0, receive
IDC-CORE# 



PE_3#show bgp vpnv6 unicast all 
BGP table version is 304, local router ID is 169.169.253.3
Status codes: s suppressed, d damped, h history, * valid, > best, i - internal,
              r RIB-failure, S Stale
Origin codes: i - IGP, e - EGP, ? - incomplete

   Network          Next Hop            Metric LocPrf Weight Path
Route Distinguisher: 9000:300 (default for vrf CHINA)
*> FC00:3:3:3::/64  FC00:169:169:FFAC::9
                                         28416             0 65533 ?
*>iFC00:15:15:15::/64
                    ::FFFF:169.169.253.2
                                             2    100      0 65556 ?
*>iFC00:25:25:25::/64
                    ::FFFF:169.169.253.1
                                             2    100      0 65556 ?
*> FC00:31:31:31::31/128
                    FC00:169:169:FFAC::9
                                        156416             0 65533 ?
*>iFC00:50:50:50::50/128
                    ::FFFF:169.169.253.2


PE_3#show mpls forwarding-table 
Local      Outgoing   Prefix           Bytes Label   Outgoing   Next Hop    
Label      Label      or Tunnel Id     Switched      interface              
3000       No Label   3.3.3.0/24[V]    570           Fa0/0      169.169.254.9
3001       No Label   183.31.0.0/16[V] 0             Fa0/0      169.169.254.9
3002       No Label   183.32.0.0/16[V] 0             Fa0/0      169.169.254.9
3005       No Label   183.33.0.0/16[V] 0             Fa0/0      169.169.254.9
3006       No Label   38.38.38.0/24[V] 0             Fa0/0      169.169.254.9
3009       No Label   39.39.39.0/24[V] 0             Fa0/0      169.169.254.9
3011       No Label   192.168.3.0/24[V]   \
                                       0             Fa0/0      169.169.254.9
3012       No Label   192.168.30.0/24[V]   \
                                       0             Fa0/0      169.169.254.9
3013       No Label   31.31.31.0/24[V] 0             Fa0/0      169.169.254.9
3014       No Label   30.30.30.0/24[V] 0             Fa0/0      169.169.254.9
3015       No Label   169.169.254.8/30[V]   \
                                       0             aggregate/CHINA 
3016       104        169.169.254.254/32   \
                                       0             Fa1/0      169.169.1.10
3017       102        169.169.253.253/32   \
                                       0             Fa1/0      169.169.1.10
3018       Pop Label  169.169.253.11/32   \
                                       0             Fa1/0      169.169.1.10
3019       100        169.169.253.2/32 0             Fa1/0      169.169.1.10
Local      Outgoing   Prefix           Bytes Label   Outgoing   Next Hop    
Label      Label      or Tunnel Id     Switched      interface              
3020       101        169.169.253.1/32 0             Fa1/0      169.169.1.10
3021       103        169.169.253.4/32 0             Fa1/0      169.169.1.10
3022       No Label   FC00:192:168:30::/64[V]   \
                                       342           Fa0/0      FE80::C822:1DFF:FE40:8
3023       No Label   FC00:183:31:3::/64[V]   \
                                       0             Fa0/0      FE80::C822:1DFF:FE40:8
3024       No Label   FC00:183:32:3::/64[V]   \
                                       0             Fa0/0      FE80::C822:1DFF:FE40:8
3025       No Label   FC00:3:3:3::/64[V]   \
                                       28218         Fa0/0      FE80::C822:1DFF:FE40:8
3026       No Label   FC00:31:31:31::31/128[V]   \
                                       0             Fa0/0      FE80::C822:1DFF:FE40:8
3028       No Label   FC00:183:33:3::/64[V]   \
                                       0             Fa0/0      FE80::C822:1DFF:FE40:8
PE_3#

P1#
*Oct 17 19:29:54.522: MPLS turbo: Fa0/1: rx: Len 102 Stack {101 0 125} {1007 0 125} - ipv6 data
*Oct 17 19:29:54.526: MPLS turbo: Fa1/0: tx: Len 98 Stack {1007 0 124} - ipv6 data
*Oct 17 19:29:54.622: MPLS turbo: Fa1/1: rx: Len 102 Stack {105 0 62} {3008 0 62} - ipv6 data
*Oct 17 19:29:54.626: MPLS turbo: Fa0/0: tx: Len 98 Stack {3008 0 61} - ipv6 data
*Oct 17 19:29:54.998: MPLS turbo: Fa1/1: rx: Len 80 Stack {101 6 255} - ipv4 data
*Oct 17 19:29:55.514: MPLS turbo: Fa0/1: rx: Len 102 Stack {101 0 125} {1007 0 125} - ipv6 data
*Oct 17 19:29:55.518: MPLS turbo: Fa1/0: tx: Len 98 Stack {1007 0 124} - ipv6 data                    
================================================================================================






