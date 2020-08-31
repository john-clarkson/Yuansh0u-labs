##bridge interface
root@eve-ng:/etc/apt# brctl show
bridge name     bridge id               STP enabled     interfaces
pnet0           8000.00505699505d       no              eth0
pnet1           8000.00505699644f       no              eth1
pnet2           8000.0050569915f5       no              eth2
pnet3           8000.000000000000       no
pnet4           8000.000000000000       no
pnet5           8000.000000000000       no
pnet6           8000.000000000000       no
pnet7           8000.000000000000       no
pnet8           8000.000000000000       no
pnet9           8000.000000000000       no
brctl show

## show interface information
## eve-ng use pnet0 as the management interface, not eth0
## if you add an addtional NIC card, you will be set the dhcp client functions as to pnet1 interface.


##enable interface
[root@juniper /]# ifup eth1

Determining IP information for eth1... done.

sudo ip link set dev eth2 up 

##disable interface
[root@juniper /]# ifdown eth1

###

root@eve-ng:/# ifconfig eth0
eth0      Link encap:Ethernet  HWaddr 00:50:56:99:67:c0  
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:745724 errors:0 dropped:0 overruns:0 frame:0
          TX packets:48503 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000 
          RX bytes:701766502 (701.7 MB)  TX bytes:32935455 (32.9 MB)

root@eve-ng:/# ifconfig pnet0
pnet0     Link encap:Ethernet  HWaddr 00:50:56:99:67:c0  
          inet addr:150.1.5.253  Bcast:150.1.255.255  Mask:255.255.0.0
          inet6 addr: fe80::250:56ff:fe99:67c0/64 Scope:Link
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:85668 errors:0 dropped:31 overruns:0 frame:0
          TX packets:48453 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000 
          RX bytes:12429593 (12.4 MB)  TX bytes:32919043 (32.9 MB)
##add default route
route add default gw 150.1.66.254 eth0
## add static route
 
## check default route
 root@eve-ng:/# route
Kernel IP routing table
Destination     Gateway         Genmask         Flags Metric Ref    Use Iface
default         150.1.1.253     0.0.0.0         UG    0      0        0 pnet0
150.1.0.0       *               255.255.0.0     U     0      0        0 pnet0
root@eve-ng:/# route -n
Kernel IP routing table
Destination     Gateway         Genmask         Flags Metric Ref    Use Iface
0.0.0.0         150.1.1.253     0.0.0.0         UG    0      0        0 pnet0
150.1.0.0       0.0.0.0         255.255.0.0     U     0      0        0 pnet0
root@eve-ng:/# 


## delete default gateway
 root@eve-ng:/# route -n
Kernel IP routing table
Destination     Gateway         Genmask         Flags Metric Ref    Use Iface
0.0.0.0         150.1.1.253     0.0.0.0         UG    0      0        0 pnet0
150.1.0.0       0.0.0.0         255.255.0.0     U     0      0        0 pnet0
root@eve-ng:/# route del default 
root@eve-ng:/# route -n 
Kernel IP routing table
Destination     Gateway         Genmask         Flags Metric Ref    Use Iface
150.1.0.0       0.0.0.0         255.255.0.0     U     0      0        0 pnet0
root@eve-ng:/# 

## if you set the wrong ip address to network adptors, please use f0llowing command to delete it.
ip addr del 10.21.0.86/24 dev eth1
## set dhcp client to pnet1
 dhclient pnet1
## check dhcp client working or not.

root@eve-ng:/etc/network# ifconfig pnet1
pnet1     Link encap:Ethernet  HWaddr 00:50:56:99:16:7a  
          inet addr:10.21.0.86  Bcast:10.21.0.255  Mask:255.255.255.0
          inet6 addr: fe80::250:56ff:fe99:167a/64 Scope:Link
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:55070 errors:0 dropped:40 overruns:0 frame:0
          TX packets:93 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000 
          RX bytes:4535049 (4.5 MB)  TX bytes:9875 (9.8 KB)

root@eve-ng:/etc/network# 
root@eve-ng:/etc/network# ping 10.21.0.1
PING 10.21.0.1 (10.21.0.1) 56(84) bytes of data.
64 bytes from 10.21.0.1: icmp_seq=1 ttl=255 time=0.604 ms
64 bytes from 10.21.0.1: icmp_seq=2 ttl=255 time=0.637 ms
^C
--- 10.21.0.1 ping statistics ---
2 packets transmitted, 2 received, 0% packet loss, time 1000ms
rtt min/avg/max/mdev = 0.604/0.620/0.637/0.029 ms
root@eve-ng:/etc/network# ping www.baidu.com
PING www.a.shifen.com (61.135.169.121) 56(84) bytes of data.
64 bytes from 61.135.169.121: icmp_seq=1 ttl=54 time=2.21 ms
^C
--- www.a.shifen.com ping statistics ---
1 packets transmitted, 1 received, 0% packet loss, time 0ms
rtt min/avg/max/mdev = 2.210/2.210/2.210/0.000 ms
root@eve-ng:/etc/network#

root@eve-ng:/etc/network# route -n
Kernel IP routing table
Destination     Gateway         Genmask         Flags Metric Ref    Use Iface
0.0.0.0         10.21.0.1       0.0.0.0         UG    0      0        0 pnet1
10.21.0.0       0.0.0.0         255.255.255.0   U     0      0        0 pnet1
150.1.0.0       0.0.0.0         255.255.0.0     U     0      0        0 pnet0
root@eve-ng:/etc/network# route   
Kernel IP routing table
Destination     Gateway         Genmask         Flags Metric Ref    Use Iface
default         bogon           0.0.0.0         UG    0      0        0 pnet1
10.21.0.0       *               255.255.255.0   U     0      0        0 pnet1
150.1.0.0       *               255.255.0.0     U     0      0        0 pnet0
root@eve-ng:/etc/network# 

##update OS and software
##Connect to your EVE server on CLI as root and type following commands:

apt-get update

apt-get upgrade

 

Clear your browser cache...

 

SPECIAL NOTES: ( update to V2.0.3-68 )

after upgrade use the command :

dpkg -l eve-ng

 

If the eve-ng version is still the same use this command:

 

apt-get dist-upgrade