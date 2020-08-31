HQ#clear cry sa   
HQ#clea
ISAKMP-ERROR: (0):Failed to find peer index node to update peer_info_list
ISAKMP-ERROR: (0):Failed to find peer index node to update peer_info_list
ISAKMP: (0):Deleting peer node by peer_reap for 103.1.1.1: 7EFF7C24E120
ISAKMP-ERROR: (0):ignoring request to send delete notify (no ISAKMP sa) src 61.128.1.1 dst 103.1.1.1 for SPI 0x3EA71AED
ISAKMP: (0):Deleting peer node by peer_reap for 103.1.1.1: 7EFF652C07E8
ISAKMP-ERROR: (0):ignoring request to send delete notify (no ISAKMP sa) src 61.128.1.1 dst 1r cr
HQ#clear crypto 03.1.1.1 for S             
HQ#
HQ#
HQ#
HQ#
HQ#
HQ#
HQ#
HQ#
HQ#
HQ#
HQ#
HQ#
HQ#
*Oct 24 04:31:10.058: %CRYPTO-4-RECVD_PKT_INV_SPI: decaps: rec'd IPSEC packet has invalid spi for destaddr=61.128.1.1, prot=50, spi=0x3EA71AED(1051138797), srcaddr=103.1.1.1, input interface=GigabitEthernet1
ISAKMP-ERROR: (0):ignoring request to send delete notify (no ISAKMP sa) src 61.128.1.1 dst 103.1.1.1 for SPI 0x3EA71AED
ISAKMP-ERROR: (0):ignoring request to send delete notify (no ISAKMP sa) src 61.128.1.1 dst 103.1.1.1 for SPI 0xD9161513
ISAKMP-ERROR: (0):ignoring request to send delete notify (no ISAKMP sa) src 61.128.1.1 dst 103.1.1.1 for SPI 0xD9161513
ISAKMP-PAK: (0):received packet from 103.1.1.1 dport 500 sport 512 Global (N) NEW SA
ISAKMP: (0):Created a peer struct for 103.1.1.1, peer port 512
ISAKMP: (0):New peer created peer = 0x7EFF7C24E120 peer_handle = 0x8000000B
ISAKMP: (0):Locking peer struct 0x7EFF7C24E120, refcount 1 for crypto_isakmp_process_block
ISAKMP: (0):local port 500, remote port 512
ISAKMP: (0):insert sa successfully sa = 7EFF654479B0
ISAKMP: (0):Input = IKE_MESG_FROM_PEER, IKE_MM_EXCH
ISAKMP: (0):Old State = IKE_READY  New State = IKE_R_MM1 

ISAKMP: (0):processing SA payload. message ID = 0
ISAKMP: (0):processing vendor id payload
ISAKMP: (0):vendor ID seems Unity/DPD but major 69 mismatch
ISAKMP: (0):vendor ID is NAT-T RFC 3947
ISAKMP: (0):processing vendor id payload
ISAKMP: (0):vendor ID seems Unity/DPD but major 245 mismatch
ISAKMP: (0):vendor ID is NAT-T v7
ISAKMP: (0):processing vendor id payload
ISAKMP: (0):vendor ID seems Unity/DPD but major 157 mismatch
ISAKMP: (0):vendor ID is NAT-T v3
ISAKMP: (0):processing vendor id payload
ISAKMP: (0):vendor ID seems Unity/DPD but major 123 mismatch
ISAKMP: (0):vendor ID is NAT-T v2
ISAKMP: (0):found peer pre-shared key matching 103.1.1.1
ISAKMP: (0):local preshared key found
ISAKMP: (0):Scanning profiles for xauth ... VPN
ISAKMP: (0):Checking ISAKMP transform 1 against priority 10 policy
ISAKMP: (0):      encryption 3DES-CBC
ISAKMP: (0):      hash SHA
ISAKMP: (0):      default group 2
ISAKMP: (0):      auth pre-share
ISAKMP: (0):      life type in seconds
ISAKMP: (0):      life duration (basic) of 6000
ISAKMP: (0):atts are acceptable. Next payload is 0
ISAKMP: (0):Acceptable atts:actual life: 6000
ISAKMP: (0):Acceptable atts:life: 0
ISAKMP: (0):Basic life_in_seconds:6000
ISAKMP: (0):Returning Actual lifetime: 6000
ISAKMP: (0):Started lifetime timer: 6000.

