Topology design

##------>Default route            INET ROUTER                   <-------Default route     
                        |                                     |     
CLIENT-1-g1 100.1.1.1/24|<----100.1.1.254-219.235.230.254---->|CA g1 219.235.230.1/24
                        |                                     |  
CLIENT-2-g1 200.1.1.1/24|<----200.1.1.254
## Loopback Assigned
CLIENT-1: loopback0 10.1.1.1/32
CLIENT-2: loopback0 10.2.2.2/32


NTP server
 CA#sh run | sec ntp
ntp source GigabitEthernet1
ntp master
CA#

NTP CLIENT
CLIENT#sh run | sec ntp
ntp peer 219.235.230.1 source GigabitEthernet1

##check ntp status
IPSEC-CE2#show ntp status 
Clock is synchronized, stratum 9, reference is 219.235.230.1  
nominal freq is 250.0000 Hz, actual freq is 249.9884 Hz, precision is 2**10
ntp uptime is 657300 (1/100 of seconds), resolution is 4016
reference time is DCE30EE0.B1A9FDD0 (23:46:40.694 UTC Wed Jun 7 2017)
clock offset is -112.0000 msec, root delay is 24.00 msec
root dispersion is 106.12 msec, peer dispersion is 4.61 msec
loopfilter state is 'CTRL' (Normal Controlled Loop), drift is 0.000046261 s/s
system poll interval is 256, last update was 1261 sec ago.
IPSEC-CE2#


PKI: 
!##server configuration:
enable 
 config ter
ip domain name hitler.com
crypto pki server ROOT_CA
 no database archive
 issuer-name CN=CA.hitler.com
 grant auto
 hash sha512
 no shutdown
!##password: cisco123
enter password:
 Re-enter password: 

CLIENT configuration:
 !##generate rsa KEY
enable
 config ter
crypto key generate rsa label PKI
% You already have RSA keys defined named PKI.
% Do you really want to replace them? [yes/no]: yes
Choose the size of the key modulus in the range of 360 to 4096 for your
  General Purpose Keys. Choosing a key modulus greater than 512 may take
  a few minutes.

How many bits in the modulus [512]: 
Jun  7 23:43:45.580: %RF_ISSU-3-INVALID_SESSION: RF ISSU CLIENT on domain (0) does not have a valid registered session.
Jun  7 23:43:45.590: %SSH-5-DISABLED: SSH 2.0 has been disabled1024
% Generating 1024 bit RSA keys, keys will be non-exportable...
[OK] (elapsed time was 0 seconds)

crypto pki trustpoint CA
 enrollment url http://219.235.230.1:80
 revocation-check none
crypto pki certificate chain CA
rsakeypair PKI

IPSEC-CE2(config)#crypto pki authenticate CA
Certificate has the following attributes:
       Fingerprint MD5: 7C96FE82 21406DC1 91ADDEB0 C8948B44 
      Fingerprint SHA1: 89D35AB9 D3F6BE58 0BD257AD 91BF0BBB C3036CA3 

% Do you accept this certificate? [yes/no]: yes
Trustpoint CA certificate accepted.

IPSEC-CE2(config)#crypto pki enroll CA
%
% Start certificate enrollment .. 
% Create a challenge password. You will need to verbally provide this
   password to the CA Administrator in order to revoke your certificate.
   For security reasons your password will not be saved in the configuration.
   Please make a note of it.

Password: 
Re-enter password: 

% The subject name in the certificate will include: IPSEC-CE2
% Include the router serial number in the subject name? [yes/no]: yes
% The serial number in the certificate will be: 9XVYC51FMT6
% Include an IP address in the subject name? [no]: yes
Enter Interface name or IP Address[]: 100.1.1.1
Request certificate from CA? [yes/no]: yes
% Certificate request sent to Certificate Authority
% The 'show crypto pki certificate verbose CA' commandwill show the fingerprint.


CLIENT#show crypto pki certificates 
Certificate
  Status: Available
  Certificate Serial Number (hex): 02
  Certificate Usage: General Purpose
  Issuer: 
    cn=CA.hitler.com
  Subject:
    Name: CLIENT
    IP Address: 200.1.1.1
    Serial Number: 98S8FAWRFAQ
    serialNumber=98S8FAWRFAQ+hostname=CLIENT+ipaddress=200.1.1.1
  Validity Date: 
    start date: 23:56:42 UTC Jun 7 2017
    end   date: 23:56:42 UTC Jun 7 2018
  Associated Trustpoints: CA 
  Storage: nvram:CAhitlercom#2.cer

CA Certificate
  Status: Available
  Certificate Serial Number (hex): 01
  Certificate Usage: Signature
  Issuer: 
    cn=CA.hitler.com
  Subject: 
    cn=CA.hitler.com
  Validity Date: 
    start date: 22:32:55 UTC Jun 7 2017
    end   date: 22:32:55 UTC Jun 6 2020
  Associated Trustpoints: CA 
  Storage: nvram:CAhitlercom#1CA.cer
