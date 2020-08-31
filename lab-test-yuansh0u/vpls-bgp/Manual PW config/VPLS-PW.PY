 init configuration
  



 R2:
 l2vpn vfi context TEST 
 vpn id 1
 member 4.4.4.4 encapsulation mpls
 member 6.6.6.6 encapsulation mpls
 !
 bridge-domain 2 
 member GigabitEthernet1 service-instance 1
 member vfi TEST
!

 interface GigabitEthernet1
 no ip address
 negotiation auto
 service instance 1 ethernet
  encapsulation default
 R4:
 l2vpn vfi context TEST 
 vpn id 1
 member 2.2.2.2 encapsulation mpls
 member 6.6.6.6 encapsulation mpls
 !
 bridge-domain 2 
 member GigabitEthernet1 service-instance 1
 member vfi TEST
!

 interface GigabitEthernet1
 no ip address
 negotiation auto
 service instance 1 ethernet
  encapsulation default

  R6:
 l2vpn vfi context TEST 
 vpn id 1
 member 2.2.2.2 encapsulation mpls
 member 4.4.4.4 encapsulation mpls
 !
 bridge-domain 2 
 member GigabitEthernet1 service-instance 1
 member vfi TEST
!

 interface GigabitEthernet1
 no ip address
 negotiation auto
 service instance 1 ethernet
  encapsulation default

  !

  R1-HQ#sh run int g1
Building configuration...

Current configuration : 162 bytes
!
interface GigabitEthernet1
 ip address 10.1.1.1 255.255.255.0
 ip pim sparse-mode
 ip ospf network point-to-multipoint
 ip ospf 1 area 0
 negotiation auto
end
R1-HQ#show ip os neighbor 

Neighbor ID     Pri   State           Dead Time   Address         Interface
10.1.1.5          0   FULL/  -        00:01:58    10.1.1.7        GigabitEthernet1
5.5.5.5           0   FULL/  -        00:01:37    10.1.1.5        GigabitEthernet1
R1-HQ# 

R1-HQ# show ip pim neighbor 
PIM Neighbor Table
Mode: B - Bidir Capable, DR - Designated Router, N - Default DR Priority,
      P - Proxy Capable, S - State Refresh Capable, G - GenID Capable,
      L - DR Load-balancing Capable
Neighbor          Interface                Uptime/Expires    Ver   DR
Address                                                            Prio/Mode
10.1.1.7          GigabitEthernet1         00:02:28/00:01:42 v2    1 / DR S P G
10.1.1.5          GigabitEthernet1         00:12:24/00:01:43 v2    1 / S P G
R1-HQ# 

===
R2-PE1#SHOW MPLS FORwarding-table 
Local      Outgoing   Prefix           Bytes Label   Outgoing   Next Hop    
Label      Label      or Tunnel Id     Switched      interface              
16         Pop Label  3.3.3.3/32       0             Gi2        23.1.1.3    
17         Pop Label  34.1.1.0/24      0             Gi2        23.1.1.3    
18         16         4.4.4.4/32       0             Gi2        23.1.1.3    
19         No Label   l2ckt(1)         12234         none       point2point 
20         No Label   l2ckt(2)         4072          none       point2point 
21         Pop Label  36.1.1.0/24      0             Gi2        23.1.1.3    
22         18         6.6.6.6/32       0             Gi2        23.1.1.3    
R2-PE1# 


R6-PE3#show bridge-domain 
Bridge-domain 2 (3 ports in all)
State: UP                    Mac learning: Enabled
Aging-Timer: 300 second(s)
    GigabitEthernet1 service instance 1
    vfi TEST neighbor 2.2.2.2 1
    vfi TEST neighbor 4.4.4.4 1
   AED MAC address    Policy  Tag       Age  Pseudoport
   0   5000.0005.0000 forward dynamic   298  TEST.1004012
   0   5000.0004.0000 forward dynamic   300  TEST.1004011
   0   5000.0007.0000 forward dynamic   294  GigabitEthernet1.EFP1

R6-PE3#

R6-PE3#show l2vpn vfi 
Legend: RT=Route-target, S=Split-horizon, Y=Yes, N=No

VFI name: TEST, state: up, type: multipoint, signaling: LDP
  VPN ID: 1
  Bridge-Domain 2 attachment circuits:
  Pseudo-port interface: pseudowire100001
  Interface          Peer Address     VC ID        S
  pseudowire100003   4.4.4.4          1            Y
  pseudowire100002   2.2.2.2          1            Y

R6-PE3#


R6-PE3#show l2vpn service vfi all detail 
Legend: St=State    XC St=State in the L2VPN Service      Prio=Priority
        UP=Up       DN=Down            AD=Admin Down      IA=Inactive
        SB=Standby  HS=Hot Standby     RV=Recovering      NH=No Hardware
        m=manually selected

  Interface          Group       Encapsulation                   Prio  St  XC St
  ---------          -----       -------------                   ----  --  -----
VPLS name: TEST, State: UP
  pw100001                       TEST(VFI)                       0     UP  UP   
  pw100003           core_pw     4.4.4.4:1(MPLS)                 0     UP  UP   
                                 Local VC label 22              
                                 Remote VC label 20             
                                                                
  pw100002           core_pw     2.2.2.2:1(MPLS)                 0     UP  UP   
                                 Local VC label 21              
                                 Remote VC label 20             
                                                                
R6-PE3#