ISAKMP: (0):processing vendor id payload
ISAKMP: (0):vendor ID seems Unity/DPD but major 69 mismatch
ISAKMP: (0):vendor ID is NAT-T RFC 3947
ISAKMP: (0):processing vendor id payload
ISAKMP: (0):vendor ID seems Unity/DPD but major 245 mismatch
ISAKMP: (0):vendor ID is NAT-T v7
ISAKMP: (0):processing vendor id payload
ISAKMP: (0):vendor ID seems Unity/DPD but major 157 mismatch
ISAKMP: (0):vendor ID is NAT-T v3
ISAKMP: (0):processing vendor id payload
ISAKMP: (0):vendor ID seems Unity/DPD but major 123 mismatch
ISAKMP: (0):vendor ID is NAT-T v2
ISAKMP: (0):Input = IKE_MESG_INTERNAL, IKE_PROCESS_MAIN_MODE
ISAKMP: (0):Old State = IKE_R_MM1  New State = IKE_R_MM1 

ISAKMP: (0):constructed NAT-T vendor-rfc3947 ID
ISAKMP-PAK: (0):sending packet to 103.1.1.1 my_port 500 peer_port 512 (R) MM_SA_SETUP
ISAKMP: (0):Sending an IKE IPv4 Packet.
ISAKMP: (0):Input = IKE_MESG_INTERNAL, IKE_PROCESS_COMPLETE
ISAKMP: (0):Old State = IKE_R_MM1  New State = IKE_R_MM2 

ISAKMP-PAK: (0):received packet from 103.1.1.1 dport 500 sport 512 Global (R) MM_SA_SETUP
ISAKMP: (0):Input = IKE_MESG_FROM_PEER, IKE_MM_EXCH
ISAKMP: (0):Old State = IKE_R_MM2  New State = IKE_R_MM3 

ISAKMP: (0):processing KE payload. message ID = 0
ISAKMP: (0):processing NONCE payload. message ID = 0
ISAKMP: (0):found peer pre-shared key matching 103.1.1.1
ISAKMP: (1003):processing vendor id payload
ISAKMP: (1003):vendor ID is DPD
ISAKMP: (1003):processing vendor id payload
ISAKMP: (1003):speaking to another IOS box!
ISAKMP: (1003):processing vendor id payload
ISAKMP: (1003):vendor ID seems Unity/DPD but major 149 mismatch
ISAKMP: (1003):vendor ID is XAUTH
ISAKMP: (1003):received payload type 20
ISAKMP: (1003):His hash no match - this node outside NAT
ISAKMP: (1003):received payload type 20
ISAKMP: (1003):His hash no match - this node outside NAT
ISAKMP: (1003):Input = IKE_MESG_INTERNAL, IKE_PROCESS_MAIN_MODE
ISAKMP: (1003):Old State = IKE_R_MM3  New State = IKE_R_MM3 

ISAKMP-PAK: (1003):sending packet to 103.1.1.1 my_port 500 peer_port 512 (R) MM_KEY_EXCH
ISAKMP: (1003):Sending an IKE IPv4 Packet.
ISAKMP: (1003):Input = IKE_MESG_INTERNAL, IKE_PROCESS_COMPLETE
ISAKMP: (1003):Old State = IKE_R_MM3  New State = IKE_R_MM4 

ISAKMP-PAK: (1003):received packet from 103.1.1.1 dport 4500 sport 4501 Global (R) MM_KEY_EXCH
ISAKMP: (1003):Input = IKE_MESG_FROM_PEER, IKE_MM_EXCH
ISAKMP: (1003):Old State = IKE_R_MM4  New State = IKE_R_MM5 

ISAKMP: (1003):processing ID payload. message ID = 0
ISAKMP: (1003):ID payload 
        next-payload : 8
        type         : 1
ISAKMP: (1003): address      : 100.64.1.2
ISAKMP: (1003): protocol     : 17 
        port         : 0 
        length       : 12
ISAKMP: (0):peer matches VPN profile
ISAKMP: (1003):Found ADDRESS key in keyring RA
ISAKMP: (1003):processing HASH payload. message ID = 0
ISAKMP: (1003):processing NOTIFY INITIAL_CONTACT protocol 1
        spi 0, message ID = 0, sa = 0x7EFF654479B0
