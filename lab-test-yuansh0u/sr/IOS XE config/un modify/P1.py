P1#sh run
P1#sh running-config 
Building configuration...

Current configuration : 4234 bytes
!
! Last configuration change at 16:24:38 UTC Sat Nov 25 2017
!
version 16.5
service timestamps debug datetime msec
service timestamps log datetime msec
platform qfp utilization monitor load 80
no platform punt-keepalive disable-kernel-core
platform console auto
!
hostname P1
!
boot-start-marker
boot-end-marker
!
!
enable password cisco
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
mpls traffic-eng pcc peer 192.168.255.254 source 1.1.1.1
mpls traffic-eng pcc report-all
!
!
multilink bundle-name authenticated
!
!
!
!
!
crypto pki trustpoint TP-self-signed-2832903953
 enrollment selfsigned
 subject-name cn=IOS-Self-Signed-Certificate-2832903953
 revocation-check none
 rsakeypair TP-self-signed-2832903953
!
!
crypto pki certificate chain TP-self-signed-2832903953
 certificate self-signed 01
  30820330 30820218 A0030201 02020101 300D0609 2A864886 F70D0101 05050030 
  31312F30 2D060355 04031326 494F532D 53656C66 2D536967 6E65642D 43657274 
  69666963 6174652D 32383332 39303339 3533301E 170D3137 31313235 30333334 
  35345A17 0D323030 31303130 30303030 305A3031 312F302D 06035504 03132649 
  4F532D53 656C662D 5369676E 65642D43 65727469 66696361 74652D32 38333239 
  30333935 33308201 22300D06 092A8648 86F70D01 01010500 0382010F 00308201 
  0A028201 0100B30E 69B71712 85C7F44F F8575CC9 630A6E6E 311FC1A4 CA12F055 
  D7169424 6B81DD15 976CF194 A0E7DA9E 1405D934 50FCABD9 4F09CD94 8814A490 
  8237A050 F986A315 4DDB7FDB AFFF098E 8D856F07 6B50A009 ACEBAF18 B3F4227D 
  FA527579 0C6A32CE 8196D79E 34D1765E 6144B5A2 7D0BBEA5 DCD6C201 9EDD5713 
  297CCCF6 DA4D410B 336C96B4 37D071B0 DC291989 871B5A23 D30FA0B4 FFD05012 
  538EB21A 72708DDD 8B3424DB 1C6A9A67 636CE477 E9546BE6 CA835A05 B9577636 
  0F05F051 E97DB83E 79EC4981 07596C56 B5F165DD 6D05C9C1 014A719E 0A8E383F 
  23A722BE B72865FB E904E5AA 02BE9933 307B197B BB9CB4F0 464822E7 5B9B8EDE 
  B8A723ED A84B0203 010001A3 53305130 0F060355 1D130101 FF040530 030101FF 
  301F0603 551D2304 18301680 145C8587 AA9B986C 2718164B E763B0F6 51636867 
  1D301D06 03551D0E 04160414 5C8587AA 9B986C27 18164BE7 63B0F651 6368671D 
  300D0609 2A864886 F70D0101 05050003 82010100 47128BBF 05CB6433 11C3FA85 
  15E55D0B F9DD78DA 2731D714 8A9FB48C B5459AC7 11E1B513 275D3086 687A07FB 
  AEEC9493 F5BF384F AD0F50DE DBBD9AE7 7D7F0398 2E65EA7A FBD34FF4 4132CC77 
  4DC44707 E88B0D06 D822F182 59231C57 EB5A14FE 8D6A440F 5AD78789 18823F3C 
  C450FE83 CFBB3FF3 8AD560C5 7F4376B5 D40F8CCA 0D3AF209 8158E3F8 1CE35EAD 
  AD4187D8 00FCB402 92DC2F11 271D8937 1E8ABBD4 69B5D344 56FABD40 2E594638 
  EB53841E 8E86CC46 DF397F11 D13078C7 031C68B1 B8B0C6EE 7B13C75F 6D7BB8F7 
  412E134C 546C50FF 61EBA5FA 28BACD06 EF8439C8 B6BEDB66 23074777 21FDF63A 
  8FDDCC2E 08C9DC91 6B056FC7 329A4F26 797E2CF1
        quit
!
!
segment-routing mpls
 !        
 connected-prefix-sid-map
  address-family ipv4
   1.1.1.1/32 index 1 range 1 
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
license udi pid CSR1000V sn 98NELSVRT4N
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
 ip address 1.1.1.1 255.255.255.255
 ip router isis fuck
!
interface GigabitEthernet1
 ip address 169.254.1.1 255.255.255.0
 ip router isis fuck
 negotiation auto
 mpls traffic-eng tunnels
 no mop enabled
 no mop sysid
 isis network point-to-point 
!
router isis fuck
 net 49.0001.0000.0001.00
 is-type level-2-only
 metric-style wide
 segment-routing mpls
 mpls traffic-eng router-id Loopback0
 mpls traffic-eng level-2
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
line vty 0 4
 exec-timeout 0 0
 password cisco
 login
 transport input telnet
line vty 5 14
 exec-timeout 0 0
 password cisco
 login
 transport input telnet
line vty 15
 exec-timeout 0 0
 password cisco
 login local
 transport input telnet
!
!
!
!
!
!
end

