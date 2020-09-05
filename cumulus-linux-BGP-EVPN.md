#  Cumulus linux introduction
### Author: yuansh0u
> cumulus linux opensource BGP EVPN Dual-stack VXLAN lab
### Officail website
https://cumulusnetworks.com/products/cumulus-vx/download/
### Documentation
https://docs.cumulusnetworks.com/display/DOCS/Cumulus+Linux+User+Guid
- Cumulus linux is debian base (ubuntu os) opensource networking software pack, think cisco ios/ios xe/ios xr with their hardware router/switch, cumulus is software layer, then you can pick your hardware switch and install cumulus linux on top of it.
- This lab is base on kvm version with eve-ng as the placeholder, then create clos fabric with cumulus linux, we will enable bgp evpn with vxlan, cuz bgp is industry standard protocol, so you can extend network with other vendors, like cisco/juniper etc.
### Design tip
* IP address with unnumbered loopback0
* Loopback0 as control-plane/data-plane source interface
* BUM traffic handle: BGP type3 inclusive multicast, no PIM underlay
* CLAG/MLAG=Cisco VPC
* Underlay=ipv4, Overlay=dual-stack

### Topology
![](https://i.imgur.com/i7QjUDU.png)


### Enable frrouting 
```shell=
##Cumulus credentials
Username:cumulus
Password:CumulusLinux!
##Enable open-source components for control-plane/data-plane.

cumulus@MLAG1:/etc/frr$ ls
daemons  daemons.conf  frr.conf  frr.conf.sav  vtysh.conf
cumulus@MLAG1:/etc/frr$ cat daemons
# This file tells the frr package which daemons to start.
#
# Entries are in the format: <daemon>=(yes|no|priority)
#   0, "no"  = disabled
#   1, "yes" = highest priority
#   2 .. 10  = lower priorities
# Read /usr/share/doc/frr/README.Debian for details.
#
# Sample configurations for these daemons can be found in
# /usr/share/doc/frr/examples/.
#
# ATTENTION:
#
# When activation a daemon at the first time, a config file, even if it is
# empty, has to be present *and* be owned by the user and group "frr", else
# the daemon will not be started by /etc/init.d/frr. The permissions should
# be u=rw,g=r,o=.
# When using "vtysh" such a config file is also needed. It should be owned by
# group "frrvty" and set to ug=rw,o= though. Check /etc/pam.d/frr, too.
#
# The watchfrr daemon is always started. Per default in monitoring-only but
# that can be changed via /etc/frr/daemons.conf.
#
zebra=yes
bgpd=yes
ospfd=yes
ospf6d=no
ripd=no
ripngd=no
isisd=no
pimd=no
ldpd=no
nhrpd=no
eigrpd=no
babeld=no
sharpd=no
pbrd=no
#edit daemons with vi/nano, modify (BGP/OSPF/Zebra) default value no to yes.
#save it

cumulus@MLAG1:/etc/frr$ sudo systemctl restart frr.service 
[sudo] password for cumulus: CumulusLinux!
#restart frr.service
$sudo systemctl status frr.service
 ![](https://i.imgur.com/JgXRLJu.jpg)
```

## Interface unnumbered IP/OSPF/BGP configuration
### SPINE configuration
```sh 
net add interface swp1-5 ip address 10.0.0.2/32
net add bgp autonomous-system 65511
net add interface swp1-5 ospf area 0.0.0.0
net add interface swp1-5 ospf network point-to-point
net add loopback lo ospf area 0.0.0.0
net add bgp router-id 10.0.0.2
net add bgp neighbor swp1 interface remote-as internal
net add bgp neighbor swp2 interface remote-as internal
net add bgp neighbor swp3 interface remote-as internal
net add bgp neighbor swp4 interface remote-as internal
net add bgp neighbor swp5 interface remote-as internal
net add bgp neighbor swp6 interface remote-as internal
net add bgp neighbor swp7 interface remote-as internal
net add bgp ipv4 unicast network 10.0.0.2/32 
net add bgp ipv4 unicast neighbor swp1 route-reflector-client
net add bgp ipv4 unicast neighbor swp2 route-reflector-client
net add bgp ipv4 unicast neighbor swp3 route-reflector-client
net add bgp ipv4 unicast neighbor swp4 route-reflector-client
net add bgp ipv4 unicast neighbor swp5 route-reflector-client
net add bgp ipv4 unicast neighbor swp6 route-reflector-client
net add bgp ipv4 unicast neighbor swp7 route-reflector-client
net add bgp l2vpn evpn  neighbor swp1 activate
net add bgp l2vpn evpn  neighbor swp1 route-reflector-client
net add bgp l2vpn evpn  neighbor swp2 activate
net add bgp l2vpn evpn  neighbor swp2 route-reflector-client
net add bgp l2vpn evpn  neighbor swp3 activate
net add bgp l2vpn evpn  neighbor swp3 route-reflector-client
net add bgp l2vpn evpn  neighbor swp4 activate
net add bgp l2vpn evpn  neighbor swp4 route-reflector-client
net add bgp l2vpn evpn  neighbor swp5 activate
net add bgp l2vpn evpn  neighbor swp5 route-reflector-client
net add bgp l2vpn evpn  neighbor swp6 activate
net add bgp l2vpn evpn  neighbor swp6 route-reflector-client
net add bgp l2vpn evpn  neighbor swp7 activate
net add bgp l2vpn evpn  neighbor swp7 route-reflector-client
net add ospf router-id 10.0.0.2
net add ospf passive-interface lo
net pending
net commit
leaf1 configuration example
##Add interface/ip address assignment
net add interface swp1 ip address 10.0.0.1/32
net add interface swp2-7
net add interface swp1 ip address 10.0.0.1/32
net add interface swp2-7
net add loopback lo ip address 10.0.0.1/32
##BGP AS number setting
net add bgp autonomous-system 65511
net add bgp router-id 10.0.0.1
##BGP IBGP neighbor advertise
net add bgp neighbor swp1 interface remote-as internal
net add bgp ipv4 unicast network 10.0.0.1/32 
##BGP EVPN AFI activate
net add bgp l2vpn evpn  neighbor swp1 activate
net add bgp l2vpn evpn  advertise-all-vni
net add bgp l2vpn evpn  advertise-default-gw
net add bgp l2vpn evpn  advertise ipv4 unicast
net add bgp l2vpn evpn  advertise ipv6 unicast
##BGP vrf-aware AS number setting for Tenant A
net add bgp vrf A autonomous-system 65511
net add bgp vrf A l2vpn evpn  advertise ipv4 unicast
net add bgp vrf A l2vpn evpn  advertise ipv6 unicast
##OSPF setting
net add loopback lo ospf area 0.0.0.0
net add interface swp1 ospf area 0.0.0.0
net add interface swp1 ospf network point-to-point
net add ospf router-id 10.0.0.1
net add ospf passive-interface lo
##Create vrf A for tenant A
net add vrf A vrf-table auto
##Create Linux VLAN-aware bridge
net add bridge bridge ports swp7,vni100,vni200,vni104001,vni104001
net add bridge bridge vids 100,200,4001
net add bridge bridge vlan-aware
##Tenant A SVI interface setting with Anycast-gateway
net add vlan 100 hwaddress 12:34:56:78:9a:bc
net add vlan 100 ip address 192.168.100.254/24
net add vlan 100 ipv6 address fc00:192:168:100::254/64
net add vlan 100 vlan-id 100
net add vlan 100 vlan-raw-device bridge
net add vlan 100 vrf A
net add vlan 200 hwaddress 12:34:56:78:9a:bc
net add vlan 200 ip address 192.168.200.254/24
net add vlan 200 ipv6 address fc00:192:168:200::254/64
net add vlan 200 vlan-id 200
net add vlan 200 vlan-raw-device bridge
net add vlan 200 vrf A
net add vrf A vni 104001
##Create VXLAN VNI
net add vxlan vni100 vxlan id 10100
net add vxlan vni104001 vxlan id 104001
net add vxlan vni200 vxlan id 10200
##VLAN mapping VXLAN VNI
net add vxlan vni100 bridge access 100
net add vxlan vni200 bridge access 200
net add vxlan vni104001 bridge access 4001
##L3VNI setting for symmetric routing
net add vlan 4001 vlan-id 4001
net add vlan 4001 vlan-raw-device bridge
net add vlan 4001 vrf A
##Disable Linux VXLAN driver default behavior
net add vxlan vni100,200,104001 bridge learning off
net add vxlan vni100,200,104001 stp bpduguard
net add vxlan vni100,200,104001 stp portbpdufilter
##Create VXLAN ENCAP/DECAP logical interface/equivalent CISCO NXOS NVE interface
net add vxlan vni100,200,104001 vxlan local-tunnelip 10.0.0.1
##Enable arp-nd suppress feature, reduce BUM traffic over the network.
net add vxlan vni104001 bridge arp-nd-suppress on
net pending
net commit
```

## Check mate
$ip a
![](https://i.imgur.com/LYI4VXr.png)
 
$net show ospf neighbor
![](https://i.imgur.com/ADM9DtW.png)
 
$net show bgp l2vpn evpn summary
 ![](https://i.imgur.com/pd7txGn.png)

$route -n
 ![](https://i.imgur.com/Oe6LLl7.png)

$ip route show
 ![](https://i.imgur.com/o1T9qgC.png)

$net show bgp l2vpn evpn vni
 ![](https://i.imgur.com/HoPor0s.png)

$net show bgp l2vpn evpn route
![](https://i.imgur.com/eLjYto4.png)

$net show bgp l2vpn evpn route type macip
 ![](https://i.imgur.com/yXySFjV.png)

 
## MLAG/CLAG
### MLAG-1 configuration
```sh
##MLAG member port setting
net add bond bond-to-host-22 bond slaves swp2
net add bond peerlink bond slaves swp3,swp4
net add bond bond-to-host-22 bridge vids 100-200
net add bond bond-to-host-22 clag id 2
net add bridge bridge ports bond-to-host-22,peerlink,vni100,vni104001,vni104001
net add bridge bridge vids 100-200,4001
net add bridge bridge vlan-aware
##Peer-link setting
net add interface peerlink.4094 clag backup-ip 10.0.0.6
net add interface peerlink.4094 clag peer-ip 169.254.1.2
net add interface peerlink.4094 clag priority 1000
net add interface peerlink.4094 clag sys-mac 44:38:39:FF:01:01
net add interface peerlink.4094 ip address 169.254.1.1/30
net add interface swp1 ip address 10.0.0.5/32
net add interface swp2-7
##Anycast-vtep loopback for BGP next-hop
net add loopback lo clag vxlan-anycast-ip 10.0.0.255
```
### MLAG-2 configuration
```sh 
##MLAG member port setting
net add bond bond-to-host-22 bond slaves swp2
net add bond peerlink bond slaves swp3,swp4
net add bond bond-to-host-22 bridge vids 100-200
net add bond bond-to-host-22 clag id 2
net add bridge bridge ports bond-to-host-22,peerlink,vni100,vni104001,vni104001
net add bridge bridge vids 100-200,4001
net add bridge bridge vlan-aware
##Peer-link setting
net add interface peerlink.4094 clag backup-ip 10.0.0.5
net add interface peerlink.4094 clag peer-ip 169.254.1.1
net add interface peerlink.4094 clag priority 1000
net add interface peerlink.4094 clag sys-mac 44:38:39:FF:01:01
net add interface peerlink.4094 ip address 169.254.1.2/30
net add interface swp1 ip address 10.0.0.6/32
net add interface swp2-7
##Anycast-vtep loopback for BGP next-hop
net add loopback lo clag vxlan-anycast-ip 10.0.0.255
```

### Server bonding configuration(ubuntu)
cumulus@HOST:/etc/network$ cat interfaces
```sh 
# This file describes the network interfaces available on your system
# and how to activate them. For more information, see interfaces(5).

source /etc/network/interfaces.d/*.intf

# The loopback network interface
auto lo
iface lo inet loopback

# The primary network interface
auto eth0
iface eth0 inet dhcp

auto swp1
iface swp1

auto swp2
iface swp2

auto bond-host-11
iface bond-host-11
    bond-slaves swp1 swp2
    bridge-vids 100-200

auto bridge
iface bridge
    bridge-ports bond-host-11
    bridge-vids 100-200
    bridge-vlan-aware yes

auto vlan100
iface vlan100
    address 192.168.100.88/24
    address fc00:192:168:100::88/64
    gateway 192.168.100.254
    gateway fc00:192:168:100::254
    vlan-id 100
    vlan-raw-device bridge
cumulus@HOST:/etc/network$
```
### Check mate
>$net show clag
![](https://i.imgur.com/aPjxzB4.png)

>$net show interface
 ![](https://i.imgur.com/8XiMGMx.png)

>/proc/net/bonding$ cat bond-host-11 
$ifconfig bond-host-11
 ![](https://i.imgur.com/hUAq2eH.png)
```text
> $ping 192.168.100.254

> $ping6 fc00:192:168:100::254
```
 ![](https://i.imgur.com/AEUgmzQ.png)
> $arp
 ![](https://i.imgur.com/ocwthpZ.png)

> $ip -6 neigh
 ![](https://i.imgur.com/uJBrRWf.png)

### BORDER-LEAF configuration>external cisco router
```sh 
Border-Leaf configuration
net add bgp autonomous-system 65511
net add loopback lo ospf area 0.0.0.0
net add interface swp1 ospf area 0.0.0.0
net add interface swp1 ospf network point-to-point
net add vrf A vni 104001
net add bgp router-id 10.0.0.4
net add bgp bestpath as-path multipath-relax
net add bgp neighbor swp1 interface remote-as internal
net add bgp l2vpn evpn  neighbor swp1 activate
net add bgp l2vpn evpn  advertise-all-vni
net add bgp l2vpn evpn  advertise-default-gw
net add bgp l2vpn evpn  advertise ipv4 unicast
net add bgp l2vpn evpn  advertise ipv6 unicast
net add bgp vrf A autonomous-system 65511
net add bgp vrf A neighbor 100.64.1.2 remote-as 65000
net add bgp vrf A neighbor fc00:100:64:1::2 remote-as 65000
net del bgp vrf A ipv4 unicast neighbor fc00:100:64:1::2 activate
net add bgp vrf A ipv6 unicast neighbor fc00:100:64:1::2 activate
net add bgp vrf A l2vpn evpn  advertise ipv4 unicast
net add bgp vrf A l2vpn evpn  advertise ipv6 unicast
net add ospf router-id 10.0.0.4
net add ospf passive-interface lo
net add dns nameserver ipv4 4.2.2.1
net add vxlan vni104001 vxlan id 104001
net add bridge bridge ports swp2,vni104001,vni104001
net add bridge bridge vids 100,4001
net add bridge bridge vlan-aware
net add interface swp1 ip address 10.0.0.4/32
net add interface swp2-7
net add loopback lo ip address 10.0.0.4/32
net add vlan 100 hwaddress 12:34:56:78:9a:bc
net add vlan 100 ip address 100.64.1.1/24
net add vlan 100 ipv6 address fc00:100:64:1::1/64
net add vlan 100 vlan-id 100
net add vlan 100 vlan-raw-device bridge
net add vlan 100 vrf A
net add vlan 4001 vlan-id 4001
net add vlan 4001 vlan-raw-device bridge
net add vlan 4001 vrf A
net add vrf A vrf-table auto
net add vxlan vni104001 bridge access 4001
net add vxlan vni104001 bridge arp-nd-suppress on
net add vxlan vni104001 bridge learning off
net add vxlan vni104001 stp bpduguard
net add vxlan vni104001 stp portbpdufilter
net add vxlan vni104001 vxlan local-tunnelip 10.0.0.4
```
### EXTERNAL CISCO ROUTER IOS XE configuration
```ios
vrf definition A
 rd 1:1
 !
 address-family ipv4
 exit-address-family
 !        
 address-family ipv6
 exit-address-family
end
interface Loopback0
 vrf forwarding A
 ip address 8.8.8.1 255.255.255.255 secondary
 ip address 8.8.8.2 255.255.255.255 secondary
 ip address 8.8.8.3 255.255.255.255 secondary
 ip address 8.8.8.4 255.255.255.255 secondary
 ip address 8.8.8.5 255.255.255.255 secondary
 ip address 8.8.8.6 255.255.255.255 secondary
 ip address 8.8.8.7 255.255.255.255 secondary
 ip address 8.8.8.8 255.255.255.255
 ipv6 address FC00:8:8:8::4/128
 ipv6 address FC00:8:8:8::5/128
 ipv6 address FC00:8:8:8::6/128
 ipv6 address FC00:8:8:8::7/128
 ipv6 address FC00:8:8:8::8/128

interface GigabitEthernet2.100
 encapsulation dot1Q 100
 vrf forwarding A
 ip address 100.64.1.2 255.255.255.0
 ipv6 address FC00:100:64:1::2/64

router bgp 65000
 bgp router-id 100.64.1.2
 bgp log-neighbor-changes
 no bgp default ipv4-unicast
 !
 address-family ipv4 vrf A
  network 8.8.8.1 mask 255.255.255.255
  network 8.8.8.2 mask 255.255.255.255
  network 8.8.8.3 mask 255.255.255.255
  network 8.8.8.4 mask 255.255.255.255
  network 8.8.8.5 mask 255.255.255.255
  network 8.8.8.6 mask 255.255.255.255
  network 8.8.8.7 mask 255.255.255.255
  network 8.8.8.8 mask 255.255.255.255
  neighbor 100.64.1.1 remote-as 65511
  neighbor 100.64.1.1 activate
 exit-address-family
 !
 address-family ipv6 vrf A
  network FC00:8:8:8::4/128
  network FC00:8:8:8::5/128
  network FC00:8:8:8::6/128
  network FC00:8:8:8::7/128
  network FC00:8:8:8::8/128
  neighbor FC00:100:64:1::1 remote-as 65511
  neighbor FC00:100:64:1::1 activate
 exit-address-family       

```
### check mate
```ios
EXTERNAL-BGP#show bgp vpnv4 unicast all summary 
BGP router identifier 100.64.1.2, local AS number 65000
BGP table version is 9659, main routing table version 9659
13 network entries using 3328 bytes of memory
13 path entries using 1560 bytes of memory
16/5 BGP path/bestpath attribute entries using 4224 bytes of memory
1 BGP AS-PATH entries using 24 bytes of memory
25 BGP extended community entries using 2310 bytes of memory
0 BGP route-map cache entries using 0 bytes of memory
0 BGP filter-list cache entries using 0 bytes of memory
BGP using 11446 total bytes of memory
BGP activity 1418/1396 prefixes, 11961/11940 paths, scan interval 60 secs

Neighbor        V           AS MsgRcvd MsgSent   TblVer  InQ OutQ Up/Down  State/PfxRcd
100.64.1.1      4        65511   34225   20569     9659    0    0 17:32:58        5

EXTERNAL-BGP#show bgp vpnv6 unicast all summary 
BGP router identifier 100.64.1.2, local AS number 65000
BGP table version is 517, main routing table version 517
8 network entries using 2240 bytes of memory
8 path entries using 1184 bytes of memory
15/4 BGP path/bestpath attribute entries using 3960 bytes of memory
1 BGP AS-PATH entries using 24 bytes of memory
35 BGP extended community entries using 3230 bytes of memory
0 BGP route-map cache entries using 0 bytes of memory
0 BGP filter-list cache entries using 0 bytes of memory
BGP using 10638 total bytes of memory
BGP activity 1418/1396 prefixes, 11964/11943 paths, scan interval 60 secs

Neighbor        V           AS MsgRcvd MsgSent   TblVer  InQ OutQ Up/Down  State/PfxRcd
FC00:100:64:1::1
                4        65511   21419   20592      517    0    0 17:33:29        3

EXTERNAL-BGP#show bgp vpnv4 unicast all 
BGP table version is 9664, local router ID is 100.64.1.2
Status codes: s suppressed, d damped, h history, * valid, > best, i - internal, 
              r RIB-failure, S Stale, m multipath, b backup-path, f RT-Filter, 
              x best-external, a additional-path, c RIB-compressed, 
Origin codes: i - IGP, e - EGP, ? - incomplete
RPKI validation codes: V valid, I invalid, N Not found

     Network          Next Hop            Metric LocPrf Weight Path
Route Distinguisher: 1:1 (default for vrf A)
 *>  8.8.8.1/32       0.0.0.0                  0         32768 i
 *>  8.8.8.2/32       0.0.0.0                  0         32768 i
 *>  8.8.8.3/32       0.0.0.0                  0         32768 i
 *>  8.8.8.4/32       0.0.0.0                  0         32768 i
 *>  8.8.8.5/32       0.0.0.0                  0         32768 i
 *>  8.8.8.6/32       0.0.0.0                  0         32768 i
 *>  8.8.8.7/32       0.0.0.0                  0         32768 i
 *>  8.8.8.8/32       0.0.0.0                  0         32768 i
 *>  192.168.100.1/32 100.64.1.1                             0 65511 i
 *>  192.168.100.254/32
                       100.64.1.1                             0 65511 i
 *>  192.168.200.2/32 100.64.1.1                             0 65511 i
 *>  192.168.200.254/32
                       100.64.1.1                             0 65511 i
EXTERNAL-BGP#show bgp vpnv6 unicast all 
BGP table version is 519, local router ID is 100.64.1.2
Status codes: s suppressed, d damped, h history, * valid, > best, i - internal, 
              r RIB-failure, S Stale, m multipath, b backup-path, f RT-Filter, 
              x best-external, a additional-path, c RIB-compressed, 
Origin codes: i - IGP, e - EGP, ? - incomplete
RPKI validation codes: V valid, I invalid, N Not found

     Network          Next Hop            Metric LocPrf Weight Path
Route Distinguisher: 1:1 (default for vrf A)
 *>  FC00:8:8:8::4/128
                       ::                       0         32768 i
 *>  FC00:8:8:8::5/128
                       ::                       0         32768 i
 *>  FC00:8:8:8::6/128
                       ::                       0         32768 i
 *>  FC00:8:8:8::7/128
                       ::                       0         32768 i
 *>  FC00:8:8:8::8/128
                       ::                       0         32768 i
 *>  FC00:192:168:100::1/128
                       FC00:100:64:1::1
                                                              0 65511 i
 *>  FC00:192:168:200::2/128
     Network          Next Hop            Metric LocPrf Weight Path
                       FC00:100:64:1::1
                                                              0 65511 i
 *>  FC00:192:168:200::254/128
                       FC00:100:64:1::1
                                                              0 65511 i
```
### Check mate
EXTERNAL-BGP#
> $net show bgp vrf A ipv4 unicast
 ![](https://i.imgur.com/CXgRjs3.png)

> $net show bgp vrf A ipv6 unicast
 ![](https://i.imgur.com/n1X5jht.png)

> $ping -I A 100.64.1.2
 ![](https://i.imgur.com/lNQBiTR.png)

> $ip route show table A
 ![](https://i.imgur.com/Jywumdh.png)

> #ping
 ![](https://i.imgur.com/V1QP9p9.png)

### PCAP
>L2VNI-IPV4 OVER IPV4
![](https://i.imgur.com/4V00yCB.png)

>L2VNI-IPV6 OVER IPV4
 ![](https://i.imgur.com/q0dPImh.png)

>L3VNI-Symmetric-routing
 ![](https://i.imgur.com/8sJ2Z4s.png)

>DF-BIT
![](https://i.imgur.com/3kEL48V.png)


 

 
