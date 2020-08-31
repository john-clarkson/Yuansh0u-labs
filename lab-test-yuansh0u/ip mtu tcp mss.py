without encrytion
 SITE_A#sh inter tun 101 | section Tunnel transport MTU
  Tunnel transport MTU 1476 bytes

VRF-CORE# ping vrf SITE_A 150.150.2.3 DF-bit size 1476 re 10
Type escape sequence to abort.
Sending 10, 1476-byte ICMP Echos to 150.150.2.2, timeout is 2 seconds:
Packet sent with the DF bit set
..!!..!.!!
Success rate is 50 percent (5/10), round-trip min/avg/max = 128/168/184 ms
VRF-CORE# ping vrf SITE_A 150.150.2.3 DF-bit size 1477 re 10
Type escape sequence to abort.
Sending 10, 1477-byte ICMP Echos to 150.150.2.2, timeout is 2 seconds:
Packet sent with the DF bit set
MMMMMMMMMM
Success rate is 0 percent (0/10)
VRF-CORE#
==============================

===================================
with encrytion
SITE_A/B(config)#int tun 101
SITE_A/B(config-if)#tunnel protection ipsec profile IPV4
SITE_A#show inter tun 101 | sec Tunnel transport MTU
  Tunnel transport MTU 1434 bytes

VRF-CORE# ping vrf SITE_A 150.150.2.2 df-bit size 1434
Type escape sequence to abort.
Sending 5, 1434-byte ICMP Echos to 150.150.2.2, timeout is 2 seconds:
Packet sent with the DF bit set
!!.!.
Success rate is 60 percent (3/5), round-trip min/avg/max = 200/213/224 ms
VRF-CORE# ping vrf SITE_A 150.150.2.2 df-bit size 1435
Type escape sequence to abort.
Sending 5, 1435-byte ICMP Echos to 150.150.2.2, timeout is 2 seconds:
Packet sent with the DF bit set
MMMMM
Success rate is 0 percent (0/5)
VRF-CORE#

SITE_A(config)#int tun 101
SITE_A(config-if)#ip mtu 1400
================================
VRF-CORE# ping vrf SITE_A 150.150.2.2 df-bit size 1401
Type escape sequence to abort.
Sending 5, 1401-byte ICMP Echos to 150.150.2.2, timeout is 2 seconds:
Packet sent with the DF bit set
MMMM.
Success rate is 0 percent (0/5)
VRF-CORE# ping vrf SITE_A 150.150.2.2 df-bit size 1400
Type escape sequence to abort.
Sending 5, 1400-byte ICMP Echos to 150.150.2.2, timeout is 2 seconds:
Packet sent with the DF bit set
!..!.
Success rate is 40 percent (2/5), round-trip min/avg/max = 152/154/156 ms
VRF-CORE#  
===============================================================================

TCP MSS
 
 SITE_A#sh run | sec ip tcp
    ip tcp mss 4321
 SITE_B#sh run | sec ip tcp
    ip tcp mss 1234

SITE_A/B(config)#int tun 101
SITE_A/B(config-if)#no tunnel protection ipsec profile IPV4

SITE_A#telnet 12.1.1.2
  check TCP SYN ACK option

=======================================
