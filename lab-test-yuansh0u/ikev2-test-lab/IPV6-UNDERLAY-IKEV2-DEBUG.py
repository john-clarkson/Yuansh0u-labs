IKEv2:(SESSION ID = 31,SA ID = 1):Deleting SA
XE-R4#
XE-R4#
XE-R4#
XE-R4#
XE-R4#CONF
Configuring from terminal, memory, or network [terminal]? 
Enter configuration commands, one per line.  End with CNTL/Z.
XE-R4(config)#
*May  2 16:05:33.248: %SYS-5-CONFIG_I: Configured from console by cisco on vty1 (150.1.1.253)
XE-R4(config)#INT TUNNEL 46
XE-R4(config-if)#SHUT
XE-R4(config-if)#
*May  2 16:05:37.450: %CRYPTO-6-ISAKMP_ON_OFF: ISAKMP is OFFno shut
XE-R4(config-if)#
*May  2 16:05:39.439: %LINEPROTO-5-UPDOWN: Line protocol on Interface Tunnel46, changed state to down
*May  2 16:05:39.440: %LINK-5-CHANGED: Interface Tunnel46, changed state to administratively down
*May  2 16:05:40.456: %CRYPTO-6-ISAKMP_ON_OFF: ISAKMP is ON
IKEv2:% Getting preshared key from profile keyring IKEV2-KEYRING
IKEv2:% Matched peer block 'ANY-IPV6'
IKEv2:Searching Policy with fvrf 0, local address FC00:123:123:123::2
IKEv2:Using the Default Policy for Proposal
IKEv2:Found Policy 'default'
IKEv2:(SESSION ID = 31,SA ID = 1):[IKEv2 -> Crypto Engine] Computing DH public key, DH Group 5
IKEv2:(SA ID = 1):[Crypto Engine -> IKEv2] DH key Computation PASSED
IKEv2:(SESSION ID = 31,SA ID = 1):Request queued for computation of DH key
IKEv2:IKEv2 initiator - no config data to send in IKE_SA_INIT exch
IKEv2:(SESSION ID = 31,SA ID = 1):Generating IKE_SA_INIT message
IKEv2:(SESSION ID = 31,SA ID = 1):IKE Proposal: 1, SPI size: 0 (initial negotiation), 
Num. transforms: 15
   AES-CBC   AES-CBC   AES-CBC   SHA512   SHA384   SHA256   SHA1   MD5   SHA512   SHA384   SHA256   SHA96   MD596   DH_GROUP_1536_MODP/Group 5   DH_GROUP_1024_MODP/Group 2 

IKEv2:(SESSION ID = 31,SA ID = 1):Sending Packet [To FC00:123:123:123::1:500/From FC00:123:123:123::2:500/VRF i0:f0] 
Initiator SPI : 1D418169B24BF95A - Responder SPI : 0000000000000000 Message id: 0
IKEv2 IKE_SA_INIT Exchange REQUEST 
Payload contents: 
 SA KE N VID VID VID VID NOTIFY(NAT_DETECTION_SOURCE_IP) NOTIFY(NAT_DETECTION_DESTINATION_IP) 

IKEv2:(SESSION ID = 31,SA ID = 1):Insert SA 

IKEv2:(SESSION ID = 31,SA ID = 1):Received Packet [From FC00:123:123:123::1:500/To FC00:123:123:123::2:500/VRF i0:f0] 
Initiator SPI : 1D418169B24BF95A - Responder SPI : A645046F734260C6 Message id: 0
IKEv2 IKE_SA_INIT Exchange RESPONSE 
Payload contents: 
 SA KE N VID VID VID VID NOTIFY(NAT_DETECTION_SOURCE_IP) NOTIFY(NAT_DETECTION_DESTINATION_IP) 

