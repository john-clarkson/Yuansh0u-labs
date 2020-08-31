﻿leaf1dcaa# sh run | no

!Command: show running-config
!Running configuration last done at: Mon Jan 13 04:49:43 2020
!Time: Mon Jan 13 15:11:04 2020

version 9.3(2) Bios:version  
hostname leaf1dcaa
vdc leaf1dcaa id 1
  limit-resource vlan minimum 16 maximum 4094
  limit-resource vrf minimum 2 maximum 4096
  limit-resource port-channel minimum 0 maximum 511
  limit-resource u4route-mem minimum 248 maximum 248
  limit-resource u6route-mem minimum 96 maximum 96
  limit-resource m4route-mem minimum 58 maximum 58
  limit-resource m6route-mem minimum 8 maximum 8

feature telnet
feature nxapi
feature bash-shell
feature scp-server
cfs eth distribute
nv overlay evpn
feature ospf
feature bgp
feature pim
feature interface-vlan
feature vn-segment-vlan-based
feature lldp
feature nv overlay

no password strength-check
username admin password 5 $5$hHfj1GlO$AlLXw4brIuFnjYA04ionSX6vAjGWEav9DNBg//kGiT/  role network-admin
ip domain-lookup
no system default switchport
copp profile strict
snmp-server user admin network-admin auth md5 0x0623befee30c279a22f0c6704c12e049 priv 0x0623befee30c279a22f0c6704c12e049 localizedkey
rmon event 1 description FATAL(1) owner PMON@FATAL
rmon event 2 description CRITICAL(2) owner PMON@CRITICAL
rmon event 3 description ERROR(3) owner PMON@ERROR
rmon event 4 description WARNING(4) owner PMON@WARNING
rmon event 5 description INFORMATION(5) owner PMON@INFO

fabric forwarding anycast-gateway-mac 1234.5678.9abc
ipv6 switch-packets lla
vlan 1,10,20,30,500,1234
vlan 20
  vn-segment 10020
vlan 30
  vn-segment 10030
vlan 1234
  name L3VNI-Routing-TENANT1
  vn-segment 101234

route-map ALL permit 10
vrf context TENANT1
  vni 101234
  rd auto
  address-family ipv4 unicast
    route-target both auto
    route-target both auto evpn
  address-family ipv6 unicast
    route-target both auto
    route-target both auto evpn
vrf context management
  ip route 0.0.0.0/0 150.1.93.254


interface Vlan1
  no ip redirects
  no ipv6 redirects

interface Vlan20
  no shutdown
  vrf member TENANT1
  no ip redirects
  ip address 172.16.1.254/24
  ipv6 address fc00:172:16:1::254/64
  no ipv6 redirects
  fabric forwarding mode anycast-gateway

interface Vlan30
  no shutdown
  vrf member TENANT1
  no ip redirects
  ip address 172.16.2.254/24
  ipv6 address fc00:172:16:2::254/64
  no ipv6 redirects
  fabric forwarding mode anycast-gateway

interface Vlan1234
  description L3VNI-Routing
  no shutdown
  vrf member TENANT1
  no ip redirects
  ip forward
  ipv6 address use-link-local-only
  no ipv6 redirects

interface nve1
  no shutdown
  host-reachability protocol bgp
  source-interface loopback0
  member vni 10020
    ingress-replication protocol bgp
  member vni 10030
    ingress-replication protocol bgp
  member vni 101234 associate-vrf

interface Ethernet1/1
  ip address 169.254.12.1/24
  ip router ospf 1 area 0.0.0.0
  no shutdown

interface Ethernet1/2
  no shutdown

interface Ethernet1/3
  no shutdown

interface Ethernet1/4
  no shutdown

interface Ethernet1/5
  no shutdown

interface Ethernet1/6
  switchport
  switchport access vlan 20
  spanning-tree port type edge

interface Ethernet1/7
  no shutdown

interface Ethernet1/8
  no shutdown

interface Ethernet1/9
  no shutdown

interface Ethernet1/10
  no shutdown

interface Ethernet1/11
  no shutdown

interface Ethernet1/12
  no shutdown

