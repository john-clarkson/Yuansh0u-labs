# Kubernetes installation on ubuntu 20.04 server/desktop version
- Note: Ensure you can access google.com
```sh 
$dig google.com

; <<>> DiG 9.10.6 <<>> google.com
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 33661
;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 512
;; QUESTION SECTION:
;google.com.			IN	A

;; ANSWER SECTION:
google.com.		269	IN	A	172.217.24.206

;; Query time: 56 msec
;; SERVER: 8.8.8.8#53(8.8.8.8)
;; WHEN: Wed Sep 23 13:52:46 CST 2020
;; MSG SIZE  rcvd: 55

```

### Kernel version
```sh 
$uname -rs
Linux 5.4.0-40-generic
```
### Login as root
```sh
$sudo -i
``` 
### Copy this shell script then run it.
```sh 
#!bin/bash
echo "turn off swap"
swapoff -a;
sed -i '/ swap / s/^/#/' /etc/fstab;
sleep 3

echo "apt update+install curl"
apt-get update && apt-get install -y apt-transport-https curl;
apt install -y gnupg2;

echo "kubernetes key"
curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add -;

echo "add apt kubernetes repo"
cat <<EOF >/etc/apt/sources.list.d/kubernetes.list
deb http://apt.kubernetes.io/ kubernetes-xenial main
EOF

# echo deb https://apt.kubernetes.io/ kubernetes-xenial main > /etc/apt/sources.list.d/kubernetes.list

echo "apt update+install docker.io"
apt-get update;
apt-get install -y docker.io;

echo "cgroup setting"
cat > /etc/docker/daemon.json <<EOF
{
  "exec-opts": ["native.cgroupdriver=systemd"],
  "log-driver": "json-file",
  "log-opts": {
    "max-size": "100m"
  },
  "storage-driver": "overlay2"
}
EOF

echo "enable docker daemon"
mkdir -p /etc/systemd/system/docker.service.d;
systemctl start docker;
systemctl enable docker;

echo "kubernetes downloading"
apt-get install -y kubelet kubeadm kubectl;
```
## Check mate
### Check version
```sh 
root@MASTER:~# apt search kubelet
Sorting... Done
Full Text Search... Done
kubelet/kubernetes-xenial,now 1.18.5-00 amd64 [installed]
  Kubernetes Node Agent

root@MASTER:~# apt search kubeadm
Sorting... Done
Full Text Search... Done
kubeadm/kubernetes-xenial,now 1.18.5-00 amd64 [installed]
  Kubernetes Cluster Bootstrapping Tool

root@MASTER:~# apt search kubectl
Sorting... Done
Full Text Search... Done
kubectl/kubernetes-xenial,now 1.18.5-00 amd64 [installed]
  Kubernetes Command Line Tool

kubetail/focal 1.6.5-2 all
  Aggregate logs from multiple Kubernetes pods into one stream

root@MASTER:~#
```
### kubeadm init
```sh 


#!/bin/bash
echo Setup kubeadm/kubectl/crictl/helm completion.
source <(kubeadm completion bash);
source <(kubectl completion bash);
source <(crictl completion bash);
source <(helm completion bash);
sleep 2
echo Refresh .bashrc
source  ~/.bashrc
sleep 2

echo Turnoff swap
swapoff -a

echo kubeadm init
kubeadm init --apiserver-advertise-address 100.64.1.99 --pod-network-cidr 10.244.0.0/16 --service-cidr 10.96.0.0/12;
sleep 2

echo Build kubeconfig
mkdir -p $HOME/.kube;
sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config;
sudo chown $(id -u):$(id -g) $HOME/.kube/config;
sleep 2
echo "
kubectl get nodes -o json | jq .items[].spec.taints
[
  {
    "effect": "NoSchedule",
    "key": "node-role.kubernetes.io/master"
  }
]
"

echo scheduled master node
kubectl taint nodes --all node-role.kubernetes.io/master-;
sleep 2

echo kubectl get nodes
kubectl get node;

echo watch kubectl get pods -n kube-system
echo Next step, Choose a CNI plugin. Have a nice day!
echo Deploy busybox with 3 replicas with pending state.
kubectl apply -f  /root/k8s/kuber-deployment/busybox-deployment.yaml;
```