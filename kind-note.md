# KIND(kubernetes in docker) Playgroud k8s v1.18.2
## Docker installation v19.03.8
## HostOS: UBUNTU 20.04.1 Desktop TLS!!!! (cuz It's ez to use...)
## VM resource: Intel I7 CPU 4 cores Memory:7GB disk: 100GB (Sata SSD) vNIC1:vnet8 NAT mode.
## kernel-version: 5.4.0
## sample output
```sh
$ cat /etc/os-release 
NAME="Ubuntu"
VERSION="20.04.1 LTS (Focal Fossa)"
ID=ubuntu
ID_LIKE=debian
PRETTY_NAME="Ubuntu 20.04.1 LTS"
VERSION_ID="20.04"
HOME_URL="https://www.ubuntu.com/"
SUPPORT_URL="https://help.ubuntu.com/"
BUG_REPORT_URL="https://bugs.launchpad.net/ubuntu/"
PRIVACY_POLICY_URL="https://www.ubuntu.com/legal/terms-and-policies/privacy-policy"
VERSION_CODENAME=focal
UBUNTU_CODENAME=focal
~
$uname -a
Linux hitler-k8s 5.4.0-42-generic #46-Ubuntu SMP Fri Jul 10 00:24:02 UTC 2020 x86_64 x86_64 x86_64 GNU/Linux
~
$

```


## Before you started, you should know this
### ubuntu 20.04 desktop version has snap package manager, which is by default, you did't have kubectl command line(kind is only care it's own core elements, cuz for kind perspective, I don't know your control-machine is.)to make sure you can talk to kind cluster.here is the example you should do.


```sh
##installation
$sudo snap install kubectl
snap "kubectl" is already installed, see 'snap help refresh'
~
##check it
$sudo snap list
Name               Version             Rev   Tracking         Publisher   Notes
chromium           85.0.4183.83        1284  latest/stable    canonical✓  -
code               a0479759            42    latest/stable    vscode✓     classic
core               16-2.45.3.1         9804  latest/stable    canonical✓  core
core18             20200724            1885  latest/stable    canonical✓  base
gnome-3-34-1804    0+git.3009fc7       36    latest/stable/…  canonical✓  -
gtk-common-themes  0.1-36-gc75f853     1506  latest/stable/…  canonical✓  -
kubectl            1.18.8              1612  latest/stable    canonical✓  classic
snap-store         3.36.0-80-g208fd61  467   latest/stable/…  canonical✓  -
snapd              2.45.3.1            8790  latest/stable    canonical✓  snapd
~
```
## Sample outputs (I did't setup kind cluster, so kubectl is confusing...)
```sh
$kubectl get nodes
The connection to the server localhost:8080 was refused - did you specify the right host or port?
~
$
```
## After you done that, you should enable completion func to make life ezier. 
```sh
##copy this to ~/.bashrc, save it, then source ~/.bashrc
source <(kind completion bash)
source <(kubectl completion bash)
source <(kubeadm completion bash)
source <(helm completion bash)
export KUBE_EDITOR="code --wait"
```
## Docker installation
```sh
$ sudo apt update
$ sudo apt install docker.io
##docker permission fix. without sudo docker
$ sudo groupadd docker
$ sudo usermod -aG docker $USER
$ newgrp docker 
$ sudo chmod 777 /var/run/docker.sock
```
## Download golang pack
### https://golang.org/dl/
```sh
cd ~/Downloads
tar -C ~/ -xzf go1.14.6.linux-amd64.tar.gz
export GOPATH=~/go/bin
export PATH=$PATH:~/go/bin
export GOROOT=~/go
$go version
go version go1.14.4 linux/amd64
### best practice: add export cli to your .bashrc or .zshrc, then source ~/.bashrc to loading them.
```

## Standard CNI pack privelege setting for kind-config-file loading.
### Usage: Mapping hostpath to containers
### Download cni binary link
https://github.com/containernetworking/plugins/releases
```sh
cd ~/Downloads/cni-plugins-linux-amd64-v0.8.6
sudo chown -R $USER:$USER $PWD
sudo chmod -R 777 $PWD
ls -al 
```

## kind installation

