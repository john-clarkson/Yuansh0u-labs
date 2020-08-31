
crypto isakmp client configuration group global
 key cisco
 dns 8.8.4.4 8.8.8.8
 pool EZVPN-POOL
 acl SPLIT-TUNNEL-ACL
 save-password
 no backup-gateway 61.128.1.1
 netmask 255.255.255.0




ip sla 1
 icmp-echo 202.100.1.254 source-interface FastEthernet0/0
ip sla schedule 1 life forever start-time now
ip sla 2
 icmp-echo 112.1.1.254 source-interface FastEthernet2/0
ip sla schedule 2 life forever start-time now

track 1 ip sla 1 reachability
!
track 2 ip sla 2 reachability

SITE_A
ip route 0.0.0.0 0.0.0.0 202.100.1.254 name DUAL-STACK-INET-IPV4-PRIMARY-PATH track 1
ip route 0.0.0.0 0.0.0.0 112.1.1.254 100 permanent name DUAL-STACK-INET-IPV4-SECONDARY-PATH 
ip route 150.150.2.0 255.255.255.0 112.1.1.254 name DUAL-STACK-INET-IPV4-SECONDARY-PATH-L2LVPN track 2

SITE_B
ip route 0.0.0.0 0.0.0.0 61.128.1.254 name DUAL-STACK-INET-IPV4-PRIMARY-PATH track 1
ip route 0.0.0.0 0.0.0.0 113.1.1.254 100 permanent name DUAL-STACK-INET-IPV4-SECONDARY-PATH 
ip route 150.150.1.0 255.255.255.0 113.1.1.254 name DUAL-STACK-INET-IPV4-SECONDARY-PATH-L2LVPN track 2

L2L VPN:
 SITE_A
crypto keyring SITE_TO_SITE_VPN  
  pre-shared-key address 113.1.1.1 key ASSHOLE

ip access-list extended NAT
 deny   ip 150.150.1.0 0.0.0.255 150.150.2.0 0.0.0.255
 permit ip 150.150.1.0 0.0.0.255 any
ip access-list extended PROXY-ACL
 permit ip 150.150.1.0 0.0.0.255 150.150.2.0 0.0.0.255

crypto keyring SITE_TO_SITE_VPN  
  pre-shared-key address 113.1.1.1 key ASSHOLE

crypto isakmp profile SITE_TO_SITE_VPN
   keyring SITE_TO_SITE_VPN
   match identity address 113.1.1.1 255.255.255.255   

crypto ipsec transform-set AES256/SHA/TUNNEL/L2L esp-aes 256 esp-sha-hmac 
 mode tunnel

crypto map EZVPN-STATIC-MAP 19 ipsec-isakmp
 set peer 113.1.1.1
 set transform-set AES256/SHA/TUNNEL/L2L 
 set isakmp-profile SITE_TO_SITE_VPN
 match address PROXY-ACL

crypto map SITE_TO_SITE 10 ipsec-isakmp 
 set peer 113.1.1.1
 set transform-set AES256/SHA/TUNNEL/L2L 
 set isakmp-profile SITE_TO_SITE_VPN
 match address PROXY-ACL

  inter f0/0
   crypto map EZVPN-STATIC-MAP
 inter f2/0
   crypto map EZVPN-STATIC-MAP
==============================================================
 SITE_B
crypto keyring SITE_TO_SITE_VPN  
  pre-shared-key address 112.1.1.1 key ASSHOLE
  pre-shared-key address 202.100.1.1 key ASSHOLE

ip access-list extended NAT
 deny   ip 150.150.2.0 0.0.0.255 150.150.1.0 0.0.0.255
 permit ip 150.150.2.0 0.0.0.255 any
ip access-list extended PROXY-ACL
 permit ip 150.150.2.0 0.0.0.255 150.150.1.0 0.0.0.255

crypto keyring SITE_TO_SITE_VPN  
  pre-shared-key address 112.1.1.1 key ASSHOLE


crypto isakmp profile SITE_TO_SITE_VPN1
   keyring SITE_TO_SITE_VPN
   match identity address 112.1.1.1 255.255.255.255 
crypto isakmp profile SITE_TO_SITE_VPN2
   keyring SITE_TO_SITE_VPN
   match identity address 202.100.1.1  255.255.255.255      

crypto ipsec transform-set AES256/SHA/TUNNEL/L2L esp-aes 256 esp-sha-hmac 
 mode tunnel

crypto map SITE_TO_SITE 10 ipsec-isakmp 
 set peer 112.1.1.1
 set transform-set AES256/SHA/TUNNEL/L2L 
 set isakmp-profile SITE_TO_SITE_VPN1
 match address PROXY-ACL
  inter f2/0
   crypto map SITE_TO_SITE

crypto map SITE_TO_SITE 20 ipsec-isakmp 
 set peer 202.100.1.1 
 set transform-set AES256/SHA/TUNNEL/L2L 
 set isakmp-profile SITE_TO_SITE_VPN2
 match address PROXY-ACL
  inter f0/0
   crypto map SITE_TO_SITE   
 ===========================================================
 DUAL-HOMED-NAT


route-map DUAL-STACK-INET-IPV4-PRIMARY-PATH permit 10
 match ip address NAT
 match interface f0/0
!
route-map DUAL-STACK-INET-IPV4-SECONDARY-PATH permit 10
 match ip address NAT
 match interface FastEthernet2/0

ip nat inside source route-map DUAL-STACK-INET-IPV4-PRIMARY-PATH interface f0/0 overload
ip nat inside source route-map DUAL-STACK-INET-IPV4-SECONDARY-PATH interface FastEthernet2/0 overload   