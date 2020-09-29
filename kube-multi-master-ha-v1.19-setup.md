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
### kube-admin.conf sample output
```sh 
root@kind-control-plane:/# cat /etc/kubernetes/admin.conf
apiVersion: v1
clusters:
- cluster:
    certificate-authority-data: LS0tLS1CRUdJTiBDRVJUSUZJQ0FURS0tLS0tCk1JSUM1ekNDQWMrZ0F3SUJBZ0lCQURBTkJna3Foa2lHOXcwQkFRc0ZBREFWTVJNd0VRWURWUVFERXdwcmRXSmwKY201bGRHVnpNQjRYRFRJd01Ea3lPVEExTkRVeE9Wb1hEVE13TURreU56QTFORFV4T1Zvd0ZURVRNQkVHQTFVRQpBeE1LYTNWaVpYSnVaWFJsY3pDQ0FTSXdEUVlKS29aSWh2Y05BUUVCQlFBRGdnRVBBRENDQVFvQ2dnRUJBT3B4CmkyTjRDdmpHUzQvM1NRR2Q3NmtQVCtmRUdpNVNEUE9PZmlJQldkVzM1U0lBMFFNZkYrdTd4U2JuKzFVa3NZNkkKWllBak5hK21wczl3K3J1dmxZRnRtcEI1MjVsN2pJQll6dlNObExMVTZiRHZGZjlvdkpVS3Nhc1NRU2RuZHlRUwpHc3FoT0FleE1DMHJjZDQ2Z21nY1pOem1OcnB2V0t5RzYrNTMwc2dpb0hza29NQUYvWUgweHpWR2N1a2hGdHQyCjg0RXEvdnQ5d0hRSVRTYVdVNmtzZFRYZjl4VW0xK0ZydzBFUndkWTFGalBLRmgwVkhDV1hOd0c2SS8zdUVFZXgKMmhSS1hPTnpHTm53K1F0MmZCc1dGZDVUd0JBdnhVVEJvNVpEbmdlMC9MR2VVVVlJeG53VEZYeXd6VjVEdmNLdwo2Y3htc2lRb0YvYzhET1RnRm5rQ0F3RUFBYU5DTUVBd0RnWURWUjBQQVFIL0JBUURBZ0trTUE4R0ExVWRFd0VCCi93UUZNQU1CQWY4d0hRWURWUjBPQkJZRUZPQzk0TzAva09EVXU0S3E1bjQ4TzFwYVFub2pNQTBHQ1NxR1NJYjMKRFFFQkN3VUFBNElCQVFCUUlBbEhpRWtVbC9IcVVTcW9NeTFqOEJUWGF3aEs4ZXh2NGpRWE5GRDAyaVkxakNsdQpOdVAvcFR4TGdqbjNiOXk5blhXTHVGSlR6QUJaeWkzc0xWWHZxTGZ1MzdDMEJYb24xaEpyemlPaDJyTDVYaFhNClBnUWp6SnhlemMrR3lhT1ZESWVhNy9xY041cWFrU21yaWgyQXFXWXVYODdkandHNStkWStjYXBzYlVqMythOUQKaUovUU1Jb0J2MzhaRk11ajZUR2hONlQ3MVpBYjllQllzN1Z6U1pza0djT0hkVTkxZ0JGSXYvL2xjb01QYTN1UApIT0o3Q0o5cnhrNk1VcXZjaXVsdlEyMloyTHhEZTNOeWZ4Y2t0dU02bW9OUFpobWlmeDBwVUpUeWtRN0YzNTFLCkV5TUFma2FWWXlMYVF5Wmw5ZmpuVW5KbzRJbTlrL2FEQUJuRQotLS0tLUVORCBDRVJUSUZJQ0FURS0tLS0tCg==
    server: https://kind-external-load-balancer:6443
  name: kind
contexts:
- context:
    cluster: kind
    user: kubernetes-admin
  name: kubernetes-admin@kind
current-context: kubernetes-admin@kind
kind: Config
preferences: {}
users:
- name: kubernetes-admin
  user:
    client-certificate-data: LS0tLS1CRUdJTiBDRVJUSUZJQ0FURS0tLS0tCk1JSURFekNDQWZ1Z0F3SUJBZ0lJTGYxQkVvOGhVa3N3RFFZSktvWklodmNOQVFFTEJRQXdGVEVUTUJFR0ExVUUKQXhNS2EzVmlaWEp1WlhSbGN6QWVGdzB5TURBNU1qa3dOVFExTVRsYUZ3MHlNVEE1TWprd05UUTFNak5hTURReApGekFWQmdOVkJBb1REbk41YzNSbGJUcHRZWE4wWlhKek1Sa3dGd1lEVlFRREV4QnJkV0psY201bGRHVnpMV0ZrCmJXbHVNSUlCSWpBTkJna3Foa2lHOXcwQkFRRUZBQU9DQVE4QU1JSUJDZ0tDQVFFQTNpc0JSUFk4Z0ZYNmpLOUMKbUd2bVlmV25TMXpvK0Z4Qlg5aGJWTE1TRDhpdGZvODM5MzN4dStsa2FLQVFIMHpRYTB5M1lITVlYYVZPUTlJOQpUWWdXSk9DVlM2UzZmdnhuVnZiN21xQmZyNHBCR2pDZ3dobFBtM3JTaGRaQXpySHRmdXY3NnRlWUcvelpRcVNnCkpZTHdGV2VmNTUrWTVMT3RCaEdTTGc1TytxaG1ucjRsYjQzb3hBWVAzNjlseG9Ra0lXVzZtYVBaemFrY2RQeC8KMTVWSTQ4bXhZUE1XeE9icitpaEQzUVgzVmNvN1Q1dFZKa0FsbjEzeWhFSkREaXR3eExZVlRieXdRVkdoY1Q0TgpKTEI5THJkejdPbEkzMWhkcENvU3loSWVNL0Z6aTg0WnNiaHRYRFRhK0tsQWtoMUpaRXE0YXhZd0ozMkU4Y0VCCms2NFJYUUlEQVFBQm8wZ3dSakFPQmdOVkhROEJBZjhFQkFNQ0JhQXdFd1lEVlIwbEJBd3dDZ1lJS3dZQkJRVUgKQXdJd0h3WURWUjBqQkJnd0ZvQVU0TDNnN1QrUTROUzdncXJtZmp3N1dscENlaU13RFFZSktvWklodmNOQVFFTApCUUFEZ2dFQkFMZXA3YzBwZWwrNkFuWGovdERGSW1YWm15SmJTamlFWks2d3NiYkloWlFrTHFLSDBYZnJzMW84CjJoM3B0SkFiTmZxZS8wMWpNMFBsT2hjcnFLVUMxYWx1eGZkcmlyUGdXT1ZUU1h5b0xZL1p3dVcvZXpxVndaT0oKS2U2ajA5Q1VrNmRFeExuMDFDY2o0Nm1ZcWJNay84dEtENDduVGtqRldpVUU1NUJ2dmNPWnlpVHB5bzZEZTdnZApxd2RXeWl1L1h0cEdQUVJyRGtmNzFIYmRTNEc1aC91ZjMrdkhlUFdRMkozM1lRVURwU3BQS2VJdVNPMEJpNUdXCm9LQ1pHdURrUUtLbE14enk2amlWKzdEODJoYzVKWHJaRXZEWlN5ZU51Tll3SnNGY3lKZnQ2UTVNQVFkZklpbjQKQm5SWDkvS0QzTUxuY1JVY3lkb24xT1hsMjhWb0U1Zz0KLS0tLS1FTkQgQ0VSVElGSUNBVEUtLS0tLQo=
    client-key-data: LS0tLS1CRUdJTiBSU0EgUFJJVkFURSBLRVktLS0tLQpNSUlFb3dJQkFBS0NBUUVBM2lzQlJQWThnRlg2aks5Q21Hdm1ZZlduUzF6bytGeEJYOWhiVkxNU0Q4aXRmbzgzCjkzM3h1K2xrYUtBUUgwelFhMHkzWUhNWVhhVk9ROUk5VFlnV0pPQ1ZTNlM2ZnZ4blZ2YjdtcUJmcjRwQkdqQ2cKd2hsUG0zclNoZFpBenJIdGZ1djc2dGVZRy96WlFxU2dKWUx3RldlZjU1K1k1TE90QmhHU0xnNU8rcWhtbnI0bApiNDNveEFZUDM2OWx4b1FrSVdXNm1hUFp6YWtjZFB4LzE1Vkk0OG14WVBNV3hPYnIraWhEM1FYM1ZjbzdUNXRWCkprQWxuMTN5aEVKRERpdHd4TFlWVGJ5d1FWR2hjVDROSkxCOUxyZHo3T2xJMzFoZHBDb1N5aEllTS9Gemk4NFoKc2JodFhEVGErS2xBa2gxSlpFcTRheFl3SjMyRThjRUJrNjRSWFFJREFRQUJBb0lCQUNoWURPSDJDU1NRK0crbAp2K1VuNnUwdEM5VXVxUXU0elJKWG1yWTEwbmpWUzFRcE05T1lwbFltV3RwNC9wU0FnWFNLdU40bDZHM1EvL1ptCjdrVHZDbjVsM2hhZmNsSnZDV0VNZHNJc2oxTzBPb0JFQmwxWTlWRFpxL01yNWhiaXpxcjJ0WWQrNFJ0ci9oUVIKQ3hma3dDNVM1QUhPeEpmN1hOYzJSNkpmYk00dGdiTlI1WEJxZlNHYU5KSU5KWDJLeXY1TlJrRlNpZkR6SG55ZQpQNFNiaXBqNHRxMjRmamE4SFhWTnJiNDc4d1VRcFdMZDN5cUhiVGs0RmFEdUpvQ09oekhYMDRST2F6NWtxQ1ZHCk9jN212ZU9yaGdSVmpPMUxGWTh0V3pXNHdhMVZ6RlF2emZjSlhXdWdUYWNvbVlNQVA2RENBZ1o4ZGZuWGhLYUYKYzc4bWdvMENnWUVBMytDa0xxVzNxaGJuL3IvYkttRnY5RkJNTXNBZit0OFVIVlViVzE5T0hJSFpMQ250cDU1UApLdDlseDdqb1RXcnphMk40TEJMcXc2NC9TYzhQMUJWenZtOXNHUTVDNzgwZFlIdEJDeHRWSWdIdSs4RXk4bXE4ClRGdEVjbjd0NzV0SHdwemdvSHBUVUZyZTcySjIzcHgxSTVERjgzZ2Q5Zno3d3RSZUdLQW5ReE1DZ1lFQS9ndVMKQ3Q5dmJ0WkNweTJhSHFRLy9pVjFsYnVaR0tnTC9DUGkzRUxkalFxRFVVek8xMWdhZzZrakFMeEtOUWNCQWJWNQpEV2R0a09oV05BTHJsdERiZnZVWG51NW5ISkV6NjJSMXRBa2hRbzdIQTI5SmQwakt1a1NZdlB5OE5qV05hV09EClpvYmtTL3dvVDdXajRYWnlkdnlCS1FHM01LeGJYMVlicnBSYmQ4OENnWUE5dWx6S2w5cTZSVEtXWlNQeTNZYlcKNEVVQ1FVTVFFdTRpNEZKNHNTQ0NiN01Ib0Uvc3haT2lpSkl4cldRdjVHdFZrc21SclcyWm9yUEVrQmtYS3dzTQoyUC8vTUpWNE5TQUNlRG1JN0hKZXZCVyt5SmhaaXVCOFZUWGNNKzg2LzUrYm8xRzBMY1pIQTZjd2JmL0VoWE11CjZUNExVWFZCWEEyMnZJTnRXc3M0alFLQmdRQzdjZ1ljQjZqTSswTEszNWJzTFAwYXBNRVI3ZzJVWjhvUUROcUMKOHNOT0lnZXFvU1d0TnRDNWZMN2ErQk00OVNZRkFNV0U0bCt4bi95YSs5eWd0eEo5cHBIN0xxVGVLelZINWlRQwo1d21uZG5uWlN1L0dGK3VkYktmV0toVWxXbll3NE1BL2tpQTVBS0V0enpSUVUzazUyaTNpOStVWEFOV2Fqb3AyClVmajdlUUtCZ0dvT1p1YzdVR3d0QXgvOW52QVVaVzJwTnYzZjd2Z2NnUXhDN0ZvYzRRTFVaeWlDTStUWndHMlIKdndyTHVNYk1nWGVNZEhzRlhxQ0JqRkdrblBMMUxZamYwK2V6U0g1UUNuR05peUUvRmt2K2ovZk43L0kza3RUZQo0aGVCcUdXOWxnLy8rcXJjZUwwcTUxOGdYZzNSV2FFK0J4Wi9VandmUXNSL2htdTRPMHJkCi0tLS0tRU5EIFJTQSBQUklWQVRFIEtFWS0tLS0tCg==
root@kind-control-plane:/#
root@kind-control-plane:/# cat /etc/hosts
127.0.0.1	localhost
::1	localhost ip6-localhost ip6-loopback
fe00::0	ip6-localnet
ff00::0	ip6-mcastprefix
ff02::1	ip6-allnodes
ff02::2	ip6-allrouters
172.18.0.5	kind-control-plane
root@kind-control-plane:/#
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