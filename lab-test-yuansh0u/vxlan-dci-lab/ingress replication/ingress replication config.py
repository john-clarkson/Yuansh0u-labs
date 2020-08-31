##spine
interface Ethernet1/2
  no ip pim sparse-mode
  no shutdown

interface Ethernet1/3
  no ip pim sparse-mode
  no shutdown

##leaf
interface nve1
  no shutdown
  host-reachability protocol bgp
  source-interface loopback0
  member vni 10020
   no mcast-group 239.20.20.20
      ingress-replication protocol bgp
  member vni 10030
   no mcast-group 239.30.30.30
        ingress-replication protocol bgp
  member vni 101234 associate-vrf


## Now bgp will generate type 3 NLRI.

DC2-SPINE# show bgp l2vpn evpn
BGP routing table information for VRF default, address family L2VPN EVPN
BGP table version is 340, Local Router ID is 10.0.0.222
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
*>i[2]:[0]:[0]:[48]:[0011.0011.0011]:[32]:[192.168.20.2]/272
                      10.0.0.201                        100          0 i
*>i[2]:[0]:[0]:[48]:[9000.9000.1111]:[32]:[192.168.20.1]/272
                      10.0.0.201                        100          0 i
*>i[2]:[0]:[0]:[48]:[0011.0011.0011]:[128]:[fc00:192:168:20::2]/368
                      10.0.0.201                        100          0 i
*>i[2]:[0]:[0]:[48]:[9000.9000.1111]:[128]:[fc00:192:168:20::1]/368
                      10.0.0.201                        100          0 i
*>i[3]:[0]:[32]:[10.0.0.201]/88
                      10.0.0.201                        100          0 i

Route Distinguisher: 10.0.0.201:32797
*>i[3]:[0]:[32]:[10.0.0.201]/88
                      10.0.0.201                        100          0 i

Route Distinguisher: 10.0.0.202:3
*>i[5]:[0]:[0]:[24]:[192.168.30.0]:[0.0.0.0]/224
                      10.0.0.202               0        100          0 ?

Route Distinguisher: 10.0.0.202:32787
*>i[3]:[0]:[32]:[10.0.0.202]/88
                      10.0.0.202                        100          0 i

Route Distinguisher: 10.0.0.202:32797
*>i[2]:[0]:[0]:[48]:[0022.0022.0022]:[32]:[192.168.30.2]/272
                      10.0.0.202                        100          0 i
*>i[2]:[0]:[0]:[48]:[9000.9000.2222]:[32]:[192.168.30.1]/272
                      10.0.0.202                        100          0 i
*>i[2]:[0]:[0]:[48]:[0022.0022.0022]:[128]:[fc00:192:168:30::2]/368
                      10.0.0.202                        100          0 i
*>i[2]:[0]:[0]:[48]:[9000.9000.2222]:[128]:[fc00:192:168:30::1]/368
                      10.0.0.202                        100          0 i
*>i[3]:[0]:[32]:[10.0.0.202]/88
                      10.0.0.202                        100          0 i


DC2-SPINE# show bgp l2vpn evpn route-type ?
  <1-6>  EVPN route type number

DC2-SPINE# show bgp l2vpn evpn route-type 3
BGP routing table information for VRF default, address family L2VPN EVPN
Route Distinguisher: 10.0.0.201:32787
BGP routing table entry for [3]:[0]:[32]:[10.0.0.201]/88, version 347
Paths: (1 available, best #1)
Flags: (0x000002) on xmit-list, is not in l2rib/evpn, is not in HW

  Advertised path-id 1
  Path type: internal, path is valid, is best path
  AS-Path: NONE, path sourced internal to AS
    10.0.0.201 (metric 41) from 10.0.0.201 (10.0.0.201)
      Origin IGP, MED not set, localpref 100, weight 0
      Extcommunity: RT:65511:10020 ENCAP:8
      PMSI Tunnel Attribute:
        flags: 0x00, Tunnel type: Ingress Replication
        Label: 10020, Tunnel Id: 10.0.0.201

  Path-id 1 advertised to peers:
    10.0.0.202     

Route Distinguisher: 10.0.0.201:32797
BGP routing table entry for [3]:[0]:[32]:[10.0.0.201]/88, version 348
Paths: (1 available, best #1)
Flags: (0x000002) on xmit-list, is not in l2rib/evpn, is not in HW

  Advertised path-id 1
  Path type: internal, path is valid, is best path
  AS-Path: NONE, path sourced internal to AS
    10.0.0.201 (metric 41) from 10.0.0.201 (10.0.0.201)
      Origin IGP, MED not set, localpref 100, weight 0
      Extcommunity: RT:65511:10030 ENCAP:8
      PMSI Tunnel Attribute:
        flags: 0x00, Tunnel type: Ingress Replication
        Label: 10030, Tunnel Id: 10.0.0.201

  Path-id 1 advertised to peers:
    10.0.0.202     

Route Distinguisher: 10.0.0.202:32787
BGP routing table entry for [3]:[0]:[32]:[10.0.0.202]/88, version 350
Paths: (1 available, best #1)
Flags: (0x000002) on xmit-list, is not in l2rib/evpn, is not in HW

  Advertised path-id 1
  Path type: internal, path is valid, is best path
  AS-Path: NONE, path sourced internal to AS
    10.0.0.202 (metric 41) from 10.0.0.202 (10.0.0.202)
      Origin IGP, MED not set, localpref 100, weight 0
      Extcommunity: RT:65511:10020 ENCAP:8
      PMSI Tunnel Attribute:
        flags: 0x00, Tunnel type: Ingress Replication
        Label: 10020, Tunnel Id: 10.0.0.202

  Path-id 1 advertised to peers:
    10.0.0.201     

Route Distinguisher: 10.0.0.202:32797
BGP routing table entry for [3]:[0]:[32]:[10.0.0.202]/88, version 355
Paths: (1 available, best #1)
Flags: (0x000002) on xmit-list, is not in l2rib/evpn, is not in HW

  Advertised path-id 1
  Path type: internal, path is valid, is best path
  AS-Path: NONE, path sourced internal to AS
    10.0.0.202 (metric 41) from 10.0.0.202 (10.0.0.202)
      Origin IGP, MED not set, localpref 100, weight 0
      Extcommunity: RT:65511:10030 ENCAP:8
      PMSI Tunnel Attribute:
        flags: 0x00, Tunnel type: Ingress Replication
        Label: 10030, Tunnel Id: 10.0.0.202

  Path-id 1 advertised to peers:
    10.0.0.201     

DC2-SPINE#  