IKEv2:(SESSION ID = 31,SA ID = 1):Processing IKE_SA_INIT message
IKEv2:(SESSION ID = 31,SA ID = 1):Verify SA init message
IKEv2:(SESSION ID = 31,SA ID = 1):Processing IKE_SA_INIT message
IKEv2:(SESSION ID = 31,SA ID = 1):Checking NAT discovery
IKEv2:(SESSION ID = 31,SA ID = 1):NAT not found
IKEv2:(SESSION ID = 31,SA ID = 1):[IKEv2 -> Crypto Engine] Computing DH secret key, DH Group 5
IKEv2:(SA ID = 1):[Crypto Engine -> IKEv2] DH key Computation PASSED
IKEv2:(SESSION ID = 31,SA ID = 1):Request queued for computation of DH secret
IKEv2:(SA ID = 1):[IKEv2 -> Crypto Engine] Calculate SKEYSEED and create rekeyed IKEv2 SA
IKEv2:(SA ID = 1):[Crypto Engine -> IKEv2] SKEYSEED calculation and creation of rekeyed IKEv2 SA PASSED
IKEv2:(SESSION ID = 31,SA ID = 1):Completed SA init exchange
IKEv2:Config data to send:
IKEv2:(SESSION ID = 31,SA ID = 1):Config-type: Config-request 
IKEv2:(SESSION ID = 31,SA ID = 1):Attrib type: app-version, length: 257, data: Cisco IOS Software [Fuji], Virtual XE Software (X86_64_LINUX_IOSD-UNIVERSALK9-M), Version 16.7.1, RELEASE SOFTWARE (fc6)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2017 by Cisco Systems, Inc.
Compiled Mon 20-Nov-17 18:57 by mcpre
IKEv2:(SESSION ID = 31,SA ID = 1):Attrib type: split-dns, length: 0
IKEv2:(SESSION ID = 31,SA ID = 1):Attrib type: banner, length: 0
IKEv2:(SESSION ID = 31,SA ID = 1):Attrib type: config-url, length: 0
IKEv2:(SESSION ID = 31,SA ID = 1):Attrib type: backup-gateway, length: 0
IKEv2:(SESSION ID = 31,SA ID = 1):Attrib type: def-domain, length: 0
IKEv2:(SESSION ID = 31,SA ID = 1):Have config mode data to send
IKEv2:(SESSION ID = 31,SA ID = 1):Check for EAP exchange
IKEv2:(SESSION ID = 31,SA ID = 1):Generate my authentication data
IKEv2:(SESSION ID = 31,SA ID = 1):Use preshared key for id FC00:123:123:123::2, key len 8
IKEv2:[IKEv2 -> Crypto Engine] Generate IKEv2 authentication data
IKEv2:[Crypto Engine -> IKEv2] IKEv2 authentication data generation PASSED
IKEv2:(SESSION ID = 31,SA ID = 1):Get my authentication method
IKEv2:(SESSION ID = 31,SA ID = 1):My authentication method is 'PSK'
IKEv2:(SESSION ID = 31,SA ID = 1):Check for EAP exchange
IKEv2:(SESSION ID = 31,SA ID = 1):Generating IKE_AUTH message
IKEv2:(SESSION ID = 31,SA ID = 1):Constructing IDi payload: 'FC00:123:123:123::2' of type 'IPv6 address'
IKEv2:(SESSION ID = 31,SA ID = 1):ESP Proposal: 1, SPI size: 4 (IPSec negotiation), 
Num. transforms: 3
   AES-CBC   SHA96   Don't use ESN
IKEv2:(SESSION ID = 31,SA ID = 1):Building packet for encryption.  
Payload contents: 
 VID IDi AUTH CFG SA TSi TSr NOTIFY(INITIAL_CONTACT) NOTIFY(USE_TRANSPORT_MODE) NOTIFY(SET_WINDOW_SIZE) NOTIFY(ESP_TFC_NO_SUPPORT) NOTIFY(NON_FIRST_FRAGS) 

IKEv2:(SESSION ID = 31,SA ID = 1):Sending Packet [To FC00:123:123:123::1:500/From FC00:123:123:123::2:500/VRF i0:f0] 
Initiator SPI : 1D418169B24BF95A - Responder SPI : A645046F734260C6 Message id: 1
IKEv2 IKE_AUTH Exchange REQUEST 
Payload contents: 
 ENCR 
 

