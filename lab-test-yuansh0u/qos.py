ENTERPRISE QoS
IDC-CORE

 ip access-list extended QOS_DSCP_TEST_UK
 permit ip any any dscp af11
 permit ip any any dscp af21
 permit ip any any dscp af31
 permit ip any any dscp af41
 permit ip any any dscp ef
 permit ip any any dscp cs1
 permit ip any any dscp cs2
 permit ip any any dscp cs3
 permit ip any any dscp cs4
 permit ip any any dscp cs5
 permit ip any any dscp cs6
 permit ip any any dscp cs7
 permit ip any any


ip access-list extended QOS_DSCP_TEST_GERMANY
 permit ip any any dscp af11
 permit ip any any dscp af21
 permit ip any any dscp af31
 permit ip any any dscp af41
 permit ip any any dscp ef
 permit ip any any dscp cs1
 permit ip any any dscp cs2
 permit ip any any dscp cs3
 permit ip any any dscp cs4
 permit ip any any dscp cs5
 permit ip any any dscp cs6
 permit ip any any dscp cs7
 permit ip any any

interface g1/0.10
 ip access-group QOS_DSCP_TEST_UK in

interface g1/0.20
 ip access-group QOS_DSCP_TEST_GERMANY in

UK:
class-map match-any DATA
 match  dscp af21 
class-map match-any INTERACTIVE-VIDEO
 match  dscp cs4  af41 
class-map match-any CRITICAL-DATA
 match  dscp cs3  af31 
class-map match-any VOICE
 match  dscp ef 
 match dscp cs5
class-map match-any SCAVENGER
 match  dscp cs1  af11 
class-map match-any ROUTING-PROTOCOL
 match protocol bgp
 match protocol ospf
 match protocol eigrp
 match protocol rip
class-map match-any NETWORK-CRITICAL
 match  dscp cs2  cs6 
!
!
policy-map MARK-ROUTING-PROTOCOL
 class ROUTING-PROTOCOL
  set dscp cs6
policy-map WAN
 class VOICE
    priority percent 10
 class INTERACTIVE-VIDEO
    priority percent 23
 class CRITICAL-DATA
    bandwidth percent 15
     random-detect dscp-based
 class DATA
    bandwidth percent 19
     random-detect dscp-based
 class SCAVENGER
    bandwidth percent 5
 class NETWORK-CRITICAL
    bandwidth percent 3
  service-policy MARK-ROUTING-PROTOCOL
 class class-default
    bandwidth percent 25
     random-detect
    fair-queue
policy-map WAN-INTERFACE-F0/0
 class class-default
    shape average 20000000
  service-policy WAN
!       
interface FastEthernet0/0
 service-policy output WAN-INTERFACE-F0/0
end  

germany
class-map match-any DATA
 match  dscp af21 
class-map match-any INTERACTIVE-VIDEO
 match  dscp cs4  af41 
class-map match-any CRITICAL-DATA
 match  dscp cs3  af31 
class-map match-any VOICE
 match  dscp ef 
class-map match-any SCAVENGER
 match  dscp cs1  af11 
class-map match-any ROUTING-PROTOCOL
 match protocol bgp
 match protocol ospf
 match protocol eigrp
 match protocol rip
class-map match-any NETWORK-CRITICAL
 match  dscp cs2  cs6 
!
!
policy-map MARK-ROUTING-PROTOCOL
 class ROUTING-PROTOCOL
  set dscp cs6
policy-map WAN
 class VOICE
    priority percent 10
 class INTERACTIVE-VIDEO
    priority percent 23
 class CRITICAL-DATA
    bandwidth percent 15
     random-detect dscp-based
 class DATA
    bandwidth percent 19
     random-detect dscp-based
 class SCAVENGER
    bandwidth percent 5
 class NETWORK-CRITICAL
    bandwidth percent 3
  service-policy MARK-ROUTING-PROTOCOL
 class class-default
    bandwidth percent 25
     random-detect
    fair-queue
policy-map WAN-INTERFACE-F0/0
 class class-default
    shape average 10000000
  service-policy WAN
