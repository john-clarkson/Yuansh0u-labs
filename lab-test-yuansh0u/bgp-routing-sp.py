##SERVER
username cisco privilege 15 password 0 cisco
!
interface FastEthernet0/0
 no ip address
 duplex half
!
interface FastEthernet0/0.192
 encapsulation dot1Q 192
 ip address 10.1.1.1 255.255.255.0 secondary
 ip address 192.168.1.1 255.255.255.0
!
interface FastEthernet1/0
 no ip address
 shutdown
 duplex half
!
ip forward-protocol nd
no ip http server
no ip http secure-server
!         
!
ip route 0.0.0.0 0.0.0.0 192.168.1.254
ip route 0.0.0.0 0.0.0.0 10.1.1.254
line con 0
 stopbits 1
line aux 0
 stopbits 1
line vty 0 4
 login local
 transport input all
!
####NAT

!
interface Loopback0
 ip address 202.100.1.1 255.255.255.255
!
interface FastEthernet0/0
 no ip address
 duplex half
!
interface FastEthernet0/0.100
 encapsulation dot1Q 100
 ip address 172.16.100.1 255.255.255.0
 ip nat outside
 ip virtual-reassembly in
 ip ospf 1 area 0
!
interface FastEthernet0/0.192
 encapsulation dot1Q 192
 ip address 10.1.1.254 255.255.255.0 secondary
 ip address 192.168.1.254 255.255.255.0
 ip nat inside
 ip virtual-reassembly in
 ip ospf 1 area 0
!
interface FastEthernet0/0.200
 encapsulation dot1Q 200
 ip address 172.16.200.1 255.255.255.0
 ip nat outside
 ip virtual-reassembly in
 ip ospf 1 area 0
!
interface FastEthernet1/0
 no ip address
 shutdown
 duplex half
!
router ospf 1
!
ip forward-protocol nd
no ip http server
no ip http secure-server
!
!
ip nat pool TEN-NAT-POOL 202.200.1.1 202.200.1.1 netmask 255.255.255.252
ip nat inside source route-map NAT interface Loopback0 overload
ip nat inside source route-map TEN-NAT pool TEN-NAT-POOL overload
ip nat inside source static tcp 192.168.1.1 23 202.100.1.1 23 extendable
ip nat inside source static tcp 10.1.1.1 23 202.200.1.1 1023 extendable
!
ip access-list extended LAN
 permit ip 192.168.1.0 0.0.0.255 any
ip access-list extended TEN-LAN
 permit ip 10.1.1.0 0.0.0.255 any
!
!
route-map TEN-NAT permit 10
 match ip address TEN-LAN
 match interface FastEthernet0/0.100
!
route-map TEN-NAT permit 20
 match ip address TEN-LAN
 match interface FastEthernet0/0.200
!
route-map NAT permit 10
 match ip address LAN
 match interface FastEthernet0/0.100
!         
route-map NAT permit 20
 match ip address LAN
 match interface FastEthernet0/0.200
!
!
####bgp-c1
interface Loopback0
 ip address 1.1.1.1 255.255.255.255
!
interface FastEthernet0/0
 no ip address
 duplex half
!
interface FastEthernet0/0.21
 encapsulation dot1Q 21
 ip address 169.254.1.1 255.255.255.0
!
interface FastEthernet0/0.100
 encapsulation dot1Q 100
 ip address 172.16.100.254 255.255.255.0
 ip ospf 1 area 0
!
interface FastEthernet1/0
 no ip address
 shutdown 
 duplex half
!
router ospf 1
 default-information originate always
!
router bgp 65511
 bgp router-id 1.2.3.4
 bgp log-neighbor-changes
 neighbor 169.254.1.254 remote-as 2
 !
 address-family ipv4
  redistribute static
  neighbor 169.254.1.254 activate
 exit-address-family
!
ip forward-protocol nd
no ip http server
no ip http secure-server
!
!
ip route 202.100.1.1 255.255.255.255 172.16.100.1
ip route 202.200.1.1 255.255.255.255 172.16.100.1
!         
!
ip prefix-list PUBLIC-IP seq 5 permit 202.100.1.1/32
!
route-map PUBLIC-IP permit 10
!

end

###bgp-c2
interface Loopback0
 ip address 2.2.2.2 255.255.255.255
!
interface FastEthernet0/0
 no ip address
 duplex half
!
interface FastEthernet0/0.22
 encapsulation dot1Q 22
 ip address 169.254.2.1 255.255.255.0
!
interface FastEthernet0/0.200
 encapsulation dot1Q 200
 ip address 172.16.200.254 255.255.255.0
 ip ospf 1 area 0
!
interface FastEthernet1/0
 no ip address
 shutdown 
 duplex half
!
router ospf 1
 router-id 2.2.2.2
 default-information originate always
!
router bgp 65511
 bgp router-id 4.3.2.1
 bgp log-neighbor-changes
 neighbor 169.254.2.254 remote-as 2
 !
 address-family ipv4
  redistribute static
  neighbor 169.254.2.254 activate
 exit-address-family
!
ip forward-protocol nd
no ip http server
no ip http secure-server
!
!
ip route 202.100.1.1 255.255.255.255 172.16.200.1
ip route 202.200.1.1 255.255.255.255 172.16.200.1
!
!

###SP-BGP

ip host www.fuck.com 202.100.1.1
ip host www.fuckten.com 202.200.1.1

interface Loopback0
 ip address 8.8.8.8 255.255.255.255 secondary
 ip address 8.8.8.9 255.255.255.255
!
interface FastEthernet0/0
 no ip address
 duplex half
!
interface FastEthernet0/0.21
 encapsulation dot1Q 21
 ip address 169.254.1.254 255.255.255.0
!
interface FastEthernet0/0.22
 encapsulation dot1Q 22
 ip address 169.254.2.254 255.255.255.0
!
interface FastEthernet1/0
 no ip address
 shutdown
 duplex half
!
router bgp 2
 bgp router-id 8.8.8.8
 bgp log-neighbor-changes
 neighbor 169.254.1.1 remote-as 65511
 neighbor 169.254.2.1 remote-as 65511
 !
 address-family ipv4
  network 8.8.8.8 mask 255.255.255.255
  network 8.8.8.9 mask 255.255.255.255
  neighbor 169.254.1.1 activate
  neighbor 169.254.2.1 activate
 exit-address-family