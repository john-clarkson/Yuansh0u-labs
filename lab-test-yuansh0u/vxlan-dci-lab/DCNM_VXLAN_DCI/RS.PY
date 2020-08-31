RS# sh run | no

!Command: show running-config
!Running configuration last done at: Mon Jan 13 14:12:08 2020
!Time: Mon Jan 13 15:00:55 2020

version 9.3(2) Bios:version  
switchname RS
vdc RS id 1
  limit-resource vlan minimum 16 maximum 4094
  limit-resource vrf minimum 2 maximum 4096
  limit-resource port-channel minimum 0 maximum 511
  limit-resource u4route-mem minimum 248 maximum 248
  limit-resource u6route-mem minimum 96 maximum 96
  limit-resource m4route-mem minimum 58 maximum 58
  limit-resource m6route-mem minimum 8 maximum 8

cfs eth distribute
nv overlay evpn
feature ospf
feature bgp
feature interface-vlan
feature vn-segment-vlan-based
feature vpc
feature lldp
feature nv overlay

username admin password 5 $5$x8iJ9sIz$xdPQxvFwfe3Stp.VJM4DR5RpmED1.nGkCl6/bkYLNr4  role network-admin
ip domain-lookup
ip name-server 4.2.2.1 use-vrf management
no system default switchport
copp profile strict
snmp-server user admin network-admin auth md5 0x611e652c8ebc7b06222bf2cb99efaaf9 priv 0x611e652c8ebc7b06222bf2cb99efaaf9 localizedkey
rmon event 1 description FATAL(1) owner PMON@FATAL
rmon event 2 description CRITICAL(2) owner PMON@CRITICAL
rmon event 3 description ERROR(3) owner PMON@ERROR
rmon event 4 description WARNING(4) owner PMON@WARNING
rmon event 5 description INFORMATION(5) owner PMON@INFO

vlan 1

route-map next-hop-unchange permit 10
  set ip next-hop unchanged
vrf context management
  ip name-server 4.2.2.1
  ip route 0.0.0.0/0 150.1.93.254


interface Vlan1

interface Ethernet1/1
  ip address 169.254.93.2/30
  ip router ospf 1 area 0.0.0.0
  no shutdown

interface Ethernet1/2
  ip address 169.254.93.5/30
  ip router ospf 1 area 0.0.0.0
  no shutdown

interface Ethernet1/3

interface Ethernet1/4

interface Ethernet1/5

interface Ethernet1/6

interface Ethernet1/7

interface Ethernet1/8

interface Ethernet1/9

interface Ethernet1/10

interface Ethernet1/11

interface Ethernet1/12

interface Ethernet1/13

interface Ethernet1/14

interface Ethernet1/15

interface Ethernet1/16

interface Ethernet1/17

interface Ethernet1/18

interface Ethernet1/19

interface Ethernet1/20

interface Ethernet1/21

interface Ethernet1/22

interface Ethernet1/23

interface Ethernet1/24

interface Ethernet1/25

interface Ethernet1/26

interface Ethernet1/27

interface Ethernet1/28

interface Ethernet1/29

interface Ethernet1/30

interface Ethernet1/31

interface Ethernet1/32

interface Ethernet1/33

interface Ethernet1/34

interface Ethernet1/35

interface Ethernet1/36

interface Ethernet1/37

interface Ethernet1/38

interface Ethernet1/39

interface Ethernet1/40

interface Ethernet1/41

interface Ethernet1/42

interface Ethernet1/43

interface Ethernet1/44

interface Ethernet1/45

interface Ethernet1/46

interface Ethernet1/47

interface Ethernet1/48

interface Ethernet1/49

interface Ethernet1/50

interface Ethernet1/51

interface Ethernet1/52

interface Ethernet1/53

interface Ethernet1/54

interface Ethernet1/55

interface Ethernet1/56

interface Ethernet1/57

interface Ethernet1/58

interface Ethernet1/59

interface Ethernet1/60

interface Ethernet1/61

interface Ethernet1/62

interface Ethernet1/63

interface Ethernet1/64

interface Ethernet1/65