!         
interface FastEthernet0/0
 service-policy output WAN-INTERFACE-F0/0

 =============================================
 UK#show policy-map interface f0/0
 FastEthernet0/0 

  Service-policy output: WAN-INTERFACE-F0/0

    Class-map: class-default (match-any)
      876 packets, 103224 bytes
      5 minute offered rate 0 bps, drop rate 0 bps
      Match: any 
      Queueing
      queue limit 64 packets
      (queue depth/total drops/no-buffer drops) 0/0/0
      (pkts output/bytes output) 876/81234
      shape (average) cir 20000000, bc 80000, be 80000
      target shape rate 20000000

      Service-policy : WAN

        queue stats for all priority classes:
          
          queue limit 64 packets
          (queue depth/total drops/no-buffer drops) 0/0/0
          (pkts output/bytes output) 0/0

        Class-map: VOICE (match-any)
          0 packets, 0 bytes
          5 minute offered rate 0 bps, drop rate 0 bps
          Match:  dscp ef (46)
            0 packets, 0 bytes
            5 minute rate 0 bps
          Priority: 10% (2000 kbps), burst bytes 50000, b/w exceed drops: 0
          

        Class-map: INTERACTIVE-VIDEO (match-any)
          0 packets, 0 bytes
          5 minute offered rate 0 bps, drop rate 0 bps
          Match:  dscp cs4 (32) af41 (34)
            0 packets, 0 bytes
            5 minute rate 0 bps
          Priority: 23% (4600 kbps), burst bytes 115000, b/w exceed drops: 0
          

        Class-map: CRITICAL-DATA (match-any)
          0 packets, 0 bytes
          5 minute offered rate 0 bps, drop rate 0 bps
          Match:  dscp cs3 (24) af31 (26)
            0 packets, 0 bytes
            5 minute rate 0 bps
          Queueing
          queue limit 64 packets
          (queue depth/total drops/no-buffer drops) 0/0/0
          (pkts output/bytes output) 0/0
          bandwidth 15% (3000 kbps)
            Exp-weight-constant: 9 (1/512)
            Mean queue depth: 0 packets
            dscp     Transmitted       Random drop      Tail drop          Minimum        Maximum     Mark
                      pkts/bytes     pkts/bytes       pkts/bytes          thresh         thresh     prob
            

        Class-map: DATA (match-any)
          0 packets, 0 bytes
          5 minute offered rate 0 bps, drop rate 0 bps
          Match:  dscp af21 (18)
            0 packets, 0 bytes
            5 minute rate 0 bps
          Queueing
          queue limit 64 packets
          (queue depth/total drops/no-buffer drops) 0/0/0
          (pkts output/bytes output) 0/0
          bandwidth 19% (3800 kbps)
            Exp-weight-constant: 9 (1/512)
            Mean queue depth: 0 packets
            dscp     Transmitted       Random drop      Tail drop          Minimum        Maximum     Mark
                      pkts/bytes     pkts/bytes       pkts/bytes          thresh         thresh     prob
            

        Class-map: SCAVENGER (match-any)
          0 packets, 0 bytes
          5 minute offered rate 0 bps, drop rate 0 bps
          Match:  dscp cs1 (8) af11 (10)
            0 packets, 0 bytes
            5 minute rate 0 bps
          Queueing
          queue limit 64 packets
          (queue depth/total drops/no-buffer drops) 0/0/0
          (pkts output/bytes output) 0/0
          bandwidth 5% (1000 kbps)

        Class-map: NETWORK-CRITICAL (match-any)
          214 packets, 36291 bytes
          5 minute offered rate 0 bps, drop rate 0 bps
          Match:  dscp cs2 (16) cs6 (48)
            214 packets, 36291 bytes
            5 minute rate 0 bps
          Queueing
          queue limit 64 packets
          (queue depth/total drops/no-buffer drops) 0/0/0
          (pkts output/bytes output) 214/14231
          bandwidth 3% (600 kbps)

          Service-policy : MARK-ROUTING-PROTOCOL

            Class-map: ROUTING-PROTOCOL (match-any)
              202 packets, 34345 bytes
              5 minute offered rate 0 bps, drop rate 0 bps
              Match: protocol bgp
                202 packets, 34345 bytes
                5 minute rate 0 bps
              Match: protocol ospf
                0 packets, 0 bytes
                5 minute rate 0 bps
              Match: protocol eigrp
                0 packets, 0 bytes
                5 minute rate 0 bps
              Match: protocol rip
                0 packets, 0 bytes
                5 minute rate 0 bps
          QoS Set
            dscp cs6
              Packets marked 202

            Class-map: class-default (match-any)
              0 packets, 0 bytes
              5 minute offered rate 0 bps, drop rate 0 bps
              Match: any 

        Class-map: class-default (match-any)
          662 packets, 66933 bytes
          5 minute offered rate 0 bps, drop rate 0 bps
          Match: any 
          Queueing
          queue limit 64 packets
          (queue depth/total drops/no-buffer drops/flowdrops) 0/0/0/0
          (pkts output/bytes output) 662/67003
          bandwidth 25% (5000 kbps)
            Exp-weight-constant: 9 (1/512)
            Mean queue depth: 0 packets
            class     Transmitted       Random drop      Tail/Flow drop Minimum Maximum Mark
                      pkts/bytes    pkts/bytes       pkts/bytes    thresh  thresh  prob
            
            0             662/67003           0/0              0/0                 20            40  1/10
            1               0/0               0/0              0/0                 22            40  1/10
            2               0/0               0/0              0/0                 24            40  1/10
            3               0/0               0/0              0/0                 26            40  1/10
            4               0/0               0/0              0/0                 28            40  1/10
            5               0/0               0/0              0/0                 30            40  1/10
            6               0/0               0/0              0/0                 32            40  1/10
            7               0/0               0/0              0/0                 34            40  1/10
          Fair-queue: per-flow queue limit 16
UK# 

UK(config)#access-list 100 permit ip any any dscp ?
  <0-63>   Differentiated services codepoint value
  af11     Match packets with AF11 dscp (001010)
  af12     Match packets with AF12 dscp (001100)
  af13     Match packets with AF13 dscp (001110)
  af21     Match packets with AF21 dscp (010010)
  af22     Match packets with AF22 dscp (010100)
  af23     Match packets with AF23 dscp (010110)
  af31     Match packets with AF31 dscp (011010)
  af32     Match packets with AF32 dscp (011100)
  af33     Match packets with AF33 dscp (011110)
  af41     Match packets with AF41 dscp (100010)
  af42     Match packets with AF42 dscp (100100)
  af43     Match packets with AF43 dscp (100110)
  cs1      Match packets with CS1(precedence 1) dscp (001000)
  cs2      Match packets with CS2(precedence 2) dscp (010000)
  cs3      Match packets with CS3(precedence 3) dscp (011000)
  cs4      Match packets with CS4(precedence 4) dscp (100000)
  cs5      Match packets with CS5(precedence 5) dscp (101000)
  cs6      Match packets with CS6(precedence 6) dscp (110000)
  cs7      Match packets with CS7(precedence 7) dscp (111000)
  default  Match packets with default dscp (000000)
  ef       Match packets with EF dscp (101110)

DSCP EF

