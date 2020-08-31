windows IP address setting: 
eth0 150.1.14.1 255.255.0.0 for management without gateway.
eth1 192.168.14.1 255.255.255.0 gateway.254 for EVE bridging(pnet2) with CISCO ISE server.
domain name: hitler.com
windows server name: hitler



##windows Active directory setting


##windows DNS server


##windows DHCP server

## AAA IOS devices configuration
## radius server is cisco ise 2.2

Router#sh running-config 
Building configuration...

Current configuration : 1147 bytes
!
! Last configuration change at 22:33:40 UTC Tue Oct 31 2017
!
version 15.2
no service timestamps debug datetime msec
no service timestamps log datetime msec
!
hostname Router
!
enable password cisco
!##enable aaa
aaa new-model 
!##Create line console without authentication,this is very inportant, if you don't set this, 
!##you will lose the management privilege by using console. and you must be careful with this!!! 
aaa authentication login CONSOLE none
!##create authentication policy by using radius first, if failed, then do local authentication. 
aaa authentication login default group radius local
!##create authorization policy
aaa authorization exec default group radius local if-authenticated 
!##this is local database, if radius server is alive then IOS will not check local database.        
username cisco privilege 15 password 0 cisco
!##for testing!!!
interface Loopback0
 ip address 1.1.1.1 255.255.255.255
!
interface FastEthernet0/0
 ip address 192.168.55.254 255.255.255.0
!##this is source-interface radius packet will be used for AAA.
ip radius source-interface FastEthernet0/0 
!##radius server settings,who is radius,password,and retry timer
radius server ISE
 address ipv4 192.168.55.1 auth-port 1645 acct-port 1646
 timeout 2
 key cisco
!##this task must do first before you do AAA!!! 
!##unless radius server already have authentication policy and you know the account, if you don't please do it first!!      
line con 0
 login authentication CONSOLE
line aux 0
 stopbits 1
line vty 0 4
!##this commands is hidden in <show runn> by default.
login authentication default
end
Router# 

##you can set authentication policy with <async> for console and <virtual> for vty.