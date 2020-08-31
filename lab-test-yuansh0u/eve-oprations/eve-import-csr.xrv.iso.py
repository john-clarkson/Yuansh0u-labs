

#eve-import-csr1kv.iso

https://www.eve-ng.net/index.php/documentation/howtos/howto-add-cisco-csrv1000-16-x-denali-everest-fuji/

/opt/qemu-2.2.0/bin/qemu-system-x86_64  -nographic -drive file=virtioa.qcow2,if=virtio,bus=0,unit=0,cache=none -machine type=pc-1.0,accel=kvm -serial mon:stdio -nographic -nodefconfig -nodefaults -rtc base=utc -cdrom csr1000v-universalk9.17.01.01.iso -boot order=dc  -m 3072


mkdir  /opt/unetlab/addons/qemu/csr1000vng-universalk9.17.01.01/

#eve import xrv9k

https://www.eve-ng.net/index.php/documentation/howtos/howto-add-cisco-xrv-9000/

/opt/qemu-2.4.0/bin/qemu-system-x86_64  -nographic -drive file=virtioa.qcow2,if=virtio,bus=0,unit=0,cache=none -machine type=pc-1.0,accel=kvm -serial mon:stdio -nographic -nodefconfig -nodefaults -rtc base=utc -cdrom xrv9k-fullk9-x.vrr.vga-7.0.1.iso -boot order=dc  -m 16384