ISAKMP: (1003):SA authentication status:
        authenticated
ISAKMP: (1003):SA has been authenticated with 103.1.1.1
ISAKMP: (1003):Detected port floating to port = 4501
ISAKMP: (1003):Trying to find existing peer 61.128.1.1/103.1.1.1/4501/
ISAKMP: (1003):SA authentication status:
        authenticated
ISAKMP: (1003):Process initial contact,
bring down existing phase 1 and 2 SA's with local 61.128.1.1 remote 103.1.1.1 remote port 4501
ISAKMP: (0):Trying to insert a peer 61.128.1.1/103.1.1.1/4501/, 
ISAKMP: (0): and inserted successfully 7EFF7C24E120.
ISAKMP: (1003):Input = IKE_MESG_INTERNAL, IKE_PROCESS_MAIN_MODE
ISAKMP: (1003):Old State = IKE_R_MM5  New State = IKE_R_MM5 

ISAKMP: (1003):SA is doing 
ISAKMP: (1003):pre-shared key authentication using id type ID_IPV4_ADDR
ISAKMP: (1003):ID payload 
        next-payload : 8
        type         : 1
ISAKMP: (1003): address      : 61.128.1.1
ISAKMP: (1003): protocol     : 17 
        port         : 0 
        length       : 12
ISAKMP: (1003):Total payload length: 12
ISAKMP-PAK: (1003):sending packet to 103.1.1.1 my_port 4500 peer_port 4501 (R) MM_KEY_EXCH
ISAKMP: (1003):Sending an IKE IPv4 Packet.
ISAKMP: (1003):Input = IKE_MESG_INTERNAL, IKE_PROCESS_COMPLETE
ISAKMP: (1003):Old State = IKE_R_MM5  New State = IKE_P1_COMPLETE 

ISAKMP: (1003):Input = IKE_MESG_INTERNAL, IKE_PHASE1_COMPLETE
ISAKMP: (1003):Old State = IKE_P1_COMPLETE  New State = IKE_P1_COMPLETE 

ISAKMP-PAK: (1003):received packet from 103.1.1.1 dport 4500 sport 4501 Global (R) QM_IDLE      
ISAKMP: (1003):set new node 1416806668 to QM_IDLE      
ISAKMP: (1003):processing HASH payload. message ID = 1416806668
ISAKMP: (1003):processing SA payload. message ID = 1416806668
ISAKMP: (1003):Checking IPSec proposal 1
ISAKMP: (1003):transform 1, ESP_3DES
ISAKMP: (1003):   attributes in transform:
ISAKMP: (1003):      encaps is 3 (Tunnel-UDP)
ISAKMP: (1003):      SA life type in seconds
ISAKMP: (1003):      SA life duration (basic) of 3600
ISAKMP: (1003):      SA life type in kilobytes
ISAKMP:      SA life duration (VPI) of  0x0 0x46 0x50 0x0 
ISAKMP: (1003):      authenticator is HMAC-SHA
ISAKMP: (1003):atts are acceptable.
ISAKMP: (1003):processing NONCE payload. message ID = 1416806668
ISAKMP: (1003):processing ID payload. message ID = 1416806668
ISAKMP: (1003):processing ID payload. message ID = 1416806668
ISAKMP: (1003):QM Responder gets spi
ISAKMP: (1003):Node 1416806668, Input = IKE_MESG_FROM_PEER, IKE_QM_EXCH
ISAKMP: (1003):Old State = IKE_QM_READY  New State = IKE_QM_SPI_STARVE
ISAKMP: (1003):Node 1416806668, Input = IKE_MESG_INTERNAL, IKE_GOT_SPI
ISAKMP: (1003):Old State = IKE_QM_SPI_STARVE  New State = IKE_QM_IPSEC_INSTALL_AWAIT
ISAKMP-ERROR: (0):Failed to find peer index node to update peer_info_list
ISAKMP: (1003):Received IPSec Install callback... proceeding with the negotiation
ISAKMP: (1003):Successfully installed IPSEC SA (SPI:0xF5AC7011) on GigabitEthernet1
ISAKMP-PAK: (1003):sending packet to 103.1.1.1 my_port 4500 peer_port 4501 (R) QM_IDLE      
ISAKMP: (1003):Sending an IKE IPv4 Packet.
ISAKMP: (1003):Node 1416806668, Input = IKE_MESG_FROM_IPSEC, IPSEC_INSTALL_DONE
ISAKMP: (1003):Old State = IKE_QM_IPSEC_INSTALL_AWAIT  New State = IKE_QM_R_QM2
ISAKMP-PAK: (1003):received packet from 103.1.1.1 dport 4500 sport 4501 Global (R) QM_IDLE      
ISAKMP: (1003):deleting node 1416806668 error FALSE reason "QM done (await)"
ISAKMP: (1003):Node 1416806668, Input = IKE_MESG_FROM_PEER, IKE_QM_EXCH
ISAKMP: (1003):Old State = IKE_QM_R_QM2  New State = IKE_QM_PHASE2_COMPLETE
















