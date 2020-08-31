P-RR#sh  
% Type "show ?" for a list of subcommands
P-RR#
P-RR#
P-RR#
P-RR#sh run
P-RR#sh running-config 
Building configuration...

Current configuration : 2075 bytes
!
! Last configuration change at 12:41:55 UTC Fri Jul 21 2017
!
version 15.5
service timestamps debug datetime msec
service timestamps log datetime msec
no platform punt-keepalive disable-kernel-core
platform console serial
!
hostname P-RR
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
!
!
!
!
!
!
license udi pid CSR1000V sn 9UHPRRC03AW
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
 ip address 3.3.3.3 255.255.255.255
 ip ospf 9809 area 0
!
interface GigabitEthernet1
 no ip address
 shutdown
 negotiation auto
!
interface GigabitEthernet2
 ip address 169.254.200.5 255.255.255.252
 ip ospf 9809 area 0
 negotiation auto
!
interface GigabitEthernet3
 ip address 169.254.200.1 255.255.255.252
 ip ospf 9809 area 0
 negotiation auto
!
interface GigabitEthernet4
 ip address 169.254.200.9 255.255.255.252
 ip ospf 9809 area 0
 negotiation auto
!         
router ospf 9809
 router-id 3.3.3.3
 prefix-suppression
 mpls ldp autoconfig
!
router bgp 9809
 bgp router-id 3.3.3.3
 bgp cluster-id 1
 bgp log-neighbor-changes
 neighbor 1.1.1.1 remote-as 9809
 neighbor 1.1.1.1 update-source Loopback0
 neighbor 2.2.2.2 remote-as 9809
 neighbor 2.2.2.2 update-source Loopback0
 neighbor 4.4.4.4 remote-as 9809
 neighbor 4.4.4.4 update-source Loopback0
 !
 address-family vpnv4
  neighbor 1.1.1.1 activate
  neighbor 1.1.1.1 send-community extended
  neighbor 1.1.1.1 route-reflector-client
  neighbor 2.2.2.2 activate
  neighbor 2.2.2.2 send-community extended
  neighbor 2.2.2.2 route-reflector-client
  neighbor 4.4.4.4 activate
  neighbor 4.4.4.4 send-community extended
  neighbor 4.4.4.4 route-reflector-client
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

