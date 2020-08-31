
FMC initial config
sudo su -
##Default password
 password:Admin123
 configure-network
  150.1.41.254
   255.255.0.0
  150.1.1.253
   
##FTD initial config
> configure manager add 150.1.41.254 12345
Manager successfully configured.
Please make note of reg_key as this will be required while adding Device in FMC.

> configure network management-port 8305
##verify cli
> show managers
Type                      : Manager
Host                      : 150.1.41.254
Registration              : Completed

Management port changed to 8305.
> show network
network               network-dhcp-server   network-static-routes 
> show network
===============[ System Information ]===============
Hostname                  : cisco.com
Management port           : 8305
IPv4 Default route
  Gateway                 : 150.1.1.253

======================[ br1 ]=======================
State                     : Enabled
Channels                  : Management & Events
Mode                      : Non-Autonegotiation 
MDI/MDIX                  : Auto/MDIX 
MTU                       : 1500
MAC Address               : 00:50:00:00:06:01
----------------------[ IPv4 ]----------------------
Configuration             : Manual
Address                   : 150.1.41.1
Netmask                   : 255.255.0.0
Broadcast                 : 150.1.255.255
----------------------[ IPv6 ]----------------------
Configuration             : Disabled

===============[ Proxy Information ]================
State                     : Disabled
Authentication            : Disabled