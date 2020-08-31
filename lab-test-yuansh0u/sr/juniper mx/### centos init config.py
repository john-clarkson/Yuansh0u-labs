### centos init config
 ## configure ip address on eth0 port 
> ifconfig eth0 x.x.x.x netmask 255.255.0.0
## enable interface eth0
>ifup eth0
##route-table
>route-n

[root@juniper /]# yum -y install vpnc
Loaded plugins: fastestmirror
Setting up Install Process

## show interface information
## eve-ng use pnet0 as the management interface, not eth0
## if you add an addtional NIC card, you will be set the dhcp client functions as to pnet1 interface.


##enable interface
[root@juniper /]# ifup eth1

Determining IP information for eth1... done.

##disable interface
[root@juniper /]# ifdown eth1

###

##add default route
route add default gw 150.1.66.254 eth0
## add static route
 
## check default route
 root@eve-ng:/# route
Kernel IP routing table
Destination     Gateway         Genmask         Flags Metric Ref    Use Iface
default         150.1.1.253     0.0.0.0         UG    0      0        0 pnet0
150.1.0.0       *               255.255.0.0     U     0      0        0 pnet0
root@eve-ng:/# route -n
Kernel IP routing table
Destination     Gateway         Genmask         Flags Metric Ref    Use Iface
0.0.0.0         150.1.1.253     0.0.0.0         UG    0      0        0 pnet0
150.1.0.0       0.0.0.0         255.255.0.0     U     0      0        0 pnet0
root@eve-ng:/# 


## delete default gateway
 root@eve-ng:/# route -n
Kernel IP routing table
Destination     Gateway         Genmask         Flags Metric Ref    Use Iface
0.0.0.0         150.1.1.253     0.0.0.0         UG    0      0        0 pnet0
150.1.0.0       0.0.0.0         255.255.0.0     U     0      0        0 pnet0
root@eve-ng:/# route del default 
root@eve-ng:/# route -n 
Kernel IP routing table
Destination     Gateway         Genmask         Flags Metric Ref    Use Iface
150.1.0.0       0.0.0.0         255.255.0.0     U     0      0        0 pnet0
root@eve-ng:/# 

## if you set the wrong ip address to network adptors, please use f0llowing command to delete it.
ip addr del 10.21.0.86/24 dev eth1
## set dhcp client to pnet1
 dhclient pnet1
## check dhcp client working or not.






[root@juniper /]# gdisk -l /dev/sdb
GPT fdisk (gdisk) version 0.8.10

Partition table scan:
  MBR: protective
  BSD: not present
  APM: not present
  GPT: present

Found valid GPT with protective MBR; using GPT.
Disk /dev/sdb: 52430848 sectors, 25.0 GiB
Logical sector size: 512 bytes
Disk identifier (GUID): 4F267336-4733-11E7-0233-9FC99A66320D
Partition table holds up to 4 entries
First usable sector is 3, last usable sector is 52430845
Partitions will be aligned on 8-sector boundaries
Total free space is 2013 sectors (1006.5 KiB)

Number  Start (sector)    End (sector)  Size       Code  Name
   1               8              37   15.0 KiB    A501  
   2              40         4194343   2.0 GiB     A503  oam
   3         4194344        46137383   20.0 GiB    A503  junos
   4        46137384        52428839   3.0 GiB     A502  swap
[root@juniper /]# 

[root@juniper etc]# yum -y install nano
[root@juniper etc]# nano fstab 
  GNU nano 2.0.9                           File: fstab                                                             


#
# /etc/fstab
# Created by anaconda on Sat Mar  3 09:45:30 2018
#
# Accessible filesystems, by reference, are maintained under '/dev/disk'
# See man pages fstab(5), findfs(8), mount(8) and/or blkid(8) for more info
#
/dev/mapper/vg_juniper-lv_root /                       ext4    defaults        1 1
UUID=64466752-7ca8-41f1-9224-fd28310de09a /boot                   ext4    defaults        1 2
/dev/mapper/vg_juniper-lv_swap swap                    swap    defaults        0 0
tmpfs                   /dev/shm                tmpfs   defaults        0 0
devpts                  /dev/pts                devpts  gid=5,mode=620  0 0
sysfs                   /sys                    sysfs   defaults        0 0
proc                    /proc                   proc    defaults        0 0
/dev/sdb                /media/J-NS3.2          ext4    defaults        0 0

