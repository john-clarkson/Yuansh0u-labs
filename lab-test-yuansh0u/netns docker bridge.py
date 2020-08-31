


OS  

    docker ubuntu --192.168.254.0/24  br 254.254  ->>-eth1 ---192.168.33.0/24 -  254  CSR 1  loop 100.64.1.1/32 ----CSR 2--Loo 100.64.1.2/32


docker network create BASE-NETWORK-002 --subnet 192.168.254.0/24 --gateway 192.168.254.254

docker run --name BASE-NETWORK-UBUNTU002 -it --net BASE-NETWORK-002 --ip 192.168.254.1 -d debian /bin/bash

docker exec -ti BASE-NETWORK-UBUNTU002 /bin/bash

brctl addif <br-id>

##static route

##interface ip assignment to br-interface
ip addr add 192.168.33.4/24 dev br-e0007c242561
## add static route
route add -net 100.64.0.0 netmask 255.255.0.0 gw 192.168.33.254 dev <br-iface>

##done-config
6: br-e0007c242561: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default 
    link/ether 02:42:86:70:94:a8 brd ff:ff:ff:ff:ff:ff
    inet 192.168.254.254/24 scope global br-e0007c242561
       valid_lft forever preferred_lft forever
    inet 192.168.33.4/24 scope global br-e0007c242561
       valid_lft forever preferred_lft forever
    inet6 fe80::42:86ff:fe70:94a8/64 scope link 
       valid_lft forever preferred_lft forever


       ###VPC
       docker run --name VPC-UBUNTU-2 -it --net VPC-NETWORK-2  -d debian /bin/bash

##show contianer proc id
pid="$(docker inspect -f '{{.State.Pid}}' "VPC-UBUNTU-1")"
##soft link
ln -s /proc/$pid/ns/net /var/run/netns/VPC-UBUNTU-1

ln -s /proc/$pid/ns/net /var/run/netns/box
##
root@localhost:/var/run/netns# echo $pid
2881
root@localhost:/var/run/netns# ls
root@localhost:/var/run/netns# ln -s /proc/$pid/ns/net /var/run/netns/VPC-UBUNTU-1
root@localhost:/var/run/netns# ip netns
VPC-UBUNTU-1 (id: 1)

###

docker inspect --format '{{.State.Pid}}' VPC-UBUNTU-2
root@localhost:/var/run/netns# docker inspect --format '{{.State.Pid}}' VPC-UBUNTU-2
3008
root@localhost:/var/run/netns# docker inspect  VPC-UBUNTU-2 
[
    {
        "Id": "eadaebda48a336077cb69cff336f42442da8c9bfb3f03862f29361e64255917d",
        "Created": "2018-09-09T05:00:36.065469451Z",
        "Path": "/bin/bash",
        "Args": [],
        "State": {
            "Status": "running",
            "Running": true,
            "Paused": false,
            "Restarting": false,
            "OOMKilled": false,
            "Dead": false,
            "Pid": 3008,



            ##turn off iptables
             root@localhost:/# /proc/sys/net/bridge/
-bash: /proc/sys/net/bridge/: Is a directory
root@localhost:/# cd /proc/sys/net/bridge/
root@localhost:/proc/sys/net/bridge# ls
bridge-nf-call-arptables  bridge-nf-call-iptables        bridge-nf-filter-vlan-tagged
bridge-nf-call-ip6tables  bridge-nf-filter-pppoe-tagged  bridge-nf-pass-vlan-input-dev
root@localhost:/proc/sys/net/bridge# cat bridge-nf-call-iptables 
1
echo 0 > /proc/sys/net/bridge/bridge-nf-call-iptables

root@localhost:~# sudo ufw disable
Firewall stopped and disabled on system startup


root@localhost:~# iptables -t nat -L
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
MASQUERADE  all  --  172.18.0.0/16        anywhere            
MASQUERADE  all  --  172.17.0.0/16        anywhere            
MASQUERADE  all  --  192.168.254.0/24     anywhere            
MASQUERADE  all  --  100.64.88.0/24       anywhere            

Chain DOCKER (2 references)
target     prot opt source               destination         
RETURN     all  --  anywhere             anywhere            
RETURN     all  --  anywhere             anywhere            
RETURN     all  --  anywhere             anywhere            
RETURN     all  --  anywhere             anywhere            
root@localhost:~# 
root@localhost:~# 
root@localhost:~# service iptables stop
Failed to stop iptables.service: Unit iptables.service not loaded.
root@localhost:~# sudo ufw status
Status: inactive
root@localhost:~# sudo ufw status
Status: inactive
root@localhost:~# 
root@localhost:~# sudo ufw status
Status: inactive
