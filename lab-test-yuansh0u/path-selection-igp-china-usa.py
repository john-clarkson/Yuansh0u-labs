perfer path:
specific route

  3.3.3.0 > CHINA-1 > USA-1> 5.5.5.0 
  183.31.0.0/16 > CHINA-2 > USA-2> 185.51.0.0/16
  183.32.0.0/16 > CHINA-2 > USA-2> 185.52.0.0/16
  183.33.0.0/16 > CHINA-2 > USA-2> 185.53.0.0/16
==================================================================
router ospf 30
 no redistribute bgp 65533 subnets
 no redistribute bgp 65533
 redistribute bgp 65533 subnets route-map SET_USA_PREFIX_OSPF_OE1
!
ip prefix-list SET_USA_PREFIX_OSPF_OE1 seq 5 permit 5.5.5.0/24  
!
route-map SET_USA_PREFIX_OSPF_OE1 permit 10
 match ip address prefix-list SET_USA_PREFIX_OSPF_OE1
 set metric-type type-1
route-map SET_USA_PREFIX_OSPF_OE1 permit 20

===================================
router ospf 30
 no redistribute bgp 65533 subnets
 no redistribute bgp 65533
 redistribute bgp 65533 subnets route-map SET_USA_PREFIX_OSPF_OE1
!
ip prefix-list SET_USA_PREFIX_OSPF_OE1 seq 5 permit 185.51.0.0/16
ip prefix-list SET_USA_PREFIX_OSPF_OE1 seq 10 permit 185.52.0.0/16
ip prefix-list SET_USA_PREFIX_OSPF_OE1 seq 15 permit 185.53.0.0/16
!
route-map SET_USA_PREFIX_OSPF_OE1 permit 10
 match ip address prefix-list SET_USA_PREFIX_OSPF_OE1
 set metric-type type-1
route-map SET_USA_PREFIX_OSPF_OE1 permit 20
=====================================

IDC-CORE#show ip route vrf CHINA 5.5.5.0

Routing Table: CHINA
Routing entry for 5.5.5.0/24
  Known via "ospf 30", distance 110, metric 2
  Tag 9000, type extern 1
  Last update from 192.168.3.254 on GigabitEthernet1/0.300, 00:10:34 ago
  Routing Descriptor Blocks:
  * 192.168.3.254, from 30.30.30.30, 00:10:34 ago, via GigabitEthernet1/0.300
      Route metric is 2, traffic share count is 1
      Route tag 9000
IDC-CORE#

IDC-CORE#show ip route vrf CHINA 185.51.0.0

Routing Table: CHINA
Routing entry for 185.51.0.0/16
  Known via "ospf 30", distance 110, metric 2
  Tag 9000, type extern 1
  Last update from 192.168.30.254 on GigabitEthernet1/0.301, 00:11:18 ago
  Routing Descriptor Blocks:
  * 192.168.30.254, from 31.31.31.31, 00:11:18 ago, via GigabitEthernet1/0.301
      Route metric is 2, traffic share count is 1
      Route tag 9000
IDC-CORE#show ip route vrf CHINA 185.52.0.0

Routing Table: CHINA
Routing entry for 185.52.0.0/16
  Known via "ospf 30", distance 110, metric 2
  Tag 9000, type extern 1
  Last update from 192.168.30.254 on GigabitEthernet1/0.301, 00:11:20 ago
  Routing Descriptor Blocks:
  * 192.168.30.254, from 31.31.31.31, 00:11:20 ago, via GigabitEthernet1/0.301
      Route metric is 2, traffic share count is 1
      Route tag 9000
IDC-CORE#show ip route vrf CHINA 185.53.0.0

Routing Table: CHINA
Routing entry for 185.53.0.0/16
  Known via "ospf 30", distance 110, metric 2
  Tag 9000, type extern 1
  Last update from 192.168.30.254 on GigabitEthernet1/0.301, 00:11:22 ago
  Routing Descriptor Blocks:
  * 192.168.30.254, from 31.31.31.31, 00:11:22 ago, via GigabitEthernet1/0.301
      Route metric is 2, traffic share count is 1
      Route tag 9000
IDC-CORE#
=================================================================================
IDC-CORE#show ip route vrf CHINA 50.50.50.50

Routing Table: CHINA
Routing entry for 50.50.50.0/24
  Known via "ospf 30", distance 110, metric 1
  Tag 9000, type extern 2, forward metric 1
  Last update from 192.168.3.254 on GigabitEthernet1/0.300, 00:11:31 ago
  Routing Descriptor Blocks:
  * 192.168.30.254, from 31.31.31.31, 00:21:30 ago, via GigabitEthernet1/0.301
      Route metric is 1, traffic share count is 1
      Route tag 9000
    192.168.3.254, from 30.30.30.30, 00:11:31 ago, via GigabitEthernet1/0.300
      Route metric is 1, traffic share count is 1
      Route tag 9000
