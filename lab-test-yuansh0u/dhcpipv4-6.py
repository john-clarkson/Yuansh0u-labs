IPV4:
service dhcp

ip dhcp excluded-address 1.1.1.254
ip dhcp excluded-address 2.2.2.254
ip dhcp excluded-address 3.3.3.254
ip dhcp excluded-address 4.4.4.254
ip dhcp excluded-address 5.5.5.254
!
ip dhcp pool UK
   vrf UK
   network 1.1.1.0 255.255.255.0
   default-router 1.1.1.254 
   dns-server 8.8.8.8 
!
ip dhcp pool GERMANY
   vrf GERMANY
   network 2.2.2.0 255.255.255.0
   default-router 2.2.2.254 
   dns-server 8.8.8.8 
!
ip dhcp pool CHINA
   vrf CHINA
   network 3.3.3.0 255.255.255.0
   default-router 3.3.3.254 
   dns-server 8.8.8.8 
!
ip dhcp pool RUSSIA
   vrf RUSSIA
   network 4.4.4.0 255.255.255.0
   default-router 4.4.4.254 
   dns-server 8.8.8.8 
!
ip dhcp pool USA
   vrf USA
   network 5.5.5.0 255.255.255.0
   default-router 5.5.5.254 
   dns-server 8.8.8.8 
!

===========================
IPV6
ipv6 unicast-routing
ipv6 cef

ipv6 dhcp pool UK
 
 dns-server 2001:DA8:202:10::36

 ipv6 dhcp pool GERMANY
 
 dns-server 2001:DA8:202:10::36

 ipv6 dhcp pool CHINA

 dns-server 2001:DA8:202:10::36

 ipv6 dhcp pool RUSSIA
 
 dns-server 2001:DA8:202:10::36

 ipv6 dhcp pool USA
  dns-server 2001:DA8:202:10::36

interface GigabitEthernet2/0.1
 ipv6 dhcp server UK_IPV6_CLIENT
 ipv6 nd other
interface GigabitEthernet2/0.2
 ipv6 dhcp server GERMANY_IPV6_CLIENT
 ipv6 nd other 
interface GigabitEthernet2/0.3
 ipv6 dhcp server CHINA_IPV6_CLIENT
 ipv6 nd other
interface GigabitEthernet2/0.4
 ipv6 dhcp server RUSSIA_IPV6_CLIENT
 ipv6 nd other
interface GigabitEthernet2/0.5
 ipv6 dhcp server USA_IPV6_CLIENT
 ipv6 nd other 