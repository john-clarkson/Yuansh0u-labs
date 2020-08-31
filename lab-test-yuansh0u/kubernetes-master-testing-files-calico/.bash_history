vi /etc/default/grub
grub-mkconfig -o /boot/grub/grub.cfg 
ip a
reboot
exit
sudo swapoff -a
exit
apt install vpnc
vpnc-connect 
exit
kubectl get pods
kubectl get nodes
kubectl get nodes -o wide
kubectl get pods -n=kube-system
ip a
exit
kubectl get pods
kubectl get node
exit
kubectl get nodes
ls
cd
ls -al
exit
cat .bashrc
nano .bashrc
ifconfig
nano .bashrc
source .bashrc
ls
source ~/.bashrc
reboot
ip a
cat .bashrc
ping www.google.com
vpnc-connect 
cd /etc/vpnc
ls
cat default.conf 
cp default.conf default.conf.origin
nano default.conf
vpnc-connect 
vpnc-disconnect 
cd 
nano .bashrc
reboot
nano .bashrc
cd /etc/
ls
cd /etc/lightdm
exit
nano .bashrc
reboot
ping www.google.com
kubectl get pods
kubectl get nodes
ping 150.1.88.2
ping 150.1.88.3
ping 150.1.88.4
kubectl config view
nmap localhost
kubectl get pod -n kube-system
ip a
kubeadm init --apiserver-advertise-address=150.1.88.1 --pod-network-cidr=192.168.0.0/16
cat /proc/sys/net/bridge/bridge-nf-call-iptables
nano /proc/sys/net/bridge/bridge-nf-call-iptables
kubeadm init --apiserver-advertise-address=150.1.88.1 --pod-network-cidr=192.168.0.0/16
kubectl config view
ls -ll
cd
ll -al
cd .kube/
ls
cat config 
cd
kubectl proxy 
sudo -b kubectl proxy --address=0.0.0.0 --accept-hosts='.*'
nmap localhost
lsof :8001
lsof -i :8001
kill -9 9243
sudo -b kubectl proxy --address=0.0.0.0 --accept-hosts='.*'
nmap localhost
kubectl get secrets default-token-clp4d 
kubectl describe secrets default-token-clp4d 
kubectl -n kube-system describe rolebinding kubernetes-dashboard-minimal
kubectl -n kube-system describe role kubernetes-dashboard-minimal
kubectl get secret $(kubectl get serviceaccount dashboard -o jsonpath="{.secrets[0].name}") -o jsonpath="{.data.token}" | base64 --decode
lsof -i :8001
kill -9 9643
sudo -b kubectl proxy --address=0.0.0.0 --accept-hosts='.*'
lsof -i :8001
kill -9 11866
kubectl proxy --address=0.0.0.0 --accept-hosts='.*'
lsof -i :8001
ls
kubectl describe deployments.extensions calico
kubectl get pods -n kube-systems
kubectl get pods -n kube-system
kubectl cluster-info 
nmap localhost
kubectl describe configmaps 
kubectl get serviceaccounts -n kube-system
kubectl describe secret kubernetes-dashboard-certs -n kube-system
kubectl describe role kubernetes-dashboard-minimal -n kube-system
kubectl get clusterrolebindings -n kube-system
clear
kubectl get pods
kubectl get nodes
kubectl config view
ping www.google.com
ip route show
vpnc-connect 
vpnc-disconnect 
vpnc-connect 
ping www.google.co
uname 
cat /etc/os-relea
apt install -y ubuntu-desktop 
reboot
ip a
ping 150.1.88.2
kubectl get nodes
ping 150.1.88.2
ping www.google.com
nmap localhost
shutdown -P 0
kubectl get nods
kubectl get nodes
kubect get pods
kubectl getpods
kubectl get pods
kubectl get pods -o wide
kubectl scale deployment --replicas=2 kuard-elb 
kubectl scale deployment --replicas=10 kuard-elb 
kubectl get pods -o wide
clear
kubectl expose deployment kuard-elb --type=LoadBalancer --port=8555 --target-port=8080
kubectl get svc
clear
kubectl getpods
kubectl get pods
kubectl get pods -o wide
kubectl scale deployment --replicas=5 kuard-elb 
kubectl get pods -o wide
kubectl exec kuard-elb-555c546964-l295z -ti ash
ping 10.233.71.4
kubectl exec kuard-elb-555c546964-l295z -ti ash
vpnc-connect 
wireshark 
vpnc-disconnect 
vpnc-connect 
kubectl completion bash
clear
kubectl create deployment debian --image=debian
clear
kubectl get pods
watch kubectl get pods
watch kubectl get pods -o wide
kubectl delete deployment debian --image=debian
kubectl delete deployment debian
kubectl get pods
vpnc-disconnect 
vpnc-connect 
ping www.google.com
kubectl create deployment debian --image=debian
kubectl get pods
kubectl get pods -o wide
iptables
man iptables
iptables -t NAT
iptables -t nat -L
kubectl get pods
kubectl delete deployment debian 
kubectl delete deployment debian kubectl delete deployment debian kubectl create deployment debian --image=debian:lasted
clear
ping www.baidu.com
ip route show
ping www.google.com
vpnc-disconnect 
ping www.baidu.com
clear
kubectl get pods
kubectl create ns policy-demo
kubectl get namespaces 
kubectl run --namespace=policy-demo nginx --replicas=2 --image=nginx
kubectl get pods -n=policy-demo 
kubectl get pods -n=policy-demo -o wide
vpnc-connect 
kubectl delete --namespace=policy-demo nginx --replicas=2 --image=nginx
kubectl delete --namespace=policy-demo nginx 
kubectl delete --namespace=policy-demo pods nginx 
clear
kubectl get pods
kubectl get pods -n policy-demo 
kubectl delete pods -n=policy-demo nginx-7cdbd8cdc9-9jf9h 
kubectl delete pods -n=policy-demo nginx-7cdbd8cdc9-kmzhj 
kubectl create deployment --namespace=policy-demo nginx --replicas=2 --image=nginx
kubectl create deployment --namespace=policy-demo nginx --image=nginx
kubectl create deployment --namespace=policy-demo calico nginx --image=nginx
kubectl get pods -n=policy-demo 
kubectl delte deployment --namespace=policy-demo nginx
kubectl delete deployment --namespace=policy-demo nginx
kubectl get pods -n=policy-demo 
kubectl create deployment --namespace=policy-demo nginx --image=nginx
clear
kubectl get pods -n=policy-demo 
kubectl get pods -n=policy-demo -o wide
kubectl delete deployment --namespace=policy-demo nginx --image=nginx
kubectl delete deployment --namespace=policy-demo nginx 
kubectl create deployment --namespace=policy-demo nginx --replicas=2 --image=nginx
kubectl get pods -n=policy-demo 
kubectl create deployment --namespace=policy-demo nginx --image=nginx
kubectl scale deployment --replicas=2 --namespace=policy-demo nginx 
kubectl get pods -n=policy-demo 
kubectl expose --namespace=policy-demo deployment nginx --port=80
kubectl get service -n=policy-demo nginx 
kubectl run --namespace=policy-demo access --rm -ti --image busybox /bin/sh
ping www.baidu.com
vpnc-disconnect 
vpnc-connect 
kubectl get pods -n=policy-demo 
kubectl delete pods -n=policy-demo access-69c6dd8f58-pv7t4 
kubectl create deployment --namespace=policy-demo access --rm -ti --image busybox /bin/sh
kubectl create deployment --namespace=policy-demo access -ti --image=busybox /bin/sh
kubectl create deployment --namespace=policy-demo access --image=busybox /bin/sh
kubectl create deployment --namespace=policy-demo access --image=busybox
kubectl delete deployment --namespace=policy-demo access 
kubectl create deployment --namespace=policy-demo access --image=busybox
clear
kubectl get pods -n=policy-demo 
ping www.google.com
vpnc-disconnect 
vpnc-connect 
ping www.google.com
kubectl get pods -n=policy-demo 
kubectl get pods -n=policy-demo -o wide
kubectl describe pods -n=policy-demo 
kubectl describe pods -n=policy-demo access-b69c845dc-vpvbm 
kubectl get pods -n=policy-demo 
kubectl delete deployment --namespace=policy-demo access
kubectl create deployment --namespace=policy-demo kuard-policy --image=gcr.io/kuar-demo/kuard-amd64:1
kubectl get pods -n=policy-demo 
kubectl exec -n=policy-demo kuard-policy-6ddb8c5965-x6qbt -ti ash
kubectl exec -n=policy-demo kuard-policy-6ddb8c5965-x6qbt -ti /bin/bash
kubectl exec -n=policy-demo kuard-policy-6ddb8c5965-x6qbt -ti bin/bash
kubectl exec -n=policy-demo kuard-policy-6ddb8c5965-x6qbt -ti ash
kubectl get pods
kubectl exec kuard-elb-555c546964-bq58h -ti ash
kubectl get pods -n=policy-demo 
kubectl exec -n=policy-demo kuard-policy-6ddb8c5965-x6qbt -ti ash
ls
cat bgp.yaml 
calicoctl get bgpPeer
sudo calicoctl node status
kubectl create -f https://k8s.io/examples/pods/commands.yaml
kubectl get pods
kubectl get pods -o wide
kubectl logs command-demo
kubectl get pods -o wide
ls
calicoctl get ippool -o wide
calicoctl get wep --all-namespaces
touch change-calico-ip-pool.yaml
gedit change-calico-ip-pool.yaml 
calicoctl create -f change-calico-ip-pool.yaml 
ls
cat change-calico-ip-pool.yaml 
calicoctl create -f change-calico-ip-pool.yaml
ls -al
chmod 777 change-calico-ip-pool.yaml 
calicoctl create -f change-calico-ip-pool.yaml
calicoctl create -f /change-calico-ip-pool.yaml
ls
ls -al
calicoctl create -f -<<EOF
apiVersion: projectcalico.org/v3
kind: IPPool
metadata:
  name: new-pool
