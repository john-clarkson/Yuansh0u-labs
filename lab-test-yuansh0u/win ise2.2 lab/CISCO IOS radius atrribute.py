Router#show aaa attributes protocol radius          

AAA ATTRIBUTE LIST:
    Type=1     Name=disc-cause-ext                 Format=Enum
        Protocol:RADIUS
        Unknown       Type=195   Name=Ascend-Disconnect-Cau Format=Enum      
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=2     Name=Acct-Status-Type               Format=Enum
        Protocol:RADIUS
        Unknown       Type=40    Name=Acct-Status-Type      Format=Enum      
    Type=3     Name=Tunnel-Packets-Lost            Format=Ulong
        Protocol:RADIUS
        Unknown       Type=86    Name=Tunnel-Packets-Lost   Format=Ulong     
    Type=4     Name=acl                            Format=String
        Protocol:RADIUS
        Unknown       Type=11    Name=Filter-Id             Format=Binary    
    Type=5     Name=auth-services                  Format=Enum
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=6     Name=auto-logon-service             Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=7     Name=azn-tag                        Format=String
    Type=8     Name=addr                           Format=IPv4 Address
        Protocol:RADIUS
        Unknown       Type=8     Name=Framed-IP-Address     Format=IPv4 Addre
    Type=9     Name=svc-assigned-ipv4-address      Format=IPv4 Address
        Protocol:RADIUS
        Unknown       Type=8     Name=Framed-IP-Address     Format=IPv4 Addre
    Type=10    Name=addrv6                         Format=IPv6 Address
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=11    Name=addr-pool                      Format=String
        Protocol:RADIUS
        Unknown       Type=88    Name=Framed-IP-Pool        Format=String    
        Unknown       Type=100   Name=Framed-IPv6-Pool      Format=String    
        Unknown       Type=218   Name=Ascend-IP-Pool        Format=Ulong     
    Type=12    Name=subscriber-route               Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=13    Name=asyncmap                       Format=Ulong
        Protocol:RADIUS
        Unknown       Type=212   Name=Ascend-Asyncmap       Format=Ulong     
    Type=14    Name=Authentic                      Format=Enum
        Protocol:RADIUS
        Unknown       Type=45    Name=Acct-Authentic        Format=Enum      
    Type=15    Name=autocmd                        Format=String
    Type=16    Name=autocmd_ipprompt               Format=String
    Type=17    Name=authen-status                  Format=Enum
    Type=18    Name=authen-method                  Format=Enum
    Type=19    Name=authen-strength                Format=Enum
    Type=20    Name=callback-dialstring            Format=String
        Protocol:RADIUS
        Unknown       Type=19    Name=Callback-Number       Format=String    
        Unknown       Type=227   Name=Ascend-Dial-Number    Format=String    
    Type=21    Name=callback-line                  Format=Ulong
    Type=22    Name=nocallback-verify              Format=Ulong
    Type=23    Name=callback-rotary                Format=Ulong
    Type=24    Name=call-drops                     Format=Ulong
    Type=25    Name=call_type                      Format=String
        Protocol:RADIUS
        Cisco VSA     Type=19    Name=call_type             Format=String    
    Type=26    Name=force-local-chap               Format=Boolean
    Type=27    Name=call-origin-endpt              Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=28    Name=call-origin-endpt-type         Format=Enum
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=29    Name=challenge                      Format=Binary
        Protocol:RADIUS
        Unknown       Type=60    Name=CHAP-Challenge        Format=Binary    
    Type=30    Name=id                             Format=Ulong
        Protocol:RADIUS
        Unknown       Type=3     Name=CHAP-Password         Format=Binary    
    Type=31    Name=response                       Format=Binary
        Protocol:RADIUS
        Unknown       Type=3     Name=CHAP-Password         Format=Binary    
    Type=32    Name=chap-authen-user               Format=String
    Type=33    Name=nas-connect-info               Format=String
        Protocol:RADIUS
        Unknown       Type=77    Name=Connect-Info          Format=String    
    Type=34    Name=user-data                      Format=Binary
    Type=35    Name=server-data                    Format=Binary
    Type=36    Name=clid                           Format=String
    Type=37    Name=formatted-clid                 Format=String
        Protocol:RADIUS
        Unknown       Type=31    Name=Calling-Station-Id    Format=String    
    Type=38    Name=circuit-id-tag                 Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=39    Name=remote-id-tag                  Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=40    Name=vendor-class-id-tag            Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=41    Name=caller-type-of-number          Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=42    Name=clid-mac-addr                  Format=Binary
    Type=43    Name=session-limit                  Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=44    Name=client-mac-address             Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=45    Name=protocolVersion                Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=46    Name=peerMode                       Format=Enum
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=47    Name=keepalivePeriod                Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=48    Name=informOwnerOnPull              Format=Enum
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=49    Name=acct-flows                     Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=50    Name=acct-flows-duration            Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=51    Name=actual-data-rate-upstream      Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=52    Name=actual-data-rate-downstream    Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=53    Name=minimum-data-rate-upstream     Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=54    Name=minimum-data-rate-downstream   Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=55    Name=attainable-data-rate-upstream  Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=56    Name=attainable-data-rate-downstrea Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=57    Name=maximum-data-rate-upstream     Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=58    Name=maximum-data-rate-downstream   Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=59    Name=minimum-data-rate-upstream-low Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=60    Name=minimum-data-rate-downstream-l Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=61    Name=maximum-interleaving-delay-ups Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=62    Name=maximum-interleaving-delay-dow Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=63    Name=actual-interleaving-delay-upst Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=64    Name=actual-interleaving-delay-down Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=65    Name=interworking-functionality-tag Format=Boolean
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=66    Name=access-loop-encapsulation      Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=67    Name=reporting-reason               Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=68    Name=dsl-type                       Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=69    Name=ancp-line-rate                 Format=Binary
        Protocol:RADIUS
        Cisco VSA     Type=201   Name=ancp-line-rate        Format=Binary    
    Type=70    Name=nas-rx-speed-kbps              Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=71    Name=nas-tx-speed-kbps              Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=72    Name=ancp-access-loop-cir-id        Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=73    Name=cmd                            Format=String
    Type=74    Name=cmd-arg                        Format=String
    Type=75    Name=connect-progress               Format=Enum
        Protocol:RADIUS
        Unknown       Type=196   Name=Ascend-Connection-Pro Format=Enum      
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=76    Name=connect-rx-speed               Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=77    Name=connect-tx-speed               Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=78    Name=nas-rx-speed                   Format=Ulong
        Protocol:RADIUS
        Unknown       Type=197   Name=Ascend-Data-Rate      Format=Ulong     
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=79    Name=data-service                   Format=Ulong
        Protocol:RADIUS
        Unknown       Type=247   Name=Ascend-Data-Service   Format=Ulong     
    Type=80    Name=dial-number                    Format=String
    Type=81    Name=trunkgroup                     Format=String
    Type=82    Name=dnis                           Format=String
        Protocol:RADIUS
        Unknown       Type=30    Name=Called-Station-Id     Format=String    
    Type=83    Name=dns-servers                    Format=String
    Type=84    Name=auto-update                    Format=String
    Type=85    Name=primary-dns                    Format=IPv4 Address
        Protocol:RADIUS
        Unknown       Type=135   Name=Ascend-Client-Primary Format=IPv4 Addre
        Microsoft VSA Type=28    Name=MS-Primary-DNS        Format=IPv4 Addre
    Type=86    Name=secondary-dns                  Format=IPv4 Address
        Protocol:RADIUS
        Unknown       Type=136   Name=Ascend-Client-Seconda Format=IPv4 Addre
        Microsoft VSA Type=29    Name=MS-Secondary-DNS      Format=IPv4 Addre
    Type=87    Name=EAP-Message                    Format=String
        Protocol:RADIUS
        Unknown       Type=79    Name=EAP-Message           Format=Binary    
    Type=88    Name=EAP-session-id                 Format=String
        Protocol:RADIUS
        Unknown       Type=102   Name=EAP-Key-Name          Format=Binary    
    Type=89    Name=assign-client-dns              Format=Ulong
        Protocol:RADIUS
        Unknown       Type=137   Name=Ascend-Client-Assign- Format=Ulong     
    Type=90    Name=email_server_ack_flag          Format=String
        Protocol:RADIUS
        Cisco VSA     Type=17    Name=email_server_ack_flag Format=String    
    Type=91    Name=event                          Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=92    Name=reason                         Format=String
    Type=93    Name=fax_account_id_origin          Format=String
        Protocol:RADIUS
        Cisco VSA     Type=3     Name=fax_account_id_origin Format=String    
    Type=94    Name=fax_auth_status                Format=String
        Protocol:RADIUS
        Cisco VSA     Type=15    Name=fax_auth_status       Format=String    
    Type=95    Name=fax_connect_speed              Format=String
        Protocol:RADIUS
        Cisco VSA     Type=8     Name=fax_connect_speed     Format=String    
    Type=96    Name=fax_coverpage_flag             Format=Boolean
    Type=97    Name=fax_dsn_address                Format=IPv4 Address
    Type=98    Name=fax_dsn_flag                   Format=Boolean
    Type=99    Name=fax_mdn_address                Format=String
        Protocol:RADIUS
        Cisco VSA     Type=13    Name=fax_mdn_address       Format=String    
    Type=100   Name=fax_mdn_flag                   Format=String
        Protocol:RADIUS
        Cisco VSA     Type=14    Name=fax_mdn_flag          Format=String    
    Type=101   Name=fax_msg_id                     Format=String
        Protocol:RADIUS
        Cisco VSA     Type=4     Name=fax_msg_id            Format=String    
    Type=102   Name=fax_modem_time                 Format=String
        Protocol:RADIUS
        Cisco VSA     Type=7     Name=fax_modem_time        Format=String    
    Type=103   Name=fax_pages                      Format=String
        Protocol:RADIUS
        Cisco VSA     Type=5     Name=fax_pages             Format=String    
    Type=104   Name=abort_cause                    Format=String
        Protocol:RADIUS
        Cisco VSA     Type=21    Name=abort_cause           Format=String    
    Type=105   Name=email_server_address           Format=String
        Protocol:RADIUS
        Cisco VSA     Type=16    Name=email_server_address  Format=String    
    Type=106   Name=fax_process_abort_flag         Format=Boolean
    Type=107   Name=fax_recipient_count            Format=Ulong
    Type=108   Name=filter-cache-refresh           Format=Enum
        Protocol:RADIUS
        Unknown       Type=56    Name=Ascend-Cache-Refresh  Format=Enum      
    Type=109   Name=filter-cache-time              Format=Ulong
        Protocol:RADIUS
        Unknown       Type=57    Name=Ascend-Cache-Time     Format=Ulong     
    Type=110   Name=filter-required                Format=Enum
        Protocol:RADIUS
        Unknown       Type=50    Name=Ascend-Filter-Require Format=Enum      
    Type=111   Name=Framed-Protocol                Format=Enum
        Protocol:RADIUS
        Unknown       Type=7     Name=Framed-Protocol       Format=Enum      
    Type=112   Name=Framed-MTU                     Format=Ulong
        Protocol:RADIUS
        Unknown       Type=12    Name=Framed-MTU            Format=Ulong     
    Type=113   Name=force-56                       Format=Boolean
        Protocol:RADIUS
        Unknown       Type=248   Name=Ascend-Force-56       Format=Ulong     
    Type=114   Name=gateway_id                     Format=String
        Protocol:RADIUS
        Cisco VSA     Type=18    Name=gateway_id            Format=String    
    Type=115   Name=ggsn grouped                   Format=Grouped
    Type=116   Name=h323-billing-model             Format=String
        Protocol:RADIUS
        Cisco VSA     Type=109   Name=h323-billing-model    Format=String    
    Type=117   Name=h323-call-origin               Format=String
        Protocol:RADIUS
        Cisco VSA     Type=26    Name=h323-call-origin      Format=String    
    Type=118   Name=h323-call-type                 Format=String
        Protocol:RADIUS
        Cisco VSA     Type=27    Name=h323-call-type        Format=String    
    Type=119   Name=h323-conf-id                   Format=String
        Protocol:RADIUS
        Cisco VSA     Type=24    Name=Conf-Id               Format=String    
    Type=120   Name=h323-connect-time              Format=String
        Protocol:RADIUS
        Cisco VSA     Type=28    Name=h323-connect-time     Format=String    
    Type=121   Name=h323-credit-amount             Format=String
        Protocol:RADIUS
        Cisco VSA     Type=101   Name=h323-credit-amount    Format=String    
    Type=122   Name=h323-credit-time               Format=String
        Protocol:RADIUS
        Cisco VSA     Type=102   Name=h323-credit-time      Format=String    
    Type=123   Name=h323-currency                  Format=String
        Protocol:RADIUS
        Cisco VSA     Type=110   Name=h323-currency         Format=String    
    Type=124   Name=h323-disconnect-cause          Format=String
        Protocol:RADIUS
        Cisco VSA     Type=30    Name=h323-disconnect-cause Format=String    
    Type=125   Name=h323-disconnect-time           Format=String
        Protocol:RADIUS
        Cisco VSA     Type=29    Name=h323-disconnect-time  Format=String    
    Type=126   Name=h323-gw-id                     Format=String
        Protocol:RADIUS
        Cisco VSA     Type=33    Name=h323-gw-id            Format=String    
    Type=127   Name=h323-incoming-conf-id          Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=128   Name=h323-ivr-in                    Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=129   Name=h323-ivr-out                   Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=130   Name=h323-preferred-lang            Format=String
        Protocol:RADIUS
        Cisco VSA     Type=107   Name=h323-preferred-lang   Format=String    
    Type=131   Name=h323-prompt-id                 Format=String
        Protocol:RADIUS
        Cisco VSA     Type=104   Name=h323-prompt-id        Format=String    
    Type=132   Name=h323-redirect-ip-address       Format=String
        Protocol:RADIUS
        Cisco VSA     Type=108   Name=h323-redirect-ip-addr Format=String    
    Type=133   Name=h323-redirect-number           Format=String
        Protocol:RADIUS
        Cisco VSA     Type=106   Name=h323-redirect-number  Format=String    
    Type=134   Name=h323-remote-address            Format=String
        Protocol:RADIUS
        Cisco VSA     Type=23    Name=h323-remote-address   Format=String    
    Type=135   Name=h323-remote-id                 Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=136   Name=h323-return-code               Format=String
        Protocol:RADIUS
        Cisco VSA     Type=103   Name=h323-return-code      Format=String    
    Type=137   Name=h323-setup-time                Format=String
        Protocol:RADIUS
        Cisco VSA     Type=25    Name=h323-setup-time       Format=String    
    Type=138   Name=h323-time-and-day              Format=String
        Protocol:RADIUS
        Cisco VSA     Type=105   Name=h323-time-and-day     Format=String    
    Type=139   Name=h323-voice-quality             Format=String
        Protocol:RADIUS
        Cisco VSA     Type=31    Name=h323-voice-quality    Format=String    
    Type=140   Name=subscriber                     Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=141   Name=release-source                 Format=Enum
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=142   Name=idletime                       Format=Ulong
        Protocol:RADIUS
        Unknown       Type=28    Name=Idle-Timeout          Format=Ulong     
        Unknown       Type=244   Name=Ascend-Idle-Limit     Format=Ulong     
    Type=143   Name=call-inacl                     Format=String
        Protocol:RADIUS
        Unknown       Type=243   Name=Ascend-Call-Filter    Format=Binary    
    Type=144   Name=inacl                          Format=String
        Protocol:RADIUS
        Unknown       Type=242   Name=Ascend-Data-Filter    Format=Binary    
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=145   Name=input-giga-words               Format=Ulong
        Protocol:RADIUS
        Unknown       Type=52    Name=Acct-Input-Giga-Words Format=Ulong     
    Type=146   Name=bytes_in                       Format=Ulong
        Protocol:RADIUS
        Unknown       Type=42    Name=Acct-Input-Octets     Format=Ulong     
    Type=147   Name=paks_in                        Format=Ulong
        Protocol:RADIUS
        Unknown       Type=47    Name=Acct-Input-Packets    Format=Ulong     
    Type=148   Name=acct-input-gigawords-ipv6      Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=149   Name=acct-input-octets-ipv6         Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=150   Name=acct-input-packets-ipv6        Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=151   Name=tariff-input-giga-words        Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=152   Name=tariff-input-octets            Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=153   Name=tariff-input-packets           Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=154   Name=tariff-input-giga-words-ipv6   Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=155   Name=tariff-input-octets-ipv6       Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=156   Name=tariff-input-packets-ipv6      Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=157   Name=tariff-output-giga-words       Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=158   Name=tariff-output-octets           Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=159   Name=tariff-output-packets          Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=160   Name=tariff-output-giga-words-ipv6  Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=161   Name=tariff-output-octets-ipv6      Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=162   Name=tariff-output-packets-ipv6     Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=163   Name=idmgr-data                     Format=Binary
    Type=164   Name=idmgr-svc-key                  Format=Binary
    Type=165   Name=pppoe-unique-key               Format=String
    Type=166   Name=session-guid                   Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=167   Name=nas-identifier                 Format=String
        Protocol:RADIUS
        Unknown       Type=32    Name=Nas-Identifier        Format=String    
    Type=168   Name=charged-units                  Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=169   Name=disconnect-text                Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=170   Name=info-type                      Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=171   Name=logical-if-index               Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=172   Name=peer-address                   Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=173   Name=peer-id                        Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=174   Name=peer-if-index                  Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=175   Name=acom-level                     Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=176   Name=tx-duration                    Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=177   Name=voice-tx-duration              Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=178   Name=noise-level                    Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=179   Name=codec-bytes                    Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=180   Name=coder-type-rate                Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=181   Name=early-packets                  Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=182   Name=late-packets                   Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=183   Name=lost-packets                   Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=184   Name=gapfill-with-interpolation     Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=185   Name=gapfill-with-prediction        Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=186   Name=gapfill-with-redundancy        Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=187   Name=gapfill-with-silence           Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=188   Name=lowater-playout-delay          Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=189   Name=hiwater-playout-delay          Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=190   Name=ontime-rv-playout              Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=191   Name=receive-delay                  Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=192   Name=round-trip-delay               Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=193   Name=remote-udp-port                Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=194   Name=session-protocol               Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=195   Name=vad-enable                     Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=196   Name=incoming-area                  Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=197   Name=outgoing-area                  Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=198   Name=in-intrfc-desc                 Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=199   Name=out-intrfc-desc                Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=200   Name=service-descriptor             Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=201   Name=in-carrier-id                  Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=202   Name=out-carrier-id                 Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=203   Name=in-trunkgroup-label            Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=204   Name=out-trunkgroup-label           Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=205   Name=alert-timepoint                Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=206   Name=gw-rxd-cdn                     Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=207   Name=gw-rxd-cgn                     Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=208   Name=gtd-gw-rxd-ocn                 Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=209   Name=gtd-gw-rxd-cnn                 Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=210   Name=gw-rxd-rdn                     Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=211   Name=gw-final-xlated-cdn            Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=212   Name=gw-final-xlated-cgn            Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=213   Name=gw-final-xlated-rdn            Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=214   Name=gk-xlated-cdn                  Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=215   Name=gk-xlated-cgn                  Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=216   Name=gw-collected-cdn               Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=217   Name=gtd-orig-cic                   Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=218   Name=gtd-term-cic                   Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=219   Name=Termination-Action             Format=Boolean
        Protocol:RADIUS
        Unknown       Type=29    Name=Termination-Action    Format=Boolean   
    Type=220   Name=aaa-unique-id                  Format=Ulong
    Type=221   Name=interface                      Format=String
        Protocol:RADIUS
        Cisco VSA     Type=2     Name=cisco-nas-port        Format=String    
        Unknown       Type=5     Name=NAS-Port              Format=Ulong     
        Unknown       Type=87    Name=NAS-Port-Id           Format=String    
    Type=222   Name=interface-config               Format=String
    Type=223   Name=parent-interface               Format=String
    Type=224   Name=parent-interface-type          Format=Enum
    Type=225   Name=port-type                      Format=Enum
        Protocol:RADIUS
        Unknown       Type=61    Name=NAS-Port-Type         Format=Enum      
    Type=226   Name=acct-interval                  Format=Ulong
        Protocol:RADIUS
        Unknown       Type=85    Name=Acct-Interim-Interval Format=Ulong     
    Type=227   Name=ip-addresses                   Format=String
    Type=228   Name=ip-address-limits              Format=String
    Type=229   Name=key-exchange                   Format=String
    Type=230   Name=vpdn-template                  Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=231   Name=l2f-cm-retransmit-retries      Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=232   Name=l2f-init-retransmit-retries    Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=233   Name=l2f-tunnel-timeout-setup       Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=234   Name=l2f-busy-list-timeout          Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=235   Name=l2tp-busy-disconnect           Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=236   Name=l2tp-framing-capabilities      Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=237   Name=l2tp-bearer-capabilities       Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=238   Name=l2tp-cm-local-window-size      Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=239   Name=l2tp-cm-max-timeout            Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=240   Name=l2tp-cm-min-timeout            Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=241   Name=l2tp-init-max-timeout          Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=242   Name=l2tp-init-min-timeout          Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=243   Name=l2tp-init-retransmit-retries   Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=244   Name=l2tp-busy-list-timeout         Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=245   Name=l2tp-drop-out-of-order         Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=246   Name=l2tp-hello-interval            Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=247   Name=l2tp-hidden-avp                Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=248   Name=l2tp-rx-speed                  Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=249   Name=l2tp-tx-speed                  Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=250   Name=l2tp-ignore-connect-speed      Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=251   Name=l2tp-max-ato                   Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=252   Name=l2tp-nosession-timeout         Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=253   Name=relay-pppoe-bba-group          Format=String
    Type=254   Name=l2tp-queue-size                Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=255   Name=l2tp-recv-win                  Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=256   Name=l2tp-cm-retransmit-retries     Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=257   Name=l2tp-sequencing                Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=258   Name=l2tp-static-rtt                Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=259   Name=l2tp-tunnel-authen             Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=260   Name=l2tp-tunnel-acct               Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=261   Name=l2tp-tunnel-password           Format=Binary
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=262   Name=l2tp-tunnel-timeout-setup      Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=263   Name=l2tp-clid-mask-method          Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=264   Name=l2tp-udp-checksum              Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=265   Name=l2tp-security-ip-address-check Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=266   Name=l2tp-security-required         Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=267   Name=l2tp-security-keep-sa          Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=268   Name=l2tp-tunnel-resync-packets     Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=269   Name=link-compression               Format=Enum
        Protocol:RADIUS
        Unknown       Type=13    Name=Framed-Compression    Format=Enum      
        Unknown       Type=233   Name=Ascend-Link-Compressi Format=Enum      
    Type=270   Name=map-class                      Format=String
    Type=271   Name=error-cause                    Format=Enum
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=272   Name=error-cause                    Format=Enum
        Protocol:RADIUS
        Unknown       Type=101   Name=Dynamic-Author-Error- Format=Enum      
    Type=273   Name=reply-message                  Format=String
        Protocol:RADIUS
        Unknown       Type=18    Name=Reply-Message         Format=Binary    
    Type=274   Name=Message-Authenticator          Format=Binary
        Protocol:RADIUS
        Unknown       Type=80    Name=Message-Authenticator Format=Binary    
    Type=275   Name=mlp-links-current              Format=Ulong
        Protocol:RADIUS
        Unknown       Type=188   Name=Ascend-Num-In-Multili Format=Ulong     
    Type=276   Name=mlp-links-max                  Format=Ulong
        Protocol:RADIUS
        Unknown       Type=51    Name=Acct-Link-Count       Format=Ulong     
    Type=277   Name=mlp-sess-id                    Format=Ulong
        Protocol:RADIUS
        Unknown       Type=50    Name=Multilink-Session-ID  Format=String    
        Unknown       Type=187   Name=Ascend-Multilink-Sess Format=Ulong     
    Type=278   Name=modem-on-hold                  Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=279   Name=modem-script                   Format=String
    Type=280   Name=spi                            Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=281   Name=static-ip-pool                 Format=String
    Type=282   Name=static-ip-addresses            Format=String
    Type=283   Name=ip-pool                        Format=String
    Type=284   Name=ip-address                     Format=String
    Type=285   Name=static-pool-def                Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=286   Name=static-addr-pool               Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=287   Name=mobileip-rfswact               Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=288   Name=dhcp-server                    Format=IPv4 Address
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=289   Name=mobile-ip-dhcp-server          Format=String
    Type=290   Name=classname                      Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=291   Name=config-source-dpm              Format=Boolean
    Type=292   Name=mcast-client                   Format=Boolean
        Protocol:RADIUS
        Unknown       Type=155   Name=Ascend-Multicast-Clie Format=Ulong     
    Type=293   Name=mcast-rlimit                   Format=Ulong
        Protocol:RADIUS
        Unknown       Type=152   Name=Ascend-Multicast-Rate Format=Ulong     
    Type=294   Name=idle-threshold                 Format=Ulong
    Type=295   Name=load-threshold                 Format=Ulong
        Protocol:RADIUS
        Unknown       Type=234   Name=Ascend-Target-Util    Format=Ulong     
    Type=296   Name=max-links                      Format=Ulong
        Protocol:RADIUS
        Unknown       Type=235   Name=Ascend-Max-Channels   Format=Ulong     
    Type=297   Name=min-links                      Format=Ulong
    Type=298   Name=ppp-multilink                  Format=Ulong
    Type=299   Name=nas-description                Format=String
    Type=300   Name=nbns-primary-server            Format=IPv4 Address
        Protocol:RADIUS
        Microsoft VSA Type=30    Name=MS-1st-NBNS-Server    Format=IPv4 Addre
    Type=301   Name=nbns-secondary-server          Format=IPv4 Address
        Protocol:RADIUS
        Microsoft VSA Type=31    Name=MS-2nd-NBNS-Server    Format=IPv4 Addre
    Type=302   Name=num-sessions                   Format=Ulong
    Type=303   Name=netmask                        Format=IPv4 Address
        Protocol:RADIUS
        Unknown       Type=9     Name=Framed-IP-Netmask     Format=IPv4 Addre
    Type=304   Name=noescape                       Format=Boolean
    Type=305   Name=nohangup                       Format=Boolean
    Type=306   Name=old-password                   Format=Binary
        Protocol:RADIUS
        Unknown       Type=17    Name=Old-Password          Format=Binary    
    Type=307   Name=old-prompts                    Format=Boolean
    Type=308   Name=call-outacl                    Format=String
        Protocol:RADIUS
        Unknown       Type=243   Name=Ascend-Call-Filter    Format=Binary    
    Type=309   Name=output-giga-words              Format=Ulong
        Protocol:RADIUS
        Unknown       Type=53    Name=Acct-Output-Giga-Word Format=Ulong     
    Type=310   Name=outacl                         Format=String
        Protocol:RADIUS
        Unknown       Type=242   Name=Ascend-Data-Filter    Format=Binary    
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=311   Name=bytes_out                      Format=Ulong
        Protocol:RADIUS
        Unknown       Type=43    Name=Acct-Output-Octets    Format=Ulong     
    Type=312   Name=paks_out                       Format=Ulong
        Protocol:RADIUS
        Unknown       Type=48    Name=Acct-Output-Packets   Format=Ulong     
    Type=313   Name=acct-output-gigawords-ipv6     Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=314   Name=acct-output-octets-ipv6        Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=315   Name=acct-output-packets-ipv6       Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=316   Name=port-bndl-hkey                 Format=Binary
    Type=317   Name=nativeip-vrf                   Format=Binary
    Type=318   Name=domainip-vrf                   Format=Binary
    Type=319   Name=system-script                  Format=String
    Type=320   Name=password                       Format=Binary
        Protocol:RADIUS
        Unknown       Type=2     Name=User-Password         Format=Binary    
        Cisco VSA     Type=249   Name=Subscriber-password   Format=Binary    
    Type=321   Name=pool-def                       Format=String
        Protocol:RADIUS
        Unknown       Type=217   Name=ascend_pool_definitio Format=String    
    Type=322   Name=pool-addr                      Format=IPv4 Address
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=323   Name=pool-mask                      Format=IPv4 Address
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=324   Name=pool-timeout                   Format=Ulong
    Type=325   Name=port                           Format=String
    Type=326   Name=Port-Limit                     Format=Ulong
        Protocol:RADIUS
        Unknown       Type=62    Name=Port-Limit            Format=Ulong     
    Type=327   Name=port_used                      Format=String
        Protocol:RADIUS
        Cisco VSA     Type=20    Name=port_used             Format=String    
    Type=328   Name=ppp-vj-slot-compression        Format=Boolean
    Type=329   Name=ppp-disconnect-cause           Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=330   Name=pre-bytes-in                   Format=Ulong
        Protocol:RADIUS
        Unknown       Type=190   Name=Ascend-Presession-Oct Format=Ulong     
    Type=331   Name=pre-bytes-out                  Format=Ulong
        Protocol:RADIUS
        Unknown       Type=191   Name=Ascend-Presession-Oct Format=Ulong     
    Type=332   Name=pre-paks-in                    Format=Ulong
        Protocol:RADIUS
        Unknown       Type=192   Name=Ascend-Presession-Pac Format=Ulong     
    Type=333   Name=pre-paks-out                   Format=Ulong
        Protocol:RADIUS
        Unknown       Type=193   Name=Ascend-Presession-Pac Format=Ulong     
    Type=334   Name=pre-session-time               Format=Ulong
        Protocol:RADIUS
        Unknown       Type=198   Name=Ascend-Presession-Tim Format=Ulong     
    Type=335   Name=priv-lvl                       Format=Ulong
    Type=336   Name=cli-view-name                  Format=String
    Type=337   Name=protocol                       Format=Enum
    Type=338   Name=proxyacl                       Format=String
    Type=339   Name=auth-required                  Format=Ulong
        Protocol:RADIUS
        Unknown       Type=201   Name=Ascend-Require-Auth   Format=Ulong     
    Type=340   Name=auth-type                      Format=String
        Protocol:RADIUS
        Unknown       Type=81    Name=Ascend-Auth-Type      Format=Ulong     
    Type=341   Name=nas-location                   Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=342   Name=auth-algo-type                 Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=343   Name=vlan-id                        Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=344   Name=service-type                   Format=Enum
        Protocol:RADIUS
        Unknown       Type=6     Name=Service-Type          Format=Enum      
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=345   Name=session-key                    Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=346   Name=ssid                           Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=347   Name=admin-capability               Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=348   Name=modem-service                  Format=String
    Type=349   Name=redirected-station             Format=String
        Protocol:RADIUS
        Unknown       Type=93    Name=Ascend-Redirect-Numbe Format=String    
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=350   Name=reload-user                    Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=351   Name=reload-reason                  Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=352   Name=ios-version                    Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=353   Name=shared-profile-enable          Format=Boolean
        Protocol:RADIUS
        Unknown       Type=128   Name=Ascend-Shared-Profile Format=Boolean   
    Type=354   Name=resource-service               Format=Enum
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=355   Name=rm-call-count                  Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=356   Name=rm-call-handle                 Format=String
    Type=357   Name=rm-call-treatment              Format=String
    Type=358   Name=rm-call-type                   Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=359   Name=rm-cp-name                     Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=360   Name=rm-dnis-group-name             Format=String
    Type=361   Name=rm-link-type                   Format=String
    Type=362   Name=multilink-id                   Format=String
    Type=363   Name=rm-nas-state                   Format=String
    Type=364   Name=rm-port-description            Format=String
    Type=365   Name=rm-request-type                Format=String
    Type=366   Name=rm-response-code               Format=String
    Type=367   Name=rm-application                 Format=String
    Type=368   Name=rm-rg-name                     Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=369   Name=rm-rg-service                  Format=String
    Type=370   Name=rm-rg-service-name             Format=String
    Type=371   Name=rm-server-state                Format=String
    Type=372   Name=rm-template-name               Format=String
    Type=373   Name=rm-protocol-version            Format=String
    Type=374   Name=rm-vpdn-tunnel-status          Format=Enum
    Type=375   Name=rm-overflow-flag               Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=376   Name=negotiated-route               Format=String
    Type=377   Name=route                          Format=String
        Protocol:RADIUS
        Unknown       Type=22    Name=Framed-Route          Format=String    
        Unknown       Type=99    Name=Framed-IPv6-Route     Format=String    
        Unknown       Type=209   Name=Ascend-IP-Direct      Format=IPv4 Addre
    Type=378   Name=pw-lifetime                    Format=Ulong
        Protocol:RADIUS
        Unknown       Type=208   Name=Ascend-PW-Liftime     Format=Ulong     
    Type=379   Name=ppp-vj-slot-comp               Format=Boolean
        Protocol:RADIUS
        Unknown       Type=210   Name=Ascend-PPP-VJ-Slot-Co Format=Boolean   
    Type=380   Name=route-ip                       Format=Boolean
        Protocol:RADIUS
        Unknown       Type=228   Name=Ascend-Route-IP       Format=Boolean   
    Type=381   Name=tunnel-private-group-id        Format=String
        Protocol:RADIUS
        Unknown       Type=81    Name=Tunnel-Private-Group- Format=String    
    Type=382   Name=state                          Format=Binary
        Protocol:RADIUS
        Unknown       Type=24    Name=State                 Format=Binary    
    Type=383   Name=class                          Format=Binary
        Protocol:RADIUS
        Unknown       Type=25    Name=Class                 Format=Binary    
    Type=384   Name=rte-fltr-in                    Format=String
    Type=385   Name=rte-fltr-out                   Format=String
    Type=386   Name=routing                        Format=Boolean
        Protocol:RADIUS
        Unknown       Type=10    Name=Framed-Routing        Format=Ulong     
    Type=387   Name=sap                            Format=String
    Type=388   Name=sap-fltr-in                    Format=String
    Type=389   Name=sap-fltr-out                   Format=String
    Type=390   Name=send-auth                      Format=Enum
        Protocol:RADIUS
        Unknown       Type=231   Name=Ascend-Send-Auth      Format=Enum      
    Type=391   Name=send-name                      Format=String
    Type=392   Name=tunnel-tos-reflect             Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=393   Name=tunnel-tos-setting             Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=394   Name=tunnel-pmtu                    Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=395   Name=tunnel-lcp-renego              Format=Ulong
    Type=396   Name=tunnel-ip-mtu-adjust           Format=Boolean
    Type=397   Name=remote-name                    Format=String
    Type=398   Name=send-secret                    Format=Binary
        Protocol:RADIUS
        Unknown       Type=214   Name=Ascend-Send-Secret    Format=Binary    
    Type=399   Name=server-admin-msg               Format=String
    Type=400   Name=svr-key                        Format=Binary
    Type=401   Name=server-name                    Format=String
    Type=402   Name=session-service                Format=Enum
    Type=403   Name=service-name                   Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=404   Name=parent-session-id              Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=405   Name=service                        Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=406   Name=event                          Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=407   Name=auto-smart-port                Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=408   Name=session-id                     Format=Ulong
        Protocol:RADIUS
        Unknown       Type=44    Name=Acct-Session-Id       Format=String    
    Type=409   Name=session-handle                 Format=Ulong
    Type=410   Name=acct_record_number             Format=Ulong
    Type=411   Name=accounting-record-type         Format=Enum
    Type=412   Name=string-session-id              Format=String
        Protocol:RADIUS
        Unknown       Type=44    Name=Acct-Session-Id       Format=String    
    Type=413   Name=subscriber-label               Format=Ulong
    Type=414   Name=elapsed_time                   Format=Ulong
        Protocol:RADIUS
        Unknown       Type=46    Name=Acct-Session-Time     Format=Ulong     
    Type=415   Name=override-session-time          Format=Ulong
        Protocol:RADIUS
        Unknown       Type=46    Name=Acct-Session-Time     Format=Ulong     
    Type=416   Name=vrrs                           Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=417   Name=source-ip                      Format=IPv4 Address
    Type=418   Name=start_time                     Format=UTC
    Type=419   Name=stop_time                      Format=UTC
    Type=420   Name=sub-policy-In                  Format=String
        Protocol:RADIUS
        Cisco VSA     Type=37    Name=Sub_Policy_In         Format=String    
    Type=421   Name=sub-qos-policy-in              Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=422   Name=sub-policy-Out                 Format=String
        Protocol:RADIUS
        Cisco VSA     Type=38    Name=Sub_Policy_Out        Format=String    
    Type=423   Name=sub-qos-policy-out             Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=424   Name=acct-policy-map                Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=425   Name=acct-policy-in                 Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=426   Name=acct-policy-out                Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=427   Name=vc-qos-policy-in               Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=428   Name=vc-qos-policy-out              Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=429   Name=vc-weight                      Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=430   Name=vc-watermark-min               Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=431   Name=vc-watermark-max               Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=432   Name=qos-policy-in                  Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=433   Name=qos-policy-out                 Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=434   Name=disc-cause                     Format=Enum
        Protocol:RADIUS
        Unknown       Type=49    Name=Acct-Terminate-Cause  Format=Enum      
    Type=435   Name=timeout                        Format=Ulong
        Protocol:RADIUS
        Unknown       Type=27    Name=Session-Timeout       Format=Ulong     
        Unknown       Type=194   Name=Ascend-Max-Time       Format=Ulong     
    Type=436   Name=timezone                       Format=String
    Type=437   Name=tunnel-client-endpoint         Format=String
        Protocol:RADIUS
        Unknown       Type=66    Name=Tunnel-Client-Endpoin Format=String    
    Type=438   Name=tunnel-id                      Format=String
        Protocol:RADIUS
        Unknown       Type=90    Name=Tunnel-Client-Auth-ID Format=String    
    Type=439   Name=gw-name                        Format=String
        Protocol:RADIUS
        Unknown       Type=91    Name=Tunnel-Server-Auth-ID Format=String    
    Type=440   Name=tunnel-medium-type             Format=Enum
        Protocol:RADIUS
        Unknown       Type=65    Name=Tunnel-Medium-Type    Format=Enum      
    Type=441   Name=tunnel-password                Format=Binary
        Protocol:RADIUS
        Unknown       Type=69    Name=Tunnel-Password       Format=Binary    
    Type=442   Name=tunnel-preference              Format=Ulong
        Protocol:RADIUS
        Unknown       Type=83    Name=Tunnel-Preference     Format=Ulong     
    Type=443   Name=tunnel-server-endpoint         Format=String
        Protocol:RADIUS
        Unknown       Type=67    Name=Tunnel-Server-Endpoin Format=String    
    Type=444   Name=tunnel-connection-id           Format=String
        Protocol:RADIUS
        Unknown       Type=68    Name=Acct-Tunnel-Connectio Format=String    
    Type=445   Name=Event-Timestamp                Format=Ulong
        Protocol:RADIUS
        Unknown       Type=55    Name=Event-Timestamp       Format=Ulong     
    Type=446   Name=tunnel-direction               Format=Ulong
    Type=447   Name=tunnel-application-type        Format=Ulong
    Type=448   Name=tunnel-type                    Format=Enum
        Protocol:RADIUS
        Unknown       Type=64    Name=Tunnel-Type           Format=Enum      
    Type=449   Name=user-maxlinks                  Format=Ulong
    Type=450   Name=username                       Format=String
        Protocol:RADIUS
        Unknown       Type=1     Name=User-Name             Format=String    
    Type=451   Name=vpdn-active-sessions           Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=452   Name=v92-info                       Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=453   Name=vpdn-logging                   Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=454   Name=dout-type                      Format=Ulong
    Type=455   Name=vpdn-domain                    Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=456   Name=vpdn-group                     Format=String
        Protocol:RADIUS
        Unknown       Type=82    Name=Tunnel-Assignment-Id  Format=String    
    Type=457   Name=vpn-domain-list                Format=String
    Type=458   Name=dout-dialer                    Format=Boolean
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=459   Name=rotary-group                   Format=Ulong
    Type=460   Name=pool-member                    Format=Ulong
    Type=461   Name=vpdn-profile                   Format=String
    Type=462   Name=vpdn-scal-vtemplate            Format=Ulong
    Type=463   Name=vpdn-vtemplate                 Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=464   Name=vpdn-redirect-id               Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=465   Name=policy-directive               Format=String
    Type=466   Name=keepalive                      Format=String
    Type=467   Name=linksec-policy                 Format=Enum
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=468   Name=proxy-method-list              Format=String
    Type=469   Name=proxy-acct-method-list         Format=String
    Type=470   Name=sss-service                    Format=Enum
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=471   Name=vpn-id                         Format=String
    Type=472   Name=vpn-vrf                        Format=String
    Type=473   Name=wins-servers                   Format=String
    Type=474   Name=leap-session-key               Format=Binary
    Type=475   Name=wins-server-primary            Format=IPv4 Address
        Protocol:RADIUS
        Microsoft VSA Type=30    Name=MS-1st-NBNS-Server    Format=IPv4 Addre
    Type=476   Name=ikev2-password-local           Format=Binary
    Type=477   Name=ikev2-password-remote          Format=Binary
    Type=478   Name=wins-server-secondary          Format=IPv4 Address
        Protocol:RADIUS
        Microsoft VSA Type=31    Name=MS-2nd-NBNS-Server    Format=IPv4 Addre
    Type=479   Name=peak-cell-rate                 Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=480   Name=sustainable-cell-rate          Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=481   Name=nas-tx-speed                   Format=Ulong
        Protocol:RADIUS
        Unknown       Type=255   Name=Ascend-Xmit-Rate      Format=Ulong     
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=482   Name=zonelist                       Format=Ulong
    Type=483   Name=login-service                  Format=Enum
        Protocol:RADIUS
        Unknown       Type=15    Name=Login-Service         Format=Enum      
    Type=484   Name=sg-service                     Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=485   Name=sg-rule                        Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=486   Name=sg-condition                   Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=487   Name=sg-action                      Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=488   Name=ssg-account-info               Format=String
        Protocol:RADIUS
        Cisco VSA     Type=250   Name=ssg-account-info      Format=String    
    Type=489   Name=ssg-service-info               Format=String
        Protocol:RADIUS
        Cisco VSA     Type=251   Name=ssg-service-info      Format=String    
    Type=490   Name=ssg-command-code               Format=Binary
        Protocol:RADIUS
        Cisco VSA     Type=252   Name=ssg-command-code      Format=Binary    
    Type=491   Name=ssg-control-info               Format=String
        Protocol:RADIUS
        Cisco VSA     Type=253   Name=ssg-control-info      Format=String    
    Type=492   Name=ssg-cookie                     Format=String
    Type=493   Name=cdma-user-class                Format=Ulong
    Type=494   Name=cdma-realm                     Format=String
    Type=495   Name=mobileip-mn-ipaddr             Format=String
    Type=496   Name=mobileip-mn-lifetime           Format=Ulong
    Type=497   Name=mobileip-mn-flags              Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=498   Name=mobileip-mn-reject-code        Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=499   Name=mobileip-mn-local-timezone     Format=Boolean
    Type=500   Name=prohibited                     Format=Boolean
    Type=501   Name=mobileip-vrf-ha-addr           Format=IPv4 Address
    Type=502   Name=mobileip-registration-source-a Format=IPv4 Address
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=503   Name=cdma-preshared-secret          Format=Binary
        Protocol:RADIUS
        3GenPP2 VSA   Type=3     Name=cdma-preshared-secret Format=Binary    
        Cisco VSA     Type=34    Name=Cisco AVpair          Format=Binary    
    Type=504   Name=cdma-container                 Format=String
        Protocol:RADIUS
        3GenPP2 VSA   Type=6     Name=cdma-container        Format=String    
        Cisco VSA     Type=34    Name=Cisco AVpair          Format=Binary    
    Type=505   Name=cdma-correlation-id            Format=String
        Protocol:RADIUS
        3GenPP2 VSA   Type=44    Name=cdma-correlation-id   Format=String    
        Cisco VSA     Type=34    Name=Cisco AVpair          Format=Binary    
    Type=506   Name=cdma-always-on                 Format=Ulong
        Protocol:RADIUS
        3GenPP2 VSA   Type=78    Name=cdma-always-on        Format=Ulong     
        Cisco VSA     Type=34    Name=Cisco AVpair          Format=Binary    
    Type=507   Name=cdma-rn-pdit                   Format=Ulong
        Protocol:RADIUS
        3GenPP2 VSA   Type=82    Name=cdma-rn-pdit          Format=Ulong     
        Cisco VSA     Type=34    Name=Cisco AVpair          Format=Binary    
    Type=508   Name=cdma-session-continue          Format=Ulong
        Protocol:RADIUS
        3GenPP2 VSA   Type=48    Name=cdma-session-continue Format=Ulong     
        Cisco VSA     Type=34    Name=Cisco AVpair          Format=Binary    
    Type=509   Name=cdma-begin-session             Format=Ulong
        Protocol:RADIUS
        3GenPP2 VSA   Type=51    Name=cdma-begin-session    Format=Ulong     
        Cisco VSA     Type=34    Name=Cisco AVpair          Format=Binary    
    Type=510   Name=cdma-ha-ip-addr                Format=IPv4 Address
        Protocol:RADIUS
        3GenPP2 VSA   Type=7     Name=cdma-ha-ip-addr       Format=IPv4 Addre
        Cisco VSA     Type=34    Name=Cisco AVpair          Format=Binary    
    Type=511   Name=cdma-ipsec-preshared-secret-re Format=Ulong
        Protocol:RADIUS
        3GenPP2 VSA   Type=1     Name=cdma-ipsec-preshared- Format=Ulong     
        Cisco VSA     Type=34    Name=Cisco AVpair          Format=Binary    
    Type=512   Name=cdma-ipsec-security            Format=Ulong
        Protocol:RADIUS
        3GenPP2 VSA   Type=2     Name=cdma-ipsec-security   Format=Ulong     
        Cisco VSA     Type=34    Name=Cisco AVpair          Format=Binary    
    Type=513   Name=cdma-reverse-tnl-spec          Format=Ulong
        Protocol:RADIUS
        3GenPP2 VSA   Type=4     Name=cdma-reverse-tnl-spec Format=Ulong     
        Cisco VSA     Type=34    Name=Cisco AVpair          Format=Binary    
    Type=514   Name=cdma-pcf-ip-addr               Format=IPv4 Address
        Protocol:RADIUS
        3GenPP2 VSA   Type=9     Name=cdma-pcf-ip-addr      Format=IPv4 Addre
        Cisco VSA     Type=34    Name=Cisco AVpair          Format=Binary    
    Type=515   Name=cdma-bs-msc-addr               Format=String
        Protocol:RADIUS
        3GenPP2 VSA   Type=10    Name=cdma-bs-msc-addr      Format=String    
        Cisco VSA     Type=34    Name=Cisco AVpair          Format=Binary    
    Type=516   Name=cdma-user-id                   Format=Ulong
        Protocol:RADIUS
        3GenPP2 VSA   Type=11    Name=cdma-user-id          Format=Ulong     
        Cisco VSA     Type=34    Name=Cisco AVpair          Format=Binary    
    Type=517   Name=cdma-forward-mux               Format=Ulong
        Protocol:RADIUS
        3GenPP2 VSA   Type=12    Name=cdma-forward-mux      Format=Ulong     
        Cisco VSA     Type=34    Name=Cisco AVpair          Format=Binary    
    Type=518   Name=cdma-reverse-mux               Format=Ulong
        Protocol:RADIUS
        3GenPP2 VSA   Type=13    Name=cdma-reverse-mux      Format=Ulong     
        Cisco VSA     Type=34    Name=Cisco AVpair          Format=Binary    
    Type=519   Name=cdma-forward-rate              Format=Ulong
        Protocol:RADIUS
        3GenPP2 VSA   Type=14    Name=cdma-forward-rate     Format=Ulong     
        Cisco VSA     Type=34    Name=Cisco AVpair          Format=Binary    
    Type=520   Name=cdma-reverse-rate              Format=Ulong
        Protocol:RADIUS
        3GenPP2 VSA   Type=15    Name=cdma-reverse-rate     Format=Ulong     
        Cisco VSA     Type=34    Name=Cisco AVpair          Format=Binary    
    Type=521   Name=cdma-service-option            Format=Ulong
        Protocol:RADIUS
        3GenPP2 VSA   Type=16    Name=cdma-service-option   Format=Ulong     
        Cisco VSA     Type=34    Name=Cisco AVpair          Format=Binary    
    Type=522   Name=cdma-forward-type              Format=Ulong
        Protocol:RADIUS
        3GenPP2 VSA   Type=17    Name=cdma-forward-type     Format=Ulong     
        Cisco VSA     Type=34    Name=Cisco AVpair          Format=Binary    
    Type=523   Name=cdma-reverse-type              Format=Ulong
        Protocol:RADIUS
        3GenPP2 VSA   Type=18    Name=cdma-reverse-type     Format=Ulong     
        Cisco VSA     Type=34    Name=Cisco AVpair          Format=Binary    
    Type=524   Name=cdma-frame-size                Format=Ulong
        Protocol:RADIUS
        3GenPP2 VSA   Type=19    Name=cdma-frame-size       Format=Ulong     
        Cisco VSA     Type=34    Name=Cisco AVpair          Format=Binary    
    Type=525   Name=cdma-forward-rc                Format=Ulong
        Protocol:RADIUS
        3GenPP2 VSA   Type=20    Name=cdma-forward-rc       Format=Ulong     
        Cisco VSA     Type=34    Name=Cisco AVpair          Format=Binary    
    Type=526   Name=cdma-reverse-rc                Format=Ulong
        Protocol:RADIUS
        3GenPP2 VSA   Type=21    Name=cdma-reverse-rc       Format=Ulong     
        Cisco VSA     Type=34    Name=Cisco AVpair          Format=Binary    
    Type=527   Name=cdma-ip-tech                   Format=Ulong
        Protocol:RADIUS
        3GenPP2 VSA   Type=22    Name=cdma-ip-tech          Format=Ulong     
        Cisco VSA     Type=34    Name=Cisco AVpair          Format=Binary    
    Type=528   Name=cdma-comp-flag                 Format=Enum
        Protocol:RADIUS
        3GenPP2 VSA   Type=23    Name=cdma-comp-flag        Format=Enum      
        Cisco VSA     Type=34    Name=Cisco AVpair          Format=Binary    
    Type=529   Name=cdma-reason-ind                Format=Enum
        Protocol:RADIUS
        3GenPP2 VSA   Type=24    Name=cdma-reason-ind       Format=Enum      
        Cisco VSA     Type=34    Name=Cisco AVpair          Format=Binary    
    Type=530   Name=cdma-dcch-frame-size           Format=Ulong
        Protocol:RADIUS
        3GenPP2 VSA   Type=50    Name=cdma-dcch-frame-size  Format=Ulong     
        Cisco VSA     Type=34    Name=Cisco AVpair          Format=Binary    
    Type=531   Name=cdma-bad-frame-count           Format=Ulong
        Protocol:RADIUS
        3GenPP2 VSA   Type=25    Name=cdma-bad-frame-count  Format=Ulong     
        Cisco VSA     Type=34    Name=Cisco AVpair          Format=Binary    
    Type=532   Name=cdma-active-time               Format=Ulong
        Protocol:RADIUS
        3GenPP2 VSA   Type=49    Name=cdma-active-time      Format=Ulong     
        Cisco VSA     Type=34    Name=Cisco AVpair          Format=Binary    
    Type=533   Name=cdma-num-active                Format=Ulong
        Protocol:RADIUS
        3GenPP2 VSA   Type=30    Name=cdma-num-active       Format=Ulong     
        Cisco VSA     Type=34    Name=Cisco AVpair          Format=Binary    
    Type=534   Name=cdma-sdb-input-octets          Format=Ulong
        Protocol:RADIUS
        3GenPP2 VSA   Type=31    Name=cdma-sdb-input-octets Format=Ulong     
        Cisco VSA     Type=34    Name=Cisco AVpair          Format=Binary    
    Type=535   Name=cdma-sdb-output-octets         Format=Ulong
        Protocol:RADIUS
        3GenPP2 VSA   Type=32    Name=cdma-sdb-output-octet Format=Ulong     
        Cisco VSA     Type=34    Name=Cisco AVpair          Format=Binary    
    Type=536   Name=cdma-numsdb-input              Format=Ulong
        Protocol:RADIUS
        3GenPP2 VSA   Type=33    Name=cdma-numsdb-input     Format=Ulong     
        Cisco VSA     Type=34    Name=Cisco AVpair          Format=Binary    
    Type=537   Name=cdma-numsdb-output             Format=Ulong
        Protocol:RADIUS
        3GenPP2 VSA   Type=34    Name=cdma-numsdb-output    Format=Ulong     
        Cisco VSA     Type=34    Name=Cisco AVpair          Format=Binary    
    Type=538   Name=cdma-hdlc-layer-bytes-in       Format=Ulong
        Protocol:RADIUS
        3GenPP2 VSA   Type=43    Name=cdma-hdlc-layer-bytes Format=Ulong     
        Cisco VSA     Type=34    Name=Cisco AVpair          Format=Binary    
    Type=539   Name=cdma-moip-inbound-count        Format=Ulong
        Protocol:RADIUS
        3GenPP2 VSA   Type=46    Name=cdma-moip-inbound     Format=Ulong     
        Cisco VSA     Type=34    Name=Cisco AVpair          Format=Binary    
    Type=540   Name=cdma-moip-outbound-count       Format=Ulong
        Protocol:RADIUS
        3GenPP2 VSA   Type=47    Name=cdma-moip-outbound    Format=Ulong     
        Cisco VSA     Type=34    Name=Cisco AVpair          Format=Binary    
    Type=541   Name=cdma-last-user-activity        Format=Ulong
        Protocol:RADIUS
        3GenPP2 VSA   Type=80    Name=cdma-last-user-activi Format=Ulong     
        Cisco VSA     Type=34    Name=Cisco AVpair          Format=Binary    
    Type=542   Name=cdma-ip-qos                    Format=Ulong
        Protocol:RADIUS
        3GenPP2 VSA   Type=36    Name=cdma-ip-qos           Format=Ulong     
        Cisco VSA     Type=34    Name=Cisco AVpair          Format=Binary    
    Type=543   Name=cdma-airlink-qos               Format=Ulong
        Protocol:RADIUS
        3GenPP2 VSA   Type=39    Name=cdma-airlink-qos      Format=Ulong     
        Cisco VSA     Type=34    Name=Cisco AVpair          Format=Binary    
    Type=544   Name=cdma-diff-svc-class-opt        Format=Ulong
        Protocol:RADIUS
        3GenPP2 VSA   Type=5     Name=cdma-diff-svc-class-o Format=Ulong     
        Cisco VSA     Type=34    Name=Cisco AVpair          Format=Binary    
    Type=545   Name=cdma-rp-session-id             Format=Ulong
        Protocol:RADIUS
        3GenPP2 VSA   Type=41    Name=cdma-rp-session-id    Format=Ulong     
        Cisco VSA     Type=34    Name=Cisco AVpair          Format=Binary    
    Type=546   Name=cdma-esn                       Format=String
        Protocol:RADIUS
        3GenPP2 VSA   Type=52    Name=cdma-esn              Format=String    
        Cisco VSA     Type=34    Name=Cisco AVpair          Format=Binary    
    Type=547   Name=cdma-mn-ha-spi                 Format=Ulong
        Protocol:RADIUS
        3GenPP2 VSA   Type=57    Name=cdma-mn-ha-spi        Format=Ulong     
        Cisco VSA     Type=34    Name=Cisco AVpair          Format=Binary    
    Type=548   Name=cdma-mn-ha-shared-key          Format=Binary
        Protocol:RADIUS
        3GenPP2 VSA   Type=58    Name=cdma-mn-ha-shared-key Format=Binary    
    Type=549   Name=cdma-mn-aaa-removal-ind        Format=Ulong
        Protocol:RADIUS
        3GenPP2 VSA   Type=81    Name=cdma-mn-aaa-removal-i Format=Ulong     
    Type=550   Name=cdma-sess-term-capability      Format=Ulong
        Protocol:RADIUS
        3GenPP2 VSA   Type=88    Name=cdma-sess-term-capabi Format=Ulong     
    Type=551   Name=cdma-prepaid-accounting-quota  Format=Binary
        Protocol:RADIUS
        3GenPP2 VSA   Type=90    Name=cdma-prepaid-accounti Format=Binary    
    Type=552   Name=cdma-prepaid-accounting-capabi Format=Binary
        Protocol:RADIUS
        3GenPP2 VSA   Type=91    Name=cdma-prepaid-accounti Format=Binary    
    Type=553   Name=cdma-disconnect-reason         Format=Ulong
        Protocol:RADIUS
        3GenPP2 VSA   Type=96    Name=cdma-disconnect-reaso Format=Ulong     
    Type=554   Name=cdma-prepaid-tariff-switching  Format=Binary
        Protocol:RADIUS
        3GenPP2 VSA   Type=98    Name=cdma-prepaid-accounti Format=Binary    
    Type=555   Name=cdma-allowed-differentiated-se Format=Binary
        Protocol:RADIUS
        3GenPP2 VSA   Type=73    Name=cdma-allowed-differen Format=Binary    
    Type=556   Name=cdma-forward-pdch-rc           Format=Ulong
        Protocol:RADIUS
        3GenPP2 VSA   Type=83    Name=cdma-forward-pdch-rc  Format=Ulong     
        Cisco VSA     Type=34    Name=Cisco AVpair          Format=Binary    
    Type=557   Name=cdma-service-ref-id            Format=Ulong
        Protocol:RADIUS
        3GenPP2 VSA   Type=94    Name=cdma-service-ref-id   Format=Ulong     
        Cisco VSA     Type=34    Name=Cisco AVpair          Format=Binary    
    Type=558   Name=cdma-meid                      Format=String
        Protocol:RADIUS
        3GenPP2 VSA   Type=116   Name=cdma-meid             Format=String    
        Cisco VSA     Type=34    Name=Cisco AVpair          Format=Binary    
    Type=559   Name=cdma-dns-server-ip-address     Format=Binary
        Protocol:RADIUS
        3GenPP2 VSA   Type=117   Name=cdma-dns-server-ip-ad Format=Binary    
    Type=560   Name=cdma-dns-update-required       Format=Ulong
        Protocol:RADIUS
        3GenPP2 VSA   Type=75    Name=cdma-dns-update-requi Format=Ulong     
    Type=561   Name=cdma-dns-update-capability     Format=Ulong
        Protocol:RADIUS
        3GenPP2 VSA   Type=95    Name=cdma-dns-update-capab Format=Ulong     
    Type=562   Name=cdma-rfswact                   Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=34    Name=Cisco AVpair          Format=Binary    
    Type=563   Name=mip-key-update-req             Format=String
        Protocol:RADIUS
        Verizon VSA   Type=1     Name=mip-key-update-req    Format=Binary    
    Type=564   Name=mip-key-data                   Format=String
        Protocol:RADIUS
        Verizon VSA   Type=2     Name=mip-key-data          Format=Binary    
    Type=565   Name=aaa-authenticator              Format=String
        Protocol:RADIUS
        Verizon VSA   Type=3     Name=aaa-authenticator     Format=Binary    
    Type=566   Name=public-key-invalid             Format=String
        Protocol:RADIUS
        Verizon VSA   Type=4     Name=public-key-invalid    Format=Binary    
    Type=567   Name=login-tcp-port                 Format=Ulong
        Protocol:RADIUS
        Unknown       Type=16    Name=login-tcp-port        Format=Ulong     
    Type=568   Name=login-ip-addr-host             Format=IPv4 Address
        Protocol:RADIUS
        Unknown       Type=14    Name=login-ip-addr-host    Format=IPv4 Addre
    Type=569   Name=login-ipv6-addr-host           Format=String
        Protocol:RADIUS
        Unknown       Type=98    Name=login-ipv6-addr-host  Format=Binary    
    Type=570   Name=login-ip-host                  Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=571   Name=crb-auth-reason                Format=Enum
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=572   Name=crb-user-id                    Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=573   Name=crb-session-id                 Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=574   Name=crb-service-id                 Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=575   Name=crb-entity-type                Format=Enum
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=576   Name=crb-duration                   Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=577   Name=crb-total-volume               Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=578   Name=crb-uplink-volume              Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=579   Name=crb-downlink-volume            Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=580   Name=crb-total-packets              Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=581   Name=crb-uplink-packets             Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=582   Name=crb-downlink-packets           Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=583   Name=crb-terminate-cause            Format=Enum
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=584   Name=cert-application               Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=585   Name=cert-trustpoint                Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=586   Name=cert-serial                    Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=587   Name=cert-serial-not                Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=588   Name=cert-lifetime-end              Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=589   Name=subjectname                    Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=590   Name=iosconfig1                     Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=591   Name=iosconfig2                     Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=592   Name=iosconfig3                     Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=593   Name=iosconfig4                     Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=594   Name=iosconfig5                     Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=595   Name=iosconfig6                     Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=596   Name=iosconfig7                     Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=597   Name=iosconfig8                     Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=598   Name=iosconfig9                     Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=599   Name=privilege                      Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=600   Name=nas-ip-address                 Format=IPv4 Address
        Protocol:RADIUS
        Unknown       Type=4     Name=NAS-IP-Address        Format=IPv4 Addre
    Type=601   Name=acct-delay-time                Format=Ulong
        Protocol:RADIUS
        Unknown       Type=41    Name=Acct-Delay-Time       Format=Ulong     
    Type=602   Name=em-title                       Format=Binary
        Protocol:RADIUS
        Cablelabs VSA Type=1     Name=EM-Title              Format=Binary    
    Type=603   Name=called-party-number            Format=Binary
        Protocol:RADIUS
        Cablelabs VSA Type=5     Name=Called-Party-Number   Format=Binary    
    Type=604   Name=call-termination-cause         Format=Binary
        Protocol:RADIUS
        Cablelabs VSA Type=11    Name=Call-Termination-Caus Format=Binary    
    Type=605   Name=related-call-billing-correlati Format=Binary
        Protocol:RADIUS
        Cablelabs VSA Type=13    Name=Related-Call-Billing- Format=Binary    
    Type=606   Name=mta-udp-portnum                Format=Ulong
        Protocol:RADIUS
        Cablelabs VSA Type=26    Name=MTA-UDP-Portnum       Format=Ulong     
    Type=607   Name=sf-id                          Format=Ulong
        Protocol:RADIUS
        Cablelabs VSA Type=30    Name=Svc-Flow-ID           Format=Ulong     
    Type=608   Name=qos-descriptor                 Format=Binary
        Protocol:RADIUS
        Cablelabs VSA Type=32    Name=QoS-Descriptor        Format=Binary    
    Type=609   Name=time-adjustment                Format=Binary
        Protocol:RADIUS
        Cablelabs VSA Type=38    Name=Time-Adjustment       Format=Binary    
    Type=610   Name=sdp-upstream                   Format=String
        Protocol:RADIUS
        Cablelabs VSA Type=39    Name=sdp-upstream          Format=String    
    Type=611   Name=sdp-downstream                 Format=String
        Protocol:RADIUS
        Cablelabs VSA Type=40    Name=sdp-downstream        Format=String    
    Type=612   Name=ccc-id                         Format=Ulong
        Protocol:RADIUS
        Cablelabs VSA Type=48    Name=ccc-id                Format=Ulong     
    Type=613   Name=financial-entity-id            Format=Binary
        Protocol:RADIUS
        Cablelabs VSA Type=49    Name=Financial-Entity-ID   Format=Binary    
    Type=614   Name=flow-direction                 Format=Binary
        Protocol:RADIUS
        Cablelabs VSA Type=50    Name=Flow-Direction        Format=Binary    
    Type=615   Name=gate-usage-info                Format=Binary
        Protocol:RADIUS
        Cablelabs VSA Type=64    Name=gate-usage-info       Format=Binary    
    Type=616   Name=element-req-qos                Format=Binary
        Protocol:RADIUS
        Cablelabs VSA Type=65    Name=element-req-qos       Format=Binary    
    Type=617   Name=qos-release-reason             Format=Binary
        Protocol:RADIUS
        Cablelabs VSA Type=66    Name=qos-release-reason    Format=Binary    
    Type=618   Name=gate-time-info                 Format=Ulong
        Protocol:RADIUS
        Cablelabs VSA Type=73    Name=gate-time-info        Format=Ulong     
    Type=619   Name=imsi                           Format=String
        Protocol:RADIUS
        3GenPP VSA    Type=1     Name=IMSI                  Format=String    
    Type=620   Name=charging-id                    Format=Ulong
        Protocol:RADIUS
        3GenPP VSA    Type=2     Name=Charging-ID           Format=Ulong     
    Type=621   Name=pdp-type                       Format=Enum
        Protocol:RADIUS
        3GenPP VSA    Type=3     Name=PDP Type              Format=Enum      
    Type=622   Name=charging-gw-addr               Format=IPv4 Address
        Protocol:RADIUS
        3GenPP VSA    Type=4     Name=Charging-Gateway-Addr Format=IPv4 Addre
    Type=623   Name=qos-profile                    Format=String
        Protocol:RADIUS
        3GenPP VSA    Type=5     Name=GPRS-QoS-Profile      Format=String    
    Type=624   Name=sgsn-addrss                    Format=IPv4 Address
        Protocol:RADIUS
        3GenPP VSA    Type=6     Name=SGSN-Address          Format=IPv4 Addre
    Type=625   Name=ggsn-address                   Format=IPv4 Address
        Protocol:RADIUS
        3GenPP VSA    Type=7     Name=GGSN-Address          Format=IPv4 Addre
    Type=626   Name=imsi-mcc-mnc                   Format=String
        Protocol:RADIUS
        3GenPP VSA    Type=8     Name=IMSI-MCC-MNC          Format=String    
    Type=627   Name=ggsn-mcc-mnc                   Format=String
        Protocol:RADIUS
        3GenPP VSA    Type=9     Name=GGSN-MCC-MNC          Format=String    
    Type=628   Name=nsapi                          Format=String
        Protocol:RADIUS
        3GenPP VSA    Type=10    Name=NSAPI                 Format=String    
    Type=629   Name=SESS_STOP_IND                  Format=Binary
        Protocol:RADIUS
        3GenPP VSA    Type=11    Name=Session-Stop-Ind      Format=Binary    
    Type=630   Name=selection-mode                 Format=String
        Protocol:RADIUS
        3GenPP VSA    Type=12    Name=Selection-Mode        Format=String    
    Type=631   Name=charging-characteristics       Format=String
        Protocol:RADIUS
        3GenPP VSA    Type=13    Name=Charging-Characterist Format=String    
    Type=632   Name=sgsn-mcc-mnc                   Format=String
        Protocol:RADIUS
        3GenPP VSA    Type=18    Name=SGSN-MCC-MNC          Format=String    
    Type=633   Name=Charging-Gateway-ipv6-addr     Format=Binary
        Protocol:RADIUS
        3GenPP VSA    Type=14    Name=Charging-Gateway-ipv6 Format=Binary    
    Type=634   Name=sgsn-ipv6-address              Format=Binary
        Protocol:RADIUS
        3GenPP VSA    Type=15    Name=sgsn-ipv6-address     Format=Binary    
    Type=635   Name=ggsn-ipv6-address              Format=Binary
        Protocol:RADIUS
        3GenPP VSA    Type=16    Name=ggsn-ipv6-address     Format=Binary    
    Type=636   Name=ipv6-dns-servers               Format=Binary
        Protocol:RADIUS
        3GenPP VSA    Type=17    Name=ipv6-dns-servers      Format=Binary    
    Type=637   Name=imeisv                         Format=Binary
        Protocol:RADIUS
        3GenPP VSA    Type=20    Name=imeisv                Format=Binary    
    Type=638   Name=Radio-access-technology-type   Format=Binary
        Protocol:RADIUS
        3GenPP VSA    Type=21    Name=radio-access-type     Format=Binary    
    Type=639   Name=user-location-information      Format=Binary
        Protocol:RADIUS
        3GenPP VSA    Type=22    Name=user-location-informa Format=Binary    
    Type=640   Name=ms-timezone                    Format=Binary
        Protocol:RADIUS
        3GenPP VSA    Type=23    Name=ms-timezone           Format=Binary    
    Type=641   Name=camel-charging-info            Format=Binary
        Protocol:RADIUS
        3GenPP VSA    Type=24    Name=camel-charging-info   Format=Binary    
    Type=642   Name=teardown-ind                   Format=Enum
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=643   Name=md-ip-addr                     Format=IPv4 Address
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=644   Name=md-port                        Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=645   Name=li-action                      Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=646   Name=intercept-id                   Format=Binary
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=647   Name=charging-profile-index         Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=648   Name=billing_plan                   Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=649   Name=quota_server                   Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=650   Name=im-entry-allowed               Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=651   Name=downlink_nexthop               Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=652   Name=gtp-pdp-session                Format=Enum
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=653   Name=apn                            Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=654   Name=http-proxy-server              Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=655   Name=http-proxy-server-port         Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=656   Name=MS-CHAP-Error                  Format=Binary
        Protocol:RADIUS
        Microsoft VSA Type=2     Name=MS-CHAP-ERROR         Format=Binary    
    Type=657   Name=MS-CHAP-NT-Enc-PW1             Format=Binary
        Protocol:RADIUS
        Microsoft VSA Type=6     Name=MS-CHAP-NT-Enc-PW     Format=Binary    
    Type=658   Name=MS-CHAP-NT-Enc-PW2             Format=Binary
        Protocol:RADIUS
        Microsoft VSA Type=6     Name=MS-CHAP-NT-Enc-PW     Format=Binary    
    Type=659   Name=MS-CHAP-NT-Enc-PW3             Format=Binary
        Protocol:RADIUS
        Microsoft VSA Type=6     Name=MS-CHAP-NT-Enc-PW     Format=Binary    
    Type=660   Name=MS-CHAP-MPPE-Keys              Format=Binary
        Protocol:RADIUS
        Microsoft VSA Type=12    Name=MS-CHAP-MPPE-Keys     Format=Binary    
    Type=661   Name=MS-MPPE-Send-Key               Format=Binary
        Protocol:RADIUS
        Microsoft VSA Type=16    Name=MS-MPPE-Send-Key      Format=Binary    
    Type=662   Name=MS-MPPE-Recv-Key               Format=Binary
        Protocol:RADIUS
        Microsoft VSA Type=17    Name=MS-MPPE-Recv-Key      Format=Binary    
    Type=663   Name=rad-serv                       Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=664   Name=rad-serv-vrf                   Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=665   Name=rad-serv-source-if             Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=666   Name=rad-serv-filter                Format=String
    Type=667   Name=ppp-authen-list                Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=668   Name=ppp-authen-type                Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=669   Name=ppp-author-list                Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=670   Name=ppp-acct-list                  Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=671   Name=ip-vrf                         Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=672   Name=ip-addr                        Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=673   Name=ip-unnumbered                  Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=674   Name=peer-ip-pool                   Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=675   Name=rad-attr44                     Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=676   Name=account-delay                  Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=677   Name=account-send-stop              Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=678   Name=account-send-success-remote    Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=679   Name=template                       Format=String
    Type=680   Name=MS-CHAP-V2-Success             Format=String
        Protocol:RADIUS
        Microsoft VSA Type=26    Name=MS-CHAP-V2-Success    Format=String    
    Type=681   Name=MS-CHAP-CPW-2                  Format=Binary
        Protocol:RADIUS
        Microsoft VSA Type=27    Name=MS-CHAP-CPW-2         Format=Binary    
    Type=682   Name=call-id                        Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=683   Name=cust-biz-grp-id                Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=684   Name=iphop                          Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=685   Name=nas-ipv6-Address               Format=String
        Protocol:RADIUS
        Unknown       Type=95    Name=NAS-IPv6-Address      Format=Binary    
    Type=686   Name=Interface-Id                   Format=Binary
        Protocol:RADIUS
        Unknown       Type=96    Name=Framed-Interface-Id   Format=Binary    
    Type=687   Name=prefix                         Format=Binary
        Protocol:RADIUS
        Unknown       Type=97    Name=Framed-IPv6-Prefix    Format=Binary    
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=688   Name=prefix-len                     Format=Ulong
    Type=689   Name=delegated-prefix               Format=Binary
        Protocol:RADIUS
        Unknown       Type=123   Name=Delegated-IPv6-Prefix Format=Binary    
    Type=690   Name=delegated-ipv6-pool            Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=691   Name=ipv6-dns-servers-addr          Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=692   Name=session-type                   Format=Enum
    Type=693   Name=remote-media-address           Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=694   Name=isup-carrier-id                Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=695   Name=calling-party-category         Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=696   Name=originating-line-info          Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=697   Name=charge-number                  Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=698   Name=transmission-medium-req        Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=699   Name=redirecting-number             Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=700   Name=backward-call-indicators       Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=701   Name=remote-media-udp-port          Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=702   Name=remote-media-id                Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=703   Name=supp-svc-xfer-by               Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=704   Name=faxrelay-start-time            Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=705   Name=faxrelay-max-jit-buf-depth     Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=706   Name=faxrelay-jit-buf-ovflow        Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=707   Name=faxrelay-mr-hs-mod             Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=708   Name=faxrelay-init-hs-mod           Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=709   Name=faxrelay-num-pages             Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=710   Name=faxrelay-direction             Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=711   Name=faxrelay-ecm-status            Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=712   Name=faxrelay-encap-prot            Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=713   Name=faxrelay-nsf-country-code      Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=714   Name=faxrelay-nsf-manuf-code        Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=715   Name=faxrelay-fax-success           Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=716   Name=faxrelay-tx-packets            Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=717   Name=faxrelay-rx-packets            Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=718   Name=faxrelay-pkt-conceal           Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=719   Name=voice-feature                  Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=720   Name=feature-operation              Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=721   Name=feature-op-status              Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=722   Name=feature-op-time                Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=723   Name=feature-id                     Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=724   Name=feature-vsa                    Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=725   Name=ip-phone-info                  Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=726   Name=ip-pbx-mode                    Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=727   Name=peer-sub-address               Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=728   Name=faxrelay-stop-time             Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=729   Name=internal-error-code            Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=730   Name=account-code                   Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=731   Name=vrf-id                         Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=732   Name=allow-subinterface             Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=733   Name=description                    Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=734   Name=sg-service-type                Format=Enum
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=735   Name=policy-name                    Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=736   Name=sg-service-group               Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=737   Name=isakmp-phase1-id               Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=738   Name=isakmp-initator-ip             Format=IPv4 Address
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=739   Name=isakmp-initator-ipv6           Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=740   Name=isakmp-group-id                Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=741   Name=l4redirect                     Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=742   Name=portbundle                     Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=743   Name=traffic-class                  Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=744   Name=client-flash                   Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=745   Name=client-available-flash         Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=746   Name=client-platform                Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=747   Name=client-image                   Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=748   Name=client-hostname                Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=749   Name=client-serial                  Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=750   Name=client-memory                  Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=751   Name=client-free-memory             Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=752   Name=client-config-version          Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=753   Name=location-id                    Format=String
        Protocol:RADIUS
        WISPr VSA     Type=1     Name=WISPr VSA             Format=String    
    Type=754   Name=location-name                  Format=String
        Protocol:RADIUS
        WISPr VSA     Type=2     Name=WISPr VSA             Format=String    
    Type=755   Name=accounting-list                Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=756   Name=reauthenticate-type            Format=Enum
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=757   Name=method                         Format=Enum
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=758   Name=precedence                     Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=759   Name=activation-mode                Format=Enum
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=760   Name=sg-version                     Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=761   Name=policy-route                   Format=String
        Protocol:RADIUS
        Unknown       Type=104   Name=Ascend-Private-Route  Format=String    
    Type=762   Name=default-domain                 Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=763   Name=user-realm                     Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=764   Name=sla-profile-name               Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=765   Name=group-lock                     Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=766   Name=configuration-url              Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=767   Name=configuration-version          Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=768   Name=pfs                            Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=769   Name=route-metric                   Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=770   Name=access-restrict                Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=771   Name=include-local-lan              Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=772   Name=user-include-local-lan         Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=773   Name=firewall                       Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=774   Name=cpp-policy                     Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=775   Name=browser-proxy                  Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=776   Name=banner                         Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=777   Name=save-password                  Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=778   Name=user-save-password             Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=779   Name=route-set-interface            Format=Ulong
    Type=780   Name=route-accept                   Format=String
    Type=781   Name=smartcard-removal-disconnect   Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=782   Name=user-smartcard-removal-disconn Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=783   Name=group-dhcp-server              Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=784   Name=dhcp-timeout                   Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=785   Name=dhcp-giaddr                    Format=IPv4 Address
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=786   Name=split-dns                      Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=787   Name=netmask                        Format=IPv4 Address
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=788   Name=user-vpn-group                 Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=789   Name=ipsec-backup-gateway           Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=790   Name=max-users                      Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=791   Name=max-logins                     Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=792   Name=ipv6-subnet-acl                Format=String
    Type=793   Name=ipv6-addr-pool                 Format=String
    Type=794   Name=ipsec-flow-limit               Format=Ulong
    Type=795   Name=max-bit-rate                   Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=796   Name=qos-class-name                 Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=797   Name=qos-policy-name                Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=798   Name=time-quota                     Format=Ulong
    Type=799   Name=volume-quota                   Format=Ulong
    Type=800   Name=giga-words-volume-quota        Format=Ulong
    Type=801   Name=tariff-time                    Format=Ulong
    Type=802   Name=ptv-quota                      Format=Ulong
    Type=803   Name=giga-words-post-tariff-volume- Format=Ulong
    Type=804   Name=is-session-idle                Format=Boolean
    Type=805   Name=volume-threshold               Format=Ulong
    Type=806   Name=time-threshold                 Format=Ulong
    Type=807   Name=prepaid-config                 Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=808   Name=prepaid-timeout                Format=Ulong
    Type=809   Name=prepaid-absolute-timeout       Format=Ulong
    Type=810   Name=drop-at-quota-reached          Format=Boolean
    Type=811   Name=drop-all                       Format=Boolean
    Type=812   Name=dhcp-vendor-class              Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=813   Name=dhcp-client-id                 Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=814   Name=dhcp-relay-info                Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=815   Name=session-duration               Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=816   Name=notifyChanges                  Format=Enum
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=817   Name=service-monitor                Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=818   Name=command                        Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=819   Name=audit-session-id               Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=820   Name=status-query-timeout           Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=821   Name=url-redirect                   Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=822   Name=url-redirect-acl               Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=823   Name=url-redirect-acl-no-match      Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=824   Name=url-redirect-acl-one-time      Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=825   Name=posture-token                  Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=826   Name=CiscoSecure-Defined-ACL        Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=827   Name=webvpn-banner                  Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=828   Name=home-page                      Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=829   Name=urllist-name                   Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=830   Name=sslvpn-acl-name                Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=831   Name=nbnslist-name                  Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=832   Name=file-browse                    Format=Boolean
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=833   Name=file-entry                     Format=Boolean
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=834   Name=file-access                    Format=Boolean
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=835   Name=port-forward-name              Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=836   Name=port-forward-auto              Format=Boolean
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=837   Name=port-forward-http-proxy        Format=Boolean
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=838   Name=port-forward-http-proxy-url    Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=839   Name=svc-enabled                    Format=Boolean
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=840   Name=svc-required                   Format=Boolean
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=841   Name=hide-urlbar                    Format=Boolean
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=842   Name=mask-urls                      Format=Boolean
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=843   Name=dpd-client-timeout             Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=844   Name=dpd-gateway-timeout            Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=845   Name=keep-svc-installed             Format=Boolean
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=846   Name=rekey-interval                 Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=847   Name=lease-duration                 Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=848   Name=svc-ie-proxy-policy            Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=849   Name=ie-proxy-server                Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=850   Name=ie-proxy-exception             Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=851   Name=split-include                  Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=852   Name=split-exclude                  Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=853   Name=cifs-urllist-name              Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=854   Name=sso-server-name                Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=855   Name=webvpn-context                 Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=856   Name=webvpn-client-ip-address       Format=IPv4 Address
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=857   Name=anyconnect-profile             Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=858   Name=dsp-id                         Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=859   Name=mcast-source-v4                Format=IPv4 Address
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=860   Name=mcast-source-v6                Format=IPv6 Address
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=861   Name=mcast-group-v4                 Format=IPv4 Address
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=862   Name=mcast-group-v6                 Format=IPv6 Address
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=863   Name=local-hostname                 Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=864   Name=authz-directive                Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=865   Name=Method-List                    Format=String
    Type=866   Name=template-name                  Format=String
    Type=867   Name=timer-name                     Format=String
    Type=868   Name=timer-value                    Format=Ulong
    Type=869   Name=nas_port_sub_id-type           Format=Enum
    Type=870   Name=identity-policy-name           Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=871   Name=media-type                     Format=Enum
    Type=872   Name=protocol-type                  Format=Enum
    Type=873   Name=domain                         Format=String
    Type=874   Name=unauthen-domain                Format=String
    Type=875   Name=unauthen-username              Format=String
    Type=876   Name=nas-port                       Format=Ulong
    Type=877   Name=tunnel-name                    Format=String
    Type=878   Name=if-handle                      Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=879   Name=parent-if-handle               Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=880   Name=tag-name                       Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=881   Name=supplicant-group               Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=882   Name=dsl-line-info-forwarding       Format=Ulong
    Type=883   Name=gk-operation                   Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=884   Name=supplicant-name                Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=885   Name=device-traffic-class           Format=Enum
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=886   Name=identity-request               Format=Enum
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=887   Name=termination-action-modifier    Format=Enum
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=888   Name=ntlm-client-cred               Format=String
    Type=889   Name=ntlm-server-cred               Format=String
    Type=890   Name=cts-pac-opaque                 Format=Binary
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=891   Name=cts-capabilities               Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=892   Name=supplicant-cts-capabilities    Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=893   Name=security-group-tag             Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=894   Name=trusted-device                 Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=895   Name=cts-rbacl-source-list          Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=896   Name=cts-rbacl-destination-list     Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=897   Name=cts-rbacl-any-any              Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=898   Name=src-dst-rbacl                  Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=899   Name=cts-rbacl                      Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=900   Name=rbacl                          Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=901   Name=rbacl-ace                      Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=902   Name=server-list                    Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=903   Name=cts-server-list                Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=904   Name=server                         Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=905   Name=authorization-expiry           Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=906   Name=cts-environment-data           Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=907   Name=cts-get-tunnel-traffic-policy  Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=908   Name=tunnel-traffic-policy          Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=909   Name=cts-tunnel-traffic-policy      Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=910   Name=tunnel-default-sgt             Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=911   Name=tunnel-reverse-check-fail-drop Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=912   Name=tunnel-gateway                 Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=913   Name=tunnel-unicast-address         Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=914   Name=tunnel-multicast-group-address Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=915   Name=multicast-group-sgt-table      Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=916   Name=cts-multicast-group-sgt-table  Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=917   Name=multicast-sgt                  Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=918   Name=cts-group-current-key          Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=919   Name=cts-group-next-key             Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=920   Name=group-spi                      Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=921   Name=group-algorithm                Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=922   Name=group-gcm-sequence-range       Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=923   Name=encapsulation-protocol-number  Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=924   Name=group-key-expiry               Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=925   Name=group-min-rekey-window         Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=926   Name=group-old-key-hold-time        Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=927   Name=tunnel-traffic-policy-expiry   Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=928   Name=environment-data-expiry        Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=929   Name=cts-peer-authorization-token   Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=930   Name=l2tp-silent-switchover         Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=931   Name=gk-endp-addr                   Format=IPv4 Address
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=932   Name=gk-endp-alias                  Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=933   Name=app-key                        Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=934   Name=random-nonce                   Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=935   Name=message-authenticator-code     Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=936   Name=in-lpcor-group                 Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=937   Name=out-lpcor-group                Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=938   Name=instance-id                    Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=939   Name=bsn-wlan-id                    Format=Ulong
        Protocol:RADIUS
        Airespace VSA Type=1     Name=Airespace-WLAN-ID     Format=Ulong     
    Type=940   Name=bsn-qos-level                  Format=Enum
        Protocol:RADIUS
        Airespace VSA Type=2     Name=Airespace-QoS-Level   Format=Enum      
    Type=941   Name=bsn-dscp                       Format=Ulong
        Protocol:RADIUS
        Airespace VSA Type=3     Name=Airespace-DSCP        Format=Ulong     
    Type=942   Name=bsn-8021p-type                 Format=Ulong
        Protocol:RADIUS
        Airespace VSA Type=4     Name=Airespace-8021P-TYPE  Format=Ulong     
    Type=943   Name=bsn-vlan-interface-name        Format=String
        Protocol:RADIUS
        Airespace VSA Type=5     Name=Airespace-VLAN-Interf Format=String    
    Type=944   Name=bsn-acl-name                   Format=String
        Protocol:RADIUS
        Airespace VSA Type=6     Name=Airespace-ACL-Name    Format=String    
    Type=945   Name=bsn-data-bandwidth-average-con Format=Ulong
        Protocol:RADIUS
        Airespace VSA Type=7     Name=Airespace-Data-BW-Avg Format=Ulong     
    Type=946   Name=bsn-realtime-bandwidth-average Format=Ulong
        Protocol:RADIUS
        Airespace VSA Type=8     Name=Airespace-Realtime-BW Format=Ulong     
    Type=947   Name=bsn-data-bandwidth-burst-contr Format=Ulong
        Protocol:RADIUS
        Airespace VSA Type=9     Name=Airespace-Data-BW-Bur Format=Ulong     
    Type=948   Name=bsn-realtime-bandwidth-burst-c Format=Ulong
        Protocol:RADIUS
        Airespace VSA Type=10    Name=Airespace-Realtime-BW Format=Ulong     
    Type=949   Name=bsn-guest-role-name            Format=String
        Protocol:RADIUS
        Airespace VSA Type=1     Name=Airespace-WLAN-ID     Format=Ulong     
    Type=950   Name=hwidb                          Format=Ulong
    Type=951   Name=swidb                          Format=Ulonglong
    Type=952   Name=iif-id                         Format=Ulonglong
    Type=953   Name=auth-profile                   Format=String
    Type=954   Name=auth-domain                    Format=Enum
    Type=955   Name=auth-mgr-ctx-state             Format=Enum
    Type=956   Name=service-template               Format=Boolean
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=957   Name=aaa-authen-type                Format=Ulong
    Type=958   Name=aaa-author-type                Format=Ulong
    Type=959   Name=aaa-authen-service             Format=Ulong
    Type=960   Name=aaa-author-service             Format=Ulong
    Type=961   Name=arp-probe                      Format=Boolean
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=962   Name=arp-probe-timeout              Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=963   Name=iaf-local-db                   Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=964   Name=authz-fail-reason              Format=Enum
    Type=965   Name=vlan-id                        Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=966   Name=nas-update                     Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=967   Name=sam-account-name               Format=String
    Type=968   Name=employee-type                  Format=String
    Type=969   Name=contact-info                   Format=String
    Type=970   Name=telephone-number               Format=String
    Type=971   Name=encapsulation-untagged         Format=Boolean
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=972   Name=encapsulation-default          Format=Boolean
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=973   Name=encapsulation-priority-tagged  Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=974   Name=efp-session-name               Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=975   Name=stag-type                      Format=Enum
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=976   Name=idmgr-mask                     Format=IPv4 Address
    Type=977   Name=fac-digits                     Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=978   Name=fac-status                     Format=Enum
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=979   Name=dynamic-vrf-service-type       Format=Enum
    Type=980   Name=media-protocol-state           Format=Enum
    Type=981   Name=stag-vlan-id                   Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=982   Name=stag-cos                       Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=983   Name=ctag-vlan-id                   Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=984   Name=ctag-cos                       Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=985   Name=payload-etype                  Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=986   Name=encapsulation-match-exact      Format=Boolean
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=987   Name=rewrite-ingress                Format=Boolean
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=988   Name=rewrite-ingress-stag-type      Format=Enum
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=989   Name=rewrite-ingress-tag-operation  Format=Enum
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=990   Name=rewrite-ingress-stag-vlanid    Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=991   Name=rewrite-ingress-ctag-vlanid    Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=992   Name=rewrite-ingress-symmetric      Format=Boolean
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=993   Name=rewrite-egress                 Format=Boolean
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=994   Name=rewrite-egress-stag-type       Format=Enum
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=995   Name=rewrite-egress-tag-operation   Format=Enum
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=996   Name=rewrite-egress-stag-vlanid     Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=997   Name=rewrite-egress-ctag-vlanid     Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=998   Name=rewrite-egress-symmetric       Format=Boolean
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=999   Name=service-instance-description   Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1000  Name=snmp-ifindex-persist           Format=Enum
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1001  Name=evc-name                       Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1002  Name=ce-vlan-map                    Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1003  Name=redundancy-group               Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1004  Name=elmi_vlan_map_untagged         Format=Boolean
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1005  Name=elmi_vlan_map_default          Format=Boolean
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1006  Name=service-group-id               Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1007  Name=subscriber-id                  Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1008  Name=port-security-enabled          Format=Enum
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1009  Name=static-mac-address             Format=MAC Address
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1010  Name=static-mac-address-drop        Format=MAC Address
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1011  Name=static-mac-address-autolearn   Format=MAC Address
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1012  Name=static-mac-address-disable-sno Format=MAC Address
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1013  Name=recovery-mac-sec-time-interval Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1014  Name=l2protocol-pdu-action          Format=Enum
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1015  Name=mac-tunnel-id                  Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1016  Name=mac-tunnel-description         Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1017  Name=btag-type                      Format=Enum
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1018  Name=btag-vlan-id                   Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1019  Name=default-destination-mac        Format=MAC Address
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1020  Name=itag                           Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1021  Name=mac-flush-proto                Format=Enum
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1022  Name=mac-flush-cos-value            Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1023  Name=bridge-domain-id               Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1024  Name=split-horizon-group            Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1025  Name=bridge-domain-type             Format=Enum
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1026  Name=max-mac-addr                   Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1027  Name=mac-learning                   Format=Boolean
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1028  Name=snmp-context                   Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1029  Name=bridge-domain-member           Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1030  Name=bridge-domain-profile          Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1031  Name=mac-security-enabled           Format=Boolean
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1032  Name=permit-mac-addr-list           Format=MAC Address
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1033  Name=deny-mac-addr-list             Format=MAC Address
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1034  Name=max-mac-addr-limit             Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1035  Name=mac-security-sticky            Format=Boolean
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1036  Name=mac-security-violation-mode    Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1037  Name=mac-security-aging-inactive    Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1038  Name=mac-security-aging-absolute    Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1039  Name=mac-security-aging-sticky      Format=Boolean
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1040  Name=mac-security-aging-static      Format=Boolean
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1041  Name=uni-count                      Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1042  Name=multi-point                    Format=Boolean
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1043  Name=oam-protocol                   Format=Enum
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1044  Name=cfm-svlan-id                   Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1045  Name=cfm-vlan-id                    Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1046  Name=service-text                   Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1047  Name=domain-name                    Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1048  Name=service-profile                Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1049  Name=service-instance-id            Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1050  Name=service-direction              Format=Boolean
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1051  Name=mip-level                      Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1052  Name=mep-domain                     Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1053  Name=mep-mpid                       Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1054  Name=mep-cos                        Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1055  Name=mep-alarm-notification         Format=Enum
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1056  Name=mep-alarm-delay                Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1057  Name=mep-alarm-reset                Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1058  Name=mip-auto-create-level          Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1059  Name=mip-auto-create-evc            Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1060  Name=mip-auto-create-lower-mep-only Format=Boolean
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1061  Name=mip-auto-create-sender-id      Format=Enum
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1062  Name=service-short-ma-name          Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1063  Name=service-fmt                    Format=Enum
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1064  Name=service-vlan-id                Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1065  Name=service-number                 Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1066  Name=service-vpn-id                 Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1067  Name=cfm-service-type               Format=Enum
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1068  Name=service-continuity-check       Format=Boolean
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1069  Name=service-continuity-check-inter Format=Enum
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1070  Name=service-continuity-check-loss- Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1071  Name=service-continuity-check-stati Format=Boolean
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1072  Name=service-continuity-check-auto- Format=Boolean
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1073  Name=service-mip-autocreate         Format=Enum
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1074  Name=service-mep-mpid               Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1075  Name=service-maximum-meps           Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1076  Name=service-ais                    Format=Boolean
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1077  Name=service-ais-period             Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1078  Name=service-ais-level              Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1079  Name=service-ais-expiry-threshold   Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1080  Name=service-ais-suppress-alarms    Format=Boolean
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1081  Name=service-lck                    Format=Boolean
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1082  Name=service-lck-period             Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1083  Name=service-lck-level              Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1084  Name=service-lck-expiry-threshold   Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1085  Name=service-sender-id-chassis      Format=Boolean
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1086  Name=forwarding-service-type        Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1087  Name=forwarding-service-id          Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1088  Name=composite-key                  Format=Binary
    Type=1089  Name=vcid                           Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1090  Name=vpnid                          Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1091  Name=pw-encapsulation               Format=Enum
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1092  Name=pw-classname                   Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1093  Name=preferred-path-tunnel          Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1094  Name=interworking                   Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1095  Name=pw-status                      Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1096  Name=sequencing-type                Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1097  Name=primary-pw                     Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1098  Name=backup-delay                   Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1099  Name=redundancy-enable-delay        Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1100  Name=redundancy-disable-delay       Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1101  Name=redundancy-disable-never       Format=Boolean
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1102  Name=redundancy-priority            Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1103  Name=vfi-name                       Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1104  Name=vpls-id                        Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1105  Name=route-distinguisher            Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1106  Name=route-target                   Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1107  Name=auto-route-target              Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1108  Name=l2-router-id                   Format=IPv4 Address
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1109  Name=forward-l2protocol-all         Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1110  Name=peer-ip-address                Format=IPv4 Address
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1111  Name=preferred-peer                 Format=IPv4 Address
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1112  Name=disable-fallback               Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1113  Name=l2vpn-control-word             Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1114  Name=vccv                           Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1115  Name=service-id                     Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1116  Name=member                         Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1117  Name=l2vpn-service-type             Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1118  Name=mtp-isid                       Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1119  Name=bmac                           Format=MAC Address
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1120  Name=cmac                           Format=MAC Address
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1121  Name=security-group-table           Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1122  Name=cts-security-group-table       Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1123  Name=security-group-info            Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1124  Name=cdp-tlv                        Format=Binary
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1125  Name=lldp-tlv                       Format=Binary
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1126  Name=dhcp-option                    Format=Binary
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1127  Name=mdns-tlv                       Format=Binary
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1128  Name=sip-tlv                        Format=Binary
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1129  Name=h323-tlv                       Format=Binary
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1130  Name=dc-profile-name                Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1131  Name=dc-device-name                 Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1132  Name=dc-device-class-tag            Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1133  Name=dc-profile-tags                Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1134  Name=dc-protocol-map                Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1135  Name=dc-certainty-metric            Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1136  Name=dc-device-id                   Format=Ulonglong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1137  Name=dc-opaque                      Format=Binary
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1138  Name=pmip6-domain-identifier        Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1139  Name=pmip6-spi-value                Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1140  Name=pmip6-spi-key                  Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1141  Name=pmip6-fixed-ll-address         Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1142  Name=pmip6-fixed-l2-address         Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1143  Name=pmip6-replay-protection        Format=Enum
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1144  Name=pmip6-timestamp-window         Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1145  Name=pmip6-encap-type               Format=Enum
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1146  Name=lma-identifier                 Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1147  Name=lma-v4-address                 Format=IPv4 Address
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1148  Name=lma-v6-address                 Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1149  Name=mag-identifier                 Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1150  Name=mag-v4-address                 Format=IPv4 Address
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1151  Name=mag-v6-address                 Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1152  Name=mn-nai                         Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1153  Name=multihomed                     Format=Boolean
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1154  Name=mip6-feature-vector            Format=Ulong
        Protocol:RADIUS
        Unknown       Type=124   Name=mip6-feature-vector   Format=Ulonglong 
    Type=1155  Name=home-lma                       Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1156  Name=visited-lma                    Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1157  Name=gre-encap                      Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1158  Name=mn-service                     Format=Enum
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1159  Name=mn-max-hnp                     Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1160  Name=home-lma-ipv6-address          Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1161  Name=visited-lma-ipv6-address       Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1162  Name=home-lma-ipv4-address          Format=IPv4 Address
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1163  Name=visited-lma-ipv4-address       Format=IPv4 Address
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1164  Name=home-hl-prefix                 Format=String
        Protocol:RADIUS
        Unknown       Type=151   Name=home-hl-prefix        Format=String    
    Type=1165  Name=home-dhcp6-server-address      Format=String
        Protocol:RADIUS
        Unknown       Type=159   Name=home-dhcp6-server-add Format=String    
    Type=1166  Name=visited-dhcp6-server-address   Format=String
        Protocol:RADIUS
        Unknown       Type=160   Name=visited-dhcp6-server- Format=String    
    Type=1167  Name=home-dhcp4-server-address      Format=IPv4 Address
        Protocol:RADIUS
        Unknown       Type=157   Name=home-dhcp4-server-add Format=IPv4 Addre
    Type=1168  Name=visited-dhcp4-server-address   Format=IPv4 Address
        Protocol:RADIUS
        Unknown       Type=158   Name=visited-dhcp4-server- Format=IPv4 Addre
    Type=1169  Name=home-ipv4-hoa                  Format=IPv4 Address
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1170  Name=visited-ipv4-hoa               Format=IPv4 Address
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1171  Name=capwap-tunnel-profile-name     Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1172  Name=ipv4-addr-save                 Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1173  Name=app-attr                       Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1174  Name=allowed-app                    Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1175  Name=allowed-action                 Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1176  Name=auto-acct                      Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1177  Name=fnf-monitor                    Format=String
    Type=1178  Name=fnf-sampler                    Format=String
    Type=1179  Name=fnf-direction                  Format=Enum
    Type=1180  Name=fnf-traffic-type               Format=Enum
    Type=1181  Name=fnf-subtraffic-type            Format=Enum
    Type=1182  Name=rpclient-source-address        Format=IPv4 Address
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1183  Name=mn-apn                         Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1184  Name=mn-network                     Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1185  Name=idle-timeout-direction         Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1186  Name=rem-lifetime                   Format=Ulong
    Type=1187  Name=user-type                      Format=Enum
    Type=1188  Name=cts-device-capability          Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1189  Name=route-set                      Format=String
    Type=1190  Name=chargeable-user-identity       Format=String
        Protocol:RADIUS
        Unknown       Type=89    Name=Chargeable-User-Ident Format=String    
    Type=1191  Name=cisco-service-selection        Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1192  Name=cisco-mobile-node-identifier   Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1193  Name=cisco-wlan-ssid                Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1194  Name=cisco-msisdn                   Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1195  Name=cisco-mn-service               Format=Enum
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1196  Name=cisco-mpc-protocol-interface   Format=Enum
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1197  Name=cisco-multihoming-support      Format=Boolean
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1198  Name=cisco-uplink-gre-key           Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1199  Name=cisco-downlink-gre-key         Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1200  Name=cisco-url-redirect             Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1201  Name=cisco-url-redirect-acl         Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1202  Name=cisco-home-lma-ipv6-address    Format=IPv6 Address
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1203  Name=cisco-visited-lma-ipv6-address Format=IPv6 Address
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1204  Name=Cisco-Home-LMA-IPv4-Address    Format=IPv4 Address
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1205  Name=cisco-visited-lma-ipv4-address Format=IPv4 Address
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1206  Name=cisco-home-ipv4-home-address   Format=IPv4 Address
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1207  Name=cisco-visited-ipv4-home-addres Format=IPv4 Address
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1208  Name=target-scope                   Format=Enum
    Type=1209  Name=roaming-info                   Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1210  Name=rbacl-monitor-all              Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1211  Name=cisco-access-vrf-id            Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1212  Name=cisco-apn-vrf-id               Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1213  Name=RP-IgnoredOpenDhcpAcct4ActiveR Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1214  Name=tunnel-if-handle               Format=Ulonglong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1215  Name=mobility-core-mtu              Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1216  Name=if-adjacency-handle            Format=Ulonglong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1217  Name=teid-enable                    Format=Boolean
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1218  Name=upstream-key-teid              Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1219  Name=downstream-key-teid            Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1220  Name=default-ipv4-gateway           Format=IPv4 Address
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1221  Name=default-gw-mac                 Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1222  Name=mobile-ipv4-address            Format=IPv4 Address
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1223  Name=mobile-ipv4-netmask            Format=IPv4 Address
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1224  Name=download-request               Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1225  Name=visited-hn-prefix              Format=String
        Protocol:RADIUS
        Unknown       Type=152   Name=visited-hn-prefix     Format=String    
    Type=1226  Name=home-interface-id              Format=String
        Protocol:RADIUS
        Unknown       Type=153   Name=home-interface-id     Format=String    
    Type=1227  Name=visited-interface-id           Format=String
        Protocol:RADIUS
        Unknown       Type=154   Name=visited-interface-id  Format=String    
    Type=1228  Name=cts-local-db                   Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1229  Name=MOS-Con                        Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1230  Name=RTCP-JB-nominal-delay          Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1231  Name=voice-quality-total-packet-los Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1232  Name=voice-quality-out-of-order     Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1233  Name=entity-attr                    Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1234  Name=voice_vlan                     Format=String
    Type=1235  Name=authz-directive-local          Format=Enum
    Type=1236  Name=eap-msk                        Format=Binary
    Type=1237  Name=eap-emsk                       Format=Binary
    Type=1238  Name=eap-session-id-fake            Format=Binary
    Type=1239  Name=session-linksec-secured        Format=Boolean
    Type=1240  Name=eap-ether                      Format=Ulong
    Type=1241  Name=reroute-ipv4                   Format=IPv4 Address
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1242  Name=reroute-ipv6                   Format=IPv6 Address
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1243  Name=relay-session-id               Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1244  Name=dhcp-option-82-string          Format=Binary
        Protocol:RADIUS
        Cisco VSA     Type=35    Name=Dhcp option 82        Format=Binary    
    Type=1245  Name=mo-server-v4-addr              Format=IPv4 Address
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1246  Name=mo-server-port                 Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1247  Name=cisco-customer-identifier      Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1248  Name=http-tlv                       Format=Binary
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1249  Name=role                           Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1250  Name=interface-template-name        Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1251  Name=ipv6_addr                      Format=IPv6 Address
        Protocol:RADIUS
        Unknown       Type=168   Name=Framed-IPv6-Address   Format=Binary    
    Type=1252  Name=identity-session-type          Format=Enum
    Type=1253  Name=Authorization-status           Format=Enum
    Type=1254  Name=Security-violation-action      Format=Enum
    Type=1255  Name=fqdn-acl-name                  Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1256  Name=vlan-auto-config               Format=Boolean
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1257  Name=vac-service-info               Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1258  Name=vac-command                    Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1259  Name=vac-subinterface-id            Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1260  Name=cpeid-tag                      Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1261  Name=auto-config-macro              Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1262  Name=client-type                    Format=Enum
        Protocol:RADIUS
                      Type=150   Name=Client Type           Format=String    
    Type=1263  Name=swbidb                         Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1264  Name=client-iif-id                  Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1265  Name=intf-id                        Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1266  Name=nsh-dc-tenant-id               Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1267  Name=nsh-dc-source-node-id          Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1268  Name=nsh-dc-source-interface-id     Format=Ulong
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1269  Name=ancp-access-loop-rem-id        Format=String
        Protocol:RADIUS
        Cisco VSA     Type=1     Name=Cisco AVpair          Format=String    
    Type=1270  Name=Vendor ID                      Format=Ulong
    Type=1271  Name=Firmware-Revision              Format=Ulong
    Type=1272  Name=HOST IP Address                Format=Address
    Type=1273  Name=Supported external vendors     Format=Ulong
    Type=1274  Name=Product name                   Format=String
    Type=1275  Name=disconnect cause               Format=Enum
    Type=1276  Name=Re-Auth-Request-Type           Format=Enum
    Type=1277  Name=Origin host information        Format=String
    Type=1278  Name=Origin Realm Information       Format=String
    Type=1279  Name=Destination host information   Format=String
    Type=1280  Name=Destination Realm Information  Format=String
    Type=1281  Name=Auth Application ID            Format=Ulong
    Type=1282  Name=Acct Application ID            Format=Ulong
    Type=1283  Name=Security supported             Format=Enum
    Type=1284  Name=Error Message                  Format=String
    Type=1285  Name=Error reporting host           Format=String
    Type=1286  Name=Failed AVP                     Format=Grouped
    Type=1287  Name=Experimental result AVP        Format=Grouped
    Type=1288  Name=Experimental result code       Format=Ulong
    Type=1289  Name=Result code                    Format=Ulong
    Type=1290  Name=Session Binding                Format=Ulong
    Type=1291  Name=Session Failover               Format=Enum
    Type=1292  Name=Termination Cause              Format=Enum
    Type=1293  Name=Session Id                     Format=String
    Type=1294  Name=Correlation ID                 Format=Ulong
    Type=1295  Name=Input octets                   Format=Ulonglong
    Type=1296  Name=Output octets                  Format=Ulonglong
    Type=1297  Name=Input packets                  Format=Ulonglong
    Type=1298  Name=Output packets                 Format=Ulonglong
    Type=1299  Name=Prepaid money units            Format=Grouped
    Type=1300  Name=Prepaid request number         Format=Ulong
    Type=1301  Name=Prepaid request type           Format=Enum
    Type=1302  Name=Prepaid service specific units Format=Ulonglong
    Type=1303  Name=Prepaid session Failover       Format=Enum
    Type=1304  Name=Prepaid subsession ID          Format=Ulonglong
    Type=1305  Name=Prepaid Time units             Format=Ulong
    Type=1306  Name=Prepaid volume granted, reques Format=Ulonglong
    Type=1307  Name=Prepaid Units                  Format=Enum
    Type=1308  Name=Prepaid service cost           Format=Grouped
    Type=1309  Name=Prepaid Failure Handling       Format=Enum
    Type=1310  Name=Prepaid message failure handli Format=Enum
    Type=1311  Name=Prepaid final unit             Format=Grouped
    Type=1312  Name=Prepaid granted unit           Format=Grouped
    Type=1313  Name=Prepaid assigned pool          Format=Ulong
    Type=1314  Name=Prepaid assigned pool          Format=Grouped
    Type=1315  Name=Prepaid info for multiple serv Format=Grouped
    Type=1316  Name=Prepaid multiple service indic Format=Enum
    Type=1317  Name=Rating group                   Format=Ulong
    Type=1318  Name=Requested service unit         Format=Grouped
    Type=1319  Name=Restricted services            Format=String
    Type=1320  Name=Service identifier             Format=String
    Type=1321  Name=Service Parameter info         Format=Grouped
    Type=1322  Name=Service Parameter Type         Format=Ulong
    Type=1323  Name=Service Parameter Value        Format=String
    Type=1324  Name=Subscription ID                Format=Grouped
    Type=1325  Name=Subscription Id type           Format=Enum
    Type=1326  Name=Subscription ID Data           Format=String
    Type=1327  Name=Tariff change usage            Format=Enum
    Type=1328  Name=Tariff time change             Format=UTC
    Type=1329  Name=Unit-value                     Format=Grouped
    Type=1330  Name=Exponent value                 Format=Grouped
    Type=1331  Name=Used-service-units             Format=Grouped
    Type=1332  Name=User-equipment-info            Format=Grouped
    Type=1333  Name=User equipment info type       Format=Enum
    Type=1334  Name=User-equipment-value-string    Format=String
    Type=1335  Name=Prepaid-value-digits           Format=Ulonglong
    Type=1336  Name=Prepaid service valid time     Format=Ulong
    Type=1337  Name=Service Context Id             Format=String
    Type=1338  Name=session-type                   Format=Enum
    Type=1339  Name=Prepaid quota consumption time Format=Ulong
    Type=1340  Name=Prepaid quota holding time     Format=Ulong
    Type=1341  Name=Prepaid quota threshold time   Format=Ulonglong
    Type=1342  Name=qt-reporting-reason            Format=Enum
    Type=1343  Name=Prepaid rule base id           Format=String
    Type=1344  Name=Service usage start time       Format=UTC
    Type=1345  Name=Service usage stop time        Format=UTC
    Type=1346  Name=Prepaid trigger                Format=Grouped
    Type=1347  Name=prepaid-trigger-type           Format=Enum
    Type=1348  Name=Prepaid quota volume threshold Format=Ulonglong
    Type=1349  Name=Prepaid User Location Info     Format=Binary
    Type=1350  Name=Vendor Specific Application Id Format=Grouped
    Type=1351  Name=AGW IPv4 address               Format=String
    Type=1352  Name=Event Trigger                  Format=Enum
    Type=1353  Name=Origin State ID                Format=Ulong
    Type=1354  Name=Ty ANCID                       Format=Grouped
    Type=1355  Name=ANCID Value                    Format=String
    Type=1356  Name=Charging Info                  Format=Grouped
    Type=1357  Name=Pri Charging Collect Func Name Format=String
    Type=1358  Name=Sec Charging Collect Func Name Format=String
    Type=1359  Name=Authorized QoS                 Format=Grouped
    Type=1360  Name=QoS Class                      Format=Enum
    Type=1361  Name=Max req bandw DL               Format=Ulong
    Type=1362  Name=Max req bandw UL               Format=Ulong
    Type=1363  Name=Charging Rule Install          Format=Grouped
    Type=1364  Name=Charging Rule Remove           Format=Grouped
    Type=1365  Name=Charging Rule Def              Format=Grouped
    Type=1366  Name=Charging Rule Base Name        Format=String
    Type=1367  Name=Charging Rule Name             Format=String
    Type=1368  Name=Charging Rule Report           Format=Grouped
    Type=1369  Name=Flow Description               Format=String
    Type=1370  Name=Flow Status                    Format=Enum
    Type=1371  Name=PCC Rule Status                Format=Enum
    Type=1372  Name=Metering Method                Format=Enum
    Type=1373  Name=Offline                        Format=Enum
    Type=1374  Name=Online                         Format=Enum
    Type=1375  Name=Precedence                     Format=Ulong
    Type=1376  Name=Reporting Level                Format=Enum
    Type=1377  Name=AF Charging ID                 Format=Binary
    Type=1378  Name=ACN Physical Access ID         Format=Grouped
    Type=1379  Name=ACN Physical Access ID Value   Format=Binary
    Type=1380  Name=ACN Physical Access ID Realm   Format=Binary
    Type=1381  Name=BM-Information                 Format=Grouped
    Type=1382  Name=BM-Address                     Format=Address
    Type=1383  Name=BM-Type                        Format=Enum
    Type=1384  Name=Service-Information            Format=Grouped
    Type=1385  Name=HoA Session ID                 Format=String
    Type=1386  Name=VoA Session ID                 Format=String
    Type=1387  Name=MIP-Mobile-Node-Address        Format=Address
    Type=1388  Name=IPGW-Address                   Format=Address