IDC-CORE#PING VRF UK
Protocol [ip]: 
Target IP address: 2.2.2.254
Repeat count [5]: 1
Datagram size [100]: 
Timeout in seconds [2]: 
Extended commands [n]: YES
Source address or interface: 1.1.1.254
Type of service [0]: 184
Set DF bit in IP header? [no]: 
Validate reply data? [no]: 
Data pattern [0xABCD]: 
Loose, Strict, Record, Timestamp, Verbose[none]: 
Sweep range of sizes [n]: 
Type escape sequence to abort.
Sending 1, 100-byte ICMP Echos to 2.2.2.254, timeout is 2 seconds:
Packet sent with a source address of 1.1.1.254 
!
Success rate is 100 percent (1/1), round-trip min/avg/max = 168/168/168 ms
IDC-CORE#


UK#show policy-map interface f0/0
 Class-map: VOICE (match-any)
          1 packets, 114 bytes
          5 minute offered rate 0 bps, drop rate 0 bps
          Match:  dscp ef (46)
            1 packets, 114 bytes
            5 minute rate 0 bps
          Priority: 10% (2000 kbps), burst bytes 50000, b/w exceed drops: 0


P1#Debug mpls packet
*Oct 15 00:26:34.887: MPLS turbo: Fa1/0: rx: Len 122 Stack {103 5 253} {2008 5 253} - ipv4 data
*Oct 15 00:26:34.891: MPLS turbo: Fa1/1: tx: Len 118 Stack {2008 5 252} - ipv4 data
*Oct 15 00:26:34.959: MPLS turbo: Fa1/1: rx: Len 122 Stack {104 5 253} {1021 5 253} - ipv4 data
*Oct 15 00:26:34.963: MPLS turbo: Fa1/0: tx: Len 118 Stack {1021 5 252} - ipv4 data          
======================================================================================

======================================================
MPLS-VPN QoS
 service provider to ENTERPRISE models
   
japan PE_1
class-map match-any CRITICAL-DATA-NETWORK-CONTROL
 match ip dscp af31 
 match ip dscp cs2 
 match ip dscp cs3 
 match ip dscp cs6 
 match ip dscp af21 
class-map match-any INTERACTIVE-VIDEO
 match ip dscp af41 
 match ip dscp cs4 
class-map match-any BULK-DATA-SCAVENGER
 match ip dscp af11 
 match ip dscp cs1 
class-map match-any VOICE-REALTIME
 match ip dscp ef 
 match ip dscp cs5 
!
!         
policy-map PE-FIVE-CLASS-SP-MODEL
 class VOICE-REALTIME
    priority percent 35
 class CRITICAL-DATA-NETWORK-CONTROL
    bandwidth percent 20
     random-detect dscp-based
 class INTERACTIVE-VIDEO
    bandwidth percent 15
     random-detect dscp-based
 class BULK-DATA-SCAVENGER
    bandwidth percent 5
     random-detect dscp-based
 class class-default
    bandwidth percent 25
     random-detect
policy-map Traffic_Shaping_Policing_20Mbps_OUTPUT
 class class-default
    police 20000000
    shape average 20000000
  service-policy PE-FIVE-CLASS-SP-MODEL
policy-map Traffic_Policing_20Mbps_INPUT
 class class-default
    police 20000000

interface FastEthernet0/0.10
 description UK_QOS_SP_TO_ENTERPRISE_MODELS
 service-policy input Traffic_Policing_20Mbps_INPUT
 service-policy output Traffic_Shaping_Policing_20Mbps_OUTPUT    

japan PE_2
 class-map match-any CRITICAL-DATA-NETWORK-CONTROL
 match ip dscp af31 
 match ip dscp cs2 
 match ip dscp cs3 
 match ip dscp cs6 
 match ip dscp af21 
class-map match-any INTERACTIVE-VIDEO
 match ip dscp af41 
 match ip dscp cs4 
class-map match-any BULK-DATA-SCAVENGER
 match ip dscp af11 
 match ip dscp cs1 
class-map match-any VOICE-REALTIME
 match ip dscp ef 
 match ip dscp cs5 
!
!         
policy-map PE-FIVE-CLASS-SP-MODEL
 class VOICE-REALTIME
    priority percent 35
 class CRITICAL-DATA-NETWORK-CONTROL
    bandwidth percent 20
     random-detect dscp-based
 class INTERACTIVE-VIDEO
    bandwidth percent 15
     random-detect dscp-based
 class BULK-DATA-SCAVENGER
    bandwidth percent 5
     random-detect dscp-based
 class class-default
    bandwidth percent 25
     random-detect
policy-map Traffic_Shaping_Policing_10Mbps_OUTPUT
 class class-default
    police 10000000
    shape average 10000000
  service-policy PE-FIVE-CLASS-SP-MODEL
policy-map Traffic_Policing_10Mbps_INPUT
 class class-default
    police 10000000

interface FastEthernet0/0.10
 description UK_QOS_SP_TO_ENTERPRISE_MODELS
 service-policy input Traffic_Policing_10Mbps_INPUT
 service-policy output Traffic_Shaping_Policing_10Mbps_OUTPUT
=================================================================
TEST:
IDC-CORE#ping vrf UK
Protocol [ip]: 
Target IP address: 2.2.2.254
Repeat count [5]: 
Datagram size [100]: 
Timeout in seconds [2]: 
Extended commands [n]: YES
Source address or interface: 1.1.1.254
Type of service [0]: 184
Set DF bit in IP header? [no]: 
Validate reply data? [no]: 
Data pattern [0xABCD]: 
Loose, Strict, Record, Timestamp, Verbose[none]: 
Sweep range of sizes [n]: 
Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 2.2.2.254, timeout is 2 seconds:
Packet sent with a source address of 1.1.1.254 
!!!!!
Success rate is 100 percent (5/5), round-trip min/avg/max = 108/148/176 ms
IDC-CORE#

