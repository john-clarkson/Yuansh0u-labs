# kubernetes v1.19 with docker-engine HA Multi-master setup (kubeadm)
1. Kubenetes version: v1.19
2. Load balancer: haproxy
3. OS: Ubuntu 20.04 LTS

- Official website ref
- https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/high-availability/
## Topology looks like
![](https://i.imgur.com/5ba1nU3.png)

## VM Environment

* LoadBalancer=172.16.16.100=klb.local.com
* Master=172.16.16.101=kmaster1.local.com
* Master=172.16.16.102=kmaster2.local.com
* Worker=172.16.16.123=kworker1.local.com
## Best prac
- Create load balancer for kube-apiserver
Note: There are many configurations for load balancers. The following example is only one option. Your cluster requirements may need a different configuration.
Create a kube-apiserver load balancer with a name that resolves to DNS.
- In a cloud environment you should place your control plane nodes behind a TCP forwarding load balancer. This load balancer distributes traffic to all healthy control plane nodes in its target list. The health check for an apiserver is a TCP check on the port the kube-apiserver listens on (default value :6443).
- It is not recommended to use an IP address directly in a cloud environment.
- The load balancer must be able to communicate with all control plane nodes on the apiserver port. It must also allow incoming traffic on its listening port.
- Make sure the address of the load balancer always matches the address of kubeadm's ControlPlaneEndpoint.
## Before you start
### Root password setting&enable ssh for root user
```sh 
#!/bin/bash

# Enable ssh password authentication
echo "Enable ssh password authentication"
sed -i 's/^PasswordAuthentication .*/PasswordAuthentication yes/' /etc/ssh/sshd_config
echo 'PermitRootLogin yes' >> /etc/ssh/sshd_config
systemctl reload sshd

# Set Root password with kubeadmin
echo "Set root password"
echo -e "kubeadmin\nkubeadmin" | passwd root >/dev/null 2>&1
```
## Install Haproxy&setup
```sh 
$apt update && apt install -y haproxy
##Configure haproxy
##Append the below lines to /etc/haproxy/haproxy.cfg

frontend kubernetes-frontend
    bind 172.16.16.100:6443
    mode tcp
    option tcplog
    default_backend kubernetes-backend

backend kubernetes-backend
    mode tcp
    option tcp-check
    balance roundrobin
    server kmaster1 172.16.16.101:6443 check fall 3 rise 2
    server kmaster2 172.16.16.102:6443 check fall 3 rise 2
##Restart haproxy service
$systemctl restart haproxy
```
## kubernetes installation
```sh 
##On all kubernetes nodes (kmaster1, kmaster2, kworker1)
##Disable Firewall
$ufw disable
#Disable swap
$swapoff -a; sed -i '/swap/d' /etc/fstab
#Update sysctl settings for Kubernetes networking
$cat >>/etc/sysctl.d/kubernetes.conf<<EOF
net.bridge.bridge-nf-call-ip6tables = 1
net.bridge.bridge-nf-call-iptables = 1
EOF
sysctl --system
##Install docker engine
{
  apt install -y apt-transport-https ca-certificates curl gnupg-agent software-properties-common
  curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add -
  add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
  apt update && apt install -y docker-ce=5:19.03.10~3-0~ubuntu-focal containerd.io
}
## Kubernetes Setup
## Add Apt repository
{
  curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add -
  echo "deb https://apt.kubernetes.io/ kubernetes-xenial main" > /etc/apt/sources.list.d/kubernetes.list
}
##Install Kubernetes components
apt update && apt install -y kubeadm=1.19.2-00 kubelet=1.19.2-00 kubectl=1.19.2-00
##On any one of the Kubernetes master node (Eg: kmaster1)
```
## Sample outputs
```sh 
##The output looks similar to:

#You can now join any number of control-plane node by running the following command on each as a root:
kubeadm join <lb-ip>:6443 --token 9vr73a.a8uxyaju799qwdjv --discovery-token-ca-cert-hash sha256:7c2e69131a36ae2a042a339b33381c6d0d43887e2de83720eff5359e26aec866 --control-plane --certificate-key f8902e114ef118304e561c3ecd4d0b543adc226b7a07f675f56564185ffe0c07
      
#Please note that the certificate-key gives access to cluster sensitive data, keep it secret!
#As a safeguard, uploaded-certs will be deleted in two hours; If necessary, you can use kubeadm init phase upload-certs to reload certs afterward.      
#Then you can join any number of worker nodes by running the following on each as root:
kubeadm join <lb-ip>:6443 --token 9vr73a.a8uxyaju799qwdjv --discovery-token-ca-cert-hash sha256:7c2e69131a36ae2a042a339b33381c6d0d43887e2de83720eff5359e26aec866
Copy this output to a text file. You will need it later to join control plane and worker nodes to the cluster.
#When --upload-certs is used with kubeadm init, the certificates of the primary control plane are encrypted and uploaded in the kubeadm-certs Secret.
#To re-upload the certificates and generate a new decryption key, use the following command on a control plane node that is already joined to the cluster:
```

## Initialize Kubernetes Cluster
```sh 
##Copy the commands to join other master nodes and worker nodes.
$kubeadm init --control-plane-endpoint="172.16.16.100:6443" --upload-certs --apiserver-advertise-address=172.16.16.101 --pod-network-cidr=192.168.0.0/16

##Deploy Calico network
$kubectl --kubeconfig=/etc/kubernetes/admin.conf create -f https://docs.projectcalico.org/v3.15/manifests/calico.yaml

##Join other nodes to the cluster (kmaster2 & kworker1)
##Use the respective kubeadm join commands you copied from the output of kubeadm init command on the first master.
##You also need to pass --apiserver-advertise-address to the join command when you join the other master node.
Downloading kube config to your local machine
On your host machine
```
### Copy kubeconfig to your control-machine
```sh 
#bin/bash
mkdir ~/.kube
scp root@172.16.16.101:/etc/kubernetes/admin.conf ~/.kube/config
kubectl get nodes -o wide;
```
### Verifying the cluster
```sh
$kubectl cluster-info
$kubectl get nodes
$kubectl get cs
```

Done!