interface Ethernet1/13
  no shutdown

interface Ethernet1/14
  no shutdown

interface Ethernet1/15
  no shutdown

interface Ethernet1/16
  no shutdown

interface Ethernet1/17
  no shutdown

interface Ethernet1/18
  no shutdown

interface Ethernet1/19
  no shutdown

interface Ethernet1/20
  no shutdown

interface Ethernet1/21
  no shutdown

interface Ethernet1/22
  no shutdown

interface Ethernet1/23
  no shutdown

interface Ethernet1/24
  no shutdown

interface Ethernet1/25
  no shutdown

interface Ethernet1/26
  no shutdown

interface Ethernet1/27
  no shutdown

interface Ethernet1/28
  no shutdown

interface Ethernet1/29
  no shutdown

interface Ethernet1/30
  no shutdown

interface Ethernet1/31
  no shutdown

interface Ethernet1/32
  no shutdown

interface Ethernet1/33
  no shutdown

interface Ethernet1/34
  no shutdown

interface Ethernet1/35
  no shutdown

interface Ethernet1/36
  no shutdown

interface Ethernet1/37
  no shutdown

interface Ethernet1/38
  no shutdown

interface Ethernet1/39
  no shutdown

interface Ethernet1/40
  no shutdown

interface Ethernet1/41
  no shutdown

interface Ethernet1/42
  no shutdown

interface Ethernet1/43
  no shutdown

interface Ethernet1/44
  no shutdown

interface Ethernet1/45
  no shutdown

interface Ethernet1/46
  no shutdown

interface Ethernet1/47
  no shutdown

interface Ethernet1/48
  no shutdown

interface Ethernet1/49
  no shutdown

interface Ethernet1/50
  no shutdown

interface Ethernet1/51
  no shutdown

interface Ethernet1/52
  no shutdown

interface Ethernet1/53
  no shutdown

interface Ethernet1/54
  no shutdown

interface Ethernet1/55
  no shutdown

interface Ethernet1/56
  no shutdown

interface Ethernet1/57
  no shutdown

interface Ethernet1/58
  no shutdown

interface Ethernet1/59
  no shutdown

interface Ethernet1/60
  no shutdown

interface Ethernet1/61
  no shutdown

interface Ethernet1/62
  no shutdown

interface Ethernet1/63
  no shutdown

interface Ethernet1/64
  no shutdown

interface Ethernet1/65
  no shutdown

interface Ethernet1/66
  no shutdown

interface Ethernet1/67
  no shutdown

interface Ethernet1/68
  no shutdown

interface Ethernet1/69
  no shutdown

interface Ethernet1/70
  no shutdown

interface Ethernet1/71
  no shutdown

interface Ethernet1/72
  no shutdown

interface Ethernet1/73
  no shutdown

interface Ethernet1/74
  no shutdown

interface Ethernet1/75
  no shutdown

interface Ethernet1/76
  no shutdown

interface Ethernet1/77
  no shutdown

interface Ethernet1/78
  no shutdown

interface Ethernet1/79
  no shutdown

interface Ethernet1/80
  no shutdown

interface Ethernet1/81
  no shutdown

interface Ethernet1/82
  no shutdown

interface Ethernet1/83
  no shutdown

interface Ethernet1/84
  no shutdown

interface Ethernet1/85
  no shutdown

interface Ethernet1/86
  no shutdown

interface Ethernet1/87
  no shutdown

interface Ethernet1/88
  no shutdown

interface Ethernet1/89
  no shutdown

interface Ethernet1/90
  no shutdown

interface Ethernet1/91
  no shutdown

interface Ethernet1/92
  no shutdown

interface Ethernet1/93
  no shutdown

interface Ethernet1/94
  no shutdown

interface Ethernet1/95
  no shutdown

interface Ethernet1/96
  no shutdown

interface Ethernet1/97
  no shutdown

interface Ethernet1/98
  no shutdown

interface Ethernet1/99
  no shutdown

interface Ethernet1/100
  no shutdown

interface Ethernet1/101
  no shutdown

interface Ethernet1/102
  no shutdown