interface Ethernet1/66

interface Ethernet1/67

interface Ethernet1/68

interface Ethernet1/69

interface Ethernet1/70

interface Ethernet1/71

interface Ethernet1/72

interface Ethernet1/73

interface Ethernet1/74

interface Ethernet1/75

interface Ethernet1/76

interface Ethernet1/77

interface Ethernet1/78

interface Ethernet1/79

interface Ethernet1/80

interface Ethernet1/81

interface Ethernet1/82

interface Ethernet1/83

interface Ethernet1/84

interface Ethernet1/85

interface Ethernet1/86

interface Ethernet1/87

interface Ethernet1/88

interface Ethernet1/89

interface Ethernet1/90

interface Ethernet1/91

interface Ethernet1/92

interface Ethernet1/93

interface Ethernet1/94

interface Ethernet1/95

interface Ethernet1/96

interface Ethernet1/97

interface Ethernet1/98

interface Ethernet1/99

interface Ethernet1/100

interface Ethernet1/101

interface Ethernet1/102

interface Ethernet1/103

interface Ethernet1/104

interface Ethernet1/105

interface Ethernet1/106

interface Ethernet1/107

interface Ethernet1/108

interface Ethernet1/109

interface Ethernet1/110

interface Ethernet1/111

interface Ethernet1/112

interface Ethernet1/113

interface Ethernet1/114

interface Ethernet1/115

interface Ethernet1/116

interface Ethernet1/117

interface Ethernet1/118

interface Ethernet1/119

interface Ethernet1/120

interface Ethernet1/121

interface Ethernet1/122

interface Ethernet1/123

interface Ethernet1/124

interface Ethernet1/125

interface Ethernet1/126

interface Ethernet1/127

interface Ethernet1/128

interface mgmt0
  vrf member management
  ip address 150.1.93.75/16

interface loopback0
  ip address 100.64.93.93/32
  ip router ospf 1 area 0.0.0.0
line console
line vty
boot nxos bootflash:/nxos.9.3.2.bin 
router ospf 1
  router-id 100.64.93.93
router bgp 65533
  router-id 100.64.93.93
  address-family l2vpn evpn
    retain route-target all
  template peer overlay-peer
    update-source loopback0
    ebgp-multihop 5
    address-family l2vpn evpn
      send-community
      send-community extended
      route-map next-hop-unchange out
  neighbor 169.254.93.1
    inherit peer overlay-peer
    remote-as 65511
    address-family l2vpn evpn
      rewrite-evpn-rt-asn
  neighbor 169.254.93.6
    inherit peer overlay-peer
    remote-as 65522
    address-family l2vpn evpn
      rewrite-evpn-rt-asn



RS# show ip os neighbors 
 OSPF Process ID 1 VRF default
 Total number of neighbors: 1
 Neighbor ID     Pri State            Up Time  Address         Interface
 169.254.93.6      1 FULL/BDR         01:30:38 169.254.93.6    Eth1/2 
RS# show ip os interface 
 Ethernet1/1 is up, line protocol is up
    IP address 169.254.93.2/30
    Process ID 1 VRF default, area 0.0.0.0
    Enabled by interface configuration
    State DR, Network type BROADCAST, cost 40
    Index 1, Transmit delay 1 sec, Router Priority 1
    Designated Router ID: 100.64.93.93, address: 169.254.93.2
    No backup designated router on this network
    0 Neighbors, flooding to 0, adjacent with 0
    Timer intervals: Hello 10, Dead 40, Wait 40, Retransmit 5
      Hello timer due in 00:00:03
    No authentication
    Number of opaque link LSAs: 0, checksum sum 0
 Ethernet1/2 is up, line protocol is up
    IP address 169.254.93.5/30
    Process ID 1 VRF default, area 0.0.0.0
    Enabled by interface configuration
    State DR, Network type BROADCAST, cost 40
    Index 2, Transmit delay 1 sec, Router Priority 1
    Designated Router ID: 100.64.93.93, address: 169.254.93.5
    Backup Designated Router ID: 169.254.93.6, address: 169.254.93.6
    1 Neighbors, flooding to 1, adjacent with 1
    Timer intervals: Hello 10, Dead 40, Wait 40, Retransmit 5
      Hello timer due in 00:00:02
    No authentication
    Number of opaque link LSAs: 0, checksum sum 0
 loopback0 is up, line protocol is up
    IP address 100.64.93.93/32
    Process ID 1 VRF default, area 0.0.0.0
    Enabled by interface configuration
    State LOOPBACK, Network type LOOPBACK, cost 1
    Index 3