================================================================
PIPE mode <UK-GERMANY>

remarking
class-map match-any VOIP-REALTIME
 match ip dscp ef 
 match ip dscp cs5 
class-map match-any BULK-DATA
 match ip dscp af11 
 match ip dscp cs1 
class-map match-any CRITICAL-DATA
 match ip dscp cs6 
 match ip dscp af31 
 match ip dscp cs3 
class-map match-any VIDEO
 match ip dscp af21 
 match ip dscp cs2 
 match ip dscp af41 
 match ip dscp cs4 

policy-map PIPE-MARKING
 class VOIP-REALTIME
   police cir percent 35
     
     conform-action set-mpls-exp-imposition-transmit 5
     exceed-action drop 
 class CRITICAL-DATA
   police cir percent 20
     
     conform-action set-mpls-exp-imposition-transmit 3
     exceed-action set-mpls-exp-imposition-transmit 7
     
 class VIDEO
   police cir percent 15
     
     conform-action set-mpls-exp-imposition-transmit 2
     exceed-action drop 
 class BULK-DATA
   police cir percent 5
     
     conform-action set-mpls-exp-imposition-transmit 1
     
     exceed-action set-mpls-exp-imposition-transmit 6
 class class-default
   police cir percent 25
     
     conform-action set-mpls-exp-imposition-transmit 0
     
     exceed-action set-mpls-exp-imposition-transmit 4
policy-map CE-POLICING
 class class-default
    police 10000000
  service-policy PIPE-MARKING

PE_1#sh run int f0/0.10
interface FastEthernet0/0.10
 service-policy input CE-POLICING
 service-policy output PE-CE-SHAPING-QUEUING  

  !!!!!!!!!!!!!!!!!!!! 

! 
class-map match-all MPLS-EXP-7
 match mpls experimental topmost 7 
class-map match-all MPLS-EXP-6
 match mpls experimental topmost 6 
class-map match-all MPLS-EXP-5
 match mpls experimental topmost 5 
class-map match-all MPLS-EXP-4
 match mpls experimental topmost 4 
class-map match-all MPLS-EXP-3
 match mpls experimental topmost 3 
class-map match-all MPLS-EXP-2
 match mpls experimental topmost 2 
class-map match-all MPLS-EXP-1
 match mpls experimental topmost 1 
class-map match-all MPLS-EXP-0
 match mpls experimental topmost 0 
!         
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
policy-map MPLSEXP-QOSGROUP-DISCARDCLASS
 class MPLS-EXP-5
  set qos-group 5
 class MPLS-EXP-3
  set qos-group 3
 class MPLS-EXP-7
  set qos-group 3
  set discard-class 1
 class MPLS-EXP-2
  set qos-group 2
 class MPLS-EXP-1
  set qos-group 1
 class MPLS-EXP-6
  set qos-group 1
  set discard-class 1
 class MPLS-EXP-0
  set qos-group 0
 class MPLS-EXP-4
  set qos-group 0
  set discard-class 1

interface FastEthernet1/0
 service-policy input MPLSEXP-QOSGROUP-DISCARDCLASS  
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
class-map match-all QOSGROUP0
 match qos-group 0
class-map match-all QOSGROUP1
 match qos-group 1
class-map match-all QOSGROUP2
 match qos-group 2
class-map match-all QOSGROUP3
 match qos-group 3 
class-map match-all QOSGROUP5
 match qos-group 5 

policy-map PE-CE-QUEUING
 class QOSGROUP5
    priority percent 35
 class QOSGROUP3
    bandwidth percent 20
     random-detect discard-class-based
     random-detect discard-class 0 30 40 10
     random-detect discard-class 1 20 40 10
 class QOSGROUP2
    bandwidth percent 15
 class QOSGROUP1
    bandwidth percent 5
     random-detect discard-class-based
     random-detect discard-class 0 30 40 10
     random-detect discard-class 1 20 40 10 
 class QOSGROUP0
bandwidth percent 24 
random-detect discard-class-based 
random-detect discard-class 0 30 40 10 
random-detect discard-class 1 20 40 10 
policy-map PE-CE-SHAPING-QUEUING
 class class-default
    shape average 10000000
  service-policy PE-CE-QUEUING

PE_1#sh run int f0/0.10
interface FastEthernet0/0.10
 service-policy output PE-CE-SHAPING-QUEUING  
====
TEST
IDC-CORE#PING VRF GERMANY 
Protocol [ip]: 
Target IP address: 1.1.1.254
Repeat count [5]: 1000
Datagram size [100]: 
Timeout in seconds [2]: 
Extended commands [n]: YES
Source address or interface: 2.2.2.254
Type of service [0]: 136
Set DF bit in IP header? [no]: 
Validate reply data? [no]: 
Data pattern [0xABCD]: 
Loose, Strict, Record, Timestamp, Verbose[none]: 
Sweep range of sizes [n]: 
Type escape sequence to abort.
Sending 1000, 100-byte ICMP Echos to 1.1.1.254, timeout is 2 seconds:
Packet sent with a source address of 2.2.2.254 
!!!!!!!!!!!!!!!!!!!!!.!!!!!!!!!!!.!!!!!!!!!!!!!!!!!!!.
Success rate is 94 percent (51/54), round-trip min/avg/max = 112/159/248 ms

PE_1#
*Oct 16 05:55:53.831: MPLS turbo: Fa1/0: rx: Len 86 Stack {0 0 254} {1000 0 255} CW {0 0 0}
*Oct 16 05:55:54.299: MPLS turbo: Fa1/0: rx: Len 122 Stack {0 2 252} {1003 2 253} - ipv4 data
*Oct 16 05:55:54.487: MPLS turbo: Fa1/0: rx: Len 122 Stack {0 2 252} {1003 2 253} - ipv4 data
*Oct 16 05:55:54.691: MPLS turbo: Fa1/0: rx: Len 122 Stack {0 2 252} {1003 2 253} - ipv4 data

