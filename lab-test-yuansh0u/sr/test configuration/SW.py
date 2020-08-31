enable
 config 

hostname FUCKER-L2-SW

 VLAN 2 
 VLAN 12 
 VLAN 13 
 VLAN 14 
 VLAN 22 
 VLAN 24 
 VLAN 34 
 VLAN 100 
 VLAN 111 
 VLAN 113 
 VLAN 200 
 VLAN 222 
 VLAN 224 
 VLAN 15
 VLAN 25
!
int rang g0/0 -3 
 switchport trunk encapsulation dot1q
 switchport mode trunk
 media-type rj45
 negotiation auto
 spanning-tree portfast edge trunk
 spanning-tree bpdufilter enable

int rang g1/0 -3 
 switchport trunk encapsulation dot1q
 switchport mode trunk
 media-type rj45
 negotiation auto
 spanning-tree portfast edge trunk
 spanning-tree bpdufilter enable
int rang g2/0 -3 
 switchport trunk encapsulation dot1q
 switchport mode trunk
 media-type rj45
 negotiation auto
 spanning-tree portfast edge trunk
 spanning-tree bpdufilter enable

int rang g3/0 -3 
 switchport trunk encapsulation dot1q
 switchport mode trunk
 media-type rj45
 negotiation auto
 spanning-tree portfast edge trunk
 spanning-tree bpdufilter enable


interface GigabitEthernet0/0
 switchport trunk encapsulation dot1q
 switchport mode trunk
 media-type rj45
 negotiation auto
 spanning-tree portfast edge trunk
 spanning-tree bpdufilter enable
!
interface GigabitEthernet0/1
 switchport trunk encapsulation dot1q
 switchport mode trunk
 media-type rj45
 negotiation auto
 spanning-tree portfast edge trunk
 spanning-tree bpdufilter enable
!
interface GigabitEthernet0/2
 switchport trunk encapsulation dot1q
 switchport mode trunk
 media-type rj45
 negotiation auto
 spanning-tree portfast edge trunk
 spanning-tree bpdufilter enable
!
interface GigabitEthernet0/3
 switchport trunk encapsulation dot1q
 switchport mode trunk
 media-type rj45
 negotiation auto
 spanning-tree portfast edge trunk
 spanning-tree bpdufilter enable
!
interface GigabitEthernet1/0
 switchport trunk encapsulation dot1q
 switchport mode trunk
 media-type rj45
 negotiation auto
 spanning-tree portfast edge trunk
 spanning-tree bpdufilter enable
!
interface GigabitEthernet1/1
 switchport trunk encapsulation dot1q
 switchport mode trunk
 media-type rj45
 negotiation auto
 spanning-tree portfast edge trunk
 spanning-tree bpdufilter enable
!
interface GigabitEthernet1/2
 switchport trunk encapsulation dot1q
 switchport mode trunk
 media-type rj45
 negotiation auto
 spanning-tree portfast edge trunk
 spanning-tree bpdufilter enable
!
interface GigabitEthernet1/3
 switchport trunk encapsulation dot1q
 switchport mode trunk
 media-type rj45
 negotiation auto
 spanning-tree portfast edge trunk
 spanning-tree bpdufilter enable
!         
interface GigabitEthernet2/0
 media-type rj45
 negotiation auto
 spanning-tree bpdufilter enable
!
interface GigabitEthernet2/1
 media-type rj45
 negotiation auto
 spanning-tree bpdufilter enable
!
interface GigabitEthernet2/2
 media-type rj45
 negotiation auto
 spanning-tree bpdufilter enable
!
interface GigabitEthernet2/3
 media-type rj45
 negotiation auto
 spanning-tree bpdufilter enable
!
interface GigabitEthernet3/0
 media-type rj45
 negotiation auto
!
interface GigabitEthernet3/1
 media-type rj45
 negotiation auto
!
interface GigabitEthernet3/2
 media-type rj45
 negotiation auto
!
interface GigabitEthernet3/3
 media-type rj45
 negotiation auto
!
ip forward-protocol nd
!
no ip http server
no ip http secure-server
!
!
!
!
!
!         
control-plane
!
banner exec ^C
**************************************************************************
* IOSv is strictly limited to use for evaluation, demonstration and IOS  *
* education. IOSv is provided as-is and is not supported by Cisco's      *
* Technical Advisory Center. Any use or disclosure, in whole or in part, *
* of the IOSv Software or Documentation to any third party for any       *
* purposes is expressly prohibited except as otherwise authorized by     *
* Cisco in writing.                                                      *
**************************************************************************^C
banner incoming ^C
**************************************************************************
* IOSv is strictly limited to use for evaluation, demonstration and IOS  *
* education. IOSv is provided as-is and is not supported by Cisco's      *
* Technical Advisory Center. Any use or disclosure, in whole or in part, *
* of the IOSv Software or Documentation to any third party for any       *
* purposes is expressly prohibited except as otherwise authorized by     *
* Cisco in writing.                                                      *
**************************************************************************^C
banner login ^C
**************************************************************************
* IOSv is strictly limited to use for evaluation, demonstration and IOS  *
* education. IOSv is provided as-is and is not supported by Cisco's      *
* Technical Advisory Center. Any use or disclosure, in whole or in part, *
* of the IOSv Software or Documentation to any third party for any       *
* purposes is expressly prohibited except as otherwise authorized by     *
* Cisco in writing.                                                      *
**************************************************************************^C
!
line con 0
line aux 0
line vty 0 4
 login
!
!
end

