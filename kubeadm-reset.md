# kubeadm reset
```sh 

#!/bin/bash
echo Reset cluster.
yes | kubeadm reset;
sleep 2

echo Delete Flannel+CNI0 interface
ip link del cni0;
ip link del flannel.1;
echo FLUSH iptables

iptables -F && iptables -t nat -F && iptables -t mangle -F && iptables -X

echo Delete CNI config.
rm -rfv /etc/cni/net.d/*;
sleep 2

echo Delete kubeconfig.
rm -rfv ~/.kube;

echo Check iptables rule is gone.
iptable -L -t nat;

done;

```
