HUB#sh run
HUB#sh running-config 
Building configuration...

Current configuration : 2961 bytes
!
! Last configuration change at 17:37:09 UTC Tue Mar 27 2018
!
version 15.5
service timestamps debug datetime msec
service timestamps log datetime msec
no platform punt-keepalive disable-kernel-core
platform console serial
!
hostname HUB
!
boot-start-marker
boot-end-marker
!
!
vrf definition IWAN-TRANSPORT-1
 rd 1:1
 !
 address-family ipv4
 exit-address-family
!
vrf definition inside-vrf
 rd 2:2
 !
 address-family ipv4
 exit-address-family
!
!
no aaa new-model
!
!
!
!
!
!
!
!
!
!
!



!
!         
!
!
!
!
!
!
!
!
subscriber templating
!
multilink bundle-name authenticated
!
!
!
!
!
!
!
!
!
!
!
!         
!
license udi pid CSR1000V sn 9QV367MGW3K
!
spanning-tree extend system-id
!
!
redundancy
!
crypto ikev2 proposal AES/CBC/256 
 encryption aes-cbc-256
 integrity sha512
 group 14
!
!
crypto ikev2 keyring DMVPN-KEYRING-1
 peer ANY
  address 0.0.0.0 0.0.0.0
  pre-shared-key c1sco123
 !
!
!
crypto ikev2 profile FVRF-IKEv2-IWAN-TRANSPORT-1
 match fvrf IWAN-TRANSPORT-1
 match identity remote address 0.0.0.0 
 authentication remote pre-share
 authentication local pre-share
 keyring local DMVPN-KEYRING-1
 ivrf inside-vrf
!
!
!
!
! 
!
!
!
!
!
crypto ipsec security-association replay window-size 1024
!
crypto ipsec transform-set AES256/SHA/TRANSPORT esp-aes 256 esp-sha-hmac 
 mode transport
!
crypto ipsec profile DMVPN-PROFILE-TRANSPORT-1
 set transform-set AES256/SHA/TRANSPORT 
 set ikev2-profile FVRF-IKEv2-IWAN-TRANSPORT-1
!
!
!
!
!
!
! 
! 
! 
! 
! 
! 
!
!
interface Loopback0
 vrf forwarding inside-vrf
 ip address 1.1.1.1 255.255.255.255
!
interface Tunnel0
 vrf forwarding inside-vrf
 ip address 100.64.1.100 255.255.255.0
 no ip redirects
 ip mtu 1400
 ip nhrp map multicast dynamic
 ip nhrp network-id 101
 ip nhrp redirect
 ip tcp adjust-mss 1360
 tunnel source GigabitEthernet1.15
 tunnel mode gre multipoint
 tunnel key 101
 tunnel vrf IWAN-TRANSPORT-1
 tunnel protection ipsec profile DMVPN-PROFILE-TRANSPORT-1
!
interface GigabitEthernet1
 no ip address
 negotiation auto
!
interface GigabitEthernet1.15
 description INET-Front-door
 encapsulation dot1Q 15
 vrf forwarding IWAN-TRANSPORT-1
 ip address 202.100.15.1 255.255.255.0
!
interface GigabitEthernet2
 no ip address
 shutdown 
 negotiation auto
!
interface GigabitEthernet3
 no ip address
 shutdown
 negotiation auto
!
interface GigabitEthernet4
 no ip address
 shutdown
 negotiation auto
!
!
router eigrp OVERLAY
 !
 address-family ipv4 unicast vrf inside-vrf autonomous-system 500
  !
  af-interface Tunnel0
   no split-horizon
  exit-af-interface
  !
  topology base
  exit-af-topology
  network 1.1.1.1 0.0.0.0
  network 100.64.1.0 0.0.0.255
  eigrp router-id 1.1.1.1
 exit-address-family
!
!
virtual-service csr_mgmt
!
ip forward-protocol nd
!
no ip http server
no ip http secure-server
ip route vrf IWAN-TRANSPORT-1 0.0.0.0 0.0.0.0 202.100.15.5
!
!
!
!
control-plane
!
 !
 !
 !
 !        
!
!
!
!
!
line con 0
 stopbits 1
line vty 0
 login
line vty 1
 login
 length 0
