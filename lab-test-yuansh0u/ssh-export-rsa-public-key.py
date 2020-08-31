
XE-P1(config)#crypto key generate rsa label SSH exportable Modulus 4096
% You already have RSA keys defined named SSH.
% They will be replaced.

% The key modulus size is 4096 bits
% Generating 4096 bit RSA keys, keys will be exportable...
[OK] (elapsed time was 8 seconds)

XE-P1(config)#ip ssh ver
XE-P1(config)#ip ssh version 2
XE-P1(config)#ip ssh
XE-P1(config)#ip ssh ?
  authentication-retries  Specify number of authentication retries
  break-string            break-string
  client                  Configuration for client
  dh                      Diffie-Hellman
  dscp                    IP DSCP value for SSH traffic
  logging                 Configure logging for SSH
  maxstartups             Maximum concurrent sessions allowed
  port                    Starting (or only) Port number to listen on
  precedence              IP Precedence value for SSH traffic
  pubkey-chain            pubkey-chain
  rekey                   Configure rekey values
  rsa                     Configure RSA keypair name for SSH
  server                  Configuration for server
  source-interface        Specify interface for source address in SSH
                          connections
  stricthostkeycheck      Enable SSH Server Authentication
  time-out                Specify SSH time-out interval
  version                  Version Supported

XE-P1(config)#ip ssh port
XE-P1(config)#ip ssh port ?
  <2000-10000>  Starting Port number

XE-P1(config)#ip ssh port 4000
% Incomplete command.

XE-P1(config)#ip ssh port 4000 ?
  rotary  Starting (or only) rotary group number

XE-P1(config)#ip ssh port 4000 ro
XE-P1(config)#ip ssh port 4000 rotary ?
  <1-127>  Low (or only) Rotary group number

XE-P1(config)#ip ssh port 4000 rotary 1 ?
  <1-127>  High Rotary group number
  <cr>

XE-P1(config)#ip ssh port 4000 rotary 1 2 ?
  <cr>

XE-P1(config)#ip ssh port 4000 rotary 1 2 
XE-P1(config)#end
XE-P1#show cry
XE-P1#show crypto ike
XE-P1#show crypto key   
XE-P1#show crypto key my
XE-P1#show crypto key mypubkey ?
  all  Show all public keys
  ec   Show ec public keys
  rsa  Show RSA public keys

XE-P1#show crypto key mypubkey rsa
XE-P1#show crypto key mypubkey rsa SSH
% Key pair was generated at: 11:34:11 UTC Feb 9 2018
Key name: SSH
Key type: RSA KEYS
 Storage Device: not specified
 Usage: General Purpose Key
 Key is exportable. Redundancy enabled.
 Key Data:
  30820222 300D0609 2A864886 F70D0101 01050003 82020F00 3082020A 02820201 
  00B0B716 2768C14E 787EFFDF AF7287EA 9260174B 3B99AC62 2C81769C 594D245B 
  0131473B AE407B2F CC54EEAD AB54D87C FED6DA2F 2BEE5AE8 8D3E0C83 9089D3AE 
  15668724 64B5CC80 1F81FEF7 FE8E8043 C6441E9C 2C450D01 70DB1FCC 76E6062D 
  5374E441 A7ABA740 2EBF1D9D 5168D73A 983470BB 579C70F8 0C9FF992 5AB6AF52 
  3ADEC15C 5E07B9BA 87E56EAC 907A1EE8 AE900530 48FBCEDC 9A6E8DBD F333F9CF 
  DD48A123 45782E12 4D78734E 8ACFF126 0F3BE957 7C3F5670 59D6D4EA 18D8AD7C 
  0DB7BD21 68A13DC8 6EEFA18A E5A7B693 73920955 882D2F33 0237258B 30D9DB89 
  6C8242A4 15E9AD88 AA65F790 09C7814B 2741DC84 947FCFE6 2481AAD6 4EF86967 
  437178D6 89BE4293 5C2F2B10 3E7E8C0E C3CAEF3F A4EB03B5 32EE0A28 523A07AD 
  0801E567 32430527 8CD64B6F 8F6F918D 08CB4633 CC45CA03 8C1D58CB 2F5E03A2 
  BF8CFC82 E2415998 1D192112 29553B6B B7EF45C1 259916CB 32D6E3B5 AA8D854E 
  6DC8AEBC E0704AF8 058793FA 23824FFC AFEEA68F 99B1D71B 2BEA591B 35102467 
  418E0493 249BB0C7 96C1E27D 9103939A 7521FDBB E29E55AD 7EDA0014 C8E8A7AA 
  CCF1AA75 284D9010 65C30C0B 87911BE5 300A1D9B FAAE6CCA B2BC08EA 58211F66 
  F96E532C 37349254 B241B3CC 233B076C 6E0A6761 EF711DEE 0ED0DBBF C8101254 
  C92D3507 BE0D92E4 E2D9F752 1ACEB2CA 4C216965 D67CD7A7 A7A8F780 50D0776B 
  A1020301 0001
