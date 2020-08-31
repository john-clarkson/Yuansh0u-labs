##topology
SITE-A dhcp-------ispL2SW----CGN<dhcp server 100.64.1.0>-----inside-<CGN NAT>---outside---INET--61.128.1.0/24-HQ
SITE-B dhcp-------                                                 <BGP AS 1000>   <BGP AS 1000>

before CGN
CGN#sh ip nat translations 
Pro  Inside global         Inside local          Outside local         Outside global
udp  103.1.1.1:512         100.64.1.2:500        61.128.1.1:500        61.128.1.1:500
udp  103.1.1.1:4502        100.64.1.3:4500       61.128.1.1:4500       61.128.1.1:4500
udp  103.1.1.1:4501        100.64.1.2:4500       61.128.1.1:4500       61.128.1.1:4500
udp  103.1.1.1:513         100.64.1.3:500        61.128.1.1:500        61.128.1.1:500
Total number of translations: 4


#CGN static mapping IPSEC WORK,TCP WORK!!!
ip nat settings mode cgn
no ip nat settings support mapping outside
ip nat inside source static 100.64.1.2 103.1.1.1
SITE-A#show cry isa sa
IPv4 Crypto ISAKMP SA
dst             src             state          conn-id status
61.128.1.1      100.64.1.2      QM_IDLE           1004 ACTIVE VPN

IPv6 Crypto ISAKMP SA


CGN#show ip nat translations 
Pro  Inside global         Inside local          Outside local         Outside global
udp  103.1.1.2:500         100.64.1.3:500        ---                   ---
---  103.1.1.1             100.64.1.2            ---                   ---
udp  103.1.1.1:4500        100.64.1.2:4500       ---                   ---
---  103.1.1.2             100.64.1.3            ---                   ---
udp  103.1.1.2:4500        100.64.1.3:4500       ---                   ---
Total number of translations: 5

CGN#

CGN#
##without overload, all working,maybe a bug!!!  CSR1000V Software (X86_64_LINUX_IOSD-UNIVERSALK9-M), Version 15.5(3)S
ip nat settings mode cgn
no ip nat settings support mapping outside
ip nat pool CGN 103.1.1.1 103.1.1.2 prefix-length 24
ip nat inside source list CGN pool CGN
HQ#show cry isa sa
IPv4 Crypto ISAKMP SA
dst             src             state          conn-id status
61.128.1.1      103.1.1.2       QM_IDLE           1008 ACTIVE
61.128.1.1      103.1.1.1       QM_IDLE           1007 ACTIVE

SITE-A#ping 3.3.3.3 sou lo0
Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 3.3.3.3, timeout is 2 seconds:
Packet sent with a source address of 1.1.1.1 
!!!!!
Success rate is 100 percent (5/5), round-trip min/avg/max = 15/21/40 ms
SITE-A#

SITE-B#ping 3.3.3.3 sou lo0
Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 3.3.3.3, timeout is 2 seconds:
Packet sent with a source address of 2.2.2.2 
!!!!!
Success rate is 100 percent (5/5), round-trip min/avg/max = 15/22/47 ms
SITE-B#

##after CGN PAT MODE with overload keywords! not working, execpt ICMP!
ip nat settings mode cgn
no ip nat settings support mapping outside
ip nat pool CGN 103.1.1.1 103.1.1.2 prefix-length 24
ip nat inside source list CGN pool CGN overload
ip forward-protocol nd
!
no ip http server
no ip http secure-server
!
ip access-list extended CGN
 permit ip 100.64.1.0 0.0.0.255 any

ipsec don't work, TELNET don't work!
SITE-A#telnet 61.128.1.1
Trying 61.128.1.1 ... 
% Connection timed out; remote host not responding

SITE-A#telnet 61.128.1.1
SITE-A#
SITE-A#
SITE-A#
SITE-A#
SITE-A#ping 61.128.1.1
Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 61.128.1.1, timeout is 2 seconds:
!!!!!
Success rate is 100 percent (5/5), round-trip min/avg/max = 15/19/34 ms
SITE-A#

ip nat settings mode cgn
no ip nat settings support mapping outside
ip nat pool CGN 103.1.1.1 103.1.1.1 prefix-length 30
ip nat inside source list CGN pool CGN overload
ip forward-protocol nd
!
no ip http server
no ip http secure-server
!
ip access-list extended CGN
 permit ip 100.64.1.0 0.0.0.255 any

CGN#show ip nat tr
CGN#show ip nat translations 
Pro  Inside global         Inside local          Outside local         Outside global
udp  103.1.1.1:1025        100.64.1.2:4500       ---                   ---
udp  103.1.1.1:512         100.64.1.2:500        ---                   ---
udp  103.1.1.1:513         100.64.1.3:500        ---                   ---
udp  103.1.1.1:1024        100.64.1.3:4500       ---                   ---
Total number of translations: 4

HQ#show cry isa sa
IPv4 Crypto ISAKMP SA
dst             src             state          conn-id status
61.128.1.1      103.1.1.1       QM_IDLE           1011 ACTIVE
61.128.1.1      103.1.1.1       QM_IDLE           1010 ACTIVE

IPv6 Crypto ISAKMP SA

HQ#wr
Building configuration...

  [OK]