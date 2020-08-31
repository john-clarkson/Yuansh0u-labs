
mkdir flash:EEM

	tclsh
	puts [ open "flash:EEM/EEM.tcl" w+ ] {
	::cisco::eem::event_register_syslog pattern COUNT
	}
	tclquit	

R1#show event manager environment all
No.  Name                          Value                         
1    _event_id                     
R1#show event manager policy registered 
No.  Class     Type    Event Type          Trap  Time Registered           Name
1    script    user    syslog              Off   Mon May 29 22:55:49 2017  EEM.tcl
 pattern {COUNT}
 nice 0 queue-priority normal maxrun 20.000 scheduler rp_primary Secu none

------------------------------------------------------------------------------------------------------

tclsh flash:EEM/EEM.tcl


enable
 configure terminal
event manager environment _show_cmd show event manager policy registered
event manager directory user policy "bootflash:/EEM"
event manager environment eem_syslog_statement ::cisco::eem::event_register_syslog pattern COUNT


no event manager applet FLAPPING_IGP
event manager applet FLAPPING_IGP
 event timer watchdog time 10 maxrun 0
    action 1.0 cli command "end"
    action 1.1 cli command "exit"
    action 1.2 cli command "enable"
    action 1.3 cli command "tclsh flash:/EEM/EEM.tcl"
    action 1.4 puts "$_cli_result"

========================================
enable
 configure terminal
   event manager applet TEST
    event none
    action 1.0 syslog msg "hahahah"
R1#event manager run TEST
==============================================
tclsh
puts [ open "flash:EEM/EEM.tcl" w+ ] {
	typeahead "yes"
    ios_config "do clear ip ospf process"
}
write memory
tclquit

no event manager applet FLAPPING_IGP
event manager applet FLAPPING_IGP
 event timer watchdog time 10 maxrun 0
    action 4.3 cli command "configure t"
    action 4.4 cli command "inter loop 123"
    action 4.5 cli command "do show ip int b"

    action 4.8 cli command "cisco"
    action 5.3 cli command "tclsh flash:/EEM/EEM.tcl"
    action 6.4 puts "$_cli_result"

no event manager applet FLAPPING_IGP
    event manager applet FLAPPING_IGP
 event timer watchdog time 5
   action 1.0 cli command "enable" 
   action 1.1 cli command "tclsh flash:/EEM/EEM.tcl"
   action 1.2 puts "$_cli_result"


no event manager applet show-ip-int-b
 event timer watchdog time 5 
   action 1.0 cli command "enable"
   action 1.1 cli command "show ip int b"
   action 1.2 puts "$_cli_result"


 
