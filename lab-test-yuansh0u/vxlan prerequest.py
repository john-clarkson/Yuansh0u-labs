BUM

 vendor
  Cisco underlay 
   PIM
  platform
    nexus 9k PIM sparse-mode with RP 
      (Join message [*,G]--->RP)
      (multicast Source [S,G--->RP])
      (RP--->SPT--->downstream--PIM prune)
      (shortest path -->source tree-->shortest path--RPF check)
      RPF check <reference IGP calculation OSPF/ISIS/EIGRP>
      RPF with BGP <BGP>IGP>
      RPF <static mroute>dynamic routing>

GRE 
  site A 
    r1 r2 r3 r4 ==ospf 
  site B 
    r5 r6 r7 r8 ==ospf

R1-OSPF COST HIGHER THAN GRE-R5

GRE  r4--Prefer--r8


Unicast topology is not fully enable PIM.

Standard PIM rp IS control plane {Seems as BGP RR}
   Nexus 5K PIM Bidir PIM (NO SG) RP <data plane>
 

  JUNIPER 
   BGP EVPN TYPE3
  H3C/HUAWEI
 
 opensource frrouting TYPE3 
####

 DCI
  underlay with PIM

  MSDP 

DC1 --RP----<MSDP tcp session to sync SG pair>----RP---DC2
Additional tcp session

  Inband PIM
PIM--->SG<SYNC--->DC2 RP>

   vendor 
    CISCO JUNIPER 
    BGP EVPN
     type 1 2 3 4 5 <6 7 8>
     
     678 are design for tenant multicast, in other words, multicast in overlay.

    opensource 2 3 5
     1-4  replace VPC MLAG=Feature BGP EVPN Multi-homing
     1=Auto discovery message
     4=ESI Ethernet segment identifier
LACP message encode on BGP update message

    

    encode 
    decode
    redistribute

OSPF >>>>>encode >>>BGP 





 

 APP-->>DISK
 cpu---mem---disk <3 location or 3 server>
 MEM----rdma----MEM----rdma----MEM
   <---------------rdma------------>

SW L2 
  Rdma over Ethernet V1
routable
 RDMA over ethernet v2 ===UDP encap

IWARP  tcp encap
 RDMA message is payload

SDS

Web page <Control-plane>

DRBD networking version Raid1+RDMA <v1 v2 IWARP>

Software defined storage. <data-plane>

FC??????FUCK

MAX=32G


aws google micro digital ocean ali tecent qingcloud easystack nutinx <they are all IP based SAN>
FC is suck!!!

PORT virtualization!!!


NIC cards
 
 IP -->>vmware kvm hyper v 

   create-->allocation to vm
    it works. pretty easy to use!!! no limited!


   BUT....FC???
    NPIV
   FC port roles
    NP P 
   FC  


what about packet loss????
First, FC networking is design for storage stack, which means, it gerentee no packet loss in the SAN network.
so, IP network ??? HOW to fix it?

the answer is QOS!!! BUT!!!this qos is design for IP SAN network. not every plaform support it!


what is it ??
this is called PFC (pause frame control)!
what plaform support it? with different vendors?
CISCO NEXUS series
DELL SW
H3C S6820 and above!
HUAWEI???NOPE...
mallox sw!
mailuosi