line vty 2 4
 login
!
!
end

HUB#show dmvpn                            
Legend: Attrb --> S - Static, D - Dynamic, I - Incomplete
        N - NATed, L - Local, X - No Socket
        T1 - Route Installed, T2 - Nexthop-override
        C - CTS Capable
        # Ent --> Number of NHRP entries with same NBMA peer
        NHS Status: E --> Expecting Replies, R --> Responding, W --> Waiting
        UpDn Time --> Up or Down Time for a Tunnel
==========================================================================

Interface: Tunnel0, IPv4 NHRP Details 
Type:Hub, NHRP Peers:2, 

 # Ent  Peer NBMA Addr Peer Tunnel Add State  UpDn Tm Attrb
 ----- --------------- --------------- ----- -------- -----
     1 202.100.25.1         100.64.1.1    UP 00:10:56     D
     1 202.100.35.1         100.64.1.2    UP 00:11:34     D

HUB#show ip eigrp vrf inside-vrf topology 
EIGRP-IPv4 VR(OVERLAY) Topology Table for AS(500)/ID(1.1.1.1)
           Topology(base) TID(0) VRF(inside-vrf)
Codes: P - Passive, A - Active, U - Update, Q - Query, R - Reply,
       r - reply Status, s - sia Status 

P 192.168.10.0/24, 1 successors, FD is 9830481920
        via 100.64.1.1 (9830481920/163840), Tunnel0
P 100.64.1.0/24, 1 successors, FD is 9830400000
        via Connected, Tunnel0
P 1.1.1.1/32, 1 successors, FD is 163840
        via Connected, Loopback0
P 192.168.20.0/24, 1 successors, FD is 9830481920
        via 100.64.1.2 (9830481920/163840), Tunnel0

HUB#show ip route vrf inside-vrf          

Routing Table: inside-vrf
Codes: L - local, C - connected, S - static, R - RIP, M - mobile, B - BGP
       D - EIGRP, EX - EIGRP external, O - OSPF, IA - OSPF inter area 
       N1 - OSPF NSSA external type 1, N2 - OSPF NSSA external type 2
       E1 - OSPF external type 1, E2 - OSPF external type 2
       i - IS-IS, su - IS-IS summary, L1 - IS-IS level-1, L2 - IS-IS level-2
       ia - IS-IS inter area, * - candidate default, U - per-user static route
       o - ODR, P - periodic downloaded static route, H - NHRP, l - LISP
       a - application route
       + - replicated route, % - next hop override, p - overrides from PfR

Gateway of last resort is not set

      1.0.0.0/32 is subnetted, 1 subnets
C        1.1.1.1 is directly connected, Loopback0
      100.0.0.0/8 is variably subnetted, 2 subnets, 2 masks
C        100.64.1.0/24 is directly connected, Tunnel0
L        100.64.1.100/32 is directly connected, Tunnel0
D     192.168.10.0/24 [90/76800640] via 100.64.1.1, 00:11:06, Tunnel0
D     192.168.20.0/24 [90/76800640] via 100.64.1.2, 00:11:46, Tunnel0
HUB#show crypto ikev2 sa                  
 IPv4 Crypto IKEv2  SA 

Tunnel-id Local                 Remote                fvrf/ivrf            Status 
1         202.100.15.1/500      202.100.25.1/500      IWAN-TRANSPORT-1/i   READY  
      Encr: AES-CBC, keysize: 256, PRF: SHA512, Hash: SHA512, DH Grp:5, Auth sign: PSK, Auth verify: PSK
      Life/Active Time: 86400/441 sec

Tunnel-id Local                 Remote                fvrf/ivrf            Status 
2         202.100.15.1/500      202.100.35.1/500      IWAN-TRANSPORT-1/i   READY  
      Encr: AES-CBC, keysize: 256, PRF: SHA512, Hash: SHA512, DH Grp:5, Auth sign: PSK, Auth verify: PSK
      Life/Active Time: 86400/441 sec

 IPv6 Crypto IKEv2  SA 

HUB#show crypto ipsec sa                  