```sh
$GO111MODULE="on" go get sigs.k8s.io/kind@v0.8.1
go: downloading sigs.k8s.io/kind v0.8.1
go: downloading github.com/pkg/errors v0.9.1
go: downloading github.com/mattn/go-isatty v0.0.12
go: downloading k8s.io/apimachinery v0.18.2
go: downloading github.com/alessio/shellescape v1.2.2
go: downloading github.com/spf13/cobra v1.0.0
go: downloading github.com/BurntSushi/toml v0.3.1
go: downloading github.com/evanphx/json-patch v4.2.0+incompatible
go: downloading sigs.k8s.io/yaml v1.2.0
go: downloading gopkg.in/yaml.v3 v3.0.0-20200121175148-a6ecf24a6d71
go: downloading github.com/pelletier/go-toml v1.7.0
go: downloading golang.org/x/sys v0.0.0-20200116001909-b77594299b42
go: downloading github.com/evanphx/json-patch/v5 v5.0.0
go: downloading github.com/spf13/pflag v1.0.5
go: downloading gopkg.in/yaml.v2 v2.2.8
go: downloading github.com/inconshreveable/mousetrap v1.0.0
~
curl -Lo ./kind https://kind.sigs.k8s.io/dl/v0.8.1/kind-linux-amd64
chmod +x ./kind
sudo mv ./kind /usr/local/bin
source <(kind completion bash)
```
## Starting kind
```sh
$docker image ls 
$kind create cluster --image=kindest/node:v1.19.0
###login control-plane node
docker exec -it kind-control-plane /bin/bash
```
## Portainer setup for WEB GUI MGMT
```sh
$sudo  docker volume create portainer_data
$sudo  docker run -d -p 8000:8000 -p 9000:9000 --name=portainer --restart=always -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer
#portainer login: http://localhost:9000
#username:admin
#password:admin@123
```

## kind load config file example.
```sh
##kind configration file
$kind create cluster --config kind-example-config.yaml
```
```yaml
kind: Cluster
apiVersion: kind.x-k8s.io/v1alpha4
networking:
  disableDefaultCNI: true
  podSubnet: "10.244.0.0/16"
  serviceSubnet: "10.96.0.0/12"
# 1 control plane node and 2 worker
nodes:
# the control plane node config
- role: control-plane
  extraMounts:
  - hostPath: /home/hitler/Downloads/cni-plugins-linux-amd64-v0.8.6/
    containerPath: /opt/cni/bin/
    readOnly: false  
# the worker
- role: worker
  extraMounts:
  - hostPath: /home/hitler/Downloads/cni-plugins-linux-amd64-v0.8.6/
    containerPath: /opt/cni/bin/
    readOnly: false
- role: worker
  extraMounts:
  - hostPath: /home/hitler/Downloads/cni-plugins-linux-amd64-v0.8.6/
    containerPath: /opt/cni/bin/
    readOnly: false
```
### Optional setting: kind-node enable ssh
```sh
##reset root password under root
root@kind-control-plane:~# passwd root
New password: 
Retype new password: 
passwd: password updated successfully

##enable ssh
$apt update
$apt install ssh
$apt install nano
$nano /etc/ssh/sshd_config
# Authentication:
#LoginGraceTime 2m
PermitRootLogin yes
#StrictModes yes
#MaxAuthTries 6
#MaxSessions 10
$service sshd restart

##copy cni binary to kind-control-plane
$scp -r ~/Downloads/cni-plugins-linux-amd64-v0.8.6/* root@172.18.0.3:/opt/cni/bin/

##check networking plugin
root@kind-control-plane:/# ls /opt/cni/bin
bandwidth  dhcp      flannel      host-local  loopback  portmap  sbr     tuning
bridge     firewall  host-device  ipvlan      macvlan   ptp      static  vlan
root@kind-control-plane:/# 
##install ping-kind-node
apt-get install iputils-ping
```
### Rancher WebUI setup

```sh
##install rancher UI for k8s
$sudo docker run -d --restart=unless-stopped -p 80:80 -p 443:443 rancher/rancher
##install rancher UI and set local mount
$sudo docker run -d --restart=unless-stopped -p 80:80 -p 443:443 -v /opt/rancher:/var/lib/rancher rancher/rancher

##rancher UI password
admin@123
##rancher server is host machine: in this case:172.18.0.1
##nav web info copy rancher setup CMD, copy to your control machine for boot it.
$ curl --insecure -sfL https://172.18.0.1/v3/import/2bdjkptgsppgxrqkb4wd7682bxjgkv5qpf88m47f6bhrhzqdvw96qr.yaml | kubectl apply -f -
clusterrole.rbac.authorization.k8s.io/proxy-clusterrole-kubeapiserver created
clusterrolebinding.rbac.authorization.k8s.io/proxy-role-binding-kubernetes-master created
namespace/cattle-system created
serviceaccount/cattle created
clusterrolebinding.rbac.authorization.k8s.io/cattle-admin-binding created
secret/cattle-credentials-f6e77d5 created
clusterrole.rbac.authorization.k8s.io/cattle-admin created
deployment.apps/cattle-cluster-agent created
daemonset.apps/cattle-node-agent created
/kuber-deployment/kubernetes/yamls$ 

##linux kubeconfig env
export KUBECONFIG=$KUBECONFIG:$HOME/.kube/config
```

