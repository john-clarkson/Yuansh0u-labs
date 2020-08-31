enable 
 config t
hostname PE1
vrf definition CEA
 rd 9809:9809
 !
 address-family ipv4
 route-target export 9809:9809
 route-target import 9809:9809

interface e1/1
 ip address 169.254.254.1 255.255.255.0
 no shut
 ip ospf 9809 area 0

interface e1/0
 vrf forwarding CEA
  no shut
 ip address 123.123.111.1 255.255.255.0
 
 interface Loopback0
 ip address 1.1.1.1 255.255.255.255
 ip ospf 9809 area 0


router ospf 9809
 mpls ldp autoconfig
 log-adjacency-changes
!
router bgp 9809
 bgp router-id 1.1.1.1
 no bgp default ipv4-unicast
 bgp log-neighbor-changes
 neighbor 2.2.2.2 remote-as 9809
 neighbor 2.2.2.2 update-source Loopback0
 neighbor 123.123.111.254 remote-as 65511

 !
 address-family ipv4
  no synchronization
  no auto-summary
 exit-address-family
 !
 address-family vpnv4
  neighbor 2.2.2.2 activate
  neighbor 2.2.2.2 send-community extended
 exit-address-family
 !

 address-family ipv4 vrf CEA
  no synchronization
  neighbor 123.123.111.254 remote-as 65511
  neighbor 123.123.111.254 activate
 exit-address-family

####
CE-1
 enable 
  config 
  hostname CE-1
  interface e1/0
 no shut
 ip address 123.123.111.254 255.255.255.0
 
 interface Loopback0
 ip address 150.150.1.1 255.255.255.255
 
router bgp 65511
 bgp router-id 150.150.1.1
 no bgp default ipv4-unicast
 bgp log-neighbor-changes
 neighbor 123.123.111.1 remote-as 9809

 !
 address-family ipv4
  neighbor 123.123.111.1 activate
  redis conn
  no synchronization
  no auto-summary
 exit-address-family


 ##
 enable 
 config t
hostname PE2
vrf definition CEA
 rd 9809:9809
 !
 address-family ipv4
 route-target export 9809:9809
 route-target import 9809:9809

interface e1/1
 ip address 169.254.254.2 255.255.255.0
 no shut
 ip ospf 9809 area 0

interface e1/0
 vrf forwarding CEA
  no shut
 ip address 123.123.222.1 255.255.255.0
 
 interface Loopback0
 ip address  2.2.2.2 255.255.255.255
 ip ospf 9809 area 0


router ospf 9809
 mpls ldp autoconfig
 log-adjacency-changes
!
router bgp 9809
 bgp router-id 2.2.2.2
 no bgp default ipv4-unicast
 bgp log-neighbor-changes
 neighbor 1.1.1.1 remote-as 9809
 neighbor 1.1.1.1 update-source Loopback0
 neighbor 123.123.222.254 remote-as 65511

 !
 address-family ipv4
  no synchronization
  no auto-summary
 exit-address-family
 !
 address-family vpnv4
  neighbor 1.1.1.1 activate
  neighbor 1.1.1.1 send-community extended
 exit-address-family
 !

 address-family ipv4 vrf CEA
  no synchronization
  neighbor 123.123.222.254 remote-as 65522
  neighbor 123.123.222.254 activate
 exit-address-family

 ###
 CE-2
 enable 
  config 
  hostname CE-2
  interface e1/0
 no shut
 ip address 123.123.222.254 255.255.255.0
 
 interface Loopback0
 ip address 150.150.2.2 255.255.255.255
 
router bgp 65522
 bgp router-id 150.150.2.2
 no bgp default ipv4-unicast
 bgp log-neighbor-changes
 neighbor 123.123.222.1 remote-as 9809

 !
 address-family ipv4
  neighbor 123.123.222.1 activate
  redis conn
  no synchronization
  no auto-summary
 exit-address-family