XE-P1#
XE-P1(config)#crypto key export rsa SSH PEM TERminal 3DES ?
  LINE  Passphrase used to protect the private key

XE-P1(config)#crypto key export rsa SSH PEM TERminal 3DES SSH
% Passphrase is too short, needs to be at least 8 chars
XE-P1(config)#crypto key export rsa SSH PEM TERminal 3DES FUCK_YOU  
% Key name: SSH
   Usage: General Purpose Key
   Key data:
-----BEGIN PUBLIC KEY-----
MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAsLcWJ2jBTnh+/9+vcofq
kmAXSzuZrGIsgXacWU0kWwExRzuuQHsvzFTuratU2Hz+1tovK+5a6I0+DIOQidOu
FWaHJGS1zIAfgf73/o6AQ8ZEHpwsRQ0BcNsfzHbmBi1TdORBp6unQC6/HZ1RaNc6
mDRwu1eccPgMn/mSWravUjrewVxeB7m6h+VurJB6HuiukAUwSPvO3Jpujb3zM/nP
3UihI0V4LhJNeHNOis/xJg876Vd8P1ZwWdbU6hjYrXwNt70haKE9yG7voYrlp7aT
c5IJVYgtLzMCNyWLMNnbiWyCQqQV6a2IqmX3kAnHgUsnQdyElH/P5iSBqtZO+Gln
Q3F41om+QpNcLysQPn6MDsPK7z+k6wO1Mu4KKFI6B60IAeVnMkMFJ4zWS2+Pb5GN
CMtGM8xFygOMHVjLL14Dor+M/ILiQVmYHRkhEilVO2u370XBJZkWyzLW47WqjYVO
bciuvOBwSvgFh5P6I4JP/K/upo+ZsdcbK+pZGzUQJGdBjgSTJJuwx5bB4n2RA5Oa
dSH9u+KeVa1+2gAUyOinqszxqnUoTZAQZcMMC4eRG+UwCh2b+q5syrK8COpYIR9m
+W5TLDc0klSyQbPMIzsHbG4KZ2HvcR3uDtDbv8gQElTJLTUHvg2S5OLZ91IazrLK
TCFpZdZ816enqPeAUNB3a6ECAwEAAQ==
-----END PUBLIC KEY-----
-----BEGIN RSA PRIVATE KEY-----
Proc-Type: 4,ENCRYPTED
DEK-Info: DES-EDE3-CBC,16A77F1A001ABC85

