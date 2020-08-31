
hostname XE-R1
!
boot-start-marker
boot-end-marker
!
!
vrf definition A
 rd 1:1
 !
 address-family ipv4
  route-target export 1:1
  route-target import 1:1
 exit-address-family
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

no ip domain lookup
ip domain name cisco.com
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
! 
! 
! 
!
mpls traffic-eng tunnels
mpls traffic-eng pcc peer 150.1.255.253 source 100.64.1.1
mpls traffic-eng pcc report-all
!
mpls traffic-eng lsp attributes AFFINITY_BLUE
 affinity 0x1 mask 0x1
!
!
multilink bundle-name authenticated
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
   100.64.1.1/32 index 1 range 1 
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
license udi pid CSR1000V sn 90TIFUVB4GQ
license boot level ax
flowspec
 local-install interface-all
 vrf A
  address-family ipv4
   local-install interface-all
diagnostic bootup level minimal
!
spanning-tree extend system-id
!
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
interface Loopback0
 ip address 100.64.1.1 255.255.255.255
 ip router isis fuck
!
interface GigabitEthernet2
no shutdown
 no ip address
 negotiation auto
!
interface GigabitEthernet2.12
!
interface GigabitEthernet2.912
 encapsulation dot1Q 912
 ip address 169.254.12.1 255.255.255.0
 ip router isis fuck
 mpls traffic-eng tunnels
 isis network point-to-point 
!
interface GigabitEthernet2.914
 encapsulation dot1Q 914
 ip address 169.254.14.1 255.255.255.0
 ip router isis fuck
 mpls traffic-eng tunnels
 isis network point-to-point 
!
interface GigabitEthernet2.915
 encapsulation dot1Q 915
 ip address 169.254.15.1 255.255.255.0
 ip router isis fuck
 mpls traffic-eng tunnels
 isis network point-to-point 
!
interface GigabitEthernet3
 no ip address
 shutdown
 negotiation auto
 no mop enabled
 no mop sysid
!
router ospf 1
 network 0.0.0.0 255.255.255.255 area 0
 mpls ldp autoconfig
!
router isis fuck
 net 49.0001.0000.0001.00
 is-type level-2-only
 metric-style wide
 segment-routing mpls
 fast-reroute per-prefix level-2 all
 fast-reroute ti-lfa level-2
 mpls traffic-eng router-id Loopback0
 mpls traffic-eng level-2
!
router bgp 9000
 bgp router-id 1.1.1.1
 bgp log-neighbor-changes
 neighbor 2.2.2.2 remote-as 9000
 !
 address-family vpnv4
  neighbor 2.2.2.2 activate
  neighbor 2.2.2.2 send-community both
 exit-address-family
 !        
 address-family vpnv4 flowspec
  neighbor 2.2.2.2 activate
  neighbor 2.2.2.2 send-community both
 exit-address-family
 !
 address-family ipv4 vrf A
  redistribute connected
 exit-address-family
 !
 address-family ipv4 flowspec vrf A
 exit-address-family
!

threat-visibility
!
virtual-service csr_mgmt
!
ip forward-protocol nd
ip http server
ip http authentication local
ip http secure-server
!
ip ssh port 4001 rotary 2
ip ssh version 2
ip ssh server algorithm encryption aes128-ctr aes192-ctr aes256-ctr
ip ssh client algorithm encryption aes128-ctr aes192-ctr aes256-ctr
!
     
line con 0
 stopbits 1
line vty 0 4
 exec-timeout 0 0
 login local
 transport input ssh
line vty 5 15
 exec-timeout 0 0
 login local
 transport input ssh
