hostname NAT64
!
!
ipv6 unicast-routing
!
!
interface g1.23
 encap dot1q 23
  ipv6 address 4001::1/96
nat64 enable
cdp enable

!
interface g1.12
 encap dot1q 12
ip address 20.20.20.1 255.255.255.0
load-interval 30
negotiation auto
nat64 enable
cdp enable
!
!
ipv6 access-list ACLv6
permit ipv6 4001::/64 any
!
!
nat64 prefix stateful 2001::/96
nat64 v4 pool pool1 27.1.1.10 27.1.1.11
nat64 v6v4 list ACLv6 pool pool1
!
end