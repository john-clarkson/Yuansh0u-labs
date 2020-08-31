hostname IPv4_Only_Router
!
 

ip cef
!
interface g1.12
encap dot1q 12
ip address 20.20.20.2 255.255.255.0
no shut
!
ip route 27.1.1.0 255.255.255.0 20.20.20.1
!
end