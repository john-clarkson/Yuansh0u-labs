IPV4

crypto keyring DMVPN-KEYRING 
  pre-shared-key address 0.0.0.0 0.0.0.0 key MOTHERFUCKERS
!
crypto isakmp policy 10
 encr aes 256
 authentication pre-share
 group 2
crypto isakmp profile DMVPN-PHASE3
   keyring DMVPN-KEYRING
   match identity address 0.0.0.0 
!
crypto ipsec security-association replay window-size 1024
!
crypto ipsec transform-set ESP/NULL/MD5/TUNNEL esp-null esp-sha-hmac 
 mode transport
!
crypto ipsec profile DMVPN-PROFILE
 set transform-set ESP/NULL/MD5/TUNNEL 
 set isakmp-profile DMVPN-PHASE3
 !
 interface tunnel x
   tunnel protection ipsec profile DMVPN-PROFILE


