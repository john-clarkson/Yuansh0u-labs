ezvpn server:  
 dynamic crypto map configuration:

 SITE-A:

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
 pool EZVPN-POOL
 acl SPLIT-TUNNEL-ACL
 backup-gateway 61.128.1.1
 banner ^CHIS IS EZVPN_SERVER_SI^C


crypto ipsec transform-set EZVPN esp-3des esp-sha-hmac
 mode tunnel
!
crypto dynamic-map EZVPN-DYNAMIC-MAP 1
 set transform-set EZVPN 
 reverse-route
! 
crypto map EZVPN-STATIC-MAP client authentication list EZVPN
crypto map EZVPN-STATIC-MAP isakmp authorization list EZVPN
crypto map EZVPN-STATIC-MAP client configuration address respond
crypto map EZVPN-STATIC-MAP 1 ipsec-isakmp dynamic EZVPN-DYNAMIC-MAP
!

ip access-list extended SPLIT-TUNNEL-ACL
 permit ip host 172.172.172.172 any
!
inter f0/0
 crypto map EZVPN-STATIC-MAP


============
 SITE-B:
 
no username cisco password cisco
username testpc1 password testpc1
username testpc2 password testpc2
ip local pool EZVPN-POOL 172.16.254.1 172.16.254.254

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
 pool EZVPN-POOL
 acl SPLIT-TUNNEL-ACL
 backup-gateway 202.100.1.1
 banner ^CHIS IS EZVPN_SERVER_SI^C


crypto ipsec transform-set EZVPN esp-3des esp-sha-hmac
 mode tunnel
!
crypto dynamic-map EZVPN-DYNAMIC-MAP 1
 set transform-set EZVPN 
 reverse-route
! 
crypto map EZVPN-STATIC-MAP client authentication list EZVPN
crypto map EZVPN-STATIC-MAP isakmp authorization list EZVPN
crypto map EZVPN-STATIC-MAP client configuration address respond
crypto map EZVPN-STATIC-MAP 1 ipsec-isakmp dynamic EZVPN-DYNAMIC-MAP
!

ip access-list extended SPLIT-TUNNEL-ACL
 permit ip host 172.172.172.172 any
!
inter f0/0
 crypto map EZVPN-STATIC-MAP 

===============================================================
ezvpn server:  
 DVTI configuration:
SITE-A:
ip local pool GLOBAL-EZVPN-USER 172.255.255.1 172.255.255.254
!
crypto isakmp client configuration group global
 key cisco
 dns 8.8.4.4 8.8.8.8
 pool GLOBAL-EZVPN-USER
 save-password
 backup-gateway 61.128.1.1
 netmask 255.255.255.0
 banner ^CGLOBAL-INET^C
 !
crypto isakmp profile EZVPN-DVTI
  match identity group global
  client authentication list EZVPN
  isakmp authorization list EZVPN
  client configuration address respond
  virtual-template 1
!
crypto ipsec transform-set EZVPN esp-3des esp-sha-hmac
 mode tunnel
crypto ipsec profile GLOBAL-EZVPN
set transform-set EZVPN
!
interface Virtual-Template1 type tunnel
ip unnumbered loopback 0
ip nat inside
tunnel mode ipsec ipv4
tunnel protection ipsec profile GLOBAL-EZVPN
!
SITE-B:
ip local pool GLOBAL-EZVPN-USER 172.255.255.1 172.255.255.254
!
crypto isakmp client configuration group global
 key cisco
 dns 8.8.4.4 8.8.8.8
 pool GLOBAL-EZVPN-USER
 save-password
 backup-gateway 202.100.1.1
 netmask 255.255.255.0
 banner ^CGLOBAL-INET^C
 !
crypto isakmp profile EZVPN-DVTI
  match identity group global
  client authentication list EZVPN
  isakmp authorization list EZVPN
  client configuration address respond
  virtual-template 1
!
crypto ipsec transform-set EZVPN esp-3des esp-sha-hmac
 mode tunnel
crypto ipsec profile GLOBAL-EZVPN
set transform-set EZVPN
!
interface Virtual-Template1 type tunnel
ip unnumbered loopback 0
ip nat inside
tunnel mode ipsec ipv4
tunnel protection ipsec profile GLOBAL-EZVPN
!
