root@eve-ng:/opt/unetlab/addons/qemu/xrv-k9-6.0.1# /opt/qemu/bin/qemu-img convert -f qcow2 -O vmdk hda.qcow2 hda.vmdk
root@eve-ng:/opt/unetlab/addons/qemu/xrv-k9-6.0.1# ls
hda.qcow2  hda.vmdk

tar xf hda.ova

## qemu to vmdk
root@eve-ng:/opt/qemu/bin/qemu-img convert -f qcow2 -O vmdk hda.qcow2 hda.vmdk
## vmdk to qemu
root@eve-ng:/opt/qemu/bin/qemu-img convert -f vmdk -O qcow2 hda.vmdk hda.qcow2


hda.qcow2