#####################################
SITE-A#clear cry sa 
SITE-A#p
ISAKMP-ERROR: (0):Failed to find peer index node to update peer_info_list
ISAKMP: (0):Deleting peer node by peer_reap for 61.128.1.1: 7F368CB80BB0
ISAKMP-ERROR: (0):ignoring request to send delete notify (no ISAKMP sa) src 100.64.1.2 dst 61.128.1.1 for SPI 0xA6BD53Eing 
SITE-A#ping 
SITE-A#ping 
SITE-A#ping 
SITE-A#ping 
SITE-A#ping 3.3.3.3 sou lo0
Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 3.3.3.3, timeout is 2 seconds:
Packet sent with a source address of 1.1.1.1 

ISAKMP: (0):SA request profile is (NULL)
ISAKMP: (0):Created a peer struct for 61.128.1.1, peer port 500
ISAKMP: (0):New peer created peer = 0x7F368CB80BB0 peer_handle = 0x80000009
ISAKMP: (0):Locking peer struct 0x7F368CB80BB0, refcount 1 for isakmp_initiator
ISAKMP: (0):local port 500, remote port 500
ISAKMP: (0):set new node 0 to QM_IDLE      
ISAKMP: (0):Find a dup sa in the avl tree during calling isadb_insert sa = 7F368CB7D310
ISAKMP: (0):Can not start Aggressive mode, trying Main mode.
ISAKMP: (0):found peer pre-shared key matching 61.128.1.1
ISAKMP: (0):constructed NAT-T vendor-rfc3947 ID
ISAKMP: (0):constructed NAT-T vendor-07 ID
ISAKMP: (0):constructed NAT-T vendor-03 ID
ISAKMP: (0):constructed NAT-T vendor-02 ID
ISAKMP: (0):Input = IKE_MESG_FROM_IPSEC, IKE_SA_REQ_MM
ISAKMP: (0):Old State = IKE_READY  New State = IKE_I_MM1 

ISAKMP: (0):beginning Main Mode exchange
ISAKMP-PAK: (0):sending packet to 61.128.1.1 my_port 500 peer_port 500 (I) MM_NO_STATE
ISAKMP: (0):Sending an IKE .!!!!
Success rate is 80 percent (4/5), round-trip min/avg/max = 16/17/20 ms
SITE-A#IPv4 Packet.
ISAKMP-PAK: (0):received packet from 61.128.1.1 dport 500 sport 500 Global (I) MM_NO_STATE
ISAKMP: (0):Input = IKE_MESG_FROM_PEER, IKE_MM_EXCH
ISAKMP: (0):Old State = IKE_I_MM1  New State = IKE_I_MM2 

ISAKMP: (0):processing SA payload. message ID = 0
ISAKMP: (0):processing vendor id payload
ISAKMP: (0):vendor ID seems Unity/DPD but major 69 mismatch
ISAKMP: (0):vendor ID is NAT-T RFC 3947
ISAKMP: (0):found peer pre-shared key matching 61.128.1.1
ISAKMP: (0):local preshared key found
ISAKMP: (0):Scanning profiles for xauth ... VPN
ISAKMP: (0):Checking ISAKMP transform 1 against priority 10 policy
ISAKMP: (0):      encryption 3DES-CBC
ISAKMP: (0):      hash SHA
ISAKMP: (0):      default group 2
ISAKMP: (0):      auth pre-share
ISAKMP: (0):      life type in seconds
ISAKMP: (0):      life duration (basic) of 6000
ISAKMP: (0):atts are acceptable. Next payload is 0
ISAKMP: (0):Acceptable atts:actual life: 0
ISAKMP: (0):Acceptable atts:life: 0
ISAKMP: (0):Basic life_in_seconds:6000
ISAKMP: (0):Returning Actual lifetime: 6000
ISAKMP: (0):Started lifetime timer: 6000.

