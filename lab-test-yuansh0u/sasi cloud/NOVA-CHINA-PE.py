NOVA-CHINA-PE#sh run
NOVA-CHINA-PE#sh running-config 
Building configuration...

Current configuration : 1784 bytes
!
! Last configuration change at 22:41:33 UTC Tue Jul 18 2017
!
version 15.5
service timestamps debug datetime msec
service timestamps log datetime msec
no platform punt-keepalive disable-kernel-core
platform console serial
!
hostname NOVA-CHINA-PE
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
license udi pid CSR1000V sn 9L6RUMJ0YKB
!
spanning-tree extend system-id
!
username cisco privilege 15 password 0 cisco
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
interface Tunnel0
 ip address 100.64.1.2 255.255.255.252
 tunnel source 219.235.229.249
 tunnel destination 114.248.1.1
!
interface GigabitEthernet1
 no ip address
 shutdown
 negotiation auto
!
interface GigabitEthernet2
 ip address 219.235.229.249 255.255.255.0
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
router bgp 9809
 bgp log-neighbor-changes
 neighbor 100.64.1.1 remote-as 65511
 neighbor 219.235.229.254 remote-as 4808
 !
 address-family ipv4
  neighbor 100.64.1.1 activate
  neighbor 100.64.1.1 route-map DENY-ALL in
  neighbor 100.64.1.1 route-map NO-Advertise out
  neighbor 219.235.229.254 activate
 exit-address-family
!
!
virtual-service csr_mgmt
!
ip forward-protocol nd
!
ip http server
ip http authentication local
no ip http secure-server
ip route 0.0.0.0 0.0.0.0 219.235.229.254
!         
!
route-map NO-Advertise permit 10
 set community no-advertise
!
route-map DENY-ALL deny 10
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
line vty 0 4
 password cisco
 login local
 transport input all
!
!
end