## Example kubectl cli introduction
```sh
##k8s deployment and replicaset
$kubectl create deployment nginx-fucking-cli --image=nginx --dry-run=client -o yaml >>nginx-fucking-cli.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  creationTimestamp: null
  labels:
    app: nginx-fucking-cli
  name: nginx-fucking-cli
spec:
  replicas: 1
  selector:
    matchLabels:
      app: nginx-fucking-cli
  strategy: {}
  template:
    metadata:
      creationTimestamp: null
      labels:
        app: nginx-fucking-cli
    spec:
      containers:
      - image: nginx
        name: nginx
        resources: {}
status: {}
```
```sh
$kubectl get replicaset -o wide
$kubectl autoscale rs nginx-deploy-76df748b9 --max=10 --min=3 --cpu-percent=50 --dry-run=client -oyaml >>kube-auto-scale-replicaset.yaml
apiVersion: autoscaling/v1
kind: HorizontalPodAutoscaler
metadata:
  creationTimestamp: null
  name: nginx-deploy-76df748b9
spec:
  maxReplicas: 10
  minReplicas: 3
  scaleTargetRef:
    apiVersion: apps/v1
    kind: ReplicaSet
    name: nginx-deploy-76df748b9
  targetCPUUtilizationPercentage: 50
status:
  currentReplicas: 0
  desiredReplicas: 0
##
$kubectl scale deployment kuard --replicas=10
```
## Helm 3 setup ref link:
### https://helm.sh/docs/intro/install/
```sh
curl https://baltocdn.com/helm/signing.asc | sudo apt-key add -
sudo apt-get install apt-transport-https --yes
echo "deb https://baltocdn.com/helm/stable/debian/ all main" | sudo tee /etc/apt/sources.list.d/helm-stable-debian.list
sudo apt-get update
sudo apt-get install helm
```

## Helm 2 setup, ref link:
### https://helm.sh/docs/intro/install/#from-the-binary-releases

```sh
##install helm version2 and tiller on k8s v1.18
Find the helm binary in the unpacked directory, and move it to its desired destination 
$mv /home/hitler/Downloads/helm-v2.16.9-linux-amd64/linux-amd64/helm /usr/local/bin/helm
/kuber-deployment$ whereis helm
helm: /usr/local/bin/helm
$kubectl -n kube-system create serviceaccount tiller
$kubectl create clusterrolebinding tiller --clusterrole cluster-admin --serviceaccount=kube-system:tiller

$ helm init --service-account tiller
Creating /home/hitler/.helm 
Creating /home/hitler/.helm/repository 
Creating /home/hitler/.helm/repository/cache 
Creating /home/hitler/.helm/repository/local 
Creating /home/hitler/.helm/plugins 
Creating /home/hitler/.helm/starters 
Creating /home/hitler/.helm/cache/archive 
Creating /home/hitler/.helm/repository/repositories.yaml 
Adding stable repo with URL: https://kubernetes-charts.storage.googleapis.com 
Adding local repo with URL: http://127.0.0.1:8879/charts 
$HELM_HOME has been configured at /home/hitler/.helm.

Tiller (the Helm server-side component) has been installed into your Kubernetes Cluster.

Please note: by default, Tiller is deployed with an insecure 'allow unauthenticated users' policy.
To prevent this, run `helm init` with the --tiller-tls-verify flag.
For more information on securing your installation see: https://v2.helm.sh/docs/securing_installation/
$ 

##helm repo update&&useful cli
$helm repo update 
$helm list
$helm search nginx-inress 
$helm install xxxx

##clusterip internal testing on kind node.
curl -s http://10.103.13.216:8080/env/api
```

## Weavescope on docker(single machine, not on k8s, kind don't load,  weave, bug?? maybe, microk8s is working fine)
```sh
$sudo curl -L git.io/scope -o /usr/local/bin/scope
$sudo chmod a+x /usr/local/bin/scope
$scope launch
Weave Scope is listening at the following URL(s):
  * http://172.18.0.1:4040/
  * http://192.168.120.136:4040/
  * http://100.64.1.1:4040/
$ 
```