PE_1#sh policy-map inter f0/0.10 
 FastEthernet0/0.10 

  Service-policy input: CE-POLICING

    Class-map: class-default (match-any)
      305 packets, 33189 bytes
      5 minute offered rate 0 bps, drop rate 0 bps
      Match: any 
      police:
          cir 10000000 bps, bc 312500 bytes
        conformed 305 packets, 33189 bytes; actions:
          transmit 
        exceeded 0 packets, 0 bytes; actions:
          drop 
        conformed 0 bps, exceed 0 bps

      Service-policy : PIPE-MARKING
        Class-map: VIDEO (match-any)
          241 packets, 28438 bytes
          5 minute offered rate 0 bps, drop rate 0 bps
          Match: ip dscp af21 (18)
            0 packets, 0 bytes
            5 minute rate 0 bps
          Match: ip dscp cs2 (16)
            0 packets, 0 bytes
            5 minute rate 0 bps
          Match: ip dscp af41 (34)
            241 packets, 28438 bytes
            5 minute rate 0 bps
          Match: ip dscp cs4 (32)
            0 packets, 0 bytes
            5 minute rate 0 bps
          police:
              cir 15 %
              cir 1500000 bps, bc 46875 bytes
            conformed 241 packets, 28438 bytes; actions:
              set-mpls-exp-topmost-transmit 2
              set-mpls-exp-imposition-transmit 2
            exceeded 0 packets, 0 bytes; actions:
              drop 
            conformed 0 bps, exceed 0 bps

  

===============================
PE_1#sh policy-map inter f0/0.10 output 
 FastEthernet0/0.10 

  Service-policy output: PE-CE-SHAPING-QUEUING

    Class-map: class-default (match-any)
      354 packets, 44682 bytes
      5 minute offered rate 0 bps, drop rate 0 bps
      Match: any 
      Queueing
      queue limit 64 packets
      (queue depth/total drops/no-buffer drops) 0/0/0
      (pkts output/bytes output) 354/36681
      shape (average) cir 10000000, bc 40000, be 40000
      target shape rate 10000000

      Service-policy : PE-CE-QUEUING

        queue stats for all priority classes:
          
          queue limit 64 packets
          (queue depth/total drops/no-buffer drops) 0/0/0
          (pkts output/bytes output) 5/590

        Class-map: QOSGROUP5 (match-all)
          5 packets, 590 bytes
          5 minute offered rate 0 bps, drop rate 0 bps
          Match: qos-group 5
          Priority: 35% (3500 kbps), burst bytes 87500, b/w exceed drops: 0
          

        Class-map: QOSGROUP3 (match-all)
          0 packets, 0 bytes
          5 minute offered rate 0 bps, drop rate 0 bps
          Match: qos-group 3
          Queueing
          queue limit 64 packets
          (queue depth/total drops/no-buffer drops) 0/0/0
          (pkts output/bytes output) 0/0
          bandwidth 20% (2000 kbps)
            Exp-weight-constant: 9 (1/512)
            Mean queue depth: 0 packets
            discard-class     Transmitted       Random drop      Tail drop          Minimum        Maximum     Mark
                      pkts/bytes     pkts/bytes       pkts/bytes          thresh         thresh     prob
            
            0               0/0               0/0              0/0                 30            40  1/10
            1               0/0               0/0              0/0                 20            40  1/10
            2               0/0               0/0              0/0                 24            40  1/10
            3               0/0               0/0              0/0                 26            40  1/10
            4               0/0               0/0              0/0                 28            40  1/10
            5               0/0               0/0              0/0                 30            40  1/10
            6               0/0               0/0              0/0                 32            40  1/10
            7               0/0               0/0              0/0                 34            40  1/10

        Class-map: QOSGROUP2 (match-all)
          241 packets, 28438 bytes
          5 minute offered rate 0 bps, drop rate 0 bps
          Match: qos-group 2
          Queueing
          queue limit 64 packets
          (queue depth/total drops/no-buffer drops) 0/0/0
          (pkts output/bytes output) 241/28438
          bandwidth 15% (1500 kbps)

        Class-map: QOSGROUP1 (match-all)
          0 packets, 0 bytes
          5 minute offered rate 0 bps, drop rate 0 bps
          Match: qos-group 1
          Queueing
          queue limit 64 packets
          (queue depth/total drops/no-buffer drops) 0/0/0
          (pkts output/bytes output) 0/0
          bandwidth 5% (500 kbps)
            Exp-weight-constant: 9 (1/512)
            Mean queue depth: 0 packets
            discard-class     Transmitted       Random drop      Tail drop          Minimum        Maximum     Mark
                      pkts/bytes     pkts/bytes       pkts/bytes          thresh         thresh     prob
            
            0               0/0               0/0              0/0                 30            40  1/10
            1               0/0               0/0              0/0                 20            40  1/10
            2               0/0               0/0              0/0                 24            40  1/10
            3               0/0               0/0              0/0                 26            40  1/10
            4               0/0               0/0              0/0                 28            40  1/10
            5               0/0               0/0              0/0                 30            40  1/10
            6               0/0               0/0              0/0                 32            40  1/10
            7               0/0               0/0              0/0                 34            40  1/10

        Class-map: QOSGROUP0 (match-all)
          108 packets, 15654 bytes
          5 minute offered rate 0 bps, drop rate 0 bps
          Match: qos-group 0
          Queueing
          queue limit 64 packets
          (queue depth/total drops/no-buffer drops) 0/0/0
          (pkts output/bytes output) 33/2333
          bandwidth 24% (2400 kbps)
            Exp-weight-constant: 9 (1/512)
            Mean queue depth: 0 packets
            discard-class     Transmitted       Random drop      Tail drop          Minimum        Maximum     Mark
                      pkts/bytes     pkts/bytes       pkts/bytes          thresh         thresh     prob
            
            0              32/2269            0/0              0/0                 30            40  1/10
            1               0/0               0/0              0/0                 20            40  1/10
            2               0/0               0/0              0/0                 24            40  1/10
            3               0/0               0/0              0/0                 26            40  1/10
            4               0/0               0/0              0/0                 28            40  1/10
            5               0/0               0/0              0/0                 30            40  1/10
            6               0/0               0/0              0/0                 32            40  1/10
            7               0/0               0/0              0/0                 34            40  1/10

        Class-map: class-default (match-any)
          0 packets, 0 bytes
          5 minute offered rate 0 bps, drop rate 0 bps
          Match: any 
          
          queue limit 64 packets
          (queue depth/total drops/no-buffer drops) 0/0/0
          (pkts output/bytes output) 75/5320