IKEv2:(SESSION ID = 31,SA ID = 1):Received Packet [From FC00:123:123:123::1:500/To FC00:123:123:123::2:500/VRF i0:f0] 
Initiator SPI : 1D418169B24BF95A - Responder SPI : A645046F734260C6 Message id: 1
IKEv2 IKE_AUTH Exchange RESPONSE 
Payload contents: 
 VID IDr AUTH NOTIFY(NO_PROPOSAL_CHOSEN) 

IKEv2:(SESSION ID = 31,SA ID = 1):Process auth response notify
IKEv2-ERROR:(SESSION ID = 31,SA ID = 1):
IKEv2:(SESSION ID = 31,SA ID = 1):Searching policy based on peer's identity 'FC00:123:123:123::1' of type 'IPv6 address'
IKEv2:Searching Policy with fvrf 0, local address FC00:123:123:123::2
IKEv2:Using the Default Policy for Proposal
IKEv2:Found Policy 'default'
IKEv2:(SESSION ID = 31,SA ID = 1):Verify peer's policy
IKEv2:(SESSION ID = 31,SA ID = 1):Peer's policy verified
IKEv2:(SESSION ID = 31,SA ID = 1):Get peer's authentication method
IKEv2:(SESSION ID = 31,SA ID = 1):Peer's authentication method is 'PSK'
IKEv2:(SESSION ID = 31,SA ID = 1):Get peer's preshared key for FC00:123:123:123::1
IKEv2:(SESSION ID = 31,SA ID = 1):Verify peer's authentication data
IKEv2:(SESSION ID = 31,SA ID = 1):Use preshared key for id FC00:123:123:123::1, key len 8
IKEv2:[IKEv2 -> Crypto Engine] Generate IKEv2 authentication data
IKEv2:[Crypto Engine -> IKEv2] IKEv2 authentication data generation PASSED
IKEv2:(SESSION ID = 31,SA ID = 1):Verification of peer's authenctication data PASSED
IKEv2:(SESSION ID = 31,SA ID = 1):Check for EAP exchange
IKEv2:(SESSION ID = 31,SA ID = 1):IKEV2 SA created; inserting SA into database. SA lifetime timer (86400 sec) started
IKEv2:(SESSION ID = 31,SA ID = 1):Session with IKE ID PAIR (FC00:123:123:123::1, FC00:123:123:123::2) is UP
IKEv2:IKEv2 MIB tunnel started, tunnel index 1
IKEv2:(SESSION ID = 31,SA ID = 1):Checking for duplicate IKEv2 SA
IKEv2:(SESSION ID = 31,SA ID = 1):No duplicate IKEv2 SA found
IKEv2:(SESSION ID = 31,SA ID = 1):Queuing IKE SA delete request reason: unknown
IKEv2:(SESSION ID = 31,SA ID = 1):Sending DELETE INFO message for IPsec SA [SPI: 0xA153CF67]
IKEv2:(SESSION ID = 31,SA ID = 1):Building packet for encryption.  
Payload contents: 
 DELETE
IKEv2:(SESSION ID = 31,SA ID = 1):Checking if request will fit in peer window 

IKEv2:(SESSION ID = 31,SA ID = 1):Sending Packet [To FC00:123:123:123::1:500/From FC00:123:123:123::2:500/VRF i0:f0] 
Initiator SPI : 1D418169B24BF95A - Responder SPI : A645046F734260C6 Message id: 2
IKEv2 INFORMATIONAL Exchange REQUEST 
Payload contents: 
 ENCR 

IKEv2:(SESSION ID = 31,SA ID = 1):Check for existing IPSEC SA
IKEv2:(SESSION ID = 31,SA ID = 1):Delete all IKE SAs
IKEv2:(SESSION ID = 31,SA ID = 1):Sending DELETE INFO message for IKEv2 SA [ISPI: 0x1D418169B24BF95A RSPI: 0xA645046F734260C6]
IKEv2:(SESSION ID = 31,SA ID = 1):Building packet for encryption.  
Payload contents: 
 DELETE
IKEv2:(SESSION ID = 31,SA ID = 1):Checking if request will fit in peer window
IKEv2:(SESSION ID = 31,SA ID = 1):Check for existing active SA
IKEv2:(SESSION ID = 31,SA ID = 1):Delete all IKE SAs 