spec:
  cidr: 10.0.0.0/16
  ipipMode: Always
  natOutgoing: true
EOF

calicoctl create -f -change-calico-ip-pool.yaml
rm change-calico-ip-pool.yaml 
ls
calicoctl get wep --all-namespaces
calicoctl get ippool -o wide
calicoctl get ippool -o yaml > pool.yaml
ls
cat pool.yaml 
gedit pool.yaml 
calicoctl apply -f pool.yaml
kubectl exec -ti -n kube-system calicoctl -- /calicoctl get profiles -o wide
kubectl get podps
kubectl get pods
kubectl get pods -n=kube-system
kubectl get pods
kubectl get pods -n=kube-system 
calicoctl apply -f pool.yaml
calicoctl get wep --all-namespaces
kubectl exec -ti -n kube-system calicoctl -- /calicoctl get profiles -o wide
kubectl get pods -n=kube-system 
kubtctl get pods
kubectl get pods
kubectl get pods -n=kube-sus
kubectl get pods -n=kube-systems
kubectl get pods -n=kube-system 
kubectl exec -ti -n kube-system calicoctl -- /calicoctl get profiles -o wide
vpnc-disconnect 
vpnc-connect 
kubectl get pods -n=kube-system 
kubectl exec -ti -n kube-system calicoctl -- /calicoctl get profiles -o wide
kubectl exec -ti -n kube-system calicoctl
kubectl exec -ti -n=kube-system calicoctl
kubectl exec -ti -n=kube-system calicoctl ash
ls
calicoctl get ippool -o wide
whereis calicoctl
calicoctl get ippool -o wide
calicoctl apply -f pool.yaml
docker ps
docker ps -a
cd /
cd proc/
ls
cd var
cat grub
clear
cd 
cd /etc
cd default/
ls
nano grub
grub-mkconfig -o /boot/grub/grub.cfg
reboot
nmap localhost
kubectl get pods
kubectl get pods -o wide
kubectl scale deployment kuard-elb --replicas=7
kubectl get pods -o wide
watch kubectl get pods -o wide
ls
cd kube-manifests/
ls
cat nodeselector-os-linux-patch.json 
gedit nodeselector-os-linux-patch.json 
ls
cd kubernetes/
ks
ls
l
ls -al
cd
clear
kubectl get pods
kubectl get pods -o wide
kubectl get svc
ifconfig eth1
ping www.google.com
clear
kubectl get nodes
kubectl get pods -n kube-system
ping www.google.com
kubectl plugin list 
cat .bashrc
clear
kubectl get pods -n=policy-demo 
ping www.google.com
kubectl get pods kuard 
kubectl get pods kuard-54b54b8-4lhkt 
kubectl get pods kuard-54b54b8-4lhkt -o yaml
clear
kubectl create -f - <<EOF
kind: NetworkPolicy
apiVersion: networking.k8s.io/v1
metadata:
  name: default-deny
  namespace: policy-demo
