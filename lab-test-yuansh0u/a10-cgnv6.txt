
topology
 windows-external ipv4 only-----a10------ ipv6 only

    10.1.1.10---10.1.1.254(e2)(e1)2019::254----2019::1/2

 ipv4/24
 ipv6/64

a10
## nat64 configuration

class-list nat64client ipv6 
  ::/0 lsn-lid 1 
!
interface ethernet 1 
  name ipv6-inside 
  enable 
  ipv6 address 2019::254/64 
  ipv6 nat inside 
!
interface ethernet 2 
  name ipv4-outside 
  enable 
  ip address 10.1.1.254 255.255.255.0 
  ip nat outside 
!
!
cgnv6 template logging log 
  log port-mappings creation 
  log port-overloading 
  log sessions 
  include-destination 
!
cgnv6 translation icmp-timeout fast 
!
!
cgnv6 nat pool nat64 10.1.1.64 10.1.1.64 netmask /24 
!
cgnv6 lsn inbound-refresh disable 
cgnv6 lsn ip-selection round-robin 
cgnv6 lsn icmp send-on-user-quota-exceeded disable 
!
cgnv6 lsn-lid 1 
  source-nat-pool nat64 shared 
!
!
cgnv6 nat64 inside source class-list nat64client 
cgnv6 nat64 icmp send-on-port-unavailable admin-filtered 
cgnv6 nat64 icmp send-on-user-quota-exceeded disable 
!       
cgnv6 nat64 alg ftp xlat-no-trans-pasv enable 
!
cgnv6 nat64 prefix 64:ff9b::/96 
!

write memory 




vThunder(config)(NOLICENSE)#show cgnv6 nat64 conversion 10.1.1.10 prefix 64:ff9b::/96  
Prefix: 64:ff9b::/96
IPv6: 64:ff9b::a01:10a
IPv4: 10.1.1.10


####

###cisco router

interface FastEthernet0/0
 ip address 192.168.1.1 255.255.255.0
 duplex half
 ipv6 address 2019::1/64
!
ip forward-protocol nd
ip http server
ip http authentication local
no ip http secure-server
!
!
ip route 0.0.0.0 0.0.0.0 192.168.1.254
!
ipv6 route ::/0 2019::254

ipv6 init traffic


ping 64:ff9b::a01:12c  =10.1.1.44
r1#ping 64:ff9b::a01:10a =10.1.1.10
Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 64:FF9B::A01:10A, timeout is 2 seconds:
!!!!!
Success rate is 100 percent (5/5), round-trip min/avg/max = 16/24/36 ms
r1#

Prot Forward Source         Forward Dest           Reverse Source         Reverse Dest           Age   Hash Flags    Type        
-----------------------------------------------------------------------------------------------------------------------------
Icmp [2019::1]:2214         [64:ff9b::a01: :0      10.1.1.44:0            10.1.1.64:2214         1     1    NSe0f0r0 LSN         
Total Sessions:          1 

###stateless NAT46
cgnv6 nat46-stateless fragmentation inbound send-icmpv6 
!
cgnv6 nat46-stateless prefix 2001::/96 
!
cgnv6 nat46-stateless static-dest-mapping 10.1.1.46 2019::1 
!

###


ping 10.1.1.46
!!!!