IDC-CORE#
=========================================================================
  5.5.5.0 > USA-1 > CHINA-1> 3.3.3.0 
  185.51.0.0/16 > USA-2 > CHINA-2> 183.31.0.0/16
  185.52.0.0/16 > USA-2 > CHINA-2> 183.32.0.0/16
  185.53.0.0/16 > USA-2 > CHINA-2> 183.33.0.0/16
USA-1
route-map SET_CHINA_PREFIX_EIGRPv4_BANDWIDTH_HIGHER permit 10
 match ip address prefix-list SET_CHINA_PREFIX_EIGRPv4_BANDWIDTH_HIGHER
 set metric 50000 100 255 1 1500
route-map SET_CHINA_PREFIX_EIGRPv4_BANDWIDTH_HIGHER permit 20
 set metric 35000 100 255 1 1500
! 
router eigrp 500
 redistribute bgp 65556 route-map SET_CHINA_PREFIX_EIGRPv4_BANDWIDTH_HIGHER
ip prefix-list SET_CHINA_PREFIX_EIGRPv4_BANDWIDTH_HIGHER seq 5 permit 3.3.3.0/24
===============================================================================
USA-2
route-map SET_CHINA_PREFIX_EIGRPv4_BANDWIDTH_HIGHER permit 10
 match ip address prefix-list SET_CHINA_PREFIX_EIGRPv4_BANDWIDTH_HIGHER
 set metric 50000 100 255 1 1500
route-map SET_CHINA_PREFIX_EIGRPv4_BANDWIDTH_HIGHER permit 20
 set metric 35000 100 255 1 1500
! 
router eigrp 500
 redistribute bgp 65556 route-map SET_CHINA_PREFIX_EIGRPv4_BANDWIDTH_HIGHER
ip prefix-list SET_CHINA_PREFIX_EIGRPv4_BANDWIDTH_HIGHER seq 5 permit 183.31.0.0/16
ip prefix-list SET_CHINA_PREFIX_EIGRPv4_BANDWIDTH_HIGHER seq 10 permit 183.32.0.0/16
ip prefix-list SET_CHINA_PREFIX_EIGRPv4_BANDWIDTH_HIGHER seq 15 permit 183.33.0.0/16  
=================================================================================
IDC-CORE#show ip route vrf USA 3.3.3.0      

Routing Table: USA
Routing entry for 3.3.3.0/24
  Known via "eigrp 500", distance 170, metric 77056
  Tag 9000, type external
  Redistributing via eigrp 500
  Last update from 192.168.5.254 on GigabitEthernet1/0.500, 00:04:45 ago
  Routing Descriptor Blocks:
  * 192.168.5.254, from 192.168.5.254, 00:04:45 ago, via GigabitEthernet1/0.500
      Route metric is 77056, traffic share count is 1
      Total delay is 1010 microseconds, minimum bandwidth is 50000 Kbit
      Reliability 255/255, minimum MTU 1500 bytes
      Loading 1/255, Hops 1
      Route tag 9000
IDC-CORE#

IDC-CORE#show ip route vrf USA 183.31.0.0

Routing Table: USA
Routing entry for 183.31.0.0/16
  Known via "eigrp 500", distance 170, metric 77056
  Tag 9000, type external
  Redistributing via eigrp 500
  Last update from 192.168.50.254 on GigabitEthernet1/0.501, 00:05:10 ago
  Routing Descriptor Blocks:
  * 192.168.50.254, from 192.168.50.254, 00:05:10 ago, via GigabitEthernet1/0.501
      Route metric is 77056, traffic share count is 1
      Total delay is 1010 microseconds, minimum bandwidth is 50000 Kbit
      Reliability 255/255, minimum MTU 1500 bytes
      Loading 1/255, Hops 1
      Route tag 9000
IDC-CORE#show ip route vrf USA 183.32.0.0

Routing Table: USA
Routing entry for 183.32.0.0/16
  Known via "eigrp 500", distance 170, metric 77056
  Tag 9000, type external
  Redistributing via eigrp 500
  Last update from 192.168.50.254 on GigabitEthernet1/0.501, 00:05:14 ago
  Routing Descriptor Blocks:
  * 192.168.50.254, from 192.168.50.254, 00:05:14 ago, via GigabitEthernet1/0.501
      Route metric is 77056, traffic share count is 1
      Total delay is 1010 microseconds, minimum bandwidth is 50000 Kbit
      Reliability 255/255, minimum MTU 1500 bytes
      Loading 1/255, Hops 1
      Route tag 9000
IDC-CORE#show ip route vrf USA 183.33.0.0