!##
CLIENT#show  crypto key mypubkey rsa
% Key pair was generated at: 23:43:49 UTC Jun 7 2017
Key name: PKI
Key type: RSA KEYS
 Storage Device: not specified
 ## Usage: General Purpose Key
 Key is not exportable. Redundancy enabled.
 Key Data:
  30819F30 0D06092A 864886F7 0D010101 05000381 8D003081 89028181 00E42D6F 
  072A5386 7FA21A58 46FD51EA 0B03C355 07213D0B 7A1551DB E76DD0B7 F9AD82EF 
  93CA671A 70F66CD8 3922BFB3 FE89E403 DE2F7065 E3CF4BA7 B606AF42 9C118F7D 
  EF09AB46 2C48573F A5A048B3 EFE01648 4B71A841 D8DCB08B 5E55E5A2 F8629D3A 
  95F56C23 8506305C 0A3D67CE 63A09FB1 8C092031 2B2EF76A 4D956EF0 D1020301 
  0001
% Key pair was generated at: 23:43:49 UTC Jun 7 2017
Key name: PKI.server
Key type: RSA KEYS
Temporary key
 Usage: Encryption Key
 Key is not exportable.
 Key Data:
  307C300D 06092A86 4886F70D 01010105 00036B00 30680261 00E63341 26F65C9F 
  E0C5F51A 1BAA4578 DA6C6264 AEF56982 A045F9D0 0BB4634C 57D376F0 617B3E2D 
  C7638F58 75203176 EA934DB8 803B6506 3043A148 9E4A353C DD5C5702 C34E3203 
  73011C52 61719A67 BD7A406A 9756A2B4 8A1E54BF 3ECF5CF8 BB020301 0001
## GRE OVER IPSEC DYNAMIC IPSEC IKEV1 VPN
## Client configuration
  
enable 
 config ter
 hostname CLIENT 
!## proxy acl defined encryte traffic use IPSEC-VPN TUNNELs
!## source is loopback 0,destination is remote site's loopback 0.

ip access-list extended PROXY-ACL
 permit ip host 10.1.1.1 host 10.2.2.2

crypto isakmp policy 1
 encr 3des
 group 2
 !## rsa-sig is default option, show run do not see it.  
 authentication rsa-sig
crypto isakmp keepalive 10 5
crypto isakmp profile UK
   !## if we use pre-shared-key to authenticate neighbor,self-identity fqdn is the same fuction as 
   !##  crypto isakmp identity hostname (ike message 5)
   self-identity fqdn
   match identity address 100.1.1.1 255.255.255.255 
   keepalive 10 retry 5
   initiate mode aggressive
!         
!         
crypto ipsec transform-set UK esp-null esp-md5-hmac 
 mode tunnel
 !
crypto map P2P-GRE 10 ipsec-isakmp 
 set peer 100.1.1.1
 set transform-set UK 
 set isakmp-profile UK
match address PROXY-ACL
interface Loopback0
 ip address 10.1.1.1 255.255.255.255
!         
interface Tunnel0
 description BGP-CONNECTION
 ip address 100.64.2.1 255.255.255.252
 ip mtu 1400
 ip nat outside
 ip tcp adjust-mss 1360
 tunnel source 10.1.1.1
 tunnel destination 10.2.2.2
!         
interface GigabitEthernet1
 ip address 200.1.1.1 255.255.255.0
 negotiation auto
 crypto map P2P-GRE


CLIENT#show crypto isakmp policy 

Global IKE policy
Protection suite of priority 1
        encryption algorithm:   Three key triple DES
        hash algorithm:         Secure Hash Standard
        authentication method:  Rivest-Shamir-Adleman Signature
        Diffie-Hellman group:   #2 (1024 bit)
        lifetime:               86400 seconds, no volume limit
CLIENT#

##IPSEC-GW configuraiton
crypto isakmp policy 10
 encr 3des
 group 2  
 lifetime 6000
crypto isakmp profile CLIENT
   keyring RA
   match identity host CLIENT
   initiate mode aggressive
!         
!         
crypto ipsec transform-set PHASE-2 esp-null esp-md5-hmac 
 mode tunnel
!         
!         
!         
crypto dynamic-map DMAP 1
 set transform-set PHASE-2 
 set isakmp-profile CLIENT
 reverse-route remote-peer 100.1.1.254
!         
!         
crypto map SMAP local-address GigabitEthernet1
crypto map SMAP 100 ipsec-isakmp dynamic DMAP 
!              
interface Loopback0
 ip address 10.2.2.2 255.255.255.255
!         
interface Tunnel2
 description CE-C1921-SEC/K9
 ip address 100.64.2.2 255.255.255.252
 ip mtu 1400
 ip tcp adjust-mss 1360
 tunnel source 10.2.2.2
 tunnel destination 10.1.1.1
!         
interface GigabitEthernet1
 ip address 100.1.1.1 255.255.255.0
 negotiation auto
 crypto map SMAP

## Verify 
CLIENT#ping 10.2.2.2 sou lo0
Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 10.2.2.2, timeout is 2 seconds:
Packet sent with a source address of 10.1.1.1 
.!!!!
Success rate is 80 percent (4/5), round-trip min/avg/max = 9/10/13 ms
CLIENT#
CLIENT#show cry isa sa
IPv4 Crypto ISAKMP SA
dst             src             state          conn-id status
100.1.1.1       200.1.1.1       QM_IDLE           1012 ACTIVE

IPv6 Crypto ISAKMP SA

CLIENT#


















