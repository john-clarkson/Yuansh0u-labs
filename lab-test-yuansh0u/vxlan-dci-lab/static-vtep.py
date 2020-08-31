static-vtep without control-plane
interface nve1
  no shutdown
  host-reachability protocol bgp
  source-interface loopback0
  member vni 10020
    ingress-replication protocol bgp
  member vni 10030
    ingress-replication protocol bgp
 
   member vni 101234 associate-vrf
 host-reachability protocol bgp
##vlan vxlan mapping
 ##all leaf
 interface nve1
  no shutdown
  source-interface loopback0
 no member vni 10020
    ingress-replication protocol bgp
 no member vni 10030
    ingress-replication protocol bgp
 no  member vni 50000
    peer-vtep 10.0.0.201
 no  member vni 101234 associate-vrf
 no host-reachability protocol bgp
##vlan vxlan mapping
vlan 50
  vn-segment 50000

##create vrf
vrf context vlan50
  vni 50000
##create SVI interface for testing only

interface Vlan50
  no shutdown
  vrf member vlan50
  ip address 50.1.1.1/24

##leaf1
   interface nve1
  no shutdown
  source-interface loopback0
  member vni 50000
    ingress-replication protocol static
      peer-ip 10.0.0.202
    peer-vtep 10.0.0.202
##leaf2
  interface nve1
  no shutdown
  source-interface loopback0
  member vni 50000
    ingress-replication protocol static
      peer-ip 10.0.0.201
    peer-vtep 10.0.0.201

DC2-LEAF1# ping 50.1.1.2 vrf vlan50 
PING 50.1.1.2 (50.1.1.2): 56 data bytes
64 bytes from 50.1.1.2: icmp_seq=0 ttl=254 time=396.05 ms
64 bytes from 50.1.1.2: icmp_seq=1 ttl=254 time=22.996 ms
64 bytes from 50.1.1.2: icmp_seq=2 ttl=254 time=18.462 ms
64 bytes from 50.1.1.2: icmp_seq=3 ttl=254 time=24.076 ms
64 bytes from 50.1.1.2: icmp_seq=4 ttl=254 time=30.938 ms

--- 50.1.1.2 ping statistics ---
5 packets transmitted, 5 packets received, 0.00% packet loss
round-trip min/avg/max = 18.462/98.504/396.05 ms
DC2-LEAF1# 
DC2-LEAF1# show ip route vrf vlan50 >show_ip_route_vrf_vlan50.cfg
DC2-LEAF1# show file bootflash:show_ip_route_vrf_vlan50.cfg
IP Route Table for VRF "vlan50"
'*' denotes best ucast next-hop
'**' denotes best mcast next-hop
'[x/y]' denotes [preference/metric]
'%<string>' in via output denotes VRF <string>

50.1.1.0/24, ubest/mbest: 1/0, attached
    *via 50.1.1.1, Vlan50, [0/0], 00:21:38, direct
50.1.1.1/32, ubest/mbest: 1/0, attached
    *via 50.1.1.1, Vlan50, [0/0], 00:21:38, local

DC2-LEAF1# 


DC2-LEAF1# show nve vni 50000 
Codes: CP - Control Plane        DP - Data Plane          
       UC - Unconfigured         SA - Suppress ARP        
       SU - Suppress Unknown Unicast
 
Interface VNI      Multicast-group   State Mode Type [BD/VRF]      Flags
--------- -------- ----------------- ----- ---- ------------------ -----
nve1      50000    UnicastStatic     Up    DP   L2 [50]                   

DC2-LEAF1# show nve vni 50000 detail 
VNI: 50000 
  NVE-Interface       : nve1
  Mcast-Addr          : UnicastStatic
  VNI State           : Up
  Mode                : data-plane
  VNI Type            : L2 [50]
  VNI Flags           :        
  Provision State     : vni-add-complete
  Vlan-BD             : 50
  SVI State           : n/a

DC2-LEAF1# 

##global aware!
##all leaf
no vrf context vlan50
default inter vlan 50
interface vlan 50
no shutdown
ip address 50.1.1.1/2/24

##
DC2-LEAF1# ping 50.1.1.2
PING 50.1.1.2 (50.1.1.2): 56 data bytes
64 bytes from 50.1.1.2: icmp_seq=0 ttl=254 time=219.962 ms
64 bytes from 50.1.1.2: icmp_seq=1 ttl=254 time=16.859 ms
64 bytes from 50.1.1.2: icmp_seq=2 ttl=254 time=25.432 ms
64 bytes from 50.1.1.2: icmp_seq=3 ttl=254 time=13.201 ms
64 bytes from 50.1.1.2: icmp_seq=4 ttl=254 time=21.803 ms

--- 50.1.1.2 ping statistics ---
5 packets transmitted, 5 packets received, 0.00% packet loss
round-trip min/avg/max = 13.201/59.451/219.962 ms


DC2-LEAF1# sh ip route 50.1.1.2
IP Route Table for VRF "default"
'*' denotes best ucast next-hop
'**' denotes best mcast next-hop
'[x/y]' denotes [preference/metric]
'%<string>' in via output denotes VRF <string>

50.1.1.2/32, ubest/mbest: 1/0, attached
    *via 50.1.1.2, Vlan50, [250/0], 00:00:59, am tunnelid: 0xffffffff encap: VXLAN
 
DC2-LEAF1# 


##RIB does not show 50.1.1.2

DC2-LEAF1# sh ip route 
IP Route Table for VRF "default"
'*' denotes best ucast next-hop
'**' denotes best mcast next-hop
'[x/y]' denotes [preference/metric]
'%<string>' in via output denotes VRF <string>

0.0.0.0/0, ubest/mbest: 1/0
    *via 172.16.1.254%DC1-SERVER, [1/0], 02:22:53, static
10.0.0.201/32, ubest/mbest: 2/0, attached
    *via 10.0.0.201, Lo0, [0/0], 02:22:40, local
    *via 10.0.0.201, Lo0, [0/0], 02:22:40, direct
10.0.0.202/32, ubest/mbest: 1/0
    *via 10.0.0.222, Eth1/1, [110/81], 02:22:16, ospf-2, intra
10.0.0.203/32, ubest/mbest: 1/0
    *via 10.0.0.222, Eth1/1, [110/81], 02:22:27, ospf-2, intra
10.0.0.222/32, ubest/mbest: 1/0
    *via 10.0.0.222, Eth1/1, [110/41], 02:22:32, ospf-2, intra
50.1.1.0/24, ubest/mbest: 1/0, attached
    *via 50.1.1.1, Vlan50, [0/0], 00:03:18, direct
50.1.1.1/32, ubest/mbest: 1/0, attached
    *via 50.1.1.1, Vlan50, [0/0], 00:03:18, local
172.16.2.0/24, ubest/mbest: 1/0
    *via 172.16.1.254%DC1-SERVER, [1/0], 02:22:53, static

DC2-LEAF1#

DC2-LEAF1# show forwarding distribution nve overlay-vlan 
nve/evpn state: enabled/disabled (disabled)

VFP counts: partition1 - 1  ; partition2 - 0
 Vlan: 50    SVP: 1     install: 1     Origin:Flood-and-Learn  VFP-region:1
Total count of Peers: 0

DC2-LEAF1# 