Routing Table: USA
Routing entry for 183.33.0.0/16
  Known via "eigrp 500", distance 170, metric 77056
  Tag 9000, type external
  Redistributing via eigrp 500
  Last update from 192.168.50.254 on GigabitEthernet1/0.501, 00:05:16 ago
  Routing Descriptor Blocks:
  * 192.168.50.254, from 192.168.50.254, 00:05:16 ago, via GigabitEthernet1/0.501
      Route metric is 77056, traffic share count is 1
      Total delay is 1010 microseconds, minimum bandwidth is 50000 Kbit
      Reliability 255/255, minimum MTU 1500 bytes
      Loading 1/255, Hops 1
      Route tag 9000
IDC-CORE#
=============================================================
IDC-CORE#show ip eigrp vrf USA topology detail-links 
EIGRP-IPv4 VR(USA) Topology Table for AS(500)/ID(5.5.5.5)
           Topology(base) TID(0) VRF(USA)
Codes: P - Passive, A - Active, U - Update, Q - Query, R - Reply,
       r - reply Status, s - sia Status 

P 183.31.0.0/16, 1 successors, FD is 77056, tag is 9000, serno 506
        via 192.168.50.254 (77056/76800), GigabitEthernet1/0.501
        via 192.168.5.254 (98816/98560), GigabitEthernet1/0.500
P 183.32.0.0/16, 1 successors, FD is 77056, tag is 9000, serno 507
        via 192.168.50.254 (77056/76800), GigabitEthernet1/0.501
        via 192.168.5.254 (98816/98560), GigabitEthernet1/0.500
P 183.33.0.0/16, 1 successors, FD is 77056, tag is 9000, serno 508
        via 192.168.50.254 (77056/76800), GigabitEthernet1/0.501
        via 192.168.5.254 (98816/98560), GigabitEthernet1/0.500
P 3.3.3.0/24, 1 successors, FD is 77056, tag is 9000, serno 511
        via 192.168.5.254 (77056/76800), GigabitEthernet1/0.500
        via 192.168.50.254 (98816/98560), GigabitEthernet1/0.501
IDC-CORE# 
===========================================================
IDC-CORE#traceroute vrf CHINA 5.5.5.254 source 3.3.3.254

Type escape sequence to abort.
Tracing the route to 5.5.5.254

  1 192.168.3.254 36 msec 116 msec 60 msec
  2 169.169.254.10 52 msec 116 msec 52 msec
  3 169.169.1.10 [MPLS: Labels 106/1008 Exp 0] 164 msec 164 msec 152 msec
  4 169.169.254.22 [MPLS: Label 1008 Exp 0] 112 msec 108 msec 112 msec
  5 169.169.254.21 136 msec 104 msec 124 msec
  6 192.168.5.1 184 msec 100 msec 116 msec
IDC-CORE#
----------------------------------------------------------------
IDC-CORE#traceroute vrf CHINA 185.51.5.5 source 183.31.3.3

Type escape sequence to abort.
Tracing the route to 185.51.5.5

  1 192.168.30.254 92 msec 48 msec 28 msec
  2 169.169.254.14 156 msec 108 msec 76 msec
  3 169.169.2.14 [MPLS: Labels 208/2023 Exp 0] 160 msec 132 msec 80 msec
  4 169.169.254.26 [MPLS: Label 2023 Exp 0] 340 msec 212 msec 136 msec
  5 169.169.254.25 204 msec 108 msec 172 msec
  6 192.168.50.1 248 msec 192 msec 160 msec
IDC-CORE#
-----------------------------------------------------------------
IDC-CORE#traceroute vrf USA 3.3.3.254 source 5.5.5.254    

Type escape sequence to abort.
Tracing the route to 3.3.3.254

  1 192.168.5.254 60 msec 92 msec 76 msec
  2 169.169.254.22 124 msec 88 msec 68 msec
  3 169.169.1.2 [MPLS: Labels 105/3013 Exp 0] 152 msec 136 msec 116 msec
  4 169.169.254.10 [MPLS: Label 3013 Exp 0] 120 msec 116 msec 196 msec
  5 169.169.254.9 252 msec 180 msec 124 msec
  6 192.168.3.1 232 msec 136 msec 156 msec
IDC-CORE#
------------------------------------------------------------------
IDC-CORE#traceroute vrf USA 183.31.3.3 source 185.51.5.5

Type escape sequence to abort.
Tracing the route to 183.31.3.3

  1 192.168.50.254 56 msec 64 msec 88 msec
  2 169.169.254.26 64 msec 72 msec 88 msec
  3 169.169.2.6 [MPLS: Labels 207/4010 Exp 0] 156 msec 108 msec 108 msec
  4 169.169.254.14 [MPLS: Label 4010 Exp 0] 96 msec 244 msec 268 msec
  5 169.169.254.13 196 msec 196 msec 132 msec
  6 192.168.30.1 312 msec 212 msec 364 msec
IDC-CORE#