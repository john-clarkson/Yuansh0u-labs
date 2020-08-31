DC1-SPINE# SH RUNning-config 

!Command: show running-config
!Time: Wed May  9 11:52:13 2018

version 7.0(3)I7(2)
hostname DC1-SPINE
vdc DC1-SPINE id 1
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
feature interface-vlan
feature vn-segment-vlan-based
feature vpc
feature lldp
feature nv overlay

no password strength-check
username admin password 5 $5$PANAAM$eVArPERkwDzmM7dTlXbnizoCPuMtno6uipjIWNKhAJ8 
 role network-admin
username cisco password 5 $5$2FNBQGhl$wykFMxgJMNMEBLGWCLK8YN6i51byJ8XHCH2gSfxJy9
5  role network-admin
ip domain-lookup
snmp-server user admin network-admin auth md5 0x95813b96d97bfb8c2e4966014f0d4da0
 priv 0x95813b96d97bfb8c2e4966014f0d4da0 localizedkey
snmp-server user cisco network-admin auth md5 0x2ac8fdb3462e90f257b1d936fbd41f0a
 priv 0x2ac8fdb3462e90f257b1d936fbd41f0a localizedkey
rmon event 1 description FATAL(1) owner PMON@FATAL
rmon event 2 description CRITICAL(2) owner PMON@CRITICAL
rmon event 3 description ERROR(3) owner PMON@ERROR
rmon event 4 description WARNING(4) owner PMON@WARNING
rmon event 5 description INFORMATION(5) owner PMON@INFO

vlan 1

vrf context management

interface Vlan1

interface Ethernet1/1
  no switchport
  medium p2p
  ip unnumbered loopback0
  ip ospf network point-to-point
  ip router ospf 2 area 0.0.0.0
  no shutdown

interface Ethernet1/2
  no switchport
  medium p2p
  ip unnumbered loopback0
  ip ospf network point-to-point
  ip router ospf 2 area 0.0.0.0
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

interface mgmt0
  vrf member management

interface loopback0
  ip address 10.0.0.1/32
  ip router ospf 2 area 0.0.0.0
line console
line vty
boot nxos bootflash:/nxos.7.0.3.I7.2.bin 
router ospf 2
router bgp 65511
  router-id 10.0.0.1
  cluster-id 65511
  address-family ipv4 unicast
  address-family l2vpn evpn
    retain route-target all
  neighbor 10.0.0.96/29
    remote-as 65511
    update-source loopback0
    address-family ipv4 unicast
      send-community
      send-community extended
      route-reflector-client
    address-family l2vpn evpn
      send-community
      send-community extended
      route-reflector-client
no logging console


