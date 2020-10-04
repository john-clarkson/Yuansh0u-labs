# Cisco SP provider core with both ISIS/OSPF design

![](https://i.imgur.com/OykwmKk.jpg)


- Redistribute with tag option

IOS XE
```ios
Router ospf 1
Redis isis level-2 subnet route-map isis-to-ospf
 
Router isis
Net 00.0000.0000.0001.00
Is-type level-2-only
Metric-style wide
Passive-interface loopback 0
Redistribute ospf 1 route-map ospf-to-isis

Address-family ipv6
 Multi-topology
!
Route-map isis-to-ospf deny 10
Match tag 110
Route-map isis-to-ospf permit 20
Set tag 115

Route-map ospf-to-isis deny 10
Match tag 115
Route-map ospf-to-isis permit 20
Set tag 110
```
IOS-XR
```ios 
Route-policy isis-to-ospf
If tag is 110 then
 Drop
Else 
Set tag 115
Pass
Endif
End-policy
!
Route-policy ospf-to-isis
If tag is 115 then
Drop
Else
Set tag 110
Pass 
Endif
End-policy
!
Router ospf 1
Redistribute isis route-policy isis-to-ospf
Area 0
 Interface loopback 0
 Interface gig x/y
Exit
!
Router isis
Net 00.0000.0000.0002.00
Address-family ipv4 unicast
 Metric-style wide
 Redistribute ospf 1 route-policy ospf-to-isis
!
Interface loopback 0
 Passive
 Address-family ipv4 unicast
 Address-family ipv6 unicast
Interface gig x/y
 Address-family ipv4 unicast
 Address-family ipv6 unicast
commit
```
## Enable LDP

IOS XE
```ios
router ospf 1
 mpls ldp autoconfig area 0
 mpls ldp sync
!
router isis
 mpls ldp autoconfig level-2
 mpls ldp sync
!
mpls ldp label 
 allocate global host-routes
```
IOS XR
```ios
!Global mpls enable
mpls ldp
address-family ipv4 unicast
 label local allocate for host-routes
 !
router isis
address-family ipv4 unicast
 mpls ldp auto-config
 Interface gig x/y
  Address-family ipv4 unicast
    mpls ldp sync
 !
router ospf 1
 mpls ldp auto-config
 mpls ldp sync
 
commit
```

## Seamless MPLS design with BGP-LU
Delete redistribution on XE/XR
IOS XE
```ios
router ospf 1
 no redis isis subnets route-map isis-to-ospf
!
router isis
 no redis ospf 1 route-map ospf-to-isis 
!
no route-map isis-to-ospf
no route-map ospf-to-isis
```
IOS XR
```ios
Router ospf 1
 no redistribute isis route-policy isis-to-ospf
Exit
!
Router isis
Net 00.0000.0000.0002.00
Address-family ipv4 unicast
 Metric-style wide
 no redistribute ospf 1 route-policy ospf-to-isis
!
no route-policy ospf-to-isis
no route-policy isis-to-ospf
```
## IOS XE/XR as IBGP ipv4-labeled RR

IOS XE
- https://www.cisco.com/c/en/us/support/docs/multiprotocol-label-switching-mpls/mpls/116127-configure-technology-00.html
```ios
router bgp X
 bgp log-neighbor-changes
 neighbor PE's-LOOPBACK remote-as X
 neighbor PE's-LOOPBACK update-source Loopback0
 neighbor PE's-LOOPBACK next-hop-self all
 neighbor PE's-LOOPBACK send-label
 neighbor PE's-LOOPBACK route-reflector-client
 network PE's-LOOPBACK mask 255.255.255.255
```
IOS XR 
- https://www.cisco.com/c/en/us/support/docs/multiprotocol-label-switching-mpls/multiprotocol-label-switching-mpls/119191-config-unified-mpls-00.html
```ios
router bgp X
 ibgp policy out enforce-modifications
 !
 neighbor PE's-LOOPBACK
 remote-as X
 update-source Loopback0
 address-family ipv4 labeled-unicast
  route-reflector-client
  route-policy my-loopback out
 !
!
route-policy my-loopback
 set next-hop self
end-policy
commit

```
## LSP trace verification
```ios 
This is how packets are forwarded from PE1 to PE2. The loopback prefix of PE2 is 10.100.1.7/32, so that prefix is of interest.

RP/0/0/CPU0:PE1#traceroute                                  
Protocol [ipv4]: 
Target IP address: 10.100.1.7
Source address: 10.100.1.1
Numeric display? [no]: 
Timeout in seconds [3]: 
Probe count [3]: 
Minimum Time to Live [1]: 
Maximum Time to Live [30]: 
Port Number [33434]: 
Loose, Strict, Record, Timestamp, Verbose[none]: 

Type escape sequence to abort.
Tracing the route to 10.100.1.7

 1  10.1.1.2 [MPLS: Labels 24000/24005 Exp 0] 439 msec  119 msec  109 msec 
 2  10.1.2.3 [MPLS: Label 24005 Exp 0] 109 msec  109 msec  109 msec 
 3  10.1.3.4 [MPLS: Labels 24001/24003 Exp 0] 99 msec  99 msec  149 msec 
 4  10.1.4.5 [MPLS: Label 24003 Exp 0] 119 msec  119 msec  99 msec 
 5  10.1.5.6 [MPLS: Label 24001 Exp 0] 109 msec  139 msec  99 msec 
 6  10.1.6.7 109 msec  *  109 msec
``` 
Label 24000 is the LDP label learned from P2 for the prefix 10.100.1.3/32. Label 24005 is the BGP RFC 3107 label learned for the prefix 10.100.1.7/32.
```ios
RP/0/0/CPU0:PE1#show route 10.100.1.7/32

Routing entry for 10.100.1.7/32
  Known via "bgp 1", distance 200, metric 0, [ei]-bgp, type internal
  BIER rid=0x0, flags=0x0, count=0
  Installed May 27 02:52:07.184 for 00:08:52
  Routing Descriptor Blocks
    10.100.1.3, from 10.100.1.3      <<< next-hop is ABR1
      Route metric is 0
  No advertising protos.
RP/0/0/CPU0:PE1#show cef 10.100.1.7/32  
10.100.1.7/32, version 89, internal 0x1000001 0x0 (ptr 0xa1470f74) 
[1], 0x0 (0xa1456614), 0xa08 (0xa16181e0)
 Updated May 27 02:52:07.203
 Prefix Len 32, traffic index 0, precedence n/a, priority 4
   via 10.100.1.3, 3 dependencies, recursive [flags 0x6000]
    path-idx 0 NHID 0x0 [0xa16806f4 0x0]
    recursion-via-/32
    next hop 10.100.1.3 via 24001/0/21
     local label 24003 
     next hop 10.1.1.2/32 Gi0/0/0/0    labels imposed {24000 24005}
RP/0/0/CPU0:PE1#show bgp ipv4 unicast labels 
BGP router identifier 10.100.1.1, local AS number 1
BGP generic scan interval 60 secs
Non-stop routing is enabled
BGP table state: Active
Table ID: 0xe0000000   RD version: 44
BGP main routing table version 44
BGP NSR Initial initsync version 2 (Reached)
BGP NSR/ISSU Sync-Group versions 0/0
BGP scan interval 60 secs

Status codes: s suppressed, d damped, h history, * valid, > best
              i - internal, r RIB-failure, S stale, N Nexthop-discard
Origin codes: i - IGP, e - EGP, ? - incomplete
   Network            Next Hop        Rcvd Label      Local Label
*> 10.100.1.1/32      0.0.0.0         nolabel         3               
*>i10.100.1.7/32      10.100.1.3      24005           24003           

Processed 2 prefixes, 2 paths
There is penultimate-hop popping (PHP) towards ABR1.

RP/0/0/CPU0:P2#show mpls forwarding labels 24000
Local  Outgoing    Prefix             Outgoing     Next Hop        Bytes       
Label  Label       or ID              Interface                    Switched    
------ ----------- ------------------ ------------ --------------- ------------
24000  Pop         10.100.1.3/32      Gi0/0/0/1    10.1.2.3        694765      
Label 24005 is swapped with label 24003 on ABR1.

RP/0/0/CPU0:ABR1#show bgp ipv4 unicast labels 
BGP router identifier 10.100.1.3, local AS number 1
BGP generic scan interval 60 secs
Non-stop routing is enabled
BGP table state: Active
Table ID: 0xe0000000   RD version: 60
BGP main routing table version 60
BGP NSR Initial initsync version 2 (Reached)
BGP NSR/ISSU Sync-Group versions 0/0
BGP scan interval 60 secs

Status codes: s suppressed, d damped, h history, * valid, > best
              i - internal, r RIB-failure, S stale, N Nexthop-discard
Origin codes: i - IGP, e - EGP, ? - incomplete
   Network            Next Hop        Rcvd Label      Local Label
*>i10.100.1.1/32      10.100.1.1      3               24003           
*>i10.100.1.7/32      10.100.1.5      24003           24005           

Processed 2 prefixes, 2 paths
RP/0/0/CPU0:ABR1#show mpls forwarding labels 24005
Wed May 27 04:08:24.255 UTC
Local  Outgoing    Prefix             Outgoing     Next Hop        Bytes       
Label  Label       or ID              Interface                    Switched    
------ ----------- ------------------ ------------ --------------- ------------
24005  24003       10.100.1.7/32                   10.100.1.5      6347        
There is PHP from P1 to ABR2.

RP/0/0/CPU0:P1#show mpls forwarding labels 24001
Local  Outgoing    Prefix             Outgoing     Next Hop        Bytes       
Label  Label       or ID              Interface                    Switched    
------ ----------- ------------------ ------------ --------------- ------------
24001  Pop         10.100.1.5/32      Gi0/0/0/1    10.1.4.5        348835      
The BGP label for the RFC 3107 route 10.100.1.7/32 receivd by ABR2 from PE2 is 3. This is the implicit null label that indicates PHP.

RP/0/0/CPU0:ABR2#show bgp ipv4 unicast labels 
BGP router identifier 10.100.1.5, local AS number 1
BGP generic scan interval 60 secs
Non-stop routing is enabled
BGP table state: Active
Table ID: 0xe0000000   RD version: 47
BGP main routing table version 47
BGP NSR Initial initsync version 2 (Reached)
BGP NSR/ISSU Sync-Group versions 0/0
BGP scan interval 60 secs

Status codes: s suppressed, d damped, h history, * valid, > best
              i - internal, r RIB-failure, S stale, N Nexthop-discard
Origin codes: i - IGP, e - EGP, ? - incomplete
   Network            Next Hop        Rcvd Label      Local Label
*>i10.100.1.1/32      10.100.1.3      24003           24005           
*>i10.100.1.7/32      10.100.1.7      3               24003           

Processed 2 prefixes, 2 paths
Label 24003 is swapped with label 24001 on ABR2.

RP/0/0/CPU0:ABR2#show mpls forwarding labels 24003
Local  Outgoing    Prefix             Outgoing     Next Hop        Bytes       
Label  Label       or ID              Interface                    Switched    
------ ----------- ------------------ ------------ --------------- ------------
24003  24001       10.100.1.7/32      Gi0/0/0/0    10.1.5.6        403676      
There is PHP from P3 to PE2.

RP/0/0/CPU0:P3#show mpls forwarding labels 24001
Local  Outgoing    Prefix             Outgoing     Next Hop        Bytes       
Label  Label       or ID              Interface                    Switched    
------ ----------- ------------------ ------------ --------------- ------------
24001  Pop         10.100.1.7/32      Gi0/0/0/1    10.1.6.7        685191      
RP/0/0/CPU0:PE2#show bgp ipv4 unicast labels 
BGP router identifier 10.100.1.7, local AS number 1
BGP generic scan interval 60 secs
Non-stop routing is enabled
BGP table state: Active
Table ID: 0xe0000000   RD version: 42
BGP main routing table version 42
BGP NSR Initial initsync version 2 (Reached)
BGP NSR/ISSU Sync-Group versions 0/0
BGP scan interval 60 secs

Status codes: s suppressed, d damped, h history, * valid, > best
              i - internal, r RIB-failure, S stale, N Nexthop-discard
Origin codes: i - IGP, e - EGP, ? - incomplete
   Network            Next Hop        Rcvd Label      Local Label
*>i10.100.1.1/32      10.100.1.5      24005           24004           
*> 10.100.1.7/32      0.0.0.0         nolabel         3               

Processed 2 prefixes, 2 paths
```
