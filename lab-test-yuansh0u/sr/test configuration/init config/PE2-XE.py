*Nov 16 14:00:08.506: %SYS-5-CONFIG_I: Configured from console by console
XE-PE2>EN
XE-PE2#SH RUN
XE-PE2#SH RUNning-config 
Building configuration...

Current configuration : 2324 bytes
!
! Last configuration change at 14:00:08 UTC Thu Nov 16 2017
!
version 15.5
service timestamps debug datetime msec
service timestamps log datetime msec
no platform punt-keepalive disable-kernel-core
platform console serial
!
hostname XE-PE2
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
segment-routing mpls
!
!
!
!
!
!
!
!         
license udi pid CSR1000V sn 938AEJ03BAS
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
 ip address 100.64.22.2 255.255.255.255
 ip router isis fuck
!
interface GigabitEthernet1
 no ip address
 negotiation auto
!
interface GigabitEthernet1.112
 encapsulation dot1Q 112
 ip address 169.254.112.2 255.255.255.0
 ip router isis fuck
!         
interface GigabitEthernet1.200
 encapsulation dot1Q 200
 vrf forwarding A
 ip address 169.254.200.254 255.255.255.0
!
interface GigabitEthernet1.222
 encapsulation dot1Q 222
 ip address 169.254.222.2 255.255.255.0
 ip router isis fuck
!
interface GigabitEthernet1.224
 encapsulation dot1Q 224
 ip address 169.254.224.2 255.255.255.0
 ip router isis fuck
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
 net 49.0001.0000.0022.00
 is-type level-2-only
 metric-style wide level-2
 segment-routing mpls
!
router bgp 9000
 bgp router-id 100.64.22.2
 bgp log-neighbor-changes
 neighbor 100.64.1.4 remote-as 9000
 neighbor 100.64.1.4 update-source Loopback0
 !
 address-family vpnv4
  neighbor 100.64.1.4 activate
  neighbor 100.64.1.4 send-community extended
 exit-address-family
 !
 address-family ipv4 vrf A
  neighbor 169.254.200.1 remote-as 65522
  neighbor 169.254.200.1 activate
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