interface Ethernet1/103
  no shutdown

interface Ethernet1/104
  no shutdown

interface Ethernet1/105
  no shutdown

interface Ethernet1/106
  no shutdown

interface Ethernet1/107
  no shutdown

interface Ethernet1/108
  no shutdown

interface Ethernet1/109
  no shutdown

interface Ethernet1/110
  no shutdown

interface Ethernet1/111
  no shutdown

interface Ethernet1/112
  no shutdown

interface Ethernet1/113
  no shutdown

interface Ethernet1/114
  no shutdown

interface Ethernet1/115
  no shutdown

interface Ethernet1/116
  no shutdown

interface Ethernet1/117
  no shutdown

interface Ethernet1/118
  no shutdown

interface Ethernet1/119
  no shutdown

interface Ethernet1/120
  no shutdown

interface Ethernet1/121
  no shutdown

interface Ethernet1/122
  no shutdown

interface Ethernet1/123
  no shutdown

interface Ethernet1/124
  no shutdown

interface Ethernet1/125
  no shutdown

interface Ethernet1/126
  no shutdown

interface Ethernet1/127
  no shutdown

interface Ethernet1/128
  no shutdown

interface mgmt0
  no cdp enable
  vrf member management
  ip address 150.1.9.11/16

interface loopback0
  ip address 100.64.1.1/32
  ip router ospf 1 area 0.0.0.0
line console
line vty
boot nxos bootflash:/nxos.9.3.2.bin 
router ospf 1
  router-id 100.64.1.1
router bgp 65511
  router-id 100.64.1.1
  log-neighbor-changes
  address-family ipv4 unicast
  address-family l2vpn evpn
  neighbor 100.64.1.2
    remote-as 65511
    update-source loopback0
    address-family ipv4 unicast
    address-family l2vpn evpn
      send-community extended
  vrf TENANT1
    address-family ipv4 unicast
      advertise l2vpn evpn
      redistribute direct route-map ALL
evpn
  vni 10020 l2
    rd auto
    route-target import auto
    route-target export auto
  vni 10030 l2
    rd auto
    route-target import auto
    route-target export auto



leaf1dcaa# show ip os neighbors 
leaf1dcaa# show bgp l2vpn evpn
BGP routing table information for VRF default, address family L2VPN EVPN
BGP table version is 157, Local Router ID is 100.64.1.1
Status: s-suppressed, x-deleted, S-stale, d-dampened, h-history, *-valid, >-best
Path type: i-internal, e-external, c-confed, l-local, a-aggregate, r-redist, I-i
njected
Origin codes: i - IGP, e - EGP, ? - incomplete, | - multipath, & - backup, 2 - b
est2

   Network            Next Hop            Metric     LocPrf     Weight Path
Route Distinguisher: 100.64.1.1:32787    (L2VNI 10020)
*>l[2]:[0]:[0]:[48]:[5000.0007.0000]:[32]:[172.16.1.2]/272
                      100.64.1.1                        100      32768 i
*>l[3]:[0]:[32]:[100.64.1.1]/88
                      100.64.1.1                        100      32768 i

Route Distinguisher: 100.64.1.1:32797    (L2VNI 10030)
*>l[3]:[0]:[32]:[100.64.1.1]/88
                      100.64.1.1                        100      32768 i

Route Distinguisher: 100.64.1.1:3    (L3VNI 101234)
*>l[5]:[0]:[0]:[24]:[172.16.1.0]/224
                      100.64.1.1               0        100      32768 ?
*>l[5]:[0]:[0]:[24]:[172.16.2.0]/224
                      100.64.1.1               0        100      32768 ?

leaf1dcaa# 
leaf1dcaa# 
leaf1dcaa# 
leaf1dcaa# show nve peers 
leaf1dcaa# show nve interface
Interface: nve1, State: Up, encapsulation: VXLAN
 VPC Capability: VPC-VIP-Only [not-notified]
 Local Router MAC: 5000.0001.0007
 Host Learning Mode: Control-Plane
 Source-Interface: loopback0 (primary: 100.64.1.1, secondary: 0.0.0.0)