RS#  sh ip os inter b
 OSPF Process ID 1 VRF default
 Total number of interface: 3
 Interface               ID     Area            Cost   State    Neighbors Status
 Eth1/1                  1      0.0.0.0         40     DR       0         up  
 Eth1/2                  2      0.0.0.0         40     DR       1         up  
 Lo0                     3      0.0.0.0         1      LOOPBACK 0         up  

RS# sh bgp l2vpn evpn summary 
BGP summary information for VRF default, address family L2VPN EVPN
BGP router identifier 100.64.93.93, local AS number 65533
BGP table version is 49, L2VPN EVPN config peers 2, capable peers 1
5 network entries and 5 paths using 1200 bytes of memory
BGP attribute entries [5/820], BGP AS path entries [1/6]
BGP community entries [0/0], BGP clusterlist entries [0/0]

Neighbor        V    AS MsgRcvd MsgSent   TblVer  InQ OutQ Up/Down  State/PfxRcd
169.254.93.1    4 65511      89     102        0    0    0 00:43:45 Idle     
169.254.93.6    4 65522     155     157       49    0    0 00:52:43 5         
RS# sh bgp l2vpn evpn 
BGP routing table information for VRF default, address family L2VPN EVPN
BGP table version is 49, Local Router ID is 100.64.93.93
Status: s-suppressed, x-deleted, S-stale, d-dampened, h-history, *-valid, >-best
Path type: i-internal, e-external, c-confed, l-local, a-aggregate, r-redist, I-i
njected
Origin codes: i - IGP, e - EGP, ? - incomplete, | - multipath, & - backup, 2 - b
est2

   Network            Next Hop            Metric     LocPrf     Weight Path
Route Distinguisher: 100.64.2.1:27001
*>e[4]:[0300.0000.00ff.f200.0309]:[32]:[100.64.2.11]/136
                      100.64.2.11                                    0 65522 i

Route Distinguisher: 100.64.2.1:32787
*>e[2]:[0]:[0]:[48]:[5000.0004.0007]:[0]:[0.0.0.0]/216
                      100.64.2.11                                    0 65522 i

Route Distinguisher: 100.64.2.2:3
*>e[5]:[0]:[0]:[24]:[172.16.1.0]/224
                      100.64.100.100           1                     0 65522 ?

Route Distinguisher: 100.64.2.2:32787
*>e[2]:[0]:[0]:[48]:[5000.0008.0000]:[0]:[0.0.0.0]/216
                      100.64.100.100        2000                     0 65522 i
*>e[2]:[0]:[0]:[48]:[5000.0008.0000]:[32]:[172.16.1.3]/272
                      100.64.100.100        2000                     0 65522 i

RS# sh bgp l2vpn evpn route
route-map    route-type   
RS# sh bgp l2vpn evpn route-type 4
BGP routing table information for VRF default, address family L2VPN EVPN
Route Distinguisher: 100.64.2.1:27001
BGP routing table entry for [4]:[0300.0000.00ff.f200.0309]:[32]:[100.64.2.11]/13
6, version 43
Paths: (1 available, best #1)
Flags: (0x000002) (high32 00000000) on xmit-list, is not in l2rib/evpn, is not i
n HW

  Advertised path-id 1
  Path type: external, path is valid, is best path, no labeled nexthop
  AS-Path: 65522 , path sourced external to AS
    100.64.2.11 (metric 41) from 169.254.93.6 (100.64.2.1)
      Origin IGP, MED not set, localpref 100, weight 0
      Extcommunity: ENCAP:8 RT:0000.0000.fff2

  Path-id 1 not advertised to any peer