PE_1#  

====
DMVPN per-tunnel QOS USA|CHINA





HUB-SPOKE
class-map match-any DATA
 match  dscp af21 
class-map match-any INTERACTIVE-VIDEO
 match  dscp cs4  af41 
class-map match-any CRITICAL-DATA
 match  dscp cs3  af31 
class-map match-any VOICE
 match  dscp ef 
 match  dscp cs5 
class-map match-any SCAVENGER
 match  dscp cs1  af11 
class-map match-any NETWORK-CRITICAL
 match  dscp cs2  cs6 

policy-map DMVPN_LOW_BANDWIDTH_SPOKE
 class VOICE
    priority percent 10
 class CRITICAL-DATA
    bandwidth percent 15
     random-detect dscp-based
 class INTERACTIVE-VIDEO
    priority percent 23
 class DATA
    bandwidth percent 19
     random-detect dscp-based
 class SCAVENGER
    bandwidth percent 5
 class NETWORK-CRITICAL
    bandwidth percent 3
 class class-default
    bandwidth percent 25
     random-detect

policy-map DMVPN_HIGH_BANDWIDTH_SPOKE
 class VOICE
    priority percent 20
 class CRITICAL-DATA
    bandwidth percent 20
     random-detect dscp-based
 class INTERACTIVE-VIDEO
    priority percent 5
 class DATA
    bandwidth percent 20
     random-detect dscp-based
 class SCAVENGER
    bandwidth percent 5
 class NETWORK-CRITICAL
    bandwidth percent 10
 class class-default
    bandwidth percent 20
     random-detect
HUB:
policy-map DMVPN_TUNNEL_SHAPING-LOW
 class class-default
    shape average 4000000
  service-policy DMVPN_LOW_BANDWIDTH_SPOKE

policy-map DMVPN_TUNNEL_SHAPING-HIGH
 class class-default
    shape average 8000000
  service-policy DMVPN_HIGH_BANDWIDTH_SPOKE  
HUB:
interface tunnel X
 ip nhrp map group DMVPN_TUNNEL_SHAPING_LOW service-policy output DMVPN_TUNNEL_SHAPING-LOW
 ip nhrp map group DMVPN_TUNNEL_SHAPING_HIGH service-policy output DMVPN_TUNNEL_SHAPING-HIGH

policy-map WAN_INTERFACE_SHAPING_50Mbps
 class class-default
    shape average 50000000
interface [WAN]
  service-policy output WAN_INTERFACE_SHAPING_50Mbps


spoke:

inter tunnel 0
 ip nhrp group DMVPN_TUNNEL_SHAPING_LOW
 
inter tunnel 0
 ip nhrp group DMVPN_TUNNEL_SHAPING_HIGH

policy-map WAN_INTERFACE_SHAPING_4Mbps
 class class-default
    shape average 4000000
interface f0/0
  service-policy output WAN_INTERFACE_SHAPING_4Mbps  

policy-map WAN_INTERFACE_SHAPING_8Mbps
 class class-default
    shape average 8000000
interface f0/0
  service-policy output WAN_INTERFACE_SHAPING_8Mbps   
=====================================
USA-1#show dmvpn detail 
Legend: Attrb --> S - Static, D - Dynamic, I - Incomplete
        N - NATed, L - Local, X - No Socket
        # Ent --> Number of NHRP entries with same NBMA peer
        NHS Status: E --> Expecting Replies, R --> Responding
        UpDn Time --> Up or Down Time for a Tunnel
==========================================================================
Tunnel51 is admin down

Interface Tunnel501 is up/up, Addr. is 10.169.128.254, VRF "" 
   Tunnel Src./Dest. addr: 58.169.1.1/MGRE, Tunnel VRF ""
   Protocol/Transport: "multi-GRE/IP", Protect "" 
   Interface State Control: Disabled

IPv4 NHS: 10.169.128.253 RE
Type:Hub/Spoke, Total NBMA Peers (v4/v6): 3

# Ent  Peer NBMA Addr Peer Tunnel Add State  UpDn Tm Attrb    Target Network
----- --------------- --------------- ----- -------- ----- -----------------
    1     58.169.1.4    10.169.128.1    UP 05:51:01    D    10.169.128.1/32
NHRP group: DMVPN_TUNNEL_SHAPING_LOW
 Output QoS service-policy applied: DMVPN_TUNNEL_SHAPING-LOW

    1     58.169.1.3    10.169.128.2    UP 05:45:47    D    10.169.128.2/32
NHRP group: DMVPN_TUNNEL_SHAPING_HIGH
 Output QoS service-policy applied: DMVPN_TUNNEL_SHAPING-HIGH

    1     58.169.1.2  10.169.128.253    UP 00:06:06    S  10.169.128.253/32


          