[root@juniper etc]# mount -a
mount: wrong fs type, bad option, bad superblock on /dev/sdb,
       missing codepage or helper program, or other error
       In some cases useful info is found in syslog - try
       dmesg | tail  or so

[root@juniper etc]#yum -y install cifs-utils
[root@juniper etc]#yum -y install nfs-utils
[root@juniper /]# fsck /dev/sdb
fsck from util-linux-ng 2.17.2
e2fsck 1.41.12 (17-May-2010)
fsck.ext2: Superblock invalid, trying backup blocks...
fsck.ext2: Bad magic number in super-block while trying to open /dev/sdb

The superblock could not be read or does not describe a correct ext2
filesystem.  If the device is valid and it really contains an ext2
filesystem (and not swap or ufs or something else), then the superblock
is corrupt, and you might try running e2fsck with an alternate superblock:
    e2fsck -b 8193 <device>


[root@juniper /]# mke2fs -n /dev/sdb
mke2fs 1.41.12 (17-May-2010)
/dev/sdb is entire device, not just one partition!
Proceed anyway? (y,n) y
warning: 256 blocks unused.

Filesystem label=
OS type: Linux
Block size=4096 (log=2)
Fragment size=4096 (log=2)
Stride=0 blocks, Stripe width=0 blocks
1641600 inodes, 6553600 blocks
327692 blocks (5.00%) reserved for the super user
First data block=0
Maximum filesystem blocks=4294967296
200 block groups
32768 blocks per group, 32768 fragments per group
8208 inodes per group
Superblock backups stored on blocks: 
        32768, 98304, 163840, 229376, 294912, 819200, 884736, 1605632, 2654208, 
        4096000


[root@juniper /]# gdisk 
GPT fdisk (gdisk) version 0.8.10

Type device filename, or press <Enter> to exit: /dev/sdb 
Partition table scan:
  MBR: protective
  BSD: not present
  APM: not present
  GPT: present

Found valid GPT with protective MBR; using GPT.

Command (? for help): GPT
b       back up GPT data to a file
c       change a partition's name
d       delete a partition
i       show detailed information on a partition
l       list known partition types
n       add a new partition
o       create a new empty GUID partition table (GPT)
p       print the partition table
q       quit without saving changes
r       recovery and transformation options (experts only)
s       sort partitions
t       change a partition's type code
v       verify disk
w       write table to disk and exit
x       extra functionality (experts only)
?       print this menu

Command (? for help): 


[root@juniper ~]# gdisk -l /dev/sda
GPT fdisk (gdisk) version 0.8.10

Partition table scan:
  MBR: protective
  BSD: not present
  APM: not present
  GPT: present

Found valid GPT with protective MBR; using GPT.
Disk /dev/sda: 52430848 sectors, 25.0 GiB
Logical sector size: 512 bytes
Disk identifier (GUID): 4F267336-4733-11E7-0233-9FC99A66320D
Partition table holds up to 4 entries
First usable sector is 3, last usable sector is 52430845
Partitions will be aligned on 8-sector boundaries
Total free space is 2013 sectors (1006.5 KiB)

Number  Start (sector)    End (sector)  Size       Code  Name
   1               8              37   15.0 KiB    A501  
   2              40         4194343   2.0 GiB     A503  oam
   3         4194344        46137383   20.0 GiB    A503  junos
   4        46137384        52428839   3.0 GiB     A502  swap
[root@juniper ~]# gdisk -l /dev/sda
GPT fdisk (gdisk) version 0.8.10

Partition table scan:
  MBR: protective
  BSD: not present
  APM: not present
  GPT: present

