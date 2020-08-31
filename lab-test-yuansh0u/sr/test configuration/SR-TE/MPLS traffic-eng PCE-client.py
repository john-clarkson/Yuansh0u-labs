 ipv4 unnumbered mpls traffic-eng Loopback0
 router isis fuck
    address-family ipv4 unicast
     mpls traffic-eng router-id loopback0
     mpls traffic-eng level-2-only
     commit
     !
     exit
     exit

mpls traffic-eng
 pce
  peer source ipv4 100.64.1.6
  peer ipv4 150.1.255.253
  !
  segment-routing
  logging events peer-status
  stateful-client
   instantiation

auto-tunnel pcc
 tunnel-id min 1 max 99
 reoptimize timers delay install 0
 commit

##verify download info from PCE(ODL)/PATHMAN SR POLICYS
RP/0/0/CPU0:XR-P3#show mpls traffic-eng tunnels 
Tue Nov 28 12:17:35.878 UTC


Name: tunnel-te14  Destination: 100.64.1.2  Ifhandle:0x1380 (auto-tunnel pcc)
  Signalled-Name: XR-P3 -> XR-P2
  Status:
    Admin:    up Oper:   up   Path:  valid   Signalling: connected

    path option 10, (Segment-Routing) type explicit (autopcc_te14) (Basis for Setup)
      Protected-by PO index: none
    G-PID: 0x0800 (derived from egress interface properties)
    Bandwidth Requested: 0 kbps  CT0
    Creation Time: Tue Nov 28 12:06:09 2017 (00:11:27 ago)
  Config Parameters:
    Bandwidth:        0 kbps (CT0) Priority:  7  7 Affinity: 0x0/0xffff
    Metric Type: TE (global)
    Path Selection:
      Tiebreaker: Min-fill (default)
      Protection: any (default)
    Hop-limit: disabled
    Cost-limit: disabled
    Path-invalidation timeout: 10000 msec (default), Action: Tear (default)
    AutoRoute: disabled  LockDown: disabled   Policy class: not set
    Forward class: 0 (default)
    Forwarding-Adjacency: disabled
    Autoroute Destinations: 0
    Loadshare:          0 equal loadshares
    Auto-bw: disabled
    Path Protection: Not Enabled
    BFD Fast Detection: Disabled
    Reoptimization after affinity failure: Enabled
    SRLG discovery: Disabled
  Auto PCC: 
    Symbolic name: XR-P3 -> XR-P2
    PCEP ID: 15
    Delegated to: 150.1.255.253
    Created by: 150.1.255.253
  History:
    Tunnel has been up for: 00:11:27 (since Tue Nov 28 12:06:09 UTC 2017)
    Current LSP:
      Uptime: 00:11:27 (since Tue Nov 28 12:06:09 UTC 2017)

  Segment-Routing Path Info (PCE controlled)
    Segment0[Node]: 100.64.1.4, Label: 16004
    Segment1[Node]: 100.64.22.2, Label: 16022
    Segment2[Node]: 100.64.1.2, Label: 16002
Displayed 1 (of 1) heads, 0 (of 0) midpoints, 0 (of 0) tails
Displayed 1 up, 0 down, 0 recovering, 0 recovered heads
RP/0/0/CPU0:XR-P3#
###streering traffic through te interface
router static
 address-family ipv4 unicast
  100.64.1.2/32 tunnel-te14
Essentially – the path that the SR-TE tunnel takes contains no real control-plane state, 
this is a real advantage for large networks as the whole thing is much more efficient.
##NOTE ODL does not surpport streering traffic to te tunnel.
The only pitfall here, is that whilst we’ve generated a Segment-routed LSP, 
like all MPLS-TE tunnels we need to tell the router to put traffic into it – 
normally we do this with autoroute-announce or a static route, 
at this time OpenDaylight doesn’t support the PCEP extensions to actually configure a static route, 
so we still need to manually put traffic into the tunnel – this is fixed in Cisco’s openSDN and WAE (wan automation engine)

##test
CE1#traceroute vrf B 2.2.2.2 source lo1
Type escape sequence to abort.
Tracing the route to 2.2.2.2
VRF info: (vrf in name/id, vrf out name/id)
  1 169.254.100.254 18 msec 18 msec 18 msec
  2 169.254.34.4 [MPLS: Labels 16022/16002/24004 Exp 0] 54 msec 68 msec 45 msec
  3 169.254.224.2 [MPLS: Labels 16002/24004 Exp 0] 47 msec 59 msec 52 msec
  4 169.254.222.22 [MPLS: Label 24004 Exp 0] 52 msec 68 msec 52 msec
  5 169.254.200.1 66 msec 67 msec * 

  