IKEv2:(SESSION ID = 31,SA ID = 1):Received Packet [From FC00:123:123:123::1:500/To FC00:123:123:123::2:500/VRF i0:f0] 
Initiator SPI : 1D418169B24BF95A - Responder SPI : A645046F734260C6 Message id: 2
IKEv2 INFORMATIONAL Exchange RESPONSE 
Payload contents: 
 

IKEv2:(SESSION ID = 31,SA ID = 1):Processing ACK to informational exchange
IKEv2:(SESSION ID = 31,SA ID = 1):Check for existing IPSEC SA
IKEv2:(SESSION ID = 31,SA ID = 1):Delete all IKE SAs 

IKEv2:(SESSION ID = 31,SA ID = 1):Sending Packet [To FC00:123:123:123::1:500/From FC00:123:123:123::2:500/VRF i0:f0] 
Initiator SPI : 1D418169B24BF95A - Responder SPI : A645046F734260C6 Message id: 3
IKEv2 INFORMATIONAL Exchange REQUEST 
Payload contents: 
 ENCR 
 

IKEv2:(SESSION ID = 31,SA ID = 1):Received Packet [From FC00:123:123:123::1:500/To FC00:123:123:123::2:500/VRF i0:f0] 
Initiator SPI : 1D418169B24BF95A - Responder SPI : A645046F734260C6 Message id: 3
IKEv2 INFORMATIONAL Exchange RESPONSE 
Payload contents: 
 

IKEv2:(SESSION ID = 31,SA ID = 1):Processing ACK to informational exchange
IKEv2:(SESSION ID = 31,SA ID = 1):Deleting SA
*May  2 16:05:42.441: %LINEPROTO-5-UPDOWN: Line protocol on Interface Tunnel46, changed state to up
*May  2 16:05:42.447: %LINK-3-UPDOWN: Interface Tunnel46, changed state to up
XE-R4(config-if)#
IKEv2:% Getting preshared key from profile keyring IKEV2-KEYRING
IKEv2:% Matched peer block 'ANY-IPV6'
IKEv2:Searching Policy with fvrf 0, local address FC00:123:123:123::2
IKEv2:Using the Default Policy for Proposal
IKEv2:Found Policy 'default'
IKEv2:(SESSION ID = 31,SA ID = 1):[IKEv2 -> Crypto Engine] Computing DH public key, DH Group 5
IKEv2:(SA ID = 1):[Crypto Engine -> IKEv2] DH key Computation PASSED
IKEv2:(SESSION ID = 31,SA ID = 1):Request queued for computation of DH key
IKEv2:IKEv2 initiator - no config data to send in IKE_SA_INIT exch
IKEv2:(SESSION ID = 31,SA ID = 1):Generating IKE_SA_INIT message
IKEv2:(SESSION ID = 31,SA ID = 1):IKE Proposal: 1, SPI size: 0 (initial negotiation), 
Num. transforms: 15
   AES-CBC   AES-CBC   AES-CBC   SHA512   SHA384   SHA256   SHA1   MD5   SHA512   SHA384   SHA256   SHA96   MD596   DH_GROUP_1536_MODP/Group 5   DH_GROUP_1024_MODP/Group 2 

IKEv2:(SESSION ID = 31,SA ID = 1):Sending Packet [To FC00:123:123:123::1:500/From FC00:123:123:123::2:500/VRF i0:f0] 
Initiator SPI : 161B5964AD200FB7 - Responder SPI : 0000000000000000 Message id: 0
IKEv2 IKE_SA_INIT Exchange REQUEST 
Payload contents: 
 SA KE N VID VID VID VID NOTIFY(NAT_DETECTION_SOURCE_IP) NOTIFY(NAT_DETECTION_DESTINATION_IP) 

IKEv2:(SESSION ID = 31,SA ID = 1):Insert SA 

