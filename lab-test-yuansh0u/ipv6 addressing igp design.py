IPV6 devices:
ipv6 unicast-routing
ipv6 cef

IDC-CORE(config)#vrf upgrade-cli multi-af-mode common-policies 
You are about to upgrade to the multi-AF VRF syntax commands.
You will lose any IPv6 address configured on interfaces
belonging to upgraded VRFs.

Are you sure ? [yes]: yes
Number of VRFs upgraded: 0
IDC-CORE(config)#

OSPFV3

US_KS_1#sh run int f0/0
interface FastEthernet0/0
 ipv6 address FC00:55:55:55:55::1/64
 ipv6 nd ra suppress
 ipv6 ospf 6 area 0
 !
end

US_KS_1#sh run int f0/1
interface FastEthernet0/1
 ipv6 address FC00:52:52:52::2/64
 ipv6 nd ra suppress
 ipv6 ospf 6 area 0
 !
end

US_KS_1#

US_KS_2#show run int f0/0
interface FastEthernet0/0
 ipv6 address FC00:25:25:25::2/64
 ipv6 nd ra suppress
 ipv6 ospf 6 area 0
 !
end

US_KS_2#
US_KS_2#show run int f0/1
interface FastEthernet0/1
 ipv6 address FC00:15:15:15::1/64
 ipv6 nd ra suppress
 ipv6 ospf 6 area 0
 !
end

US_KS_2#

USA-1#show run inter f2/0
 ipv6 address FC00:55:55:55::254/64
 ipv6 nd ra suppress
 ipv6 ospf 6 area 0
 !
end

USA-1#show run inter f2/1 
 ipv6 address FC00:15:15:15::254/64
 ipv6 nd ra suppress
 ipv6 ospf 6 area 0
 !
end

USA-1#

USA-2#show run int f2/0
interface FastEthernet2/0
 ipv6 address autoconfig
 ipv6 nd ra suppress
 ipv6 ospf 6 area 0
 !
end

USA-2#show run int f2/1
interface FastEthernet2/1
 ipv6 address FC00:25:25:25::254/64
 ipv6 ospf 6 area 0
 !
end

USA-2#

========
OSPF v3
ipv6 router ospf 6
 router-id [IPv4 address format]

US_KS_1#show ipv6 ospf interface b
Interface    PID   Area            Intf ID    Cost  State Nbrs F/C
Lo0          6     0               10         1     LOOP  0/0
Fa0/1        6     0               4          1     DR    1/1
Fa0/0        6     0               3          1     DR    1/1

US_KS_1#show ipv6 ospf neighbor 

Neighbor ID     Pri   State           Dead Time   Interface ID    Interface
51.51.51.51       1   FULL/BDR        00:00:31    7               FastEthernet0/1
50.50.50.50       1   FULL/BDR        00:00:32    7               FastEthernet0/0

US_KS_1#show ipv6 route
IPv6 Routing Table - default - 12 entries
Codes: C - Connected, L - Local, S - Static, U - Per-user Static route
       B - BGP, HA - Home Agent, MR - Mobile Router, R - RIP
       I1 - ISIS L1, I2 - ISIS L2, IA - ISIS interarea, IS - ISIS summary
       D - EIGRP, EX - EIGRP external, ND - Neighbor Discovery
       O - OSPF Intra, OI - OSPF Inter, OE1 - OSPF ext 1, OE2 - OSPF ext 2
       ON1 - OSPF NSSA ext 1, ON2 - OSPF NSSA ext 2
O   FC00:15:15:15::/64 [110/2]
     via FE80::C81C:12FF:FE10:38, FastEthernet0/0
O   FC00:25:25:25::/64 [110/2]
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
     via FE80::C81C:12FF:FE10:38, FastEthernet0/0
     via FE80::C81E:1EFF:FEE4:38, FastEthernet0/1
L   FF00::/8 [0/0]
     via Null0, receive
US_KS_1#

US_KS_1# ping FC00:155:155:155::2     

Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to FC00:155:155:155::2, timeout is 2 seconds:
!!!!!
Success rate is 100 percent (5/5), round-trip min/avg/max = 32/46/64 ms
US_KS_1#

US_KS_1#ping ipv6 FC00:155:155:155::2

Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to FC00:155:155:155::2, timeout is 2 seconds:
!!!!!
Success rate is 100 percent (5/5), round-trip min/avg/max = 52/69/84 ms
US_KS_1#
=======================
eigrp v6


CHINA-1
ipv6 router eigrp 300
 eigrp router-id 30.30.30.30

CHINA-2
ipv6 router eigrp 300
 eigrp router-id 31.31.31.31

IDC-CORE
router eigrp CHINA
 !
 address-family ipv6 unicast vrf CHINA autonomous-system 300
  !
  topology base
  exit-af-topology
  eigrp router-id 183.33.3.3
 exit-address-family


CHINA-1#show ipv6 eigrp neighbors 
EIGRP-IPv6 Neighbors for AS(300)
H   Address                 Interface       Hold Uptime   SRTT   RTO  Q  Seq
                                            (sec)         (ms)       Cnt Num
0   Link-local address:     Fa0/1             12 00:08:41 1044  5000  0  6
    FE80::C800:1EFF:FE80:1C

IDC-CORE#show eigrp address-family ipv6 vrf CHINA interface
EIGRP-IPv6 VR(CHINA) Address-Family Interfaces for AS(300)
           VRF(CHINA)
                        Xmit Queue   Mean   Pacing Time   Multicast    Pending
Interface        Peers  Un/Reliable  SRTT   Un/Reliable   Flow Timer   Routes
Gi1/0.300          1        0/0        40       0/1          132           0
Gi1/0.301          1        0/0       101       0/1          464           0
Lo31               0        0/0         0       0/1            0           0
Lo32               0        0/0         0       0/1            0           0
Lo33               0        0/0         0       0/1            0           0
IDC-CORE#


IDC-CORE#show ipv6 rout vrf CHINA EIGRP
IPv6 Routing Table - CHINA - 13 entries
Codes: C - Connected, L - Local, S - Static, U - Per-user Static route
       B - BGP, HA - Home Agent, MR - Mobile Router, R - RIP
       I1 - ISIS L1, I2 - ISIS L2, IA - ISIS interarea, IS - ISIS summary
       D - EIGRP, EX - EIGRP external, ND - Neighbor Discovery
       O - OSPF Intra, OI - OSPF Inter, OE1 - OSPF ext 1, OE2 - OSPF ext 2
       ON1 - OSPF NSSA ext 1, ON2 - OSPF NSSA ext 2
D   FC00:30:30:30::30/128 [90/130816]
     via FE80::C822:1DFF:FE40:6, GigabitEthernet1/0.300
D   FC00:31:31:31::31/128 [90/130816]
     via FE80::C821:1DFF:FE40:6, GigabitEthernet1/0.301
IDC-CORE#

IDC-CORE#ping vrf CHINA ipv6 FC00:30:30:30::30

Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to FC00:30:30:30::30, timeout is 2 seconds:
!!!!!
Success rate is 100 percent (5/5), round-trip min/avg/max = 8/47/144 ms

IDC-CORE#ping vrf CHINA ipv6 FC00:31:31:31::31

Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to FC00:31:31:31::31, timeout is 2 seconds:
!!!!!
Success rate is 100 percent (5/5), round-trip min/avg/max = 24/73/128 ms
IDC-CORE#

============================================================


  