Crypto Session Details: 
--------------------------------------------------------------------------------

Pending DMVPN Sessions:

USA-1# 
USA-1#show ip nhrp 
10.169.169.253/32 via 10.169.169.253
   Tunnel51 created 06:25:48, never expire 
   Type: static, Flags: 
   NBMA address: 58.169.1.2 
10.169.128.1/32 via 10.169.128.1
   Tunnel501 created 05:50:35, expire 01:53:51
   Type: dynamic, Flags: unique registered 
   NBMA address: 58.169.1.4 
   Group: DMVPN_TUNNEL_SHAPING_LOW
10.169.128.2/32 via 10.169.128.2
   Tunnel501 created 05:45:40, expire 01:53:50
   Type: dynamic, Flags: unique registered 
   NBMA address: 58.169.1.3 
   Group: DMVPN_TUNNEL_SHAPING_HIGH
10.169.128.253/32 via 10.169.128.253
   Tunnel501 created 05:50:39, never expire 
   Type: static, Flags: used 
   NBMA address: 58.169.1.2 
USA-1#         

USA-1#show policy-map multipoint | include Interface Tunnel
Interface Tunnel501 <--> 58.169.1.3
Interface Tunnel501 <--> 58.169.1.4
USA-1#


IDC-CORE#ping vrf USA
Protocol [ip]: 
Target IP address: 155.1.1.1
Repeat count [5]: 1000000
Datagram size [100]: 
Timeout in seconds [2]: 
Extended commands [n]: YES
Source address or interface: 5.5.5.254
Type of service [0]: 184
Set DF bit in IP header? [no]: 
Validate reply data? [no]: 
Data pattern [0xABCD]: 
Loose, Strict, Record, Timestamp, Verbose[none]: 
Sweep range of sizes [n]: 
Type escape sequence to abort.
Sending 1000000, 100-byte ICMP Echos to 155.1.1.1, timeout is 2 seconds:
Packet sent with a source address of 5.5.5.254 
!.!!!!!!!!!!!!!!!!!!!!!!.!!!!!!!!!!!!!!!!!!!!!!!.!!!!!!!!!!!.!!!!!!!!!
!!!!!!!!!!!!!!.!!!!!!!!!!!!!!!!!!!!!!!.!!!!!!!!!!!!!!!!!!!!!!.!!!!!!!!
!!!!!!!!!!!!!.!!!!!!!!!!!!!!!!!!!!!!!.!!!!!!!!!!!!!!!!!!!!!!!.!!!!!!!!
!!!.!!!!!!!!!!!!!!!!!!!!!!!.!!!!!!!!!!.!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
!!!!!!!!!!!!!!.!!!!!!!!!!!!!!!!!!!!!!.!!!!!!!!!!!!!!!!!!!!!!!.!!!!!!!!
!!!!!!!!!!!!!!!.!!!!!!!!!!!!!!!!!!!!!!!.!!!!!!!!!!!!!!!!.!!!!!!!!!!!!!
!!!!.!!!!!!!!!!!!!!!!!!!!!.!!!!.!!!!!!.!!!!!!!!!!!!!!!!!!!!!!!.!!!!!!!
!!!.!!!!!!!!!!!!!!!!!!!!!!!.!!!!!!.!!!!!!!!!!!!!!!!!!!!!!!!!!!!.!!!!!!
!!!.!!!!!!!!!!!!!!!!!!!!!!!.!!!!!!!!!!!!!!!!!!!!!.!!!!!!!!!!!!!.!!!!!!
!!!!!!!!!!!!!!!!!.!!!!!!!!!!!!!!!!!!!!!!!.!!!!!!!!!!!!!!!.!!!!!!!!!!!!
!!!!!.!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!.!!!!!!!!!!!!.!!!
!!!!!!.!!!!!!!!!!!!!!!!!!!!!!!.!!!!!!!!!!!.!!!!!!!!!!.!!!!!!!!!.!!!!!!
!!!!!!.!!!!!!!!!!!!!!!!!!!!!!!.!!!!!!!!!!!!!!!!!!!!!!!.!!!!!!!!!!!!.!!
!!!!!!!!!!!!!!!!!!!!.!!!!!!!!.!!.!!!!!!!!!!!!!!!!!!!!!.!!.!!!!!!!.!!!!
!!!!!!!!!!!!!!!!!!!.!!!!!!!!!!.!!!!!!!!!!!!!!!!!!!!!!!.!!!!!!!!!!!!!!!
.!!!!!!!.!!!!!!!!!.!!!!!!!!!!.!!!!!.!!!!!.!!!!!!!!!!!!!!!!!!!!!!!.!.!!
!!!!!!!.!!!!!!!!!!!!!!!!!!!!!!!.!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!.!!!
!!!!!!!!!.!!!!!!!!!!!!!!!!!!!!!.!!!!!!!!.!.!!!!!!!!!!!!!!!!!!!!!!!..!!
!!!!!!!!!!!!!!!!!!!!.!!!!!!!!.!!!!!!!!!!!!.!!!!!!!!!!!!!!!!!!!!!!.!!!!
!!!!!!!!!!!!!!!!!!!.!!!!!!.!!!!.!!!!!!!!!!!!!!!!!!!!!!!.!!!!!!!!!!!!!!
!!!!!!!!!.!!!!!!!!!!!!!!!!!!!!!!.!!!!!!!!!!!!!!!!!!!!!!.!!!!!!!!!!!!!!
!!!!!!!!!.!!!!!!!!!!!!!!!!!!!!!!.!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!.!
!.!!!!!!!!.!!!!!!!!!.!!!!!!!!!!.!!!!!!!!!!!!!!!!!!!!!!!!.!!!!!!!!!!!!!
!!!!!!!!!.!!!!!!!!!!!!!!!!!!!!!!!.!!!!!!.!!!!.!!!!!!!!!!!!!!!!!!!.!!!!
!!!!!!!!!!.!.!!!!!!!!.!!!!!!!!!!!!!!!!!!!!!!.!!!!!!!!!!!.!!!!!!!!!!!!!
!!!!!!!.!!!!!!!!!!.!!!!!!!!!!!!!!!!!!!!!!!.!!!!!!!!!