spec:
  podSelector:
    matchLabels: {}
EOF

vpnc-connect 
vpnc-disconnect 
vpnc-connect 
kubectl create deployment busybox --image=busybox
kubectl get pods
ping www.google.com
vpnc-disconnect 
vpnc-con
vpnc-connect 
ping www.google.com
kubectl get pods
kubectl get pods -o wide
gedit .bashrc
source .bashrc
source ~/.bashrc
ping www.google.com
vpnc-disconnect 
kubectl get pods
kubectl delete deployments.extensions busybox 
vpnc-connect 
ping www.google.com
kubectl create deployment busybox --image=busybox
kubectl get pods
watch kubectl get pods
clear
vpnc-disconnect 
vpnc-connect 
ping www.google.com
kubectl logs busybox-7676789f95-68jvx -p
kubectl logs busybox-7676789f95-68jvx 
kubectl get pods
kubectl logs busybox-7676789f95-68jvx 
kubectl logs pods  busybox-7676789f95-68jvx 
kubectl describe pods  busybox-7676789f95-68jvx 
clear
journalctl -u kubelet
ping 150.1.88.1
ping 150.1.88.2
ping 150.1.88.3
ping 150.1.88.4
kubectl get nodes
kubectl create deployment busybox --image=busybox --dry-run -o yaml
kubectl create deployment busybox --image=busybox
kubectl create deployment busybox1 --image=busybox
kubectl get pods
kubectl delete deployment busybox
kubectl get pods
kubectl delete deployment busybox1
kubectl get pods
kubectl get pods -o wide
kubectl get pods
kubectl get pods -n=policy-demo 
ping www.google.com
vpnc-disconnect 
vpnc-connect 
touch busybox.yaml
gedit  busybox.yaml
ls
kubectl apply -f busybox.yaml 
kubectl get pods
kubectl exec busybox -ti /bin/bash
kubectl exec busybox -ti bin/bash
kubectl exec busybox -ti 
kubectl exec busybox -ti ash
kubectl get pods
kubectl apply -f busybox.yaml --namespace=policy-demo 
gedit busybox.yaml 
cp busybox.yaml busybox-policy-demo.yaml 
ls
gedit busybox-policy-demo.yaml 
\
kubectl apply -f busybox-policy-demo.yaml
kubectl get pods -n=policy-demo 
kubectl exec -n=policy-demo busybox ash
kubectl exec -n=policy-demo busybox -ti ash
kubectl exec -n=policy-demo kuard-policy-6ddb8c5965-x6qbt -ti ash
kubectl get networkpolicies.extensions 
kubectl get networkpolicies.extensions default-deny
kubectl get networkpolicies.networking.k8s.io
kubectl create -f - <<EOF
kind: NetworkPolicy
apiVersion: networking.k8s.io/v1
metadata:
  name: access-nginx
  namespace: policy-demo
