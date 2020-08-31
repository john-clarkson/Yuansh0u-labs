##UBUNTU Docker
 $ apt-get update && apt-get install docker.io
 $ docker version
 $ docker info
 $ docker search nginx
 $ docker search debian
 ##Downloading images from dockerhub
 $ docker pull nginx && docker pull debian
 ///
 ##Running nginx image with iptables policy, doing port forwarding operations.
 $ docker run --name docker-nginx -p 80:80 -d nginx
 #docker run --name <container-name> -p 80:80 -d <image>
///
##Running debian image and login into container
 $docker run --name debianhitler -it debian /bin/bash
#docker run --name <container-name> -it <image> /bin/bash
##The -i means "run interactively", and -t means "allocate a pseudo-tty".
///
##check docker status,and delete all test dockers
 $ docker ps -a 
 $ docker stop $(docker ps -a -q) && docker rm $(docker ps -a -q)
 $ docker rm <container-id>
 $ docker container start docker-nginx
##Docker container location list
root@VPC1-U001:/var/lib/docker/containers# ls
1c7dd828d58faa0fc920a604a3ddc11eb54e0c0219bf324d292a6fdfd4dc9d21

##login container
docker rename <original-name> <target-name>
docker container attach <container-ID|container-name>
##ctrl+d to exit container without shutdown
docker exec -ti debianhitler /bin/bash
docker exec -ti  tomcat
docker exec -ti  tomcat apt install -y net-tools
apt-get update
apt install net-tools       # ifconfig 
apt install -y iputils-ping     # ping

service nginx restart
root@VPC1-U002:/# find . |grep index.html
./var/lib/docker/aufs/diff/f46179b478b9a2dacbbf85ac91640dee4e57ef7c2dac6b1a3c8d522feafe64bd/usr/share/nginx/html/index.html
root@VPC1-U002:/# nano./var/lib/docker/aufs/diff/f46179b478b9a2dacbbf85ac91640dee4e57ef7c2dac6b1a3c8d522feafe64bd/usr/share/nginx/html/index.html
<html>
<head>
<title>FUCK!!!Welcome to nginx!</title>
<style>
    body {
        width: 35em;
        margin: 0 auto;
        font-family: Tahoma, Verdana, Arial, sans-serif;
    }
</style>
</head>
<body>
<h1> hello! cao ta gu!!!ok?? han zi dou xian shi bu chu lai ,ni ge po web!</h1>
<p>If you see this page, the nginx web server is successfully installed and
working. Further configuration is required.</p>

<p>For online documentation and support please refer to
<a href="http://nginx.org/">nginx.org</a>.<br/>
Commercial support is available at
<a href="http://nginx.com/">nginx.com</a>.</p>