+ejsIUi5EmpkaDEwHKol2OfyuaIyoNJVZ5jfF4s3uGFq7VAIUVNkAuxRDsABJyqs
28MGz+Y2wkWW05nZCswTlofbj5EweXu6hPeG/8tiXlQGJIw7brHVz6eLFPiDcAvf
aqEuTFzhd9UJuTEYACXSuM08vEtY+lvSjiIgver7ElniNFbwPvUdv/viGW/QxPeC
rtKiWHAkc2bW9waHGXdJaYy2gXfq92m8slcyWcGQiSobDQ85ANVmGdBelNWph49H
fiuaGMzwzj1jCFUod3p1uuMDmPEfHVA6hyf4rTh0CZjuFQ9/anc6UF+zJSbQ1quM
DpzXx8eieP9gVKsVb/GlKX8xcpoSYgJwrLiATwdSK1cfYrb3RQjfsrigDJWubwZL
yEC90GTHat0YRxttg/WhEzR2BhgPqb+wZRHOCGNT0SNNbxpbvKlEj2veoMizEg3T
lqpXdKnOWWAzQ9Ik3P9q6d+hqq9TK0HBioC+cyL63cjhOEVpFzjukFCbxwGPJJwb
L1YY7C+KTpHaRJw0n616MZSMkEODBCJ1ZY4us8evlQ9LyLkkW/5tNKFEF/FyZA6c
/EWjoXDNpHP2YVBG/56zcpeVo5QgAe1vBdkUckzDKqe2Q5Qsl4TK8wplJwO3HLUS
XlykW1ti8IDGzIZV5KvqeHA+ybR95MzTcF8Wes55HW/xMd3pLieghwss0fGUOxIu
aWwozbwcrlrsxtu2GSLJfOim0v6SlSmPJhEkt4ptpmoVz21Wel2qhbyuHfIUYaNl
da/2ietL0kvUHIxx0yFmCCvxzE3ZB8J4vbtHXxpZlWqKyzPM4oW6CWR/4/s0FL4J
Y25yjuPJQvI5YMnsWVKDII1xbCq4gVjvcGtGDus45ztuYGKBB4vVjrVOFDeyYEdr
RN3UYSMWua4uVLiVdHGBepeZ9QrOlBZjEXdSih1/lolFD2HSJbKDKk7iwhL6as+L
YGmpLCMrPGmue1Q5U0TfQDDOAw2No4XPBbzfCmSt7KSvuU9lzzdM0LdN20Q4HSnH
wBu2wChO7lUxEEUareADhD7DMcXxHF3YTnzow7U3iZHxM+F+Gf6T81aR80p3JTyQ
//mxFjAG2xN9vzA2nWmkIzm7SuQ4oe5H6yz+xl0W5nfIgUDsUt1z2Sc3kKjnbV8z
2C64cuULtV5sNbUcwHPXUdtaT5WVP8EA8mmiAWrXTVad+QI8ScoU4fSYnqIVX1bM
02ve8HtzmsiaBdvGzMrofr/9SsLsht9h/88uwewQg8OehueqnLC7e9qTEo6AB+LY
5YrD/spdgvRfIb22NgHmN2qtZzyMs5LnymHZO4wNFjk6p6dy3gtCnC21uyUsOEsQ
6ly7pNo5dFdIQC+GZDqXPqSU3oii8WJt2ofI//c9EZG6nivPzTyvXU5ZQjGTksbS
pT4RVLIHY17M2rJL9oFwOGQ1wmqsodofscCoYpisAM05vQ6kERptDzA5FeaLuJJT
hdgfTnuzVT6X0rtvTRCgua9m1dKv5IT6lwVe5QBLR0kjFbp9OfqbJkLqrg7yu88M
h2WaVag1FBDt1StQiy9rWm0gJjez0ElkZx3fZHLXz32R7VAb1uFEEFNn/9nfLI4c
+eL3Td7i4EIdeuextXGOLSBRib384LkBy1eiemR49PuEocTFFupenwfR9JRpPjEO
nQQV41Soh8cB87h50CCnRDiVIBP5JNT0FnS8ZeJZBRcPe4HpocaWWmb9ynZUEF22
SZ1g9SF+jhw/JpWdhfAEFwVQlboZzBjK/atD35uKYIn748BaOnm9fnouw2steIZF
3oCa0L7ST9oMmEUN1OR+rrReQbGdxzEGy5OOc3Y2jUxBJPqUXOcHIGqhHsbGKGyL
gwiTqtknAEpB8RJjEJSzdGKfnlmY9Fq87dhMlrgiOrT/MX5qpAt7ByMY2ffvRPeo
oxQC+4+BgpW1lerZoN7YJw7ZLvYxjmrNm8ttJHaXNVY5Gnk5MrpV9MUh3ebW2GPK
tb3tb+uIn1vBQESI5sTKNCF60rN6kNaLywbTP6H4dIUnkm51bCHUkGznn0G+MQFl
SczGP/VB7vpWwtRpGER4roYGbXZ2dDywxsEhqnxVY3T3mEEBCvQGoeOpfrAiylKy
UAe/5qos/ZY05iTQBxJjxFlOocLoMCdEZZQJKrGJQTHSNBIJZFUcVHQtuDsMsDkn
vcfOfPqZAfqFqVtPu6HIyog1a1dCJNZ2a7g8oHXbCyKpSIRpEibuCLRZEmu40eWq
4RcZMAHU+y+gYZcZbyrRG86x8at0vK8L88llUx1rFe9NVSOcMKgGm1v9iAoAZvDs
oLKX9bsthini8ubYfm9V/oZe43Pa0UR7mKXOJSG1MeHNk4lfr6CFzU0zuKBPUER3
5OorjcgjX21nK5FpgAXSlNk87B+qxsCPoqyWHIehqZf7IpgNRnEBosWHg1iUyblH
llxONkxUQwCDTEM9TjHMc8WBT+bOYQjiOV1QLmOb7Z/hC2k/nMyMGgzwsuS3On4P
pX/kjDiwHCgTz+1FL0dkoVDmYVGcO3JqLS3pu3i0rUa37RbVNENps7tFzCwg579Z
83yKrFUSl+naUtwfXUxEj6+hcmpynBEM8G7XvP7YJyrt0N7lynHZ2OZPPIqWbAAu
t6RBCjzMWix0sJPNh4/pb+aPPwZrtaNTgwzGbyaHc51HreJB0h2Eo0N3flLEyeBl
JMKTV1yLLZviJMW4bPnecnFBGv5RA3lmUaNIKLNAD+mItyD06+jO2l2JCBydoy3Q
xYD+T6COxcNIIacadQmmf723vzYb0YXQ2NxFbkNHny9F0J/Eh8iNlWitNVBPHymo
8bHBzAL6QjieXxHpBdIw3U0tuZ+3zQfPBEgPGh5ZezFVeUSVxbEKPb0dHxfvFy+I
EgLYmcTt4+SIZEjoUff/QaxoR58e89dqWaRymZp7nY1vcvxlOqIqILWng4IoLq01
wPnnA1wtktkARSj5n2SQZSBc3JfXWLj+o8yf62zKQTlJAhRR3Bjmdk0xJmqDSXOA
n3FJHCmLxXZK0RgkbRs3hmUTPDwJ9+ndDir/QmkUFbx9w0/g9mNjuia9mC6USFrI
mUfTDztuH6QM/3b+VqRhD+j8yriDnd57iLxcTQrULSHLduY4R7NckrKrqO28YPZV
-----END RSA PRIVATE KEY-----

XE-P1(config)#