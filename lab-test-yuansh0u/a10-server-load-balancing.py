###ipv4 inet > ipv4 lb >backends

interface ethernet 1 
  name lan-inside 
  enable 
  ip address 172.31.1.254 255.255.255.0 
  ip nat inside 
!
interface ethernet 2 
  name inet-outside 
  enable 
  ip address 150.1.1.254 255.255.255.0 
  ip nat outside 
!
slb common 
  snat-on-vip 
!
slb server 172.31.1.1 172.31.1.1 
  port 80 tcp 
!       
slb server 172.31.1.2 172.31.1.2 
  port 80 tcp 
!       
slb service-group vip-150.1.1.80 tcp 
  method least-request 
  health-check ping 
  member 172.31.1.1 80 
  member 172.31.1.2 80 
!       
slb virtual-server 150.1.1.80 150.1.1.80 
  port 80 http
    source-nat pool snat
!!!without source-nat pool snat
!!!inet client ip address don't change
!!!with source-nat pool snat
!!!inet client ip address will modify to snat pool policy IP
!!!this is an optional setting,both works!   
    service-group vip-150.1.1.80

ip route 0.0.0.0 /0 150.1.1.254 


##internal access inet
ip access-list lan 
  permit ip 172.31.1.0 0.0.0.255 any 
!
ip nat pool snat 150.1.1.80 150.1.1.80 netmask /24 
!
ip nat inside source list name lan pool snat 
!

!
###
R1-web# ping vrf fuck 202.100.1.1 re 1
Type escape sequence to abort.
Sending 1, 100-byte ICMP Echos to 202.100.1.1, timeout is 2 seconds:
!
Success rate is 100 percent (1/1), round-trip min/avg/max = 48/48/48 ms



###ipv4-inet-to-ipv6-backend

ipv4-client---<inet>---<a10>---ipv6-only-server


ip access-list lan 
  permit ip 172.31.1.0 0.0.0.255 any 
!
interface ethernet 1 
  name lan-inside 
  enable 
  ip address 172.31.1.254 255.255.255.0 
  ip nat inside 
  ipv6 address 2019::254/64 
!
interface ethernet 2 
  name inet-outside 
  enable 
  ip address 150.1.1.1 255.255.255.0 
  ip nat outside 
!
interface ethernet 3 
!       
interface ethernet 4 
!
!
ip nat pool snat 150.1.1.81 150.1.1.81 netmask /24 
!
ip nat inside source list name lan pool snat 
!
ipv6 nat pool snatv6 2019::66 2019::66 netmask 64 
!
ip route 0.0.0.0 /0 150.1.1.254 
!
slb server web1 2019::1 
  port 80 tcp 
!
slb server web2 2019::2 
  port 80 tcp 
!
slb service-group vip-46 tcp 
  member web1 80 
  member web2 80 
!
slb template http http 
!
slb virtual-server 46 150.1.1.81 
  port 80 http 
    source-nat pool snatv6 
    service-group vip-46 
    template http http

!
##
 ipv4 client<http://150.1.1.81>
   inet routing 
      {ipv4-inet}  a10 {ipv6-backends}
 src-ip=202.100.1.1   src-ip->2019::66
 dst-ip=150.1.1.81    dst-ip->2019::1/2

###ipv6-inet-to-ipv4-backend
interface ethernet 1 
  name lan-inside 
  enable 
  ip address 172.31.1.254 255.255.255.0 
  ip nat inside 
  ipv6 address 2019::254/64 
  ipv6 nat inside 
!
interface ethernet 2 
  name inet-outside 
  enable 
  ip address 150.1.1.1 255.255.255.0 
  ip nat outside 
  ipv6 address 2001::1/64 
  ipv6 nat outside 
!
interface ethernet 3 
!
interface ethernet 4 
!
!
ip nat pool snat 150.1.1.81 150.1.1.81 netmask /24 
!
ip nat inside source list name lan pool snat 
!
ipv6 nat pool snatv6 2019::66 2019::66 netmask 64 
!
ip route 0.0.0.0 /0 150.1.1.254 
!
ipv6 route ::/0 2001::254 
!
slb server web1-v4 172.31.1.1 
  port 80 tcp 
!       
!
slb service-group vip-64 tcp 
  member web1-v4 80
  member web2-v4 80 
!
slb template http http 
!
slb virtual-server 64 2001::64 
  port 80 http 
    source-nat pool snat 
    service-group vip-64 
    template http http 
!

###testing
inet-router#telnet 2001::64 80
Trying 2001::64, 80 ... Open


###final config
ip access-list lan 
  permit ip 172.31.1.0 0.0.0.255 any 
!
ipv6 access-list LANV6 
  permit ipv6 2019::/64 any 
!
interface ethernet 1 
  name lan-inside 
  enable 
  ip address 172.31.1.254 255.255.255.0 
  ip nat inside 
  ipv6 address 2019::254/64 
  ipv6 nat inside 
!
interface ethernet 2 
  name inet-outside 
  enable 
  ip address 150.1.1.1 255.255.255.0 
  ip nat outside 
  ipv6 address 2001::1/64 
  ipv6 nat outside 
!
interface ethernet 3 
!
interface ethernet 4 
!
!
ip nat pool snat 150.1.1.81 150.1.1.81 netmask /24 
!
ip nat inside source list name lan pool snat 
!
ipv6 nat pool snatv6 2019::66 2019::66 netmask 64 
!
ip route 0.0.0.0 /0 150.1.1.254 
!
ipv6 route ::/0 2001::254 
!
slb server web1-v4 172.31.1.1 
  port 80 tcp 
!       
slb server web1-v6 2019::1 
  port 80 tcp 
!
slb server web2-v4 172.31.1.2 
  port 80 tcp 
!
slb server web2-v6 2019::2 
  port 80 tcp 
!
slb service-group vip-44-150.1.1.80 tcp 
  member web1-v4 80 
  member web2-v4 80 
!
slb service-group vip-4to6150.1.1.81 tcp 
  member web1-v6 80 
  member web2-v6 80 
!
slb service-group vip-64 tcp 
  member web1-v4 80 
  member web2-v4 80 
!
slb template http http 
!
slb virtual-server 44-150.1.1.80 150.1.1.80 
  port 80 http 
    service-group vip-44-150.1.1.80 
    template http http 
!
slb virtual-server 4to6150.1.1.81 150.1.1.81 
  port 80 http 
    source-nat pool snatv6 
    service-group vip-4to6150.1.1.81 
    template http http 
!
slb virtual-server 64 2001::64 
  port 80 http 
    source-nat pool snat 
    service-group vip-64 
    template http http 
!
end