<p><em>Thank you for using nginx.</em></p>
</body>
</html>
ctrl+x 
yes

  
##Docker NAT,this is default operation that docker engine automatic do it for you.
##Traffic flow <container---veth-----veth<docker0>---->iptables<SNAT>---NIC---->pysical network
root@VPC1-U001:/# iptables -t nat -l
iptables v1.6.0: unknown option "-l"
Try `iptables -h' or 'iptables --help' for more information.
root@VPC1-U001:/# iptables -t nat -L
Chain PREROUTING (policy ACCEPT)
target     prot opt source               destination         
DOCKER     all  --  anywhere             anywhere             ADDRTYPE match dst-type LOCAL

Chain INPUT (policy ACCEPT)
target     prot opt source               destination         

Chain OUTPUT (policy ACCEPT)
target     prot opt source               destination         
DOCKER     all  --  anywhere            !127.0.0.0/8          ADDRTYPE match dst-type LOCAL

Chain POSTROUTING (policy ACCEPT)
target     prot opt source               destination         
MASQUERADE  all  --  172.17.0.0/16        anywhere            
MASQUERADE  tcp  --  172.17.0.2           172.17.0.2           tcp dpt:http

Chain DOCKER (2 references)
target     prot opt source               destination         
RETURN     all  --  anywhere             anywhere            
DNAT       tcp  --  anywhere             anywhere             tcp dpt:http to:172.17.0.2:80
root@VPC1-U001:/# 

root@VPC1-U001:/# iptables -t nat -L -n -v
Chain PREROUTING (policy ACCEPT 0 packets, 0 bytes)
 pkts bytes target     prot opt in     out     source               destination         
14968  897K DOCKER     all  --  *      *       0.0.0.0/0            0.0.0.0/0            ADDRTYPE match dst-type LOCAL

Chain INPUT (policy ACCEPT 0 packets, 0 bytes)
 pkts bytes target     prot opt in     out     source               destination         

Chain OUTPUT (policy ACCEPT 11 packets, 757 bytes)
 pkts bytes target     prot opt in     out     source               destination         
    0     0 DOCKER     all  --  *      *       0.0.0.0/0           !127.0.0.0/8          ADDRTYPE match dst-type LOCAL

Chain POSTROUTING (policy ACCEPT 52 packets, 3217 bytes)
 pkts bytes target     prot opt in     out     source               destination         
   65  4148 MASQUERADE  all  --  *      !docker0  172.17.0.0/16        0.0.0.0/0           
    0     0 MASQUERADE  tcp  --  *      *       172.17.0.2           172.17.0.2           tcp dpt:80

Chain DOCKER (2 references)
 pkts bytes target     prot opt in     out     source               destination         
    0     0 RETURN     all  --  docker0 *       0.0.0.0/0            0.0.0.0/0           
  244 14640 DNAT       tcp  --  !docker0 *       0.0.0.0/0            0.0.0.0/0            tcp dpt:80 to:172.17.0.2:80
root@VPC1-U001:/# 

##Create own network
root@localhost:~# docker network create HITLER-BR
b642883400449e280a2939d8146e84441ca7c66be644c254f0988dab8a62215a
root@localhost:~# docker network ls
NETWORK ID          NAME                DRIVER              SCOPE
b64288340044        HITLER-BR           bridge              local
c921af890ada        bridge              bridge              local
442cc6e14a4a        host                host                local
ca7ceefbfd86        none                null                local
root@localhost:~# 

##Create network namespaces
sudo ip netns add HITLER1
##Delete network namespaces
sudo ip netns del HITLER1
##show netns instance
seaomi@localhost:/$ sudo ip netns show
HITLER2
HITLER1
##Create vETH pair
 sudo ip link add DICK type veth peer name PUSSY
##veth allocate to namespace HITLER1
sudo ip link set PUSSY netns HITLER1
##login netns
sudo ip netns exec HITLER1 bash
seaomi@localhost:/$ sudo ip netns exec HITLER1 bash
root@localhost:/# ip a
1: lo: <LOOPBACK> mtu 65536 qdisc noop state DOWN group default qlen 1
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
19: PUSSY@if20: <BROADCAST,MULTICAST> mtu 1500 qdisc noop state DOWN group default qlen 1000
    link/ether 0e:ce:ea:94:f0:3c brd ff:ff:ff:ff:ff:ff link-netnsid 0
root@localhost:/# 
##Assign IP address to veth interface <DICK=root netns/PUSSY=HITLER1 netns>
ip netns exec HITLER1 ifconfig PUSSY 10.1.1.1/24 up
sudo ifconfig DICK 10.1.1.2/24 up
##PING TEST
seaomi@localhost:/$ ping 10.1.1.1
PING 10.1.1.1 (10.1.1.1) 56(84) bytes of data.
64 bytes from 10.1.1.1: icmp_seq=1 ttl=64 time=0.067 ms
^C
###


sudo ip netns exec HITLER1 ip link add edge_bridge1 type bridge


                                                                      source NAT-POSTROUTING source DOCKER SUBNETS-->anywhere
                                    |                                |  after NAT SOURCE= ETH0 
DOCKER-1 172.17.0.1-------veth------|Docker0<bridge=L2SW-172.17.0.254|---[ ip tables ] eth0 192.168.1.1-->192.168.1.254  --->>>>>outside<INET>
DOCKER-2 172.17.0.2-------veth------|                                |                                          


docker1 <Aport---veth----Bport> docker2 

docker= container<APP>
##docker software
ubuntu---OS--->docker engine| container <APP nginx> unique IP
                            | container <debian> unique IP
 <                          |
##DOCKER---SWARM
##K8S control-plane 

distribution system
  

   k8S master--->>command=control-plane
    
k8s 
worker
   multiple container ---->>single POD <namespace> ---1 IP 
   ->pod pod connect <FLANNEL=etcd data store <JSON format>--data-plane--VXLAN>
                     <CALICO=BGP IPV4 unicast/distribution Firewall=iptables=namespace>  
   ->pod to service  <Cluser IP=VRRP-VIP-Load balancing>
   ->pod to external < >

   network
   storage
   status




Security issue < >

hacker--><VM-VIRUS>>>>HYPER>>>OS <SAFE>  ===>Public cloud

hacker->>docker app <> ---OS<VAR/PATH/FOLDER/PID> kill <PID> <Private cloud>




  linuxOS >>hypervisor<VMware KVM hyper-V>
                                          >virtual hardware CPU/MEM/DISK/NIC/USB <driver> <VM=GUEST OS> VCPU >hyper/KVM

                                            NESTED VM 
        hardware CPU-intel-VT/MEM/Disk                      VCPU/MEM/vmdk 
 
  linuxOS--->containerize->DOCKER LXC 

        linux lib>var>system>kernel

     Kernel network/Storage/Resources pool<CPU/MEM>
              netns cgroup <container>    <<<<<-APP 




 #####modufy docker0 default ip<172.17.0.0/16>
 #####THIS IS DEFAULT OUTPUT
  ip a 
  4: docker0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default 
    link/ether 02:42:32:72:cd:dc brd ff:ff:ff:ff:ff:ff
    inet 172.17.0.1/16 scope global docker0        
###STEP
You can configure the default bridge network by providing the bip option along with the desired subnet in the daemon.json (default location at /etc/docker/daemon.json on Linux) file as follows:

{
  "bip": "172.26.0.1/16"
}
Then restart the docker daemon (sudo systemctl restart docker on systemd based Linux operating systems).    

###create daemon.json file under etc/docker
root@localhost:/etc/docker# touch daemon.json
root@localhost:/etc/docker# vi daemon.json
{
  "bip": "100.64.88.1/24"
}
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
"daemon.json" 3L, 30C written                                                      
root@localhost:/etc/docker# 
root@localhost:/etc/docker# 


root@localhost:/etc/docker# ip a
****
4: docker0: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc noqueue state DOWN group default 
    link/ether 02:42:32:72:cd:dc brd ff:ff:ff:ff:ff:ff
    inet 172.17.0.1/16 scope global docker0
       valid_lft forever preferred_lft forever
    inet6 fe80::42:32ff:fe72:cddc/64 scope link 
       valid_lft forever preferred_lft forever
****       
root@localhost:/etc/docker# systemctl stop docker
root@localhost:/etc/docker# systemctl start docker
root@localhost:/etc/docker# 
root@localhost:/etc/docker# 
root@localhost:/etc/docker# 
root@localhost:/etc/docker# 
root@localhost:/etc/docker# docker ps
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES
root@localhost:/etc/docker# docker ps -a
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS                          PORTS               NAMES
bafb896f499d        debian              "/bin/bash"         38 hours ago        Exited (0) About a minute ago                       debianhitler
root@localhost:/etc/docker# 
root@localhost:/etc/docker# 
root@localhost:/etc/docker# ip a
****
4: docker0: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc noqueue state DOWN group default 
    link/ether 02:42:32:72:cd:dc brd ff:ff:ff:ff:ff:ff
    inet 100.64.88.1/16 scope global docker0
       valid_lft forever preferred_lft forever
    inet6 fe80::42:32ff:fe72:cddc/64 scope link 
       valid_lft forever preferred_lft forever
****       
root@localhost:/etc/docker# docker start debianhitler debianhitler 
debianhitler
debianhitler
root@localhost:/etc/docker# docker ps
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES
bafb896f499d        debian              "/bin/bash"         38 hours ago        Up 5 seconds                            debianhitler
root@localhost:/etc/docker# 
root@localhost:/etc/docker# docker exec -ti debianhitler debianhitler bin/bash
rpc error: code = 2 desc = oci runtime error: exec failed: container_linux.go:247: starting container process caused "exec: \"debianhitler\": executable file not found in $PATH"

root@localhost:/etc/docker# docker exec -ti debianhitler bin/bash
root@bafb896f499d:/# ls
bin   dev  home  lib64  mnt  proc  run   srv  tmp  var
boot  etc  lib   media  opt  root  sbin  sys  usr
root@bafb896f499d:/# ip a
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host 
       valid_lft forever preferred_lft forever
7: eth0@if8: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default 
    link/ether 02:42:64:40:00:01 brd ff:ff:ff:ff:ff:ff link-netnsid 0
    inet 100.64.0.1/16 scope global eth0
       valid_lft forever preferred_lft forever
    inet6 fe80::42:64ff:fe40:1/64 scope link 
       valid_lft forever preferred_lft forever
root@bafb896f499d:/# ping www.baidu.com
PING www.wshifen.com (104.193.88.123) 56(84) bytes of data.
64 bytes from 104.193.88.123 (104.193.88.123): icmp_seq=1 ttl=127 time=219 ms
64 bytes from 104.193.88.123 (104.193.88.123): icmp_seq=2 ttl=127 time=219 ms
^C
--- www.wshifen.com ping statistics ---
2 packets transmitted, 2 received, 0% packet loss, time 1001ms
rtt min/avg/max/mdev = 219.075/219.336/219.597/0.261 ms
root@bafb896f499d:/# 

##show docker container IP address

##docker inspect --format '{{ .NetworkSettings.IPAddress }}' <container-ID>
root@localhost:/# docker ps 
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                NAMES
7778b8c56417        nginx               "nginx -g 'daemon ..."   4 seconds ago       Up 3 seconds        0.0.0.0:80->80/tcp   docker-nginx
bafb896f499d        debian              "/bin/bash"              39 hours ago        Up 4 minutes                             debianhitler
root@localhost:/# docker inspect --format '{{ .NetworkSettings.IPAddress }}' 7778b8c56417
100.64.88.3
root@localhost:/# 



docker run --name debianhitler2 -it debian /bin/bash



root@localhost:/etc/default# ll
total 96
drwxr-xr-x  2 root root 4096 Sep  5 00:22 ./
drwxr-xr-x 93 root root 4096 Sep  5 08:06 ../
-rw-r--r--  1 root root  125 Aug 20  2015 bridge-utils
-rw-r--r--  1 root root  222 May 22  2012 bsdmainutils
-rw-r--r--  1 root root  283 Aug 21 00:21 console-setup
-rw-r--r--  1 root root  549 Aug 22  2014 crda
-rw-r--r--  1 root root  183 Apr  5  2016 cron
-rw-r--r--  1 root root  297 Dec  1  2015 dbus
-rw-r--r--  1 root root   92 Jan 19  2016 devpts
-rw-r--r--  1 root root  556 Apr 17 18:20 docker
-rw-r--r--  1 root root 1264 Aug 21 00:26 grub
-rw-r--r--  1 root root   86 Jan 19  2016 halt
-rw-r--r--  1 root root  126 Aug 21 00:25 irqbalance
-rw-r--r--  1 root root  150 Aug 21 00:21 keyboard
-rw-r--r--  1 root root   72 Aug 21 00:21 locale
-rw-r--r--  1 root root  306 Jun  2  2015 networking
-rw-r--r--  1 root root 1756 Apr 13  2016 nss
-rw-r--r--  1 root root  620 Aug 21 00:26 rcS
-rw-r--r--  1 root root 1768 Sep 30  2013 rsync
-rw-r--r--  1 root root  124 Jan 27  2016 rsyslog
-rw-r--r--  1 root root  133 Mar 16  2017 ssh
-rw-r--r--  1 root root 1409 Nov 17  2015 ubuntu-fan
-rw-r--r--  1 root root 1754 Apr 14  2016 ufw
-rw-r--r--  1 root root 1118 Mar 29  2016 useradd
root@localhost:/etc/default# 



Connect a container to a user-defined bridge
When you create a new container, you can specify one or more --network flags. This example connects a Nginx container to the my-net network. It also publishes port 80 in the container to port 8080 on the Docker host, so external clients can access that port. Any other container connected to the my-net network has access to all ports on the my-nginx container, and vice versa.

$ docker create --name my-nginx \
  --network my-net \
  --publish 8080:80 \
  nginx:latest
To connect a running container to an existing user-defined bridge, use the docker network connect command. The following command connects an already-running my-nginx container to an already-existing my-net network:

$ docker network connect my-net my-nginx

##########
docker-bridge without iptables and connect to pysical NIC port
#pysical NIC port
ens33: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP group default qlen 1000
    link/ether 00:0c:29:dc:91:4e brd ff:ff:ff:ff:ff:ff
    inet 192.168.80.155/24
#
#create docker-bridge with IP settings
root@localhost:/etc/default# docker network create FUCK-BR2 --subnet 123.123.123.0/24 --gateway 123.123.123.1
43f3e14dc65eaf70b2df2c2b7213538335c5619418b26188a221d9660af3350c
root@localhost:/etc/default# 
root@localhost:/etc/default# 
root@localhost:/etc/default# 
root@localhost:/etc/default# docker network inspect 
bridge    FUCK-BR   FUCK-BR2  host      none      
root@localhost:/etc/default# docker network inspect FUCK-BR2
[
    {
        "Name": "FUCK-BR2",
        "Id": "43f3e14dc65eaf70b2df2c2b7213538335c5619418b26188a221d9660af3350c",
        "Created": "2018-09-07T03:12:53.372525371-07:00",
        "Scope": "local",
        "Driver": "bridge",
        "EnableIPv6": false,
        "IPAM": {
            "Driver": "default",
            "Options": {},
            "Config": [
                {
                    "Subnet": "123.123.123.0/24",
                    "Gateway": "123.123.123.1"
                }
            ]
        },
        "Internal": false,
        "Attachable": false,
        "Containers": {},
        "Options": {},
        "Labels": {}
    }
]
root@localhost:/etc/default# 

docker inspect -f '{{.State.Pid}}' "VPC-UBUNTU-1

##addiface
ifup vlan33
ping 192.168.33.254

##BASE NETWORK BR WITH TEST-INTERFACE


brctl addif br-981a89a08ba7 ens33
ip addr del 192.168.80.155/24 dev ens33
ip addr add 192.168.80.155/24 dev br-981a89a08ba7
ip route add default via 192.168.80.2 dev br-981a89a08ba7

docker run --name debianhitler3 -it debian /bin/bash

##create container with network allocation with static IP address!
docker run --name docker-nginx-FUCK-BR2 --net FUCK-BR --ip 172.17.0.253 -d nginx 
docker run --name BASE-NETWORK-UBUNTU001 -it --net BASE-NETWORK-BR --ip 192.168.255.1 -d debian /bin/bash

##start 
docker start docker-nginx-FUCK-BR
docker start docker-nginx-FUCK-BR2
docker start debianhitler
docker start debianhitler2
docker start debianhitler3

docker exec -ti debianhitler /bin/bash

 
docker exec -ti debianhitler /bin/bash
docker exec -ti debianhitler2 /bin/bash
docker exec -ti debianhitler3 /bin/bash


docker stop debianhitler
docker stop debianhitler2
docker stop debianhitler3

##DOCKER NETNS LOCATION
root@localhost:/# cd /var/run/docker/netns
root@localhost:/var/run/docker/netns# ls
4f433a7a1adf  b4f2c33430f6

##issue docker networking namespace not visible in ip netns list

root@localhost:/var/run/docker/netns# docker inspect --format '{{.State.Pid}}' debianhitler
2143

root@localhost:/var/run/docker/netns# docker inspect --format '{{.State.Pid}}' debianhitler2
2263


root@localhost:/# nsenter -t 2143 -n ip addr show
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host 
       valid_lft forever preferred_lft forever
8: eth0@if9: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default 
    link/ether 02:42:ac:11:00:02 brd ff:ff:ff:ff:ff:ff link-netnsid 0
    inet 172.17.0.2/16 scope global eth0
       valid_lft forever preferred_lft forever
    inet6 fe80::42:acff:fe11:2/64 scope link 
       valid_lft forever preferred_lft forever

//////
//////

root@localhost:/# nsenter -t 2263 -n ip addr show
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host 
       valid_lft forever preferred_lft forever
10: eth0@if11: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default 
    link/ether 02:42:ac:11:00:03 brd ff:ff:ff:ff:ff:ff link-netnsid 0
    inet 172.17.0.3/16 scope global eth0
       valid_lft forever preferred_lft forever
    inet6 fe80::42:acff:fe11:3/64 scope link 
       valid_lft forever preferred_lft forever
root@localhost:/# 



###VPC network test
ip netns add VXLAN-NETNS1
ip netns add VXLAN-NETNS2
ip netns add VXLAN-NETNS3


ip netns exec VXLAN-NETNS1 bash

docker run --name VXLAN-DEBIAN1 -it debian /bin/bash
exit
docker run --name VXLAN-DEBIAN2 -it debian /bin/bash
exit
docker run --name VXLAN-DEBIAN3 -it debian /bin/bash
exit

docker start VXLAN-DEBIAN1
docker start VXLAN-DEBIAN2
docker start VXLAN-DEBIAN3

docker run --name box -it busybox
$ docker run --name box -it busybox
$ pid="$(docker inspect -f '{{.State.Pid}}' "box")"
$ echo $pid