#!bin/bash
##This file is for ubuntu server init
sudo apt install -y nmap
sudo apt install -y vpnc
sudo apt install -y ifupdown     
sudo apt install -y ifupdown2    
sudo apt install -y netscript-2.4
sudo apt install -y python-pip
pip2 install --upgrade pip
sudo apt install python3-pip
sudo chown hitler -R /usr/bin/pip
sudo dhclient eth0 
sudo ip addr add 150.1.88.1/16 dev eth1
sudo ifconfig eth1 up
sudo ifconfig eth2 up