Found valid GPT with protective MBR; using GPT.
Disk /dev/sda: 52430848 sectors, 25.0 GiB
Logical sector size: 512 bytes
Disk identifier (GUID): 4F267336-4733-11E7-0233-9FC99A66320D
Partition table holds up to 4 entries
First usable sector is 3, last usable sector is 52430845
Partitions will be aligned on 8-sector boundaries
Total free space is 2013 sectors (1006.5 KiB)

Number  Start (sector)    End (sector)  Size       Code  Name
   1               8              37   15.0 KiB    A501  
   2              40         4194343   2.0 GiB     A503  oam
   3         4194344        46137383   20.0 GiB    A503  junos
   4        46137384        52428839   3.0 GiB     A502  swap
[root@juniper ~]# gdisk -l /dev/sda
GPT fdisk (gdisk) version 0.8.10

Partition table scan:
  MBR: protective
  BSD: not present
  APM: not present
  GPT: present

Found valid GPT with protective MBR; using GPT.
Disk /dev/sda: 52430848 sectors, 25.0 GiB
Logical sector size: 512 bytes
Disk identifier (GUID): 4F267336-4733-11E7-0233-9FC99A66320D
Partition table holds up to 4 entries
First usable sector is 3, last usable sector is 52430845
Partitions will be aligned on 8-sector boundaries
Total free space is 2013 sectors (1006.5 KiB)

Number  Start (sector)    End (sector)  Size       Code  Name
   1               8              37   15.0 KiB    A501  
   2              40         4194343   2.0 GiB     A503  oam
   3         4194344        46137383   20.0 GiB    A503  junos
   4        46137384        52428839   3.0 GiB     A502  swap
[root@juniper ~]# gdisk /dev/sda
GPT fdisk (gdisk) version 0.8.10

Partition table scan:
  MBR: protective
  BSD: not present
  APM: not present
  GPT: present

Found valid GPT with protective MBR; using GPT.


Command (? for help): i
Partition number (1-4): 
Partition number (1-4): 1
Partition GUID code: 83BD6B9D-7F41-11DC-BE0B-001560B84F0F (FreeBSD boot)
Partition unique GUID: 4F266CD8-4733-11E7-0567-C7697351FF4A
First sector: 8 (at 4.0 KiB)
Last sector: 37 (at 18.5 KiB)
Partition size: 30 sectors (15.0 KiB)
Attribute flags: 0000000000000000
Partition name: ''

Command (? for help): i
Partition number (1-4): 2
Partition GUID code: 516E7CB6-6ECF-11D6-8FF8-00022D09712B (FreeBSD UFS)
Partition unique GUID: 4F266CE2-4733-11E7-18EC-29CDBAABF2FB
First sector: 40 (at 20.0 KiB)
Last sector: 4194343 (at 2.0 GiB)
Partition size: 4194304 sectors (2.0 GiB)
Attribute flags: 0000000000000000
Partition name: 'oam'

Command (? for help): i
Partition number (1-4): 3
Partition GUID code: 516E7CB6-6ECF-11D6-8FF8-00022D09712B (FreeBSD UFS)
Partition unique GUID: 4F266CEC-4733-11E7-29E3-477CC254F81B
First sector: 4194344 (at 2.0 GiB)
Last sector: 46137383 (at 22.0 GiB)
Partition size: 41943040 sectors (20.0 GiB)
Attribute flags: 0000000000000000
Partition name: 'junos'

Command (? for help): i
Partition number (1-4): 4
Partition GUID code: 516E7CB5-6ECF-11D6-8FF8-00022D09712B (FreeBSD swap)
Partition unique GUID: 4F266CEC-4733-11E7-29E8-E78D765A2E63
First sector: 46137384 (at 22.0 GiB)
Last sector: 52428839 (at 25.0 GiB)
Partition size: 6291456 sectors (3.0 GiB)
Attribute flags: 0000000000000000
Partition name: 'swap'

Command (? for help): 