interface: Tunnel0
    Crypto map tag: Tunnel0-head-0, local addr 202.100.15.1

   protected vrf: inside-vrf
   local  ident (addr/mask/prot/port): (202.100.15.1/255.255.255.255/47/0)
   remote ident (addr/mask/prot/port): (202.100.35.1/255.255.255.255/47/0)
   current_peer 202.100.35.1 port 500
     PERMIT, flags={origin_is_acl,}
    #pkts encaps: 102, #pkts encrypt: 102, #pkts digest: 102
    #pkts decaps: 102, #pkts decrypt: 102, #pkts verify: 102
    #pkts compressed: 0, #pkts decompressed: 0
    #pkts not compressed: 0, #pkts compr. failed: 0
    #pkts not decompressed: 0, #pkts decompress failed: 0
    #send errors 0, #recv errors 0

     local crypto endpt.: 202.100.15.1, remote crypto endpt.: 202.100.35.1
     plaintext mtu 1362, path mtu 1400, ip mtu 1400, ip mtu idb Tunnel0
     current outbound spi: 0x8DD9D24(148741412)
     PFS (Y/N): N, DH group: none

     inbound esp sas:
      spi: 0x122E236(19063350)
        transform: esp-256-aes esp-sha-hmac ,
        in use settings ={Transport, }
        conn id: 2004, flow_id: CSR:4, sibling_flags FFFFFFFF80000008, crypto map: Tunnel0-head-0
        sa timing: remaining key lifetime (k/sec): (4607988/3155)
        IV size: 16 bytes
        replay detection support: Y  replay window size: 1024
        Status: ACTIVE(ACTIVE)

     inbound ah sas:

     inbound pcp sas:

     outbound esp sas:
      spi: 0x8DD9D24(148741412)
        transform: esp-256-aes esp-sha-hmac ,
        in use settings ={Transport, }
        conn id: 2003, flow_id: CSR:3, sibling_flags FFFFFFFF80000008, crypto map: Tunnel0-head-0
        sa timing: remaining key lifetime (k/sec): (4607992/3155)
        IV size: 16 bytes
        replay detection support: Y  replay window size: 1024
        Status: ACTIVE(ACTIVE)
          
     outbound ah sas:

     outbound pcp sas:

   protected vrf: inside-vrf
   local  ident (addr/mask/prot/port): (202.100.15.1/255.255.255.255/47/0)
   remote ident (addr/mask/prot/port): (202.100.25.1/255.255.255.255/47/0)
   current_peer 202.100.25.1 port 500
     PERMIT, flags={origin_is_acl,}
    #pkts encaps: 97, #pkts encrypt: 97, #pkts digest: 97
    #pkts decaps: 96, #pkts decrypt: 96, #pkts verify: 96
    #pkts compressed: 0, #pkts decompressed: 0
    #pkts not compressed: 0, #pkts compr. failed: 0
    #pkts not decompressed: 0, #pkts decompress failed: 0
    #send errors 0, #recv errors 0

     local crypto endpt.: 202.100.15.1, remote crypto endpt.: 202.100.25.1
     plaintext mtu 1362, path mtu 1400, ip mtu 1400, ip mtu idb Tunnel0
     current outbound spi: 0x7A70E7A(128388730)
     PFS (Y/N): N, DH group: none

     inbound esp sas:
      spi: 0xFB47100C(4215738380)
        transform: esp-256-aes esp-sha-hmac ,
        in use settings ={Transport, }
        conn id: 2002, flow_id: CSR:2, sibling_flags FFFFFFFF80000008, crypto map: Tunnel0-head-0
        sa timing: remaining key lifetime (k/sec): (4607989/3155)
        IV size: 16 bytes
        replay detection support: Y  replay window size: 1024
        Status: ACTIVE(ACTIVE)

     inbound ah sas:

     inbound pcp sas:

     outbound esp sas:
      spi: 0x7A70E7A(128388730)
        transform: esp-256-aes esp-sha-hmac ,
        in use settings ={Transport, }
        conn id: 2001, flow_id: CSR:1, sibling_flags FFFFFFFF80000008, crypto map: Tunnel0-head-0
        sa timing: remaining key lifetime (k/sec): (4607993/3155)
        IV size: 16 bytes
        replay detection support: Y  replay window size: 1024
        Status: ACTIVE(ACTIVE)

     outbound ah sas:

     outbound pcp sas:
