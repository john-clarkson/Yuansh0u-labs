p2#sh run
p2#sh running-config 
Building configuration...

Current configuration : 4707 bytes
!
! Last configuration change at 16:23:09 UTC Sat Nov 25 2017 by cisco
!
version 16.5
no service timestamps debug uptime
no service timestamps log uptime
platform qfp utilization monitor load 80
no platform punt-keepalive disable-kernel-core
platform console auto
!
hostname p2
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

no ip domain lookup
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
mpls traffic-eng pcc peer 192.168.255.254 source 2.2.2.2
mpls traffic-eng pcc report-all
!
!
multilink bundle-name authenticated
!
!
!
!
!
crypto pki trustpoint TP-self-signed-3933599890
 enrollment selfsigned
 subject-name cn=IOS-Self-Signed-Certificate-3933599890
 revocation-check none
 rsakeypair TP-self-signed-3933599890
!
!
crypto pki certificate chain TP-self-signed-3933599890
 certificate self-signed 01
  30820330 30820218 A0030201 02020101 300D0609 2A864886 F70D0101 05050030 
  31312F30 2D060355 04031326 494F532D 53656C66 2D536967 6E65642D 43657274 
  69666963 6174652D 33393333 35393938 3930301E 170D3137 31313235 30333335 
  31335A17 0D323030 31303130 30303030 305A3031 312F302D 06035504 03132649 
  4F532D53 656C662D 5369676E 65642D43 65727469 66696361 74652D33 39333335 
  39393839 30308201 22300D06 092A8648 86F70D01 01010500 0382010F 00308201 
  0A028201 0100C5D6 F1A74EF2 DABEDDF2 C34945CB 95C476A9 DF8CF2E9 A7C581ED 
  0F66D28A 4997A214 E265E057 F3BB1719 A2633A49 0877B4AA 394C3BEC AD92668B 
  3556ABE0 6AC26019 B7DA868B CC72A112 79EDAA4C 1F5E0E50 E307E4C2 13711D3A 
  41197390 B9E6614A 1F1437EB BF6D8CA6 D94AAE77 32906E5E 88025383 F47B0AFA 
  45E1798E 160DA32E 2946C777 608CBC46 E9DB8654 9325D153 BB9AE447 6073B29E 
  B2FF334B 3C19CD51 EAA099BF 9FF63A71 E7709170 0D76461B 58174285 2EA35D73 
  DC35E8FF 48A047E3 8F290C64 12778D16 2E0B4F59 4B384299 6A93E4DE 00AA3B8E 
  0A9A85D7 50AAC4A6 4A900190 1B882153 B8903A2C 92274157 3DF9DD59 247F8A39 
  3B76B5CD D5250203 010001A3 53305130 0F060355 1D130101 FF040530 030101FF 
  301F0603 551D2304 18301680 1452282B 0F3BB4F8 BAB8DC01 B3CD4A2C 4B92A316 
  44301D06 03551D0E 04160414 52282B0F 3BB4F8BA B8DC01B3 CD4A2C4B 92A31644 
  300D0609 2A864886 F70D0101 05050003 82010100 006A4EA2 D2B44B2B 0F040E0C 
  06F36A0E 4AAFAFD2 CD3DAE8B 2F550327 AB9C1A78 5E385900 C0B64841 8F23658F 
  ADD29D74 92289B83 0E76C5DD 3C036B9D A391AFD6 2215E1C8 887885D4 D476ABE5 
  F5B5813B 7E860205 BC490B48 34065A59 7BF31A71 64AAAFFC 1E113299 689DAC4F 
  719D304E 95EAA06C 463264F3 961265E3 C645D6F6 D87D64CB B702DBF2 D3AA283F 
  25CEE36F D8F98243 4332462F 95365336 2231DB51 E47B22FF B988F685 05E369E5 
  CBD32042 8534DF36 65985B1D CEEA117A 98D5486D 06123744 19C1BAA8 6D852343 
  E0C055AB AB98374A A05A4DE6 CECF72B3 8FE0A453 8357342A AC1B178A B92939BB 
  E80C5BC0 55C330A2 1A5F68A9 E8ABE831 72992D3D
        quit
!
!
segment-routing mpls
 !
 connected-prefix-sid-map
  address-family ipv4
   2.2.2.2/32 index 2 range 1 
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
license udi pid CSR1000V sn 9FNLUUJDEH8
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
 ip address 2.2.2.2 255.255.255.255
 ip router isis fuck
!         
interface GigabitEthernet1
 ip address 169.254.1.2 255.255.255.0
 ip router isis fuck
 negotiation auto
 mpls traffic-eng tunnels
 no mop enabled
 no mop sysid
 isis network point-to-point 
!
interface GigabitEthernet2
 ip address 192.168.255.1 255.255.255.0
 ip router isis fuck
 negotiation auto
 no mop enabled
 no mop sysid
!
router isis fuck
 net 49.0001.0000.0002.00
 is-type level-2-only
 metric-style wide
 distribute link-state
 segment-routing mpls
 mpls traffic-eng router-id Loopback0
 mpls traffic-eng level-2
!
router bgp 9000
 bgp router-id 2.2.2.2
 bgp log-neighbor-changes
 neighbor 192.168.255.254 remote-as 9000
 neighbor 192.168.255.254 update-source Loopback0
 !
 address-family ipv4
  redistribute connected
  neighbor 192.168.255.254 activate
 exit-address-family
 !
 address-family link-state link-state
  neighbor 192.168.255.254 activate
  neighbor 192.168.255.254 route-reflector-client
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
ip ssh server algorithm encryption aes128-ctr aes192-ctr aes256-ctr
ip ssh client algorithm encryption aes128-ctr aes192-ctr aes256-ctr
!
!
!
route-map x permit 10
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
 exec-timeout 0 0
 login local
 transport input telnet
line vty 5 15
 exec-timeout 0 0
 login local
 transport input telnet
!
!
!
!
!
!
end