IKEv2:(SESSION ID = 31,SA ID = 1):Received Packet [From FC00:123:123:123::1:500/To FC00:123:123:123::2:500/VRF i0:f0] 
Initiator SPI : 161B5964AD200FB7 - Responder SPI : A1FE3FC96058584F Message id: 0
IKEv2 IKE_SA_INIT Exchange RESPONSE 
Payload contents: 
 SA KE N VID VID VID VID NOTIFY(NAT_DETECTION_SOURCE_IP) NOTIFY(NAT_DETECTION_DESTINATION_IP) 

IKEv2:(SESSION ID = 31,SA ID = 1):Processing IKE_SA_INIT message
IKEv2:(SESSION ID = 31,SA ID = 1):Verify SA init message
IKEv2:(SESSION ID = 31,SA ID = 1):Processing IKE_SA_INIT message
IKEv2:(SESSION ID = 31,SA ID = 1):Checking NAT discovery
IKEv2:(SESSION ID = 31,SA ID = 1):NAT not found
IKEv2:(SESSION ID = 31,SA ID = 1):[IKEv2 -> Crypto Engine] Computing DH secret key, DH Group 5
IKEv2:(SA ID = 1):[Crypto Engine -> IKEv2] DH key Computation PASSED
IKEv2:(SESSION ID = 31,SA ID = 1):Request queued for computation of DH secret
IKEv2:(SA ID = 1):[IKEv2 -> Crypto Engine] Calculate SKEYSEED and create rekeyed IKEv2 SA
IKEv2:(SA ID = 1):[Crypto Engine -> IKEv2] SKEYSEED calculation and creation of rekeyed IKEv2 SA PASSED
IKEv2:(SESSION ID = 31,SA ID = 1):Completed SA init exchange
IKEv2:Config data to send:
IKEv2:(SESSION ID = 31,SA ID = 1):Config-type: Config-request 
IKEv2:(SESSION ID = 31,SA ID = 1):Attrib type: app-version, length: 257, data: Cisco IOS Software [Fuji], Virtual XE Software (X86_64_LINUX_IOSD-UNIVERSALK9-M), Version 16.7.1, RELEASE SOFTWARE (fc6)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2017 by Cisco Systems, Inc.
Compiled Mon 20-Nov-17 18:57 by mcpre
IKEv2:(SESSION ID = 31,SA ID = 1):Attrib type: split-dns, length: 0
IKEv2:(SESSION ID = 31,SA ID = 1):Attrib type: banner, length: 0
IKEv2:(SESSION ID = 31,SA ID = 1):Attrib type: config-url, length: 0
IKEv2:(SESSION ID = 31,SA ID = 1):Attrib type: backup-gateway, length: 0
IKEv2:(SESSION ID = 31,SA ID = 1):Attrib type: def-domain, length: 0
IKEv2:(SESSION ID = 31,SA ID = 1):Have config mode data to send
IKEv2:(SESSION ID = 31,SA ID = 1):Check for EAP exchange
IKEv2:(SESSION ID = 31,SA ID = 1):Generate my authentication data
IKEv2:(SESSION ID = 31,SA ID = 1):Use preshared key for id FC00:123:123:123::2, key len 8
IKEv2:[IKEv2 -> Crypto Engine] Generate IKEv2 authentication data
IKEv2:[Crypto Engine -> IKEv2] IKEv2 authentication data generation PASSED
IKEv2:(SESSION ID = 31,SA ID = 1):Get my authentication method
IKEv2:(SESSION ID = 31,SA ID = 1):My authentication method is 'PSK'
IKEv2:(SESSION ID = 31,SA ID = 1):Check for EAP exchange
IKEv2:(SESSION ID = 31,SA ID = 1):Generating IKE_AUTH message
IKEv2:(SESSION ID = 31,SA ID = 1):Constructing IDi payload: 'FC00:123:123:123::2' of type 'IPv6 address'
IKEv2:(SESSION ID = 31,SA ID = 1):ESP Proposal: 1, SPI size: 4 (IPSec negotiation), 
Num. transforms: 3
   AES-CBC   SHA96   Don't use ESN
