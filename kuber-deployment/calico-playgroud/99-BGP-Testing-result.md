# BGP-testing-result <calico---frrouting>
## Topology
```text
Network subnet range: 172.18.0.0/16
+-------------+                 +-------------+          +---------------+
| KIND nodes*3|----------------| kind bridge |----------| FRR container |
+-------------+                 +-------------+          +---------------+                                                             
```
## Calico-bird
```sh
$kubectl exec -ti calico-node-s7qqp sh
sh-4.4# ip route show
#default via 172.18.0.1 dev eth0 
#4.3.2.1 via 172.18.0.5 dev eth0 proto bird 
#10.244.82.0/26 via 172.18.0.2 dev eth0 proto bird 
#blackhole 10.244.110.128/26 proto bird 
#10.244.110.130 dev cali19ef06519d0 scope link 
#10.244.110.131 dev califaff92fdf81 scope link 
#10.244.110.132 dev cali6658969f19c scope link 
#10.244.162.128/26 via 172.18.0.4 dev eth0 proto bird 
100.64.255.0/24 via 172.18.0.5 dev eth0 proto bird ####frrouting sec nic-->docker new-bridge
#172.18.0.0/16 dev eth0 proto kernel scope link src 172.18.0.3 
sh-4.4# 
```
## FRROUTING container=docker manage, not k8s pods
### $docker exec ti frrouting sh
### FIB table
```sh
FRR# sh ip route
Codes: K - kernel route, C - connected, S - static, R - RIP,
       O - OSPF, I - IS-IS, B - BGP, E - EIGRP, N - NHRP,
       T - Table, v - VNC, V - VNC-Direct, A - Babel, D - SHARP,
       F - PBR, f - OpenFabric,
       > - selected route, * - FIB route

K>* 0.0.0.0/0 [0/0] via 172.18.0.1, eth0, 00:10:33
B>  3.3.3.3/32 [200/0] via 172.18.0.2, eth0, 00:10:32
                       via 172.18.0.3, eth0, 00:10:32
                       via 172.18.0.4, eth0, 00:10:32
B>  4.4.4.4/32 [200/0] via 172.18.0.2, eth0, 00:10:32
                       via 172.18.0.3, eth0, 00:10:32
                       via 172.18.0.4, eth0, 00:10:32
B>  10.96.0.0/12 [200/0] via 172.18.0.2, eth0, 00:10:32
                         via 172.18.0.3, eth0, 00:10:32
                         via 172.18.0.4, eth0, 00:10:32
B>  10.244.82.0/26 [200/0] via 172.18.0.2, eth0, 00:10:32
B>  10.244.110.128/26 [200/0] via 172.18.0.3, eth0, 00:10:32
B>  10.244.162.128/26 [200/0] via 172.18.0.4, eth0, 00:10:32
C>* 172.18.0.0/16 is directly connected, eth0, 00:10:33
```
### BGP RIB table
```sh
FRR# show bgp summary 

IPv4 Unicast Summary:
BGP router identifier 1.2.3.4, local AS number 65000 vrf-id 0
BGP table version 11
RIB entries 15, using 2280 bytes of memory
Peers 3, using 41 KiB of memory

Neighbor        V         AS MsgRcvd MsgSent   TblVer  InQ OutQ  Up/Down State/PfxRcd
172.18.0.2      4      65000      17      20        0    0    0 00:12:31            4
172.18.0.3      4      65000      17      20        0    0    0 00:12:31            4
172.18.0.4      4      65000      18      20        0    0    0 00:12:31            4

Total number of neighbors 3
```
### BGP running config
```sh
##sh run  
router bgp 65000
 bgp router-id 1.2.3.4
 neighbor 172.18.0.2 remote-as 65000
 neighbor 172.18.0.3 remote-as 65000
 neighbor 172.18.0.4 remote-as 65000
 !
 address-family ipv4 unicast
  network 4.3.2.1/32
  network 9.9.9.9/32
  redist conne ##adv 100.64.255.0 to calico
  neighbor 172.18.0.2 route-reflector-client
  neighbor 172.18.0.3 route-reflector-client
  neighbor 172.18.0.4 route-reflector-client
 exit-address-family
```
### Verification
```sh
#####busybox->frrouting-sec-nic
$kubectl exec -ti busybox-deployment1-65ff9b6c7b-th2kt sh
/ # ip route show
default via 169.254.1.1 dev eth0 
169.254.1.1 dev eth0 scope link 
/ # ping 100.64.255.2
PING 100.64.255.2 (100.64.255.2): 56 data bytes
64 bytes from 100.64.255.2: seq=0 ttl=63 time=0.100 ms
64 bytes from 100.64.255.2: seq=1 ttl=63 time=0.090 ms
64 bytes from 100.64.255.2: seq=2 ttl=63 time=0.254 ms
64 bytes from 100.64.255.2: seq=3 ttl=63 time=0.085 ms
