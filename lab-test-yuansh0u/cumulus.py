cumulus-linux
#username 
cumulus
#password
CumulusLinux!  

##check interface list
ip a 
##enable interfaces
 net add interface swp1-7
 net pending
 net commit
##loopback address assignment
 net add loopback lo ip address 10.0.0.11/32
  net commit

  net add loopback lo ip address 10.0.0.12/32
  net commit
  
  net add loopback lo ip address 10.0.0.13/32
  net commit  

##ospf unnumbered
net add ospf router-id 10.0.0.3
net add loopback lo ip address 10.0.0.3/32
net add loopback lo ospf area 0.0.0.0
net add ospf passive-interface lo 
net add interface swp1 ip address 10.0.0.3/32
net add interface swp1 ospf area 0.0.0.0
net add interface swp1 ospf network point-to-point
net pending
net commit


##create SVI interface with VRF a, Then assign anycast-gateway
##create bridge with swp7 interface,verification <brctl show>

##cumulus@leaf2:/etc/network$ brctl show
##bridge name     bridge id               STP enabled     interfaces
##bridge          8000.005000000207       yes             swp7
##                                                        vni100
 net add bridge bridge ports swp7
 net add vlan 100 ip address 192.168.100.254/24
 net add vlan 100 ipv6 address fc00:192:168:100::254/64
##vrf allocation  
 net add vlan 100 vrf A
##anycast-gateway for L3VNI  
 net add vlan 100 hwaddress 12:34:56:78:9a:bc

 net add vlan 200 ip address 192.168.200.254/24
 net add vlan 200 ipv6 address fc00:192:168:200::254/64
##vrf allocation 
 net add vlan 200 vrf A
##anycast-gateway for L3VNI 
 net add vlan 200 hwaddress 12:34:56:78:9a:bc
net pending
net commit 

##Delete configuration
net del bridge bridge ports swp7
net del vlan 100 ip address 192.168.100.254/24

 ##sudo vtysh
spine1# configure terminal 
spine1(config)# interface lo
spine1(config-if)# ip ospf area 0.0.0.0
spine1(config-if)# do wr

##BGP unnumbered Ipv4 Unicast AFI/EVPN
##leaf
net add bgp autonomous-system 65511
net add bgp router-id 10.0.0.3
net add bgp neighbor swp1 interface remote-as internal
net add bgp neighbor swp1 remote-as internal
net add bgp l2vpn evpn neighbor swp1 activate
net add bgp l2vpn evpn advertise-all-vni
net add bgp l2vpn evpn advertise-default-gw
net pending
net commit
##EVPN type-5 Route announce
net add bgp vrf A autonomous-system 65511
net add bgp vrf A l2vpn evpn advertise ipv4 unicast
net add bgp vrf A l2vpn evpn advertise ipv6 unicast
net add bgp l2vpn evpn  advertise ipv6 unicast
##Border leaf
net add bgp vrf A autonomous-system 65511
net add bgp vrf A neighbor 100.64.1.2 remote-as 65000
net add bgp vrf A neighbor fc00:100:64:1::2 remote-as 65000
net del bgp vrf A ipv4 unicast neighbor fc00:100:64:1::2 activate
net add bgp vrf A ipv6 unicast neighbor fc00:100:64:1::2 activate
net add bgp vrf A l2vpn evpn  advertise ipv4 unicast
net add bgp vrf A l2vpn evpn  advertise ipv6 unicast
##SPINE AS RR
net add bgp autonomous-system 65511
net add bgp router-id 10.0.0.2
net add bgp neighbor swp1-7 interface remote-as internal
net add bgp neighbor swp1-7 route-reflector-client
net add bgp l2vpn evpn neighbor swp1-7 activate
net add bgp l2vpn evpn neighbor swp1-7 route-reflector-clientnet
net pending
net commit

##vlan mapping vxlan
##Define NVE interface
##vlan mapping to vxlan vni 10100 
net add vxlan vni100 vxlan id 10100
net add vxlan vni100 vxlan local-tunnelip 10.0.0.3
net add vxlan vni100 bridge access 100
net add vxlan vni100 bridge learning off
net commit
##vlan mapping to vxlan vni 10200 
net add vxlan vni200 vxlan id 10200
net add vxlan vni200 vxlan local-tunnelip 10.0.0.1
net add vxlan vni200 bridge access 200
net add vxlan vni200 bridge learning off
net commit

