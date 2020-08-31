CE:
 UK-CLIENT-USER#show cry route 
No VPN routes to display

UK-CLIENT-USER#show cry isa sa
IPv4 Crypto ISAKMP SA
dst             src             state          conn-id status
219.235.255.42  61.128.1.1      QM_IDLE           1001 ACTIVE

IPv6 Crypto ISAKMP SA

UK-CLIENT-USER#

===================
UK-CLIENT-USER#show ip access-lists 
Extended IP access list 101
    10 permit ip host 100.65.2.2 host 219.235.255.42 (32 matches)
    20 permit ip host 100.65.3.3 host 219.235.255.42 (164 matches)
UK-CLIENT-USER#



UK-CLIENT-USER#show cry ipsec sa

interface: FastEthernet0/1
    Crypto map tag: P2P-GRE, local addr 61.128.1.1

   protected vrf: (none)
   local  ident (addr/mask/prot/port): (100.65.2.2/255.255.255.255/0/0)
   remote ident (addr/mask/prot/port): (219.235.255.42/255.255.255.255/0/0)
   current_peer 219.235.255.42 port 500
     PERMIT, flags={origin_is_acl,}
    #pkts encaps: 23, #pkts encrypt: 23, #pkts digest: 23
    #pkts decaps: 8, #pkts decrypt: 8, #pkts verify: 8
    #pkts compressed: 0, #pkts decompressed: 0
    #pkts not compressed: 0, #pkts compr. failed: 0
    #pkts not decompressed: 0, #pkts decompress failed: 0
    #send errors 1, #recv errors 1

     local crypto endpt.: 61.128.1.1, remote crypto endpt.: 219.235.255.42
     path mtu 1500, ip mtu 1500, ip mtu idb FastEthernet0/1
     current outbound spi: 0x58614FE0(1482772448)
     PFS (Y/N): N, DH group: none

     inbound esp sas:
      spi: 0xB0E405F8(2967733752)
        transform: esp-3des esp-sha-hmac ,
        in use settings ={Tunnel, }
        conn id: 3, flow_id: SW:3, sibling_flags 80000046, crypto map: P2P-GRE
        sa timing: remaining key lifetime (k/sec): (4455931/2876)
        IV size: 8 bytes
        replay detection support: Y
        Status: ACTIVE

     inbound ah sas:

     inbound pcp sas:

     outbound esp sas:
      spi: 0x58614FE0(1482772448)
        transform: esp-3des esp-sha-hmac ,
        in use settings ={Tunnel, }
        conn id: 4, flow_id: SW:4, sibling_flags 80000046, crypto map: P2P-GRE
        sa timing: remaining key lifetime (k/sec): (4455928/2876)
        IV size: 8 bytes
        replay detection support: Y
        Status: ACTIVE

     outbound ah sas:
          
     outbound pcp sas:

   protected vrf: (none)
   local  ident (addr/mask/prot/port): (100.65.3.3/255.255.255.255/0/0)
   remote ident (addr/mask/prot/port): (219.235.255.42/255.255.255.255/0/0)
   current_peer 219.235.255.42 port 500
     PERMIT, flags={origin_is_acl,}
    #pkts encaps: 76, #pkts encrypt: 76, #pkts digest: 76
    #pkts decaps: 0, #pkts decrypt: 0, #pkts verify: 0
    #pkts compressed: 0, #pkts decompressed: 0
    #pkts not compressed: 0, #pkts compr. failed: 0
    #pkts not decompressed: 0, #pkts decompress failed: 0
    #send errors 14, #recv errors 0

     local crypto endpt.: 61.128.1.1, remote crypto endpt.: 219.235.255.42
     path mtu 1500, ip mtu 1500, ip mtu idb FastEthernet0/1
     current outbound spi: 0x48E28E78(1222807160)
     PFS (Y/N): N, DH group: none

     inbound esp sas:
      spi: 0x80601988(2153781640)
        transform: esp-3des esp-sha-hmac ,
        in use settings ={Tunnel, }
        conn id: 1, flow_id: SW:1, sibling_flags 80000046, crypto map: P2P-GRE
        sa timing: remaining key lifetime (k/sec): (4470745/2869)
        IV size: 8 bytes
        replay detection support: Y
        Status: ACTIVE

     inbound ah sas:

     inbound pcp sas:

     outbound esp sas:
      spi: 0x48E28E78(1222807160)
        transform: esp-3des esp-sha-hmac ,
        in use settings ={Tunnel, }
        conn id: 2, flow_id: SW:2, sibling_flags 80000046, crypto map: P2P-GRE
        sa timing: remaining key lifetime (k/sec): (4470733/2869)
        IV size: 8 bytes
        replay detection support: Y
        Status: ACTIVE

     outbound ah sas:

     outbound pcp sas:


     UK-CLIENT-USER#sh run inter tunnel 4
Building configuration...

Current configuration : 203 bytes
!
interface Tunnel4
 description IPV4 OVER IPV4 Tunnel
 ip address 100.65.68.174 255.255.255.252
 ip mtu 1400
 ip tcp adjust-mss 1360
 tunnel source 100.65.2.2
 tunnel destination 219.235.255.42
 !
end

UK-CLIENT-USER#sh run inter tunnel 6
Building configuration...

Current configuration : 217 bytes
!
interface Tunnel6
 description IPV6 OVER IPV4 TUNNEL
 ip address 100.65.67.174 255.255.255.252
 ipv6 address FC00:1:1:1::1/64
 ipv6 ospf 1 area 0
 tunnel source 100.65.3.3
 tunnel destination 219.235.255.42
 !
end

UK-CLIENT-USER#


======================================================
UK-CLIENT-USER#ping 8.8.8.8 sou 103.103.103.103

Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 8.8.8.8, timeout is 2 seconds:
Packet sent with a source address of 103.103.103.103 
!!!!!
Success rate is 100 percent (5/5), round-trip min/avg/max = 156/194/220 ms
UK-CLIENT-USER#ping FC00:123:123:123::254 sou
UK-CLIENT-USER#ping FC00:123:123:123::254 source 103:103:103::103 

Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to FC00:123:123:123::254, timeout is 2 seconds:
Packet sent with a source address of 103:103:103::103
!!!!!
Success rate is 100 percent (5/5), round-trip min/avg/max = 184/193/208 ms
UK-CLIENT-USER#