ISAKMP: (0):processing vendor id payload
ISAKMP: (0):vendor ID seems Unity/DPD but major 69 mismatch
ISAKMP: (0):vendor ID is NAT-T RFC 3947
ISAKMP: (0):Input = IKE_MESG_INTERNAL, IKE_PROCESS_MAIN_MODE
ISAKMP: (0):Old State = IKE_I_MM2  New State = IKE_I_MM2 

ISAKMP-PAK: (0):sending packet to 61.128.1.1 my_port 500 peer_port 500 (I) MM_SA_SETUP
ISAKMP: (0):Sending an IKE IPv4 Packet.
ISAKMP: (0):Input = IKE_MESG_INTERNAL, IKE_PROCESS_COMPLETE
ISAKMP: (0):Old State = IKE_I_MM2  New State = IKE_I_MM3 

ISAKMP-PAK: (0):received packet from 61.128.1.1 dport 500 sport 500 Global (I) MM_SA_SETUP
ISAKMP: (0):Input = IKE_MESG_FROM_PEER, IKE_MM_EXCH
ISAKMP: (0):Old State = IKE_I_MM3  New State = IKE_I_MM4 

ISAKMP: (0):processing KE payload. message ID = 0
ISAKMP: (0):processing NONCE payload. message ID = 0
ISAKMP: (0):found peer pre-shared key matching 61.128.1.1
ISAKMP: (1003):processing vendor id payload
ISAKMP: (1003):vendor ID is Unity
ISAKMP: (1003):processing vendor id payload
ISAKMP: (1003):vendor ID is DPD
ISAKMP: (1003):processing vendor id payload
ISAKMP: (1003):speaking to another IOS box!
ISAKMP: (1003):received payload type 20
ISAKMP: (1003):NAT found, both nodes inside NAT
ISAKMP: (1003):received payload type 20
ISAKMP: (1003):My hash no match -  this node inside NAT
ISAKMP: (1003):Input = IKE_MESG_INTERNAL, IKE_PROCESS_MAIN_MODE
ISAKMP: (1003):Old State = IKE_I_MM4  New State = IKE_I_MM4 

ISAKMP: (1003):Send initial contact
ISAKMP: (1003):SA is doing 
ISAKMP: (1003):pre-shared key authentication using id type ID_IPV4_ADDR
ISAKMP: (1003):ID payload 
        next-payload : 8
        type         : 1
ISAKMP: (1003): address      : 100.64.1.2
ISAKMP: (1003): protocol     : 17 
        port         : 0 
        length       : 12
ISAKMP: (1003):Total payload length: 12
ISAKMP-PAK: (1003):sending packet to 61.128.1.1 my_port 4500 peer_port 4500 (I) MM_KEY_EXCH
ISAKMP: (1003):Sending an IKE IPv4 Packet.
ISAKMP: (1003):Input = IKE_MESG_INTERNAL, IKE_PROCESS_COMPLETE
ISAKMP: (1003):Old State = IKE_I_MM4  New State = IKE_I_MM5 

ISAKMP-PAK: (1003):received packet from 61.128.1.1 dport 4500 sport 4500 Global (I) MM_KEY_EXCH
ISAKMP: (1003):processing ID payload. message ID = 0
ISAKMP: (1003):ID payload 
        next-payload : 8
        type         : 1
ISAKMP: (1003): address      : 61.128.1.1
ISAKMP: (1003): protocol     : 17 
        port         : 0 
        length       : 12
ISAKMP: (0):peer matches VPN profile
ISAKMP: (1003):Found ADDRESS key in keyring VPN
ISAKMP: (1003):processing HASH payload. message ID = 0
ISAKMP: (1003):SA authentication status:
        authenticated
ISAKMP: (1003):SA has been authenticated with 61.128.1.1
ISAKMP: (1003):Setting UDP ENC peer struct 0x7F36A89EE650 sa= 0x7F368CB7D310
ISAKMP: (0):Trying to insert a peer 100.64.1.2/61.128.1.1/4500/, 
ISAKMP: (0): and inserted successfully 7F368CB80BB0.
ISAKMP: (1003):Input = IKE_MESG_FROM_PEER, IKE_MM_EXCH
ISAKMP: (1003):Old State = IKE_I_MM5  New State = IKE_I_MM6 