IKEv2:(SESSION ID = 31,SA ID = 1):Building packet for encryption.  
Payload contents: 
 VID IDi AUTH CFG SA TSi TSr NOTIFY(INITIAL_CONTACT) NOTIFY(USE_TRANSPORT_MODE) NOTIFY(SET_WINDOW_SIZE) NOTIFY(ESP_TFC_NO_SUPPORT) NOTIFY(NON_FIRST_FRAGS) 

IKEv2:(SESSION ID = 31,SA ID = 1):Sending Packet [To FC00:123:123:123::1:500/From FC00:123:123:123::2:500/VRF i0:f0] 
Initiator SPI : 161B5964AD200FB7 - Responder SPI : A1FE3FC96058584F Message id: 1
IKEv2 IKE_AUTH Exchange REQUEST 
Payload contents: 
 ENCR 
 

IKEv2:(SESSION ID = 31,SA ID = 1):Received Packet [From FC00:123:123:123::1:500/To FC00:123:123:123::2:500/VRF i0:f0] 
Initiator SPI : 161B5964AD200FB7 - Responder SPI : A1FE3FC96058584F Message id: 1
IKEv2 IKE_AUTH Exchange RESPONSE 
Payload contents: 
 VID IDr AUTH NOTIFY(NO_PROPOSAL_CHOSEN) 

IKEv2:(SESSION ID = 31,SA ID = 1):Process auth response notify
IKEv2-ERROR:(SESSION ID = 31,SA ID = 1):
IKEv2:(SESSION ID = 31,SA ID = 1):Searching policy based on peer's identity 'FC00:123:123:123::1' of type 'IPv6 address'
IKEv2:Searching Policy with fvrf 0, local address FC00:123:123:123::2
IKEv2:Using the Default Policy for Proposal
IKEv2:Found Policy 'default'
IKEv2:(SESSION ID = 31,SA ID = 1):Verify peer's policy
IKEv2:(SESSION ID = 31,SA ID = 1):Peer's policy verified
IKEv2:(SESSION ID = 31,SA ID = 1):Get peer's authentication method
IKEv2:(SESSION ID = 31,SA ID = 1):Peer's authentication method is 'PSK'
IKEv2:(SESSION ID = 31,SA ID = 1):Get peer's preshared key for FC00:123:123:123::1
IKEv2:(SESSION ID = 31,SA ID = 1):Verify peer's authentication data
IKEv2:(SESSION ID = 31,SA ID = 1):Use preshared key for id FC00:123:123:123::1, key len 8
IKEv2:[IKEv2 -> Crypto Engine] Generate IKEv2 authentication data
IKEv2:[Crypto Engine -> IKEv2] IKEv2 authentication data generation PASSED
IKEv2:(SESSION ID = 31,SA ID = 1):Verification of peer's authenctication data PASSED
IKEv2:(SESSION ID = 31,SA ID = 1):Check for EAP exchange
IKEv2:(SESSION ID = 31,SA ID = 1):IKEV2 SA created; inserting SA into database. SA lifetime timer (86400 sec) started
IKEv2:(SESSION ID = 31,SA ID = 1):Session with IKE ID PAIR (FC00:123:123:123::1, FC00:123:123:123::2) is UP
IKEv2:IKEv2 MIB tunnel started, tunnel index 1
IKEv2:(SESSION ID = 31,SA ID = 1):Checking for duplicate IKEv2 SA
IKEv2:(SESSION ID = 31,SA ID = 1):No duplicate IKEv2 SA found
IKEv2:(SESSION ID = 31,SA ID = 1):Queuing IKE SA delete request reason: unknown
IKEv2:(SESSION ID = 31,SA ID = 1):Sending DELETE INFO message for IPsec SA [SPI: 0x555E9566]
IKEv2:(SESSION ID = 31,SA ID = 1):Building packet for encryption.  
Payload contents: 
 DELETE
IKEv2:(SESSION ID = 31,SA ID = 1):Checking if request will fit in peer window 

IKEv2:(SESSION ID = 31,SA ID = 1):Sending Packet [To FC00:123:123:123::1:500/From FC00:123:123:123::2:500/VRF i0:f0] 
Initiator SPI : 161B5964AD200FB7 - Responder SPI : A1FE3FC96058584F Message id: 2
IKEv2 INFORMATIONAL Exchange REQUEST 
Payload contents: 
 ENCR 

