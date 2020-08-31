XE-P7-BGP-LS-RR#sh run
XE-P7-BGP-LS-RR#sh running-config 
Building configuration...

Current configuration : 5239 bytes
!
! Last configuration change at 11:16:56 UTC Sat Dec 2 2017 by cisco
!
version 16.5
service timestamps debug datetime msec
service timestamps log datetime msec
platform qfp utilization monitor load 80
no platform punt-keepalive disable-kernel-core
platform console auto
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
! 
! 
! 
!
mpls traffic-eng tunnels
mpls traffic-eng pcc peer 150.1.255.253 source 100.64.1.7
mpls traffic-eng pcc report-all
!
!
multilink bundle-name authenticated
!
!
!
!
!
crypto pki trustpoint TP-self-signed-3443038474
 enrollment selfsigned
 subject-name cn=IOS-Self-Signed-Certificate-3443038474
 revocation-check none
 rsakeypair TP-self-signed-3443038474
!
!
crypto pki certificate chain TP-self-signed-3443038474
 certificate self-signed 01
  30820330 30820218 A0030201 02020101 300D0609 2A864886 F70D0101 05050030 
  31312F30 2D060355 04031326 494F532D 53656C66 2D536967 6E65642D 43657274 
  69666963 6174652D 33343433 30333834 3734301E 170D3137 30383135 31383031 
  31395A17 0D323030 31303130 30303030 305A3031 312F302D 06035504 03132649 
  4F532D53 656C662D 5369676E 65642D43 65727469 66696361 74652D33 34343330 
  33383437 34308201 22300D06 092A8648 86F70D01 01010500 0382010F 00308201 
  0A028201 0100B0DE C84585A9 D9E323FC D5FE5E4B 5BCE15D6 E70F3DD3 24C73889 
  812C7B7E D3304235 4899695D 8CACD801 D1FC2D47 9FB087A6 C9BE4A6B 605A1988 
  4E5AA78F C1087799 EC683794 51373466 FB12B18B AA020211 56FE790A 16366932 
  197A2C3C 735E50E3 40B69989 7E9B1B44 8A3843A7 4F776DFA B286A131 638982F5 
  4B0FF79D 767EFFAB 2A2C4C6E 0C1E7A29 AC52C0F3 2F732A0A 032E251D 43658378 
  073637E7 1EB3FDA6 D81EC861 83272AD3 D0A73AF9 FC7A5A89 C537ED02 3B9B3118 
  A0702018 B36B691E DA739A74 3C997EB6 0C2F91B0 B681B4FA F7587AC7 1309B17F 
  6907FFD6 2565D916 CDBCB7C8 915869D2 72F50D51 8C578B15 71DBCBFD F219A43B 
  8F699AB3 43F70203 010001A3 53305130 0F060355 1D130101 FF040530 030101FF 
  301F0603 551D2304 18301680 1422C3FA 61095B5F 13C0E151 5639444E A2B05943 
  21301D06 03551D0E 04160414 22C3FA61 095B5F13 C0E15156 39444EA2 B0594321 
  300D0609 2A864886 F70D0101 05050003 82010100 1970DB80 9D7B931A 2A0223DD 
  373AE297 7D7B8799 98CC4084 0C24D85C A7142F86 A6453AF0 8DF0F7A7 15106FA8 
  8F34EDDD 342D90D5 BC397385 F7865802 A7A35C88 5E9A5635 2725CFB4 E992D1E1 
  438D770D 6D1BF70B 05F0FE82 79C1D705 DD69E675 55D268EF 1BDE8995 ADB5E9CF 
  0A18B1C3 75099F21 821105C4 9B5C9F62 373E7388 DDBA4B77 4D71860B B4021FFC 
  990CAFC0 CA3336BA 1E611F71 7BD201F2 86313337 4DCEFE6C 1EE2CDDC AB208EFD 
  FD8B6714 3E05F275 90F67005 5252EE27 820B1509 32F1B743 9731E656 0C9977F6 
  5C2ABB7D 31351549 417F546A 348BADEA B6E0BB85 0397B867 9BE2962F 96ED3418 
  699BB4D8 1A1A94F1 5B54C49B C44AE8AB 07118837
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
license udi pid CSR1000V sn 9FYK7EN05FS
license boot level ax
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
 ip address 100.64.1.7 255.255.255.255
 ip router isis fuck
!
interface Loopback77
 ip address 77.77.77.77 255.255.255.255
!         
interface GigabitEthernet1
 ip address 150.1.66.254 255.255.0.0
 negotiation auto
 no mop enabled
 no mop sysid
!
interface GigabitEthernet2
 no ip address
 negotiation auto
!
interface GigabitEthernet2.12
 encapsulation dot1Q 12
 ip address 169.254.1.2 255.255.255.0
 ip router isis fuck
 shutdown
 mpls traffic-eng tunnels
 isis network point-to-point 
!
interface GigabitEthernet2.67
 encapsulation dot1Q 67
 ip address 169.254.67.7 255.255.255.0
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
 mpls traffic-eng router-id Loopback0
 mpls traffic-eng level-2
!
router bgp 9000
 bgp router-id 100.64.1.7
 bgp log-neighbor-changes
 neighbor 150.1.255.253 remote-as 9000
 neighbor 150.1.255.253 update-source Loopback0
 !
 address-family ipv4
  network 77.77.77.77 mask 255.255.255.255
  network 100.64.1.7 mask 255.255.255.255
  neighbor 150.1.255.253 activate
 exit-address-family
 !
 address-family link-state link-state
  neighbor 150.1.255.253 activate
  neighbor 150.1.255.253 route-reflector-client
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
 exec-timeout 0 0
 password cisco
 login local
line vty 1
 exec-timeout 0 0
 password cisco
 login local
 length 0
line vty 2 4
 exec-timeout 0 0
 password cisco
 login local
line vty 5 15
 exec-timeout 0 0
 password cisco
 login local
!
!
!
!
!
!
end