ISAKMP: (1003):Input = IKE_MESG_INTERNAL, IKE_PROCESS_MAIN_MODE
ISAKMP: (1003):Old State = IKE_I_MM6  New State = IKE_I_MM6 

ISAKMP: (1003):Input = IKE_MESG_INTERNAL, IKE_PROCESS_COMPLETE
ISAKMP: (1003):Old State = IKE_I_MM6  New State = IKE_P1_COMPLETE 

ISAKMP: (1003):beginning Quick Mode exchange, M-ID of 1025971884
ISAKMP: (1003):QM Initiator gets spi
ISAKMP-PAK: (1003):sending packet to 61.128.1.1 my_port 4500 peer_port 4500 (I) QM_IDLE      
ISAKMP: (1003):Sending an IKE IPv4 Packet.
ISAKMP: (1003):Node 1025971884, Input = IKE_MESG_INTERNAL, IKE_INIT_QM
ISAKMP: (1003):Old State = IKE_QM_READY  New State = IKE_QM_I_QM1
ISAKMP: (1003):Input = IKE_MESG_INTERNAL, IKE_PHASE1_COMPLETE
ISAKMP: (1003):Old State = IKE_P1_COMPLETE  New State = IKE_P1_COMPLETE 

ISAKMP-PAK: (1003):received packet from 61.128.1.1 dport 4500 sport 4500 Global (I) QM_IDLE      
ISAKMP: (1003):set new node 1319368483 to QM_IDLE      
ISAKMP: (1003):processing HASH payload. message ID = 1319368483
ISAKMP: (1003):processing DELETE payload. message ID = 1319368483
ISAKMP: (1003):peer does not do paranoid keepalives.
ISAKMP: (1003):Enqueued KEY_MGR_DELETE_SAS for IPSEC SA (SPI:0xF5AC7011)
ISAKMP: (1003):deleting node 1319368483 error FALSE reason "Informational (in) state 1"
ISAKMP-PAK: (1003):received packet from 61.128.1.1 dport 4500 sport 4500 Global (I) QM_IDLE      
ISAKMP: (1003):processing HASH payload. message ID = 1025971884
ISAKMP: (1003):processing SA payload. message ID = 1025971884
ISAKMP: (1003):Checking IPSec proposal 1
ISAKMP: (1003):transform 1, ESP_3DES
ISAKMP: (1003):   attributes in transform:
ISAKMP: (1003):      encaps is 3 (Tunnel-UDP)
ISAKMP: (1003):      SA life type in seconds
ISAKMP: (1003):      SA life duration (basic) of 3600
ISAKMP: (1003):      SA life type in kilobytes
ISAKMP:      SA life duration (VPI) of  0x0 0x46 0x50 0x0 
ISAKMP: (1003):      authenticator is HMAC-SHA
ISAKMP: (1003):atts are acceptable.
ISAKMP: (1003):processing NONCE payload. message ID = 1025971884
ISAKMP: (1003):processing ID payload. message ID = 1025971884
ISAKMP: (1003):processing ID payload. message ID = 1025971884
ISAKMP: (1003):Node 1025971884, Input = IKE_MESG_FROM_PEER, IKE_QM_EXCH
ISAKMP: (1003):Old State = IKE_QM_I_QM1  New State = IKE_QM_IPSEC_INSTALL_AWAIT
ISAKMP-ERROR: (0):Failed to find peer index node to update peer_info_list
ISAKMP: (1003):Received IPSec Install callback... proceeding with the negotiation
ISAKMP: (1003):Successfully installed IPSEC SA (SPI:0xCB02AF0F) on GigabitEthernet1
ISAKMP-PAK: (1003):sending packet to 61.128.1.1 my_port 4500 peer_port 4500 (I) QM_IDLE      
ISAKMP: (1003):Sending an IKE IPv4 Packet.
ISAKMP: (1003):deleting node 1025971884 error FALSE reason "No Error"
ISAKMP: (1003):Node 1025971884, Input = IKE_MESG_FROM_IPSEC, IPSEC_INSTALL_DONE
ISAKMP: (1003):Old State = IKE_QM_IPSEC_INSTALL_AWAIT  New State = IKE_QM_PHASE2_COMPLETE
