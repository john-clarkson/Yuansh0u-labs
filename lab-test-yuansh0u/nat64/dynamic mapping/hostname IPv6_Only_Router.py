hostname IPv6_Only_Router
!
!
ipv6 unicast-routing
ipv6 cef
!
!
interface Gig1.23
encap dot1q 23
ip address 10.10.10.2 255.255.255.0
duplex auto
speed auto
ipv6 address 4001::2/96
!
!
ipv6 route 2001::/96 4001::1
!
!
end