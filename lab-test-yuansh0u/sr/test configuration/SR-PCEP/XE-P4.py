XE-P4-RR#SH RUN
XE-P4-RR#SH RUNning-config 
Building configuration...

Current configuration : 2524 bytes
!
! Last configuration change at 12:07:44 UTC Tue Nov 21 2017
!
version 15.5
service timestamps debug datetime msec
service timestamps log datetime msec
no platform punt-keepalive disable-kernel-core
platform console serial
!
hostname XE-P4-RR
!
boot-start-marker
boot-end-marker
!
!
!
no aaa new-model
!
!
!
!
!         
!
!
!
!
!
!



!
!
!
ipv6 unicast-routing
!
!
!
!
!
!
!
subscriber templating
!
multilink bundle-name authenticated
!
!
!
!
!
!
!
segment-routing mpls
 !
 connected-prefix-sid-map
  address-family ipv4
   100.64.1.4/32 4 range 1
  exit-address-family
 !
!
!
!
!
!
!
!
!
license udi pid CSR1000V sn 97MZ3MCHTEI
!
spanning-tree extend system-id
!
!
redundancy
!
!
!
!
!
!
! 
!
!
!
!
!
!
!
!
!
!
!         
!
! 
! 
! 
! 
! 
! 
!
!
interface Loopback0
 ip address 100.64.1.4 255.255.255.255
!
interface GigabitEthernet1
 no ip address
 negotiation auto
!
interface GigabitEthernet1.14
 encapsulation dot1Q 14
 ip address 169.254.14.4 255.255.255.0
 ip router isis fuck
 isis network point-to-point 
 isis metric 999 level-2
!         
interface GigabitEthernet1.34
 encapsulation dot1Q 34
 ip address 169.254.34.4 255.255.255.0
 ip router isis fuck
 isis network point-to-point 
 isis metric 999 level-2
!
interface GigabitEthernet1.224
 encapsulation dot1Q 224
 ip address 169.254.224.4 255.255.255.0
 ip router isis fuck
 bfd interval 250 min_rx 250 multiplier 3
 isis network point-to-point 
 isis metric 999 level-2
 isis bfd
!
interface GigabitEthernet2
 no ip address
 shutdown
 negotiation auto
!
interface GigabitEthernet3
 no ip address
 shutdown
 negotiation auto
!
interface GigabitEthernet4
 no ip address
 shutdown
 negotiation auto
!
router isis fuck
 net 49.0001.0000.0044.00
 is-type level-2-only
 metric-style wide
 log-adjacency-changes
 segment-routing mpls
 fast-reroute per-prefix level-2 all
 passive-interface Loopback0
!
router bgp 9000
 bgp router-id 100.64.1.4
 bgp cluster-id 9.9.9.9
 bgp log-neighbor-changes
 bgp listen range 100.64.0.0/16 peer-group PE
 no bgp default ipv4-unicast
 neighbor PE peer-group
 neighbor PE remote-as 9000
 neighbor PE update-source Loopback0
 !
 address-family ipv4
 exit-address-family
 !
 address-family vpnv4
  neighbor PE activate
  neighbor PE send-community extended
  neighbor PE route-reflector-client
 exit-address-family
!
!
virtual-service csr_mgmt
!
ip forward-protocol nd
!
no ip http server
no ip http secure-server
!
!
!         
!
control-plane
!
 !
 !
 !
 !
!
!
!
!
!
line con 0
 stopbits 1
line vty 0
 login
line vty 1
 login
 length 0
line vty 2 4
 login
!
!         
end

