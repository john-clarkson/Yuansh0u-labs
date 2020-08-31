bgp default-route

IGP>EGP>incompelte

## Redistribution 


 router bgp 65522
 bgp router-id 150.150.2.2
 bgp log-neighbor-changes
 no bgp default ipv4-unicast
 neighbor 123.123.222.1 remote-as 9000
 !
 address-family ipv4
  network 150.150.2.2 mask 255.255.255.255
  network 192.168.200.0
  redistribute static
  neighbor 123.123.222.1 activate
  default-information originate
 exit-address-family

 ip route 0.0.0.0 0.0.0.0 Null0


 CE-2#show ip bgp 0.0.0.0
BGP routing table entry for 0.0.0.0/0, version 8
Paths: (2 available, best #2, table default)
  Advertised to update-groups:
     4         
  Refresh Epoch 1
  9000 65511
    123.123.222.1 from 123.123.222.1 (2.2.2.2)
      Origin IGP, localpref 100, valid, external
      unknown transitive attribute: flag 0xE0 type 0x15 length 0x5
        value FF00 00FF E7
      rx pathid: 0, tx pathid: 0
  Refresh Epoch 1
  Local
    0.0.0.0 from 0.0.0.0 (150.150.2.2)
      Origin incomplete, metric 0, localpref 100, weight 32768, valid, sourced, best
      rx pathid: 0, tx pathid: 0x0
CE-2#



####

###neighbor -base default-originate


 router bgp 65522
 bgp router-id 150.150.2.2
 bgp log-neighbor-changes
 no bgp default ipv4-unicast
 neighbor 123.123.222.1 remote-as 9000
 !
 address-family ipv4
  neighbor 123.123.222.1 default-originate

## If bgp speaker advertised a default route to a neighbor with neighbor x.x.x.x default-originate commands,
## the output info origin code is IGP,then with a local default-originate messages.
CE-2#sh ip bgp 
BGP table version is 11, local router ID is 150.150.2.2
Status codes: s suppressed, d damped, h history, * valid, > best, i - internal, 
              r RIB-failure, S Stale, m multipath, b backup-path, f RT-Filter, 
              x best-external, a additional-path, c RIB-compressed, 
Origin codes: i - IGP, e - EGP, ? - incomplete
RPKI validation codes: V valid, I invalid, N Not found

     Network          Next Hop            Metric LocPrf Weight Path
     0.0.0.0          0.0.0.0                                0 i
 *>  150.150.1.1/32   123.123.222.1                          0 9000 65511 i
 *>  150.150.2.2/32   0.0.0.0                  0         32768 i
 *>  192.168.100.0    123.123.222.1                          0 9000 65511 i
 *>  192.168.200.0    0.0.0.0                  0         32768 i
CE-2#

CE-2#
CE-2#show ip bgp 0.0.0.0
BGP routing table entry for 0.0.0.0/0, version 11
Paths: (1 available, no best path)
  Advertised to update-groups:
     5         
  Refresh Epoch 1
  Local, (default-originate)
    0.0.0.0 from 0.0.0.0 (150.150.2.2)
      Origin IGP, localpref 100, external
      rx pathid: 0, tx pathid: 0x0
CE-2#

router bgp 65522
  network 0.0.0.0


  