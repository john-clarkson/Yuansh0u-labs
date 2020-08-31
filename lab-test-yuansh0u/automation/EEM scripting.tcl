
enable
 ter monitor
 configure ter
  logging console 7 
  hostname R1
no ip domain-look
interface g1
 ip address 10.1.1.1 255.255.255.0
 no shut
 ip ospf 1 area 0

router bgp 1
  neigh 10.1.1.2 remote-as 1
  redis con

enable
 ter monitor
 configure ter
  logging console 7 
hostname R2
no ip domain-look
  interface g1
 ip address 10.1.1.2 255.255.255.0
 no shut
 ip ospf 1 area 0
  interface loo 0
    ip address 2.2.2.2 255.255.255.255
     ip ospf 1 area 0
router bgp 1
  neigh 10.1.1.1 remote-as 1
   redis con



EEM scripting

Danger command:

!!!!!!////disable enable mode 

event manager applet DIS-Enable
 event cli pattern "enable" skip yes sync no


!!!!!!////disable configure mode 

event manager applet DIS-CONFIG-MODE
 event cli pattern "configure terminal" skip yes sync no

!!!!!!////disable sh run

event manager applet DIS-SH-RUN
 event cli pattern "show running-config" skip yes period 0 sync no
  action 1.0 cli command "enable"
  action 1.1 syslog msg "You know what?"
  action 1.5 puts "$_cli_result"
ROUTER#sh run
*May 28 19:53:06.705: %HA_EM-6-LOG: DIS-SH-RUN: You know what
ROUTER#sh runn
ROUTER#sh running-config 
ROUTER#sh running-config | sec ospf
===================================================

!!!!!!//// Disable routing control-plane

event manager applet DIS-ROUTING
  event cli pattern "router [eEoObBiIRr].*" sync no skip yes

motherfucker(config)#router ospf 1
motherfucker(config)#router eigrp 1
motherfucker(config)#router bgp 1  
====================================================

event manager applet test-hostname
 event cli pattern "hostname fuck" sync yes
  action 1.0 cli command "enable"
  action 1.1 cli command "config terminal"
  action 1.2 cli command "hostname motherfucker"
  action 1.3 cli command "interface loop 0"
  action 1.4 cli command "no shutdown"
=========================================================
event manager applet ENABLE-DEBUG
 event timer watchdog time 10
       !// 1 seconds
    action 1.0 cli command "enable"
    action 1.1 cli command "debug ip packet detail"
    action 1.2 cli command "ping 255.255.255.255 repeat 1"
    action 1.3 puts "$_cli_result"


!///Worked!!!!
enable
configure terminal
no event manager applet FLAPPING_BGP
event manager applet FLAPPING_BGP
 event timer watchdog time 10 maxrun 0
       !// 10 seconds
    action 1.0 cli command "enable"
    action 1.1 cli command "clear ip bgp *"
    action 1.3 puts "$_cli_result"

___________________________________________________________

||testing!!!!!!
enable
 configure terminal
event manager applet FLAPPING_IGP
 event timer watchdog time 10 maxrun 0
       !// 1 seconds
    action 1.0 cli command "enable"
    action 1.1 cli command "clear ip ospf process"
    action 1.2 cli command "yes"

    action 1.3 puts "$_cli_result"
___________________________________________________________

event manager applet RELOAD_SYSTEM
 event timer watchdog time 10 
    action 1.0 cli command "enable"
    action 1.1 cli command "write"
    action 1.2 cli command "terminal no monitor"
    action 1.3 cli command "configure terminal"
    action 1.4 cli command "no logging console"
    action 1.5 reload
    action 1.6 puts "$_cli_result"


event manager environment _cron_entry 0-59/2 0-23/1 * * 0-6
event manager policy tm_cli_cmd.tcl type system
=======================================================
event manager applet show-ip-int-b
 event timer watchdog time 1 
   action 1.0 cli command "enable"
   action 1.1 cli command "show ip int b"
   action 1.2 puts "$_cli_result"
motherfucker#show event manager  policy registered 
No.  Class     Type    Event Type          Trap  Time Registered           Name
1    applet    user    timer watchdog      Off   Sun May 28 21:04:18 2017  show-ip-int-b
 time 5.000
 maxrun 20.000
 action 1.0 cli command "enable"
 action 1.1 cli command "show ip int b"
 action 1.2 puts "$_cli_result"

motherfucker#


=================
enable 
 config t
    no event manager applet ENABLE-DEBUG
    no event manager applet RELOAD-BOX
    no event manager applet show-ip-int-b
    no event manager applet FLAPPING_BGP

    clear  line vty 0/1/2/3/4