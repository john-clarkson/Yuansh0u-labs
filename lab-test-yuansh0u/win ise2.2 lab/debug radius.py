Router#debug radius
Radius protocol debugging is on
Radius protocol brief debugging is off
Radius protocol verbose debugging is off
Radius packet hex dump debugging is off
Radius packet protocol debugging is on
Radius elog debugging debugging is off
Radius packet retransmission debugging is off
Radius server fail-over debugging is off
Radius elog debugging debugging is off
Router#telnet 192.168.55.254
Trying 192.168.55.254 ... Open

User Access Verification

Username: 
*Oct 31 21:50:10.736: RADIUS/ENCODE(00000014): ask "Username: "
*Oct 31 21:50:10.736: RADIUS/ENCODE(00000014): send packet; GET_USERhitler-level1
Password: 
*Oct 31 21:50:25.556: RADIUS/ENCODE(00000014): ask "Password: "
*Oct 31 21:50:25.556: RADIUS/ENCODE(00000014): send packet; GET_PASSWORD
*Oct 31 21:50:29.488: RADIUS/ENCODE(00000014):Orig. component type = Exec
*Oct 31 21:50:29.492: RADIUS:  AAA Unsupported Attr: interface         [221] 4   1763797908
*Oct 31 21:50:29.496: RADIUS/ENCODE(00000014): dropping service type, "radius-server attribute 6 on-for-login-auth" is off
*Oct 31 21:50:29.496: RADIUS(00000014): Config NAS IP: 192.168.55.254
*Oct 31 21:50:29.496: RADIUS(00000014): Config NAS IPv6: ::
*Oct 31 21:50:29.500: RADIUS/ENCODE(00000014): acct_session_id: 7
*Oct 31 21:50:29.500: RADIUS(00000014): sending
*Oct 31 21:50:29.508: RADIUS(00000014): Send Access-Request to 192.168.55.1:1645 id 1645/8, len 77
*Oct 31 21:50:29.512: RADIUS:  authenticator 58 80 52 B4 DB 61 FB 11 - 12 44 43 35 18 D4 94 7E
*Oct 31 21:50:29.512: RADIUS:  User-Name           [1]   15  "hitler-level1"
*Oct 31 21:50:29.512: RADIUS:  User-Password       [2]   18  *
*Oct 31 21:50:29.512: RADIUS:  NAS-Port            [5]   6   2                         
*Oct 31 21:50:29.512: RADIUS:  NAS-Port-Id         [87]  6   "tty2"
*Oct 31 21:50:29.512: RADIUS:  NAS-Port-Type       [61]  6   Virtual                   [5]
*Oct 31 21:50:29.512: RADIUS:  NAS-IP-Address      [4]   6   192.168.55.254            
*Oct 31 21:50:29.512: RADIUS(00000014): Sending a IPv4 Radius Packet
*Oct 31 21:50:29.512: RADIUS(00000014): Started 2 sec timeout
*Oct 31 21:50:29.520: RADIUS: Received from id 1645/8 192.168.55.1:1645, Access-Accept, len 183
*Oct 31 21:50:29.524: RADIUS:  authenticator 3A 1F D6 4A 85 93 96 D2 - 76 B6 98 20 1D D4 E5 27
*Oct 31 21:50:29.524: RADIUS:  User-Name           [1]   15  "hitler-level1"
*Oct 31 21:50:29.528: RADIUS:  State               [24]  67  
*Oct 31 21:50:29.528: RADIUS:   52 65 61 75 74 68 53 65 73 73 69 6F 6E 3A 39 36  [ReauthSession:96]
*Oct 31 21:50:29.532: RADIUS:   30 31 33 37 30 31 63 79 6D 64 78 69 65 39 4D 6C  [013701cymdxie9Ml]
*Oct 31 21:50:29.536: RADIUS:   56 66 65 4B 59 63 49 78 6F 63 76 66 61 5F 78 39  [VfeKYcIxocvfa_x9]
*Oct 31 21:50:29.536: RADIUS:   2F 5F 48 78 4C 76 35 68 70 39 61 31 51 6C 75 4C  [/_HxLv5hp9a1QluL]
*Oct 31 21:50:29.540: RADIUS:   34                 [ 4]
*Oct 31 21:50:29.540: RADIUS:  Class               [25]  81  
*Oct 31 21:50:29.544: RADIUS:   43 41 43 53 3A 39 36 30 31 33 37 30 31 63 79 6D  [CACS:96013701cym]
*Oct 31 21:50:29.544: RADIUS:   64 78 69 65 39 4D 6C 56 66 65 4B 59 63 49 78 6F  [dxie9MlVfeKYcIxo]
*Oct 31 21:50:29.548: RADIUS:   63 76 66 61 5F 78 39 2F 5F 48 78 4C 76 35 68 70  [cvfa_x9/_HxLv5hp]
*Oct 31 21:50:29.548: RADIUS:   39 61 31 51 6C 75 4C 34 3A 45 4E 54 45 52 50 52  [9a1QluL4:ENTERPR]
*Oct 31 21:50:29.548: RADIUS:   49 53 45 2F 32 39 38 37 37 35 30 32 33 2F 38   [ ISE/298775023/8]
*Oct 31 21:50:29.548: RADIUS(00000014): Received from id 1645/8