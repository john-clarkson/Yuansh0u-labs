
Cisco Router <----->PA firewall<---- 202.10.71.1/24 ||202.10.71.254/24--->INET<---219.235.229.254/24||219.235.229.239/24---->PE
                    staic NAT  
                      source 172.16.10.13
                        destination untrust zone
                          destination ip address 219.235.229.249
                      source translated address <202.10.71.1>  
                           bidir <no check>

         GRE TUNNEL<---100.64.1.1/24-                        ospf full                                 -100.64.1.254/24--->GRE TUNNEL
 
         tunnel source 172.16.10.13                                                                     tunnel source 219.235.229.239   
         tunnel destination 219.235.229.239                                                             tunnel destination 202.10.71.1

##Cli test
Modify MGMT ip address
 set devicesetting system ip-address <MGMT-IP> netmask 255.255.255.0 default-gate 192.168.71.254
 commit force 
MGMT ping test
 ping host 192.168.71.1

Data-plane ping test
 ping source <ip address> host <destination-IP> 

##login PA firewall
  https://192.168.71.1
   username admin
   password admin
###security policy
  ALLOW-GRE universal source zone trust> destination zone untrust application GRE  action ALLOW 
  ALLOW-PING universal source zone trust> destination zone untrust application PING action ALLOW 
  ALLOW-ICMP universal source zone trust> destination zone untrust application ICMP action ALLOW 
  ACCESS-INET universal source zone trust> destination zone untrust application any action ALLOW 

###Nat policy

 ##STATIC NAT FOR GRE  
   source zone:trust
     source ip address 172.16.10.13 (cisco router GRE tunnel source)
   destination zone:untrust
      destination address 219.235.229.239/219.230.229.249 (NOVA PE PUBLIC IP)
      destination interface eth1/1 (Facing to INET)
source address translation
translation type <staic IP>
   translated address <202.10.1.1> (ETH1 PUBLIC IP)
    service any
    ## this bidir option must be not check, because the traffic from outside network will hit this policy (if you check bidir option, 
    ## it will automatic create outside into inside Destination NAT policy and it will match all source/service), the source is any,
    ## destination is 202.10.1.1, and it will translate the destination address back to 172.16.10.13, which is all traffic will send to 172.16.10.13.
    ## this opration will cause outside network can not access PA  firewall outside interface.

    bidirectional <no check>

 ##Dynamic ip and port for INET 
   source zone:trust
     source ip address 192.168.100.0/24 (LAN subnets)
   destination zone:untrust
      destination interface eth1/1 (Facing to INET)
source address translation
translation type <Dynamic ip and port>
   address type <interfae address>
   interface <eth1/1>
   ip address <202.10.71.1/24>
##Virtual router
  ##static route 
     name <default-route>
      destination <0.0.0.0/0>
      interface <none>
      next-hop <202.10.71.254>
      <click>OK
  ## redistribute profile setting
   name <redis-default> redistribute <check>
   priority <1>
   Gerneral filter 
      source type <static>
      <click>OK


   ##BGP setting
   <check>enable box router ID 202.10.71.1
   AS number 65511
    Gerneral 
      options 
      check> reject default route
      check> install route
      check> aggregate MED
      default local preference <100>

    peer group 
     add 
     name <EBGP-PEER>
      enable
      type EBGP
      import next-hop <use peer>
      export next-hop <use self>
peer as <XXX>
local address
interface <eth1/3>
ip <172.16.10.14/30>
peer address 
IP <172.16.10.13>
<check>OK




##SVTI mode IPSEC
 network 
  add tunnel interface 
    set ip address 
    zone setting  <trust>
    virtual router <default>
     management profile <permit all>

 ## IKE CRYPTO
  ## you can use default option to create your ipsec tunnels
  SVTI-IKE 
   encry <3des>
   authentication <md5>
   DH group <group2>

 ## SVTI-PHASE2
  ## For study testing purposes, you can set ESP-NULL to decrease resources usage and ESP payload is visible
  ## Wireshark can crack ESP-NULL payload. 
  ## Wireshark > edit > preference > protocols> ESP > check [attempt to detect/decode NULL encrypred ESP payloads]
    ipsec protocol <ESP>
    encryption <3des>
    dh-group <no-pfs>
    authentication <md5> 

IKE gateways
 ## peer setting/pre-shared key etc..
  ##Gerneral 
  name <SVTI>
  version <IKEv1 only>
  address type <IPV4>
  interface <eth1/1>
  local ip address 202.10.71.1/24
  peer ip type <static>
  peer ip address 202.20.71.1
  authentication <pre-shared key>
  pre-shared key <cisco>
  comfirm pre-shared key <cisco>
   local identification <none>
   peer identification <none>

  ##Advanced options
      IKEv1 
       exchange mode <mode>
       IKE Crypto profile <SVTI-IKE>

 ## ISPEC TUNNEL
  ##Gerneral
   name <SVTI>
   tunnel interface <tunnel.12>
   address type <IPV4>
   type <auto key>
   IKE gateway <SVTI>
    ipsec crypto profile <SVTI-PHASE2>
    <check> show Advanced options
     ##Tunnel monitor
      destination IP <202.20.71.1>
       profile <default>      





     