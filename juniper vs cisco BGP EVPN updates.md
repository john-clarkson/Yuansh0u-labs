# Juniper vs Cisco BGP EVPN updates
## Cisco BGP EVPN type 2 update pcap
![](https://i.imgur.com/3oOvLQM.jpg)
## Juniper BGP EVPN type 2 update pcap
![](https://i.imgur.com/XjLlkRj.jpg)



## show bgp evpn type2
### Cisco NEXUS
![](https://i.imgur.com/I4HFUO6.jpg)

### Juniper QFX/MX
![](https://i.imgur.com/foQgAYw.png)

### Note
Juniper BGP EVPN type 2 updates does not include host ip information by default.
If you want to advertise host ip information on junos, just enable VMTO(Virtual Machine Traffic Optimization) feature set.
 - Ref link
https://www.juniper.net/documentation/en_US/junos/topics/concept/evpn-ingress-vmto.html
