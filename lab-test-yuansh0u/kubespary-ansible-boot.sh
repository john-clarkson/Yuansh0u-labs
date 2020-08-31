hitler@hitler-virtual-machine:~$ cat ansible-playbook-cli.sh 
sudo apt-get install sshpass

# Install dependencies from ``requirements.txt``
cd kubespary
sudo pip install -r requirements.txt

# Copy ``inventory/sample`` as ``inventory/mycluster``
cp -rfp inventory/sample inventory/mycluster

# Update Ansible inventory file with inventory builder
declare -a IPS=(10.10.1.3 10.10.1.4 10.10.1.5)
declare -a IPS=(10.21.0.63 10.21.0.64)
CONFIG_FILE=inventory/mycluster/hosts.ini python3 contrib/inventory_builder/inventory.py ${IPS[@]}


declare -a IPS=(10.10.1.3 10.10.1.4 10.10.1.5)
CONFIG_FILE=inventory/mycluster/hosts.yml python3 contrib/inventory_builder/inventory.py ${IPS[@]}

# Review and change parameters under ``inventory/mycluster/group_vars``
cat inventory/mycluster/group_vars/all/all.yml
cat inventory/mycluster/group_vars/k8s-cluster/k8s-cluster.yml

# Deploy Kubespray with Ansible Playbook - run the playbook as root
# The option `-b` is required, as for example writing SSL keys in /etc/,
# installing packages and interacting with various systemd daemons.
# Without -b the playbook will fail to run!
ansible-playbook -i inventory/mycluster/hosts.ini --become --become-user=root cluster.yml -e "ansible_user=root ansible_ssh_pass=toor ansible_sudo_pass=toor"

ansible-playbook -i inventory/mycluster/hosts.ini --become --become-user=root cluster.yml -e "ansible_user=root ansible_ssh_pass=toor ansible_sudo_pass=toor" 

ansible-playbook xxxx/xx.yml  


###
ansible-playbook -i inventory/mycluster/hosts.ini --become --become-user=hitler cluster.yml --private-key=~/.ssh/id_rsa.pub
ssh-copy-id -i ~/.ssh/id_rsa.pub root@150.1.88.1