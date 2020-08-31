[root@Juniper-C media]# cd NorthStar_Bundle_3_2_0/
[root@Juniper-C NorthStar_Bundle_3_2_0]# LS
-bash: LS: command not found
[root@Juniper-C NorthStar_Bundle_3_2_0]# ls
NorthStar-Bundle-3.2.0-20171205_110647_71810_178.x86_64.rpm  README.txt
[root@Juniper-C NorthStar_Bundle_3_2_0]# rpm -Uvh NorthStar-Bundle-3.2.0-20171205_110647_71810_178.x86_64.rpm 
Preparing...                ########################################### [100%]
INFO: Checking OS requirement
INFO: Centos version installed is CentOS release 6.9 (Final)
Pass OS checking. Will proceed with installation.
INFO: Current available disk space for /opt is 
6%. Will proceed with installation.
   1:NorthStar-Bundle       ########################################### [100%]


To continue the installation/upgrade, please run:

A) To install/upgrade NorthStar + JunosVM in this server, please run:
      1. cd /opt/northstar/northstar_bundle_3.2.0/ && ./install.sh

OR

B) To install/upgrade NorthStar in this server, please run:
      1. cd /opt/northstar/northstar_bundle_3.2.0/ && ./install-vm.sh

OR

C) To install/upgrade NorthStar + JunosVM + Analytics in this server, please run:
      1. cd /opt/northstar/northstar_bundle_3.2.0/ && ./install.sh
      2. cd /opt/northstar/northstar_bundle_3.2.0/ && ./install-analytics.sh

OR

D) To install/upgrade NorthStar + Analytics in this server, please run:
      1. cd /opt/northstar/northstar_bundle_3.2.0/ && ./install-vm.sh
      2. cd /opt/northstar/northstar_bundle_3.2.0/ && ./install-analytics.sh

OR

E) To install/upgrade Analytics in this server, please run:
      a. cd /opt/northstar/northstar_bundle_3.2.0/ && ./install-analytics.sh

OR

F) To install/upgrade Collector Slave in this server, please run:
      a. cd /opt/northstar/northstar_bundle_3.2.0/ && ./collector.sh

Optional parameters:
 --vm          : use this to install NorthStar in 2 VM scenario (default is non-VM)
                 2 VM means NorthStar-JunOS VM is outside NorthStar-App VM
                 This is the same as ./install-vm.sh
 --setup-fw    : re-initialize firewall using NorthStar recommended rules (default: firewall is not changed)
                 Firewall rules example will be available in /opt/northstar/utils/firewall.sh
 --skip-bridge : for non-VM install, skip checking external0 and mgmt0 bridges (default: perform verification on external0 and mgmt0 bridges configuration)
 --csd         : use this to install NorthStar inside CSD
 --ip          : use this to change NTAD/Junosvm ip. Example --ip <junosvm_ip>

[root@Juniper-C NorthStar_Bundle_3_2_0]# 

[root@Juniper-C NorthStar_Bundle_3_2_0]# cd /opt/northstar/northstar_bundle_3.2.0/
[root@Juniper-C northstar_bundle_3.2.0]# pwd
/opt/northstar/northstar_bundle_3.2.0
[root@Juniper-C northstar_bundle_3.2.0]# ./install.sh

Checking current disk space

INFO: Current available disk space for /opt/northstar is 
11%. Will proceed with installation.


This script will install Juniper Northstar Controller Packages
This script may require access to standard Centos Repository to download any missing third party packages

Continue Install Northstar (Y/n)? y

Step 1: Verifying if the Network Manager daemon is running .....
-------------------------------------------------------------------------------------
Network Manager is disabled (OK)



Step 2: Verifying if external0 and mgmt0 bridge interfaces have been configured .....
-------------------------------------------------------------------------------------
external0: error fetching interface information: Device not found
bridge: external0 is not configured. Please configure external0 bridge before continue.


Here are the example of the external0 bridge configuration:
  - The following example assume that the interface name for router facing connection is "eth0"
    Please adjust any "eth0" with your actual interface name
  - Create/modify /etc/sysconfig/network-scripts/ifcfg-eth0 with the following content:
      DEVICE=eth0
      ONBOOT=yes
      BRIDGE=external0
  - Create/modify /etc/sysconfig/network-scripts/ifcfg-external0 with the following content:
      DEVICE=external0
      BOOTPROTO=static
      IPADDR=172.25.152.171  <please adjust with your actual IP>
      NETMASK=255.255.254.0  <please adjust with your actual netmask>
      IPV6INIT=no
      NM_CONTROLLED=no
      ONBOOT=yes
      TYPE=Bridge
      STP=off
      DELAY=0
  - Reboot the server or run the following to apply the changes:
      brctl addbr external0
      service network restart

[root@Juniper-C northstar_bundle_3.2.0]# 

[root@juniper-c northstar_bundle_3.2.0]# nano /etc/sysconfig/network-scripts/ifcfg-external0
DEVICE=external0
      BOOTPROTO=static
      IPADDR=10.21.0.182  
      NETMASK=255.255.255.0 
      IPV6INIT=no
      NM_CONTROLLED=no
      ONBOOT=yes
      TYPE=Bridge
      STP=off
      DELAY=0
ctrl+X 

[root@juniper-c northstar_bundle_3.2.0]# brctl addbr external0
[root@juniper-c northstar_bundle_3.2.0]# service network restart
Please wait 60 seconds
............................................................

Please enter new DB and MQ password (at least one digit, one lower case, one uppercase and no space) :Juniper@123
Please enter new UI Admin password :Juniper@cisco
Changing UI Admin password ...

ERROR: KVM is not supported, NorthStar-JunosVM is not installed



---------------------------------------------------------------------------------------------------------------
 
Installation script is done.

To complete the installation setup, you MUST perform the following:
 
A) Enable the NorthStar license
 
  1. Copy or move the license file to file: /opt/pcs/db/sys/npatpw
  2. Set the license file owner to the pcs user. 
     - Run command: chown pcs:pcs /opt/pcs/db/sys/npatpw
  3. Restart all the NorthStar processes. 
     - Run command: service northstar restart
  4. Wait until all the processes are up and running. 
     - This may take at least 3 minutes to start all processes.
     - To check their status, run command: service northstar status
 
B) Adjust firewall policies
 
  1. CentOS default iptables rules may prevent NorthStar related traffic
  2. Please refer to Getting Started guide for the ports that need to be allowed by iptables and firewall.
  3. Sample of iptables rules is available in /opt/northstar/utils/firewall.sh
 
C) Configure the interfaces on the JUNOS VM or Host
 
  1. Launch the Net Setup utility. Run command: net_setup.py
     - Please make sure JunOS VM is up before configuring it
        - To check: ping 172.16.16.2
  
The NorthStar web client can be accessed at: https://<this-server-ip>:8443

For high availability setup:

If this server is part of a HA cluster, please make sure following

1) SSH key-based authentication is needed for root login to all servers and to northstar login of all Junos VMs. 
2) All server time should be sync'ed by ntp.
3) The Database and RabbitMQ password are consistent between every member server.

--------------------------------------------------------------------------------------------------------------



[root@juniper-c northstar_bundle_3.2.0]# 
[root@juniper-c northstar_bundle_3.2.0]# service iptables stop
iptables: Setting chains to policy ACCEPT: filter          [  OK  ]
iptables: Flushing firewall rules:                         [  OK  ]
iptables: Unloading modules:                               [  OK  ]
[root@juniper-c northstar_bundle_3.2.0]# 