IKEv2:(SESSION ID = 31,SA ID = 1):Check for existing IPSEC SA
IKEv2:(SESSION ID = 31,SA ID = 1):Delete all IKE SAs
IKEv2:(SESSION ID = 31,SA ID = 1):Sending DELETE INFO message for IKEv2 SA [ISPI: 0x161B5964AD200FB7 RSPI: 0xA1FE3FC96058584F]
IKEv2:(SESSION ID = 31,SA ID = 1):Building packet for encryption.  
Payload contents: 
 DELETE
IKEv2:(SESSION ID = 31,SA ID = 1):Checking if request will fit in peer window
IKEv2:(SESSION ID = 31,SA ID = 1):Check for existing active SA
IKEv2:(SESSION ID = 31,SA ID = 1):Delete all IKE SAs 

IKEv2:(SESSION ID = 31,SA ID = 1):Received Packet [From FC00:123:123:123::1:500/To FC00:123:123:123::2:500/VRF i0:f0] 
Initiator SPI : 161B5964AD200FB7 - Responder SPI : A1FE3FC96058584F Message id: 2
IKEv2 INFORMATIONAL Exchange RESPONSE 
Payload contents: 
 

IKEv2:(SESSION ID = 31,SA ID = 1):Processing ACK to informational exchange
IKEv2:(SESSION ID = 31,SA ID = 1):Check for existing IPSEC SA
IKEv2:(SESSION ID = 31,SA ID = 1):Delete all IKE SAs 

IKEv2:(SESSION ID = 31,SA ID = 1):Sending Packet [To FC00:123:123:123::1:500/From FC00:123:123:123::2:500/VRF i0:f0] 
Initiator SPI : 161B5964AD200FB7 - Responder SPI : A1FE3FC96058584F Message id: 3
IKEv2 INFORMATIONAL Exchange REQUEST 
Payload contents: 
 ENCR 
 

IKEv2:(SESSION ID = 31,SA ID = 1):Received Packet [From FC00:123:123:123::1:500/To FC00:123:123:123::2:500/VRF i0:f0] 
Initiator SPI : 161B5964AD200FB7 - Responder SPI : A1FE3FC96058584F Message id: 3
IKEv2 INFORMATIONAL Exchange RESPONSE 
Payload contents: 
 

IKEv2:(SESSION ID = 31,SA ID = 1):Processing ACK to informational exchange
IKEv2:(SESSION ID = 31,SA ID = 1):Deleting SA
IKEv2:% Getting preshared key from profile keyring IKEV2-KEYRING
IKEv2:% Matched peer block 'ANY-IPV6'
IKEv2:Searching Policy with fvrf 0, local address FC00:123:123:123::2
IKEv2:Using the Default Policy for Proposal
IKEv2:Found Policy 'default'
IKEv2:(SESSION ID = 31,SA ID = 1):[IKEv2 -> Crypto Engine] Computing DH public key, DH Group 5
IKEv2:(SA ID = 1):[Crypto Engine -> IKEv2] DH key Computation PASSED
IKEv2:(SESSION ID = 31,SA ID = 1):Request queued for computation of DH key
IKEv2:IKEv2 initiator - no config data to send in IKE_SA_INIT exch
IKEv2:(SESSION ID = 31,SA ID = 1):Generating IKE_SA_INIT message
IKEv2:(SESSION ID = 31,SA ID = 1):IKE Proposal: 1, SPI size: 0 (initial negotiation), 
Num. transforms: 15
   AES-CBC   AES-CBC   AES-CBC   SHA512   SHA384   SHA256   SHA1   MD5   SHA512   SHA384   SHA256   SHA96   MD596   DH_GROUP_1536_MODP/Group 5   DH_GROUP_1024_MODP/Group 2 