spec:
  podSelector:
    matchLabels:
      run: nginx
  ingress:
    - from:
      - podSelector:
          matchLabels:
            run: access
EOF

kubectl get networkpolicies.networking.k8s.io
kubectl get networkpolicies.networking.k8s.io/access-nginx
vpnc-disconnect 
vpnc-connect 
kubectl get pods
cp busybox-policy-demo.yaml busybox-policy-demo-access.yaml 
gedit busybox-policy-demo-access.yaml 
kubectl apply -f busybox-policy-demo-access.yaml 
kubectl get pods -n=policy-demo 
kubectl get networkpolicies.networking.k8s.io 
kubectl get networkpolicies.networking.k8s.io -n=policy-demo 
kubectl exec -n=policy-demo access -ti ash
kubectl get pods -n=policy-demo 
kubectl run --namespace=policy-demo access --rm -ti --image busybox /bin/sh
kubectl run --namespace=policy-demo access1 --rm -ti --image busybox /bin/sh
clear
kubectl get pods -n=policy-demo 
kubectl delete pods  --namespace=policy-demo access1
kubectl delete pods --namespace=policy-demo access1
kubectl delete pods --namespace=policy-demo access1-f9f84b548-cplk5 
kubectl create -f - <<EOF
kind: NetworkPolicy
apiVersion: networking.k8s.io/v1
metadata:
  name: access-nginx
  namespace: policy-demo
spec:
  podSelector:
    matchLabels:
      run: nginx
  ingress:
    - from:
      - podSelector:
          matchLabels:
            run: access
EOF

kubectl get pods -n=policy-demo 
kubectl delete -f busybox-policy-demo-access.yaml
kubectl get pods -n=policy-demo 
kubectl run --namespace=policy-demo access --rm -ti --image busybox /bin/sh
kubectl get pods
kubectl get pods -n=policy-demo 
kubectl delete pods -n=policy-demo access1-f9f84b548-cwx68 
kubectl get pods -n=policy-demo 
kubectl run --namespace=policy-demo access1 --rm -ti --image busybox /bin/sh
kubectl scale -n=policy-demo pods access1-f9f84b548-nj895 --replicas=0
kubectl scale -n=policy-demo deployment  access1-f9f84b548-nj895 --replicas=0
kubectl get pods
kubectl get pods -n=policy-demo 
kubectl delete ns policy-demo
kubectl get pods
cat /etc/calico/calicoctl.cfg
calicoctl 
swapoff -a
calicoctl 
man calicoctl
clear
kubectl get pods -n=kube-system
kubectl get pods
kubectl get pods -o wide
ls
gedit bgp.yaml 
ssh root@150.1.88.2
kubectl get opds
kubectl get pods
ls
ls -al
ll
ls
kubectl get pods
whereis calicoctl
ls -al /usr/local/bin/calicoctl
exit
