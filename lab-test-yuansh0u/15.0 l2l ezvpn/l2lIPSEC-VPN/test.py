no username cisco password cisco
username testpc1 password testpc1
username testpc2 password testpc2
ip local pool EZVPN-POOL 172.16.255.1 172.16.255.254

aaa new-model
aaa authentication login CONSOLE line none
aaa authentication login EZVPN group radius local
aaa authorization network EZVPN group radius local
!
crypto isakmp policy 100
 hash md5
 authentication pre-share
 group 2
 en des

crypto isakmp client configuration group ezvpn
 key cisco
 dns 8.8.4.4 8.8.8.8
 backup-gateway 202.200.1.1
 pool EZVPN-POOL
 acl SPLIT-TUNNEL-ACL
 


crypto ipsec transform-set VPN esp-3des esp-sha-hmac
 mode tunnel
!
crypto dynamic-map EZVPN-DYNAMIC-MAP 1
 set transform-set VPN 
 reverse-route
! 
crypto map VPN1 client authentication list EZVPN
crypto map VPN1 isakmp authorization list EZVPN
crypto map VPN1 client configuration address respond
crypto map VPN1 1 ipsec-isakmp dynamic EZVPN-DYNAMIC-MAP
!

ip access-list extended SPLIT-TUNNEL-ACL
 permit ip host 172.172.172.172 any


crypto isakmp client configuration group ezvpn2
 key cisco
 dns 8.8.4.4 8.8.8.8
 backup-gateway 202.100.1.1
 pool EZVPN-POOL
 acl SPLIT-TUNNEL-ACL

 crypto map VPN2 client authentication list EZVPN
crypto map VPN2 isakmp authorization list EZVPN
crypto map VPN2 client configuration address respond
crypto map VPN2 1 ipsec-isakmp dynamic EZVPN-DYNAMIC-MAP
================================================================= 


crypto isakmp profile VPN2
   keyring VPN
   match identity address 61.128.1.1 255.255.255.255 
   local-address FastEthernet0/1
crypto map VPN2 10 ipsec-isakmp 
 set peer 61.128.1.1
 set transform-set VPN 
 match address PROXY-ACL
 reverse-route static

R2:
crypto isakmp policy 100
 hash md5
 authentication pre-share
 group 2
 en des
! 
crypto keyring VPN 
  pre-shared-key address 202.100.1.1 key VPN
  pre-shared-key address 202.200.1.1 key VPN
!
crypto isakmp policy 100
 hash md5
 authentication pre-share
 group 2
crypto isakmp keepalive 10 periodic
crypto isakmp profile VPN
   keyring VPN
   match identity address 202.100.1.1 255.255.255.255
   match identity address 202.200.1.1 255.255.255.255  
  
!
!
crypto ipsec transform-set VPN esp-3des esp-sha-hmac 
!
crypto map VPN1 10 ipsec-isakmp 
 set peer 202.100.1.1
 set peer 202.200.1.1
 set transform-set VPN 
 match address PROXY-ACL
 reverse-route static