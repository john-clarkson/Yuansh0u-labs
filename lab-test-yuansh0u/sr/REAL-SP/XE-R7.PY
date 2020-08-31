XE-P7-BGP-LS-RR#sh rn
                    ^
% Invalid input detected at '^' marker.

XE-P7-BGP-LS-RR#sh run
XE-P7-BGP-LS-RR#sh running-config 
Building configuration...

Current configuration : 5209 bytes
!
! Last configuration change at 10:41:39 UTC Sat Mar 17 2018
!
version 16.7
service timestamps debug datetime msec
service timestamps log datetime msec
platform qfp utilization monitor load 80
no platform punt-keepalive disable-kernel-core
platform console virtual
!
hostname XE-P7-BGP-LS-RR
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
mpls traffic-eng pcc peer 150.1.255.253 source 100.64.1.7
mpls traffic-eng pcc report-all
mpls traffic-eng auto-tunnel p2p config unnumbered-interface Loopback0
mpls traffic-eng auto-tunnel p2p tunnel-num min 1 max 100
!
!
multilink bundle-name authenticated
!
!
!
!
!
crypto pki trustpoint TP-self-signed-372516875
 enrollment selfsigned
 subject-name cn=IOS-Self-Signed-Certificate-372516875
 revocation-check none
 rsakeypair TP-self-signed-372516875
!
!
crypto pki certificate chain TP-self-signed-372516875
 certificate self-signed 01
  3082032E 30820216 A0030201 02020101 300D0609 2A864886 F70D0101 05050030 
  30312E30 2C060355 04031325 494F532D 53656C66 2D536967 6E65642D 43657274 
  69666963 6174652D 33373235 31363837 35301E17 0D313830 33313731 30333030 
  395A170D 32303031 30313030 30303030 5A303031 2E302C06 03550403 1325494F 
  532D5365 6C662D53 69676E65 642D4365 72746966 69636174 652D3337 32353136 
  38373530 82012230 0D06092A 864886F7 0D010101 05000382 010F0030 82010A02 
  82010100 D8F0E8C0 DEF17124 9CB3888B 4A16C9A2 F2279774 422F43F0 F6E65C9E 
  B8E00CD8 7ABBB0F9 037A0357 AA76990F 9A85DCDA DDF81C48 073E33E2 CA23CFC5 
  F7749BCF CA2C0584 EF9C8FEE 972E74B0 8326F739 78E08343 E8BBEBC9 9F9AD6C8 
  68DD210B 26200BE2 23D8F822 13CC93D5 453D30E6 4E072D34 AAFA2930 4C79E3B5 
  0A8896B1 8BDF1825 7FDCC21E 8A6823AE 2926A98E 3E1FB113 51B53D95 5D9DEB74 
  DC809221 306E8DCE 5538569F BFD9B1F6 FB759B6F 69F7E335 F83EDAA4 B05A5F92 
  C841C894 C304BA83 686EA51A CA01B4EE C4121EFF BCE9E013 7CBA22D1 E42753E9 
  DBC68440 4075E80B 2712FDC2 2AF78045 B6CEF5AB 807539E1 C414FF0F AE23EDCF 
  1529F4FF 02030100 01A35330 51300F06 03551D13 0101FF04 05300301 01FF301F 
  0603551D 23041830 168014C9 BDB2E842 158B410F 2F25D8E2 9E236AE6 0DEEAA30 
  1D060355 1D0E0416 0414C9BD B2E84215 8B410F2F 25D8E29E 236AE60D EEAA300D 
  06092A86 4886F70D 01010505 00038201 0100C251 42FF9938 752C5D7B C143C10D 
  E7B6EAA5 A0752C0A 9649E18D 4D981CB5 92AEC4C7 1703C310 01F95A99 184E17B4 
  42A1678C AC521F0D 393117DD 15D542B9 2B06A619 3F2BD41C 5F8105AD F02D88D4 
  6E4D364D A68E82CC 92682E04 018D1AA9 766D258C 615037A9 F5D22BBF 464E993E 
  CBD0302D A8F30C93 9E62F972 D0107929 5C5F1904 4144CE2E 9176982C A43DDA66 
  03DE7DC3 98DA919C 8AC9A6C8 98620107 D659720D 548C0C4E 9496A131 F35FE0F7 
  359BA454 B7BFB949 E33ECA9F 7EF6ABD9 8193507C 9D05FB7F BB82C944 91D50CA9 
  6844A6A1 6D5216FA BAA38D97 896428F7 5D960B36 35F56241 17FFA19A 5A88D2D4 
  132614B7 3B374E3F 15C07D8F 8D2D7E37 2130
        quit
!
!
segment-routing mpls
 !
 connected-prefix-sid-map
  address-family ipv4
   100.64.1.7/32 index 7 range 1 
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
!
license udi pid CSR1000V sn 9PE3AIS7QT5
license boot level ax
no license smart enable
diagnostic bootup level minimal
!
spanning-tree extend system-id
!
!
!
username cisco privilege 15 secret 5 $1$AOwi$jAQYkDOGsoHAOakKLcERt0
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
interface Loopback0
 ip address 100.64.1.7 255.255.255.255
 ip router isis fuck
!
interface GigabitEthernet1
 ip address 150.1.87.7 255.255.0.0
 negotiation auto
 no mop enabled
 no mop sysid
!
interface GigabitEthernet2
 no ip address
 negotiation auto
 no mop enabled
 no mop sysid
!
interface GigabitEthernet2.67
 encapsulation dot1Q 67
 ip address 169.254.67.7 255.255.255.0
 ip router isis fuck
 shutdown
 mpls traffic-eng tunnels
 isis network point-to-point 
!
interface GigabitEthernet2.947
 encapsulation dot1Q 947
 ip address 169.254.47.7 255.255.255.0
 ip router isis fuck
 mpls traffic-eng tunnels
 isis network point-to-point 
!
interface GigabitEthernet2.957
 encapsulation dot1Q 957
 ip address 169.254.57.7 255.255.255.0
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
router isis fuck
 net 49.0001.0000.0007.00
 is-type level-2-only
 metric-style wide
 distribute link-state
 segment-routing mpls
 fast-reroute per-prefix level-2 all
 fast-reroute ti-lfa level-2
 mpls traffic-eng router-id Loopback0
 mpls traffic-eng level-2
!
router bgp 9000
 bgp router-id 100.64.1.7
 bgp log-neighbor-changes
 neighbor 150.1.255.253 remote-as 9000
 neighbor 150.1.255.253 update-source Loopback0
 !
 address-family link-state link-state
  neighbor 150.1.255.253 activate
 exit-address-family
!
!
virtual-service csr_mgmt
 ip shared host-interface GigabitEthernet1
!
ip forward-protocol nd
ip http server
ip http authentication local
ip http secure-server
!
!
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
line con 0
 stopbits 1
line vty 0 4
 exec-timeout 0 0
 login local
line vty 5 15
 exec-timeout 0 0
 login local
!
wsma agent exec
!
wsma agent config
!
wsma agent filesys
!
wsma agent notify
!
!
end

