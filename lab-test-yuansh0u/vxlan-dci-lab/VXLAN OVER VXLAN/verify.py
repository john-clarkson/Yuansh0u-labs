##underlay VXLAN SPINE RR
DC2-SPINE# show bgp l2vpn evpn
BGP routing table information for VRF default, address family L2VPN EVPN
BGP table version is 263, Local Router ID is 10.0.0.222
Status: s-suppressed, x-deleted, S-stale, d-dampened, h-history, *-valid, >-best
Path type: i-internal, e-external, c-confed, l-local, a-aggregate, r-redist, I-injected
Origin codes: i - IGP, e - EGP, ? - incomplete, | - multipath, & - backup

   Network            Next Hop            Metric     LocPrf     Weight Path
Route Distinguisher: 10.0.0.201:3
*>i[5]:[0]:[0]:[24]:[192.168.20.0]:[0.0.0.0]/224
                      10.0.0.201               0        100          0 ?

Route Distinguisher: 10.0.0.201:32787
*>i[2]:[0]:[0]:[48]:[0011.0011.0011]:[0]:[0.0.0.0]/216
                      10.0.0.201                        100          0 i
*>i[2]:[0]:[0]:[48]:[9000.9000.1111]:[0]:[0.0.0.0]/216
                      10.0.0.201                        100          0 i
*>i[2]:[0]:[0]:[48]:[0011.0011.0011]:[32]:[192.168.20.2]/272
                      10.0.0.201                        100          0 i
*>i[2]:[0]:[0]:[48]:[9000.9000.1111]:[32]:[192.168.20.1]/272
                      10.0.0.201                        100          0 i
*>i[2]:[0]:[0]:[48]:[0011.0011.0011]:[128]:[fc00:192:168:20::2]/368
                      10.0.0.201                        100          0 i
*>i[2]:[0]:[0]:[48]:[9000.9000.1111]:[128]:[fc00:192:168:20::1]/368
                      10.0.0.201                        100          0 i

Route Distinguisher: 10.0.0.202:3
*>i[5]:[0]:[0]:[24]:[192.168.30.0]:[0.0.0.0]/224
                      10.0.0.202               0        100          0 ?

Route Distinguisher: 10.0.0.202:32797
*>i[2]:[0]:[0]:[48]:[0022.0022.0022]:[0]:[0.0.0.0]/216
                      10.0.0.202                        100          0 i
*>i[2]:[0]:[0]:[48]:[1234.5678.9abc]:[0]:[0.0.0.0]/216
                      10.0.0.202                        100          0 i
*>i[2]:[0]:[0]:[48]:[9000.9000.2222]:[0]:[0.0.0.0]/216
                      10.0.0.202                        100          0 i
*>i[2]:[0]:[0]:[48]:[0022.0022.0022]:[32]:[192.168.30.2]/272
                      10.0.0.202                        100          0 i
*>i[2]:[0]:[0]:[48]:[9000.9000.2222]:[32]:[192.168.30.1]/272
                      10.0.0.202                        100          0 i
*>i[2]:[0]:[0]:[48]:[0022.0022.0022]:[128]:[fc00:192:168:30::2]/368
                      10.0.0.202                        100          0 i
*>i[2]:[0]:[0]:[48]:[9000.9000.2222]:[128]:[fc00:192:168:30::1]/368
                      10.0.0.202                        100          0 i

DC2-SPINE#  

##OVERLAY Router VXLAN dummy-vxlan
##R1
interface Tunnel9000
 description VXLAN OVER VXLAN
 ip address 192.168.2.1 255.255.255.0
 ip pim sparse-mode
 ip ospf 1 area 0
 ipv6 address FC00:192:168:2::1/64
 ipv6 ospf 1 area 0
 tunnel source GigabitEthernet3.20
 tunnel mode vxlan ipv4 default-mac
 tunnel destination 192.168.30.1
 tunnel vrf DC2-R1
 tunnel vxlan vni 123456
##R2
interface Tunnel9000
 description VXLAN OVER VXLAN
 ip address 192.168.2.2 255.255.255.0
 ip pim sparse-mode
 ip ospf 1 area 0
 ipv6 address FC00:192:168:2::2/64
 ipv6 ospf 1 area 0
 tunnel source GigabitEthernet3.30
 tunnel mode vxlan ipv4 default-mac
 tunnel destination 192.168.20.1
 tunnel vrf DC2-R2
 tunnel vxlan vni 123456
end

XE-R4-DC2-R2#show platform software vxlan fp active udp-port 
VXLAN UDP Port: 4789
VXLAN GPE Tunnel UDP Port: 4790
VXLAN Dummy L2 Tunnel UDP Port: 4789
VXLAN UDP Source Port Range: 1025 - 65535
VXLAN GPE Tunnel UDP Source Port Range: 1025 - 65535
VXLAN Dummy L2 Tunnel UDP Source Port Range: 1025 - 65535

XE-R4-DC2-R2#
XE-R4-DC2-R2#sh inter tunnel 9000
Tunnel9000 is up, line protocol is up 
  Hardware is Tunnel
  Description: VXLAN OVER VXLAN
  Internet address is 192.168.2.2/24
  MTU 9950 bytes, BW 100 Kbit/sec, DLY 50000 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation TUNNEL, loopback not set
  Keepalive not set
  Tunnel linestate evaluation up
  Tunnel source 192.168.30.1 (GigabitEthernet3.30), destination 192.168.20.1
   Tunnel Subblocks:
      src-track:
         Tunnel9000 source tracking subblock associated with GigabitEthernet3.30
          Set of tunnels with source GigabitEthernet3.30, 1 member (includes iterators), on interface <OK>
  Tunnel protocol/transport UDP/IP
    TEID 0x0, sequencing disabled
    Checksumming of packets disabled
    VXLAN vni:123456, source_port:Dyn 5 tuple, destination_port:4789
    source_mac: 0000.5e00.5213, destination_mac: 0000.5e00.5214
  Tunnel TTL 255
  Tunnel transport MTU 1450 bytes
  Tunnel transmit bandwidth 8000 (kbps)
  Tunnel receive bandwidth 8000 (kbps)
  Last input 00:00:04, output never, output hang never
  Last clearing of "show interface" counters 03:24:00
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/0 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     1851 packets input, 163874 bytes, 0 no buffer
     Received 0 broadcasts (0 IP multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored, 0 abort
     2079 packets output, 285350 bytes, 0 underruns
     0 output errors, 0 collisions, 0 interface resets
     0 unknown protocol drops
     0 output buffer failures, 0 output buffers swapped out
XE-R4-DC2-R2#

XE-R4-DC2-R2#show ip os neighbor 

Neighbor ID     Pri   State           Dead Time   Address         Interface
100.64.1.1        0   FULL/  -        00:00:30    192.168.2.1     Tunnel9000
XE-R4-DC2-R2#show ipv os nei
XE-R4-DC2-R2#show ipv os neighbor 

            OSPFv3 Router with ID (100.64.1.4) (Process ID 1)

Neighbor ID     Pri   State           Dead Time   Interface ID    Interface
100.64.1.1        0   FULL/  -        00:00:34    16              Tunnel9000
XE-R4-DC2-R2#

copy running-config flash:vxlan_over_vxlan.crg
more flash:vxlan_over_vxlan.cfg