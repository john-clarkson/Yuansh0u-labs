cd tmp
root@eve-ng:unzip -p C7200-AD.bin 
 > c7200-AD.image
root@eve-ng:  mv C7200-AD.image /opt/unetlab/addons/dynamips/
root@eve-ng: dynamips -p 7200 -t 7200 /opt/unetlab/addons/dynamips/c7200-adventerprisek9-mz.152-4.S6.image

top
 q
kill {PID number}
 
 dynamips -p 7200 -t 7200 /opt/unetlab/addons/dynamips/c7200-adventerprisek9-mz.152-4.S6.image 

 ctrl + ] i

dynamips -p 7200 -t 7200  --idle-pc 0x80369ac4 /opt/unetlab/addons/dynamips/c7200-adventerprisek9-mz.152-4.S6.image 



0x62f224ac (count=25)

C:\Program Files\EVE-NG\

 ===//
 root@eve-ng:~# cd /tmp
root@eve-ng:/tmp# ls
ade  hsperfdata_tomcat8  netio32768  PA-VM-ESX-6.1.0.ova  tomcat8-tomcat8-tmp  vmware-root
root@eve-ng:/tmp# tar xf ../PA-VM-ESX-6.1.0.ova
tar: ../PA-VM-ESX-6.1.0.ova: Cannot open: No such file or directory
tar: Error is not recoverable: exiting now
root@eve-ng:/tmp# tar xf PA-VM-ESX-6.1.0.ova

#####

root@eve-ng:/tmp# ls
ade                 PA-VM-ESX-6.1.0-disk1.vmdk  PA-VM-ESX-6.1.0.ovf
hsperfdata_tomcat8  PA-VM-ESX-6.1.0.mf          tomcat8-tomcat8-tmp
netio32768          PA-VM-ESX-6.1.0.ova         vmware-root
root@eve-ng:/tmp# 

/opt/qemu/bin/qemu-img convert -f vmdk -O qcow2 PA-VM-ESX-6.1.0-disk1.vmdk virtioa.qcow2

root@eve-ng:/tmp# /opt/qemu/bin/qemu-img convert -f vmdk -O qcow2 PA-VM-ESX-6.1.0-disk1.vmdk virtioa.qcow2
root@eve-ng:/tmp# ls
ade                 PA-VM-ESX-6.1.0-disk1.vmdk  PA-VM-ESX-6.1.0.ovf  vmware-root
hsperfdata_tomcat8  PA-VM-ESX-6.1.0.mf          tomcat8-tomcat8-tmp
netio32768          PA-VM-ESX-6.1.0.ova         virtioa.qcow2
root@eve-ng:/tmp# cd ..
root@eve-ng:/# mkdir -p /opt/unetlab/addons/qemu/paloalto-6.1.0
root@eve-ng:/# mv virtioa.qcow2 /opt/unetlab/addons/qemu/paloalto-6.1.0
mv: cannot stat 'virtioa.qcow2': No such file or directory
root@eve-ng:/# cd /tmp
root@eve-ng:/tmp# mv virtioa.qcow2 /opt/unetlab/addons/qemu/paloalto-6.1.0
root@eve-ng:/tmp# 