IKEv2:(SESSION ID = 31,SA ID = 1):Sending Packet [To FC00:123:123:123::1:500/From FC00:123:123:123::2:500/VRF i0:f0] 
Initiator SPI : 352F8CB45CC6EE7E - Responder SPI : 0000000000000000 Message id: 0
IKEv2 IKE_SA_INIT Exchange REQUEST 
Payload contents: 
 SA KE N VID VID VID VID NOTIFY(NAT_DETECTION_SOURCE_IP) NOTIFY(NAT_DETECTION_DESTINATION_IP) 

IKEv2:(SESSION ID = 31,SA ID = 1):Insert SA
IKEv2:(SESSION ID = 31,SA ID = 1):Retransmitting packet 

IKEv2:(SESSION ID = 31,SA ID = 1):Sending Packet [To FC00:123:123:123::1:500/From FC00:123:123:123::2:500/VRF i0:f0] 
Initiator SPI : 352F8CB45CC6EE7E - Responder SPI : 0000000000000000 Message id: 0
IKEv2 IKE_SA_INIT Exchange REQUEST 
Payload contents: 
 SA KE N VID VID VID VID NOTIFY(NAT_DETECTION_SOURCE_IP) NOTIFY(NAT_DETECTION_DESTINATION_IP) 

IKEv2:(SESSION ID = 31,SA ID = 1):Retransmitting packet 

IKEv2:(SESSION ID = 31,SA ID = 1):Sending Packet [To FC00:123:123:123::1:500/From FC00:123:123:123::2:500/VRF i0:f0] 
Initiator SPI : 352F8CB45CC6EE7E - Responder SPI : 0000000000000000 Message id: 0
IKEv2 IKE_SA_INIT Exchange REQUEST 
Payload contents: 
 SA KE N VID VID VID VID NOTIFY(NAT_DETECTION_SOURCE_IP) NOTIFY(NAT_DETECTION_DESTINATION_IP) 

XE-R4(config-if)#
XE-R4(config-if)#
XE-R4(config-if)#EXIT
XE-R4(config)#
XE-R4(config)#U ALL
                ^
% Invalid input detected at '^' marker.

XE-R4(config)#exit
XE-R4#u all
*May  2 16:06:52.754: %SYS-5-CONFIG_I: Configured from console by cisco on vty1 (150.1.1.253)
All possible debugging has been turned off
XE-R4#debut
IKEv2:(SESSION ID = 31,SA ID = 1):Retransmitting packet 

IKEv2:(SESSION ID = 31,SA ID = 1):Sending Packet [To FC00:123:123:123::1:500/From FC00:123:123:123::2:500/VRF i0:f0] 
Initiator SPI : 352F8CB45CC6EE7E - Responder SPI : 0000000000000000 Message id: 0
IKEv2 IKE_SA_INIT Exchange REQUEST 
Payload contents: 
 SA KE N VID VID VID VID NOTIFY(NAT_DETECTION_SOURCE_IP) NOTIFY(NAT_DETECTION_DESTINATION_IP) 

XE-R4#debut
XE-R4#debut
XE-R4#debug
XE-R4#debug cry
XE-R4#debug crypto ike
XE-R4#debug crypto ikev2 er
XE-R4#debug crypto ikev2 error ?
  <cr>

XE-R4#debug crypto ikev2 ?     
  client    Client
  cluster   IKEv2 Cluster load-balancer debugging
  error     IKEv2 Error debugging
  internal  IKEv2 Internal debugging
  packet    IKEv2 Packet debugging
  <cr>

XE-R4#debug crypto ikev2 pa
XE-R4#debug crypto ikev2 packet ?
  hexdump  Also hexdumps the packet
  <cr>

XE-R4#debug crypto ikev2 err    
XE-R4#debug crypto ikev2 error 
IKEv2 error debugging is on
XE-R4#clear cry
XE-R4#clear crypto ike
XE-R4#clear crypto ikev2 ?
  certificate-cache  Clear IKEv2 certificate cache
  client             Client
  diagnose           Clear ikev2 diagnostic
  sa                 Clear ikev2 SAs
  stats              Clears IKEv2 Statistics

XE-R4#clear crypto ikev2 sa 
XE-R4#
IKEv2-ERROR:(SESSION ID = 31,SA ID = 1):Initial exchange failed: Initial exchange failed
XE-R4#u all
All possible debugging has been turned off
