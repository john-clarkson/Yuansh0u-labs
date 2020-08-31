 

 enable 
  config 
  VLAN 2 
 VLAN 12 
 VLAN 13 
 VLAN 14 
 VLAN 22 
 VLAN 24 
 VLAN 34
 vlan 15
 vlan 56
 vlan 67 
 VLAN 100 
 VLAN 101 
 VLAN 111 
 VLAN 112 
 VLAN 113 
 VLAN 200 
 VLAN 201 
 VLAN 202 
 VLAN 222 
 VLAN 224 

no service timestamps debug datetime msec
no service timestamps log datetime msec
no service password-encryption
service compress-config
!
hostname FUCKER-L2-SW
!

!
interface GigabitEthernet0/0
 switchport trunk encapsulation dot1q
 spanning-tree bpdufilter enable
 switchport mode trunk
 media-type rj45
 negotiation auto
 spanning-tree portfast edge trunk
!
interface GigabitEthernet0/1
 switchport trunk encapsulation dot1q
 spanning-tree bpdufilter enable
 switchport mode trunk
 media-type rj45
 negotiation auto
 spanning-tree portfast edge trunk
!
interface GigabitEthernet0/2
 switchport trunk encapsulation dot1q
 spanning-tree bpdufilter enable
 switchport mode trunk
 media-type rj45
 negotiation auto
 spanning-tree portfast edge trunk
!
interface GigabitEthernet0/3
 switchport trunk encapsulation dot1q
 spanning-tree bpdufilter enable
 switchport mode trunk
 media-type rj45
 negotiation auto
 spanning-tree portfast edge trunk
!
interface GigabitEthernet1/0
 switchport trunk encapsulation dot1q
 spanning-tree bpdufilter enable
 switchport mode trunk
 media-type rj45
 negotiation auto
 spanning-tree portfast edge trunk
!
interface GigabitEthernet1/1
 switchport trunk encapsulation dot1q
 spanning-tree bpdufilter enable
 switchport mode trunk
 media-type rj45
 negotiation auto
 spanning-tree portfast edge trunk
!
interface GigabitEthernet1/2
 switchport trunk encapsulation dot1q
 spanning-tree bpdufilter enable
 switchport mode trunk
 media-type rj45
 negotiation auto
 spanning-tree portfast edge trunk
!
interface GigabitEthernet1/3
 switchport trunk encapsulation dot1q
 spanning-tree bpdufilter enable
 switchport mode trunk
 media-type rj45
 negotiation auto
 spanning-tree portfast edge trunk
!
interface GigabitEthernet2/0
 switchport trunk encapsulation dot1q
 spanning-tree bpdufilter enable
 switchport mode trunk
 media-type rj45
 negotiation auto
 spanning-tree portfast edge trunk
!
!
interface GigabitEthernet2/1
switchport trunk encapsulation dot1q
 spanning-tree bpdufilter enable
 switchport mode trunk
 media-type rj45
 negotiation auto
 spanning-tree portfast edge trunk
!
!
interface GigabitEthernet2/2
 switchport trunk encapsulation dot1q
 spanning-tree bpdufilter enable
 switchport mode trunk
 media-type rj45
 negotiation auto
 spanning-tree portfast edge trunk
!
interface GigabitEthernet2/3
switchport trunk encapsulation dot1q
 spanning-tree bpdufilter enable
 switchport mode trunk
 media-type rj45
 negotiation auto
 spanning-tree portfast edge trunk
!
!
interface GigabitEthernet3/0
 switchport trunk encapsulation dot1q
 spanning-tree bpdufilter enable
 switchport mode trunk
 media-type rj45
 negotiation auto
 spanning-tree portfast edge trunk
!
interface GigabitEthernet3/1
switchport trunk encapsulation dot1q
 spanning-tree bpdufilter enable
 switchport mode trunk
 media-type rj45
 negotiation auto
 spanning-tree portfast edge trunk
!
!
interface GigabitEthernet3/2
switchport trunk encapsulation dot1q
 spanning-tree bpdufilter enable
 switchport mode trunk
 media-type rj45
 negotiation auto
 spanning-tree portfast edge trunk
!
!
interface GigabitEthernet3/3
switchport trunk encapsulation dot1q
 spanning-tree bpdufilter enable
 switchport mode trunk
 media-type rj45
 negotiation auto
 spanning-tree portfast edge trunk
!
