  no password strength-check
  switchname 213123
vrf context management
ip route 0.0.0.0/0 1.2.3.2
exit
  no feature telnet
  ssh key rsa 1024 force
  feature ssh
  system default switchport
  no system default switchport shutdown
  copp profile strict
interface mgmt0
ip address 1.2.3.4 255.255.255.0
no shutdown