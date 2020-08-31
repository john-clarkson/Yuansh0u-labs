vrf definition A
 rd 1:1
 vpn id 1:1

address-family ipv4
  mdt auto-discovery mldp
  mdt default mpls mldp p2mp
  mdt overlay use-bgp

  ##
  PE1#sh run | sec router bgp
router bgp 9000
 bgp router-id 1.1.1.1
 bgp log-neighbor-changes
 no bgp default ipv4-unicast
 neighbor 4.4.4.4 remote-as 9000
 neighbor 4.4.4.4 update-source Loopback0
 !
 address-family ipv4
 exit-address-family
 !
 address-family ipv4 mvpn
  neighbor 4.4.4.4 activate
  neighbor 4.4.4.4 send-community extended
 exit-address-family
 !
 address-family vpnv4
  neighbor 4.4.4.4 activate
  neighbor 4.4.4.4 send-community extended
 exit-address-family
 !
 address-family ipv4 vrf A
  neighbor 169.254.11.254 remote-as 60000
  neighbor 169.254.11.254 activate
  neighbor 169.254.11.254 as-override
 exit-address-family

 PE1#show bgp ipv4 mvpn vrf A 
BGP table version is 50, local router ID is 1.1.1.1
Status codes: s suppressed, d damped, h history, * valid, > best, i - internal, 
              r RIB-failure, S Stale, m multipath, b backup-path, f RT-Filter, 
              x best-external, a additional-path, c RIB-compressed, 
Origin codes: i - IGP, e - EGP, ? - incomplete
RPKI validation codes: V valid, I invalid, N Not found

     Network          Next Hop            Metric LocPrf Weight Path
Route Distinguisher: 1:1 (default for vrf A)
 *>  [1][1:1][1.1.1.1]/12
                       0.0.0.0                            32768 ?
 *>i [1][1:1][2.2.2.2]/12
                       2.2.2.2                  0    100      0 ?
 *>i [1][1:1][3.3.3.3]/12
                       3.3.3.3                  0    100      0 ?
 *>  [5][1:1][10.10.10.10][232.1.1.1]/18
                       0.0.0.0                            32768 ?
 *>i [5][1:1][20.20.20.20][232.2.2.2]/18
                       2.2.2.2                  0    100      0 ?
 *>i [7][1:1][9000][10.10.10.10/32][232.1.1.1/32]/22
                       2.2.2.2                  0    100      0 ?
 *>  [7][1:1][9000][20.20.20.20/32][232.2.2.2/32]/22
     Network          Next Hop            Metric LocPrf Weight Path
                       0.0.0.0                            32768 ?
PE1#