## kuard demo app playgroud
```sh
##Kubernetes modify service load-balancer with external-ip
$kubectl patch service kuard -p '{"spec": {"type": "LoadBalancer", "externalIPs":["1.2.3.4"]}}'

##kubernetes add service with external-ip option
$kubectl expose deployment kuard --name=kuardelb --port 8080 --type=LoadBalancer --external-ip=6.6.6.6

##ExternalIPtesting, host add static route to worker1=172.18.0.2
$ sudo ip route add 1.2.3.4/32 via 172.18.0.2 dev br-0a1a1395012d
[sudo] password for hitler: 
$ ip route show
default via 192.168.120.2 dev ens33 proto dhcp metric 100 
1.2.3.4 via 172.18.0.2 dev br-0a1a1395012d

## curl kube service testing
$ curl -s http://1.2.3.4:8080/env/api
{"commandLine":["/kuard"],"env":{"HOME":"/","HOSTNAME":"kuard-74684b58b8-w57zs","KUBERNETES_PORT":"tcp://10.96.0.1:443","KUBERNETES_PORT_443_TCP":"tcp://10.96.0.1:443","KUBERNETES_PORT_443_TCP_ADDR":"10.96.0.1","KUBERNETES_PORT_443_TCP_PORT":"443","KUBERNETES_PORT_443_TCP_PROTO":"tcp","KUBERNETES_SERVICE_HOST":"10.96.0.1","KUBERNETES_SERVICE_PORT":"443","KUBERNETES_SERVICE_PORT_HTTPS":"443","PATH":"/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"}}
$

##linux static-route-ECMP
sudo ip route add 1.2.3.4/32 nexthop via 172.18.0.4 dev br-0a1a1395012d nexthop via 172.18.0.3 dev br-0a1a1395012d
sudo ip route add 6.6.6.6/32 nexthop via 172.18.0.4 dev br-0a1a1395012d nexthop via 172.18.0.3 dev br-0a1a1395012d
$ ip route show
default via 192.168.120.2 dev ens33 proto dhcp metric 100 
1.2.3.4 
	nexthop via 172.18.0.2 dev br-0a1a1395012d weight 1 
	nexthop via 172.18.0.3 dev br-0a1a1395012d weight 1 
6.6.6.6 
	nexthop via 172.18.0.2 dev br-0a1a1395012d weight 1 
	nexthop via 172.18.0.3 dev br-0a1a1395012d weight 1

## curl loop testing
$ while true ; do curl -s http://1.2.3.4:8080/env/api | jq '.env.HOSTNAME'; done
"kuard-74684b58b8-2d2nl"
"kuard-74684b58b8-2d2nl"
"kuard-74684b58b8-w57zs"
"kuard-74684b58b8-vpjmq"
"kuard-74684b58b8-2d2nl"
"kuard-74684b58b8-nsgr8"
"kuard-74684b58b8-vpjmq"
"kuard-74684b58b8-2d2nl"
"kuard-74684b58b8-2d2nl"
"kuard-74684b58b8-w57zs"
"kuard-74684b58b8-2d2nl"

##kubernetes service iptables cli check, login kind-worker node.
$docker exec -it kind-worker /bin/bash
root@kind-worker:/# iptables -L -t nat |grep 1.2.3.4
KUBE-MARK-MASQ  tcp  --  anywhere             1.2.3.4              /* default/kuard: external IP */ tcp dpt:8080
KUBE-SVC-CUXC5A3HHHVSSN62  tcp  --  anywhere             1.2.3.4              /* default/kuard: external IP */ tcp dpt:8080 PHYSDEV match ! --physdev-is-in ADDRTYPE match src-type !LOCAL
KUBE-SVC-CUXC5A3HHHVSSN62  tcp  --  anywhere             1.2.3.4              /* default/kuard: external IP */ tcp dpt:8080 ADDRTYPE match dst-type LOCAL
root@kind-worker:/# 
root@kind-worker:/# iptables -L -t nat |grep 6.6.6.6          
KUBE-MARK-MASQ  tcp  --  anywhere             6.6.6.6              /* default/motherfucker: external IP */ tcp dpt:8080
KUBE-SVC-A7YGKRTI6TALCQ54  tcp  --  anywhere             6.6.6.6              /* default/motherfucker: external IP */ tcp dpt:8080 PHYSDEV match ! --physdev-is-in ADDRTYPE match src-type !LOCAL
KUBE-SVC-A7YGKRTI6TALCQ54  tcp  --  anywhere             6.6.6.6              /* default/motherfucker: external IP */ tcp dpt:8080 ADDRTYPE match dst-type LOCAL
root@kind-worker:/# 
```
