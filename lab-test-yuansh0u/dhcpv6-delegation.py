###DHCPv6 delegation for address allocation
##ISP
ipv6 unicast-routing
ipv6 dhcp pool dhcpv6

!--- The DHCP pool is named "dhcpv6."

!
prefix-delegation pool dhcpv6-pool1 lifetime 1800 600

!--- The prefix delegation pool name is "dhcpv6-pool1."

!
dns-server 2001:DB8:3000:3000::42
domain-name example.com
!

 interface FastEthernet0/0
 ipv6 address FE80::1111 link-local
 ipv6 enable
 ipv6 dhcp server dhcpv6
 !ipv6 address 2010:AB8:0:1::1/64
 ipv6 enable
!
ipv6 local pool dhcpv6-pool1 2001:DB8:1200::/56 64


!
end

##home-router
ipv6 unicast-routing
!
ipv6 route ::/0 FastEthernet0/0 fe80::1111
interface f0/0
no ip address
!ipv6 address autoconfig default

!--- The autoconfig default adds a static ipv6 
!--- default route pointing to upstream DHCP server.

!
ipv6 enable
ipv6 dhcp client pd prefix-from-provider

!--- The DHCP client prefix delegation is 
!--- given the name prefix-from-provider.

!
interface FastEthernet1/0
no ip address
ipv6 address prefix-from-provider ::1:0:0:0:1/64

##clients