USA-1#sh policy-map multipoint 

Interface Tunnel501 <--> 58.169.1.4

  Service-policy output: DMVPN_TUNNEL_SHAPING-LOW

    Class-map: class-default (match-any)
      22152 packets, 2784949 bytes
      5 minute offered rate 4000 bps, drop rate 0 bps
      Match: any 
      Queueing
      queue limit 1000 packets
      (queue depth/total drops/no-buffer drops) 0/0/0
      (pkts output/bytes output) 20803/2953906
      shape (average) cir 4000000, bc 16000, be 16000
      target shape rate 4000000

      Service-policy : DMVPN_LOW_BANDWIDTH_SPOKE

        queue stats for all priority classes:
          
          queue limit 330 packets
          (queue depth/total drops/no-buffer drops) 0/0/0
          (pkts output/bytes output) 20796/2953032

        Class-map: VOICE (match-any)
          20843 packets, 2666588 bytes
          5 minute offered rate 4000 bps, drop rate 0 bps
          Match:  dscp ef (46)
            20843 packets, 2666588 bytes
            5 minute rate 4000 bps
          Match:  dscp cs5 (40)
            0 packets, 0 bytes
            5 minute rate 0 bps
          Priority: 10% (400 kbps), burst bytes 10000, b/w exceed drops: 0
          

        Class-map: CRITICAL-DATA (match-any)
          0 packets, 0 bytes
          5 minute offered rate 0 bps, drop rate 0 bps
          Match:  dscp cs3 (24) af31 (26)
            0 packets, 0 bytes
            5 minute rate 0 bps
          Queueing
          queue limit 150 packets
          (queue depth/total drops/no-buffer drops) 0/0/0
          (pkts output/bytes output) 0/0
          bandwidth 15% (600 kbps)
            Exp-weight-constant: 9 (1/512)
            Mean queue depth: 0 packets
            dscp     Transmitted       Random drop      Tail drop          Minimum        Maximum     Mark
                      pkts/bytes     pkts/bytes       pkts/bytes          thresh         thresh     prob
            

        Class-map: INTERACTIVE-VIDEO (match-any)
          0 packets, 0 bytes
          5 minute offered rate 0 bps, drop rate 0 bps
          Match:  dscp cs4 (32) af41 (34)
            0 packets, 0 bytes
            5 minute rate 0 bps
          Priority: 23% (920 kbps), burst bytes 23000, b/w exceed drops: 0
          

        Class-map: DATA (match-any)
          0 packets, 0 bytes
          5 minute offered rate 0 bps, drop rate 0 bps
          Match:  dscp af21 (18)
            0 packets, 0 bytes
            5 minute rate 0 bps
          Queueing
          queue limit 190 packets
          (queue depth/total drops/no-buffer drops) 0/0/0
          (pkts output/bytes output) 0/0
          bandwidth 19% (760 kbps)
            Exp-weight-constant: 9 (1/512)
            Mean queue depth: 0 packets
            dscp     Transmitted       Random drop      Tail drop          Minimum        Maximum     Mark
                      pkts/bytes     pkts/bytes       pkts/bytes          thresh         thresh     prob
            

        Class-map: SCAVENGER (match-any)
          0 packets, 0 bytes
          5 minute offered rate 0 bps, drop rate 0 bps
          Match:  dscp cs1 (8) af11 (10)
            0 packets, 0 bytes
            5 minute rate 0 bps
          Queueing
          queue limit 50 packets
          (queue depth/total drops/no-buffer drops) 0/0/0
          (pkts output/bytes output) 0/0
          bandwidth 5% (200 kbps)

        Class-map: NETWORK-CRITICAL (match-any)
          1295 packets, 116270 bytes
          5 minute offered rate 0 bps, drop rate 0 bps
          Match:  dscp cs2 (16) cs6 (48)
            1295 packets, 116270 bytes
            5 minute rate 0 bps
          Queueing
          queue limit 30 packets
          (queue depth/total drops/no-buffer drops) 0/0/0
          (pkts output/bytes output) 2/164
          bandwidth 3% (120 kbps)

        Class-map: class-default (match-any)
          14 packets, 2091 bytes
          5 minute offered rate 0 bps, drop rate 0 bps
          Match: any 
          Queueing
          queue limit 250 packets
          (queue depth/total drops/no-buffer drops) 0/0/0
          (pkts output/bytes output) 5/710
          bandwidth 25% (1000 kbps)
            Exp-weight-constant: 9 (1/512)
            Mean queue depth: 0 packets
            class     Transmitted       Random drop      Tail drop          Minimum        Maximum     Mark
                      pkts/bytes     pkts/bytes       pkts/bytes          thresh         thresh     prob
            
            0               5/710             0/0              0/0                 20            40  1/10
            1               0/0               0/0              0/0                 22            40  1/10
            2               0/0               0/0              0/0                 24            40  1/10
            3               0/0               0/0              0/0                 26            40  1/10
            4               0/0               0/0              0/0                 28            40  1/10
            5               0/0               0/0              0/0                 30            40  1/10
            6               0/0               0/0              0/0                 32            40  1/10
            7               0/0               0/0              0/0                 34            40  1/10
USA-1#  

  GRE OVER IPSEC QoS