calico
calicoctl install

 kubectl apply -f \
 https://docs.projectcalico.org/v3.5/getting-started/kubernetes/installation/hosted/calicoctl.yaml

 kubectl apply -f \
 https://docs.projectcalico.org/v3.5/getting-started/kubernetes/installation/hosted/kubernetes-datastore/calicoctl.yaml

##enable-ipv6
root@node1:/# cat ./proc/sys/net/ipv6/conf/all/forwarding
0
root@node1:/# nano ./proc/sys/net/ipv6/conf/all/forwarding
  GNU nano 2.9.3                         ./proc/sys/net/ipv6/conf/all/forwarding                                   

1

root@node1:/# kubectl get pods -n kube-system
NAME                                       READY   STATUS    RESTARTS   AGE
calico-kube-controllers-566f586756-hv244   1/1     Running   0          88m
calico-node-2sg57                          1/1     Running   0          88m
calico-node-bql7n                          1/1     Running   0          88m
calicoctl                                  1/1     Running   0          40m
coredns-6fd7dbf94c-hfl4l                   1/1     Running   0          87m
coredns-6fd7dbf94c-n9tgp                   1/1     Running   0          87m
dns-autoscaler-5b4847c446-kl4fk            1/1     Running   0          87m
kube-apiserver-node1                       1/1     Running   0          89m
kube-controller-manager-node1              1/1     Running   0          89m
kube-proxy-2x2gr                           1/1     Running   0          86m
kube-proxy-ghn5h                           1/1     Running   0          88m
kube-scheduler-node1                       1/1     Running   0          89m
kubernetes-dashboard-57bf7b5bf6-mx6kh      1/1     Running   0          87m
nginx-proxy-node2                          1/1     Running   0          89m


root@node1:/#  calicoctl get bgpconfig default
WARNING: Your kernel does not support swap limit capabilities or the cgroup is not mounted. Memory limited without swap.
NAME      LOGSEVERITY   MESHENABLED   ASNUMBER   
default   Info          true          64512      


###
root@node1:/# calicoctl get ippool -o wide
WARNING: Your kernel does not support swap limit capabilities or the cgroup is not mounted. Memory limited without swap.
NAME           CIDR             NAT    IPIPMODE   DISABLED   
default-pool   10.233.64.0/18   true   Always     false      

root@node1:/# 

root@node1:/#  calicoctl get bgpconfig default
WARNING: Your kernel does not support swap limit capabilities or the cgroup is not mounted. Memory limited without swap.
NAME      LOGSEVERITY   MESHENABLED   ASNUMBER   
default   Info          true          64512   


root@node1:/#  calicoctl get bgpconfig default --export -o yaml > bgp.yaml
WARNING: Your kernel does not support swap limit capabilities or the cgroup is not mounted. Memory limited without swap.
root@node1:/# 
root@node1:/# ls
bgp.yaml  dev   initrd.img      lib64       mnt   root  snap      sys  var
bin       etc   initrd.img.old  lost+found  opt   run   srv       tmp  vmlinuz
boot      home  lib             media       proc  sbin  swap.img  usr  vmlinuz.old
root@node1:/# cat bgp.yaml 
apiVersion: projectcalico.org/v3
kind: BGPConfiguration
metadata:
  creationTimestamp: null
  name: default
spec:
  asNumber: 64512
  logSeverityScreen: Info
  nodeToNodeMeshEnabled: true
root@node1:/# 

calicoctl replace -f bgp.yaml

##bgp peers
cat << EOF | calicoctl create -f -
apiVersion: projectcalico.org/v3
kind: BGPPeer
metadata:
  name: external-bgp
spec:
  peerIP: 10.21.0.36
  asNumber: 64512
EOF
calicoctl delete bgppeer external-bgp

XE-R1-DC2-R1(config)#router bgp 64512
XE-R1-DC2-R1(config-router)#nei
XE-R1-DC2-R1(config-router)#neighbor 10.21.0.63 remote
XE-R1-DC2-R1(config-router)#neighbor 10.21.0.63 remote-as 64512
XE-R1-DC2-R1(config-router)#neighbor 10.21.0.64 remote-as 64512
XE-R1-DC2-R1(config-router)#end
XE-R1-DC2-R1#show bgp ipv
XE-R1-DC2-R1#show bgp ipv4 
XE-R1-DC2-R1#show bgp ipv4 un
XE-R1-DC2-R1#show bgp ipv4 unicast su
XE-R1-DC2-R1#show bgp ipv4 unicast summary 
BGP router identifier 100.64.1.1, local AS number 64512
BGP table version is 1, main routing table version 1
2 network entries using 496 bytes of memory
2 path entries using 272 bytes of memory
2/0 BGP path/bestpath attribute entries using 560 bytes of memory
0 BGP route-map cache entries using 0 bytes of memory
0 BGP filter-list cache entries using 0 bytes of memory
BGP using 1328 total bytes of memory
BGP activity 2/0 prefixes, 2/0 paths, scan interval 60 secs

Neighbor        V           AS MsgRcvd MsgSent   TblVer  InQ OutQ Up/Down  State/PfxRcd
10.21.0.63      4        64512       4       2        1    0    0 00:00:10        1
10.21.0.64      4        64512       4       2        1    0    0 00:00:03        1
XE-R1-DC2-R1#
XE-R1-DC2-R1#show ip bgp 
BGP table version is 1, local router ID is 100.64.1.1
Status codes: s suppressed, d damped, h history, * valid, > best, i - internal, 
              r RIB-failure, S Stale, m multipath, b backup-path, f RT-Filter, 
              x best-external, a additional-path, c RIB-compressed, 
              t secondary path, L long-lived-stale,
Origin codes: i - IGP, e - EGP, ? - incomplete
RPKI validation codes: V valid, I invalid, N Not found

     Network          Next Hop            Metric LocPrf Weight Path
 * i  10.233.75.0/26   10.21.0.64                    100      0 i
 * i  10.233.102.128/26
                      10.21.0.63                    100      0 i
XE-R1-DC2-R1#


sudo calicoctl node status
root@node1:/# sudo calicoctl node status
WARNING: Your kernel does not support swap limit capabilities or the cgroup is not mounted. Memory limited without swap.
Calico process is running.

IPv4 BGP status
+--------------+-------------------+-------+----------+-------------+
| PEER ADDRESS |     PEER TYPE     | STATE |  SINCE   |    INFO     |
+--------------+-------------------+-------+----------+-------------+
| 10.21.0.64   | node-to-node mesh | up    | 09:30:24 | Established |
| 10.21.0.36   | global            | up    | 11:28:01 | Established |
+--------------+-------------------+-------+----------+-------------+

IPv6 BGP status
No IPv6 peers found.

root@node1:/# 



10.233.0.0/18

kubectl patch ds -n kube-system calico-node --patch \
    '{"spec": {"template": {"spec": {"containers": [{"name": "calico-node", "env": [{"name": "CALICO_ADVERTISE_CLUSTER_IPS", "value": "10.233.0.0/18"}]}]}}}}’

kubectl -n kube-system patch daemonset calico-node -p '{"spec":{"template":{"spec":{"containers":[{"name": "calico-node", "env":[{"name":"CALICO_ADVERTISE_CLUSTER_IPS","value":"10.233.0.0/18"}]}]}}}}'