##Symmetric routing with l3VNI = CISCO interface vlan for l3VNI/ALL Leafs
net add vxlan vni104001 vxlan id 104001
net add vxlan vni104001 bridge access 4001
net add vxlan vni104001 vxlan local-tunnelip 10.0.0.4
net add vxlan vni104001 bridge learning off
net add vxlan vni104001 bridge arp-nd-suppress on
net add bridge bridge ports vni104001
net add vlan 4001 vrf A 
net add vrf A vni 104001
net pending
net commit

##When two vteps are operating in VXLAN active active mode with symmetric mode, configure this router MAC
##corresponding to each layer3 VNI to ensure both VTEPs use the same MAC address.
net add vlan 4001 hwaddress 44:44:44:44:44:44
##anycast-loopback for BGP next-hop
net add loopback lo clag vxlan-anycast-ip 10.0.0.255

cumulus@leaf1:/etc/frr$ net show bgp evpn vni 
Advertise Gateway Macip: Enabled
Advertise All VNI flag: Enabled
Number of L2 VNIs: 2
Number of L3 VNIs: 1
Flags: * - Kernel
  VNI        Type RD                    Import RT                 Export RT                 Tenant VRF                           
* 10200      L2   10.0.0.1:3            65511:10200               65511:10200              A                                    
* 10100      L2   10.0.0.1:2            65511:10100               65511:10100              A                                    
* 104001     L3   192.168.200.254:4     65511:104001              65511:104001             A                                    
cumulus@leaf1:/etc/frr$ 


###MLAG-1
net add clag peer sys-mac 44:38:39:FF:01:01 interface swp3-4 primary backup-ip 10.0.0.6
net add vlan 100-200
net add clag port bond bond-to-host-77 interface swp7 clag-id 7
net add bond bond-to-host-77 bridge access 100
net pending
net commit

###MLAG-2
net add clag peer sys-mac 44:38:39:FF:01:01 interface swp3-4 secondary backup-ip 10.0.0.5
net add vlan 100-200
net add clag port bond bond-to-host-77 interface swp7 clag-id 7
net add bond bond-to-host-77 bridge access 100
net pending
net commit

##ubuntu-linux bond4 configuration
# eth2 is manually configured, and slave to the "bond0" bonded NIC
auto eth2
iface eth2 inet manual
    bond-master bond0

# eth1 ditto, thus creating a 2-link bond.
auto eth1
iface eth1 inet manual
    bond-master bond0

# bond0 is the bonded NIC and can be used like any other normal NIC.
# bond0 is configured using static network information.
auto bond0
iface bond0 inet static
    address 192.168.100.77
    gateway 192.168.100.254
    netmask 255.255.255.0

    # bond0 uses standard IEEE 802.3ad LACP bonding protocol
    bond-mode 4
    bond-miimon 100
    bond-lacp-rate 1
    bond-slaves eth2 eth1
 ########
##Bonding verification
 cat /proc/net/bonding/bond0


##Docker Lab
sudo apt-key adv --keyserver hkp://p80.pool.skskeyservers.net:80 --recv-keys
cumulus@switch:$ sudo nano /etc/apt/sources.list.d/jessie.list
...
deb http://httpredir.debian.org/debian jessie main contrib nonfree
deb-src http://httpredir.debian.org/debian jessie main contrib non-free

cumulus@switch:$ sudo nano /etc/apt/sources.list.d/docker.list
deb https://apt.dockerproject.org/repo debian-jessie main

$sudo apt update
$sudo apt install -y nmap
$sudo apt install -y vpnc
$sudo apt install -y git
$sudo apt install -y curl
$sudo apt install docker-engine

$sudo systemctl start docker
$docker pull nginx && docker pull debian
$sudo docker pull debian
$sudo docker run --name debian -d debian
$sudo docker exec -it <container-ID> /bin/bash
$sudo docker stop $(docker ps -a -q) && docker rm $(docker ps -a -q)
