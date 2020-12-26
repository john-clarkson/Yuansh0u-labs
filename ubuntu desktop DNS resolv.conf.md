# ubuntu desktop 20.04 DNS resolv.conf playground

### Default settings
$ cat /etc/resolv.conf
```shell=
╰─ cat /etc/resolv.conf                                                                                    ─╯
# This file is managed by man:systemd-resolved(8). Do not edit.
#
# This is a dynamic resolv.conf file for connecting local clients to the
# internal DNS stub resolver of systemd-resolved. This file lists all
# configured search domains.
#
# Run "resolvectl status" to see details about the uplink DNS servers
# currently in use.
#
# Third party programs must not access this file directly, but only through the
# symlink at /etc/resolv.conf. To manage man:resolv.conf(5) in a different way,
# replace this symlink by a static file or a different symlink.
#
# See man:systemd-resolved.service(8) for details about the supported modes of
# operation for /etc/resolv.conf.

nameserver 127.0.0.53
options edns0
search localdomain


```
$systemctl status systemd-resolved.service
```shell=
╰─ systemctl status systemd-resolved.service                                                               ─╯
● systemd-resolved.service - Network Name Resolution
     Loaded: loaded (/lib/systemd/system/systemd-resolved.service; enabled; vendor preset: enabled)
     Active: active (running) since Sat 2020-12-26 18:19:17 HKT; 25min ago
       Docs: man:systemd-resolved.service(8)
             https://www.freedesktop.org/wiki/Software/systemd/resolved
             https://www.freedesktop.org/wiki/Software/systemd/writing-network-configuration-managers
             https://www.freedesktop.org/wiki/Software/systemd/writing-resolver-clients
   Main PID: 52988 (systemd-resolve)
     Status: "Processing requests..."
      Tasks: 1 (limit: 4648)
     Memory: 5.9M
     CGroup: /system.slice/systemd-resolved.service
             └─52988 /lib/systemd/systemd-resolved

Dec 26 18:19:17 hitler-k8s systemd[1]: Starting Network Name Resolution...
Dec 26 18:19:17 hitler-k8s systemd-resolved[52988]: Positive Trust Anchors:
Dec 26 18:19:17 hitler-k8s systemd-resolved[52988]: . IN DS 20326 8 2 e06d44b80b8f1d39a95c0b0d7c65d08458e8804>
Dec 26 18:19:17 hitler-k8s systemd-resolved[52988]: Negative trust anchors: 10.in-addr.arpa 16.172.in-addr.ar>
Dec 26 18:19:17 hitler-k8s systemd-resolved[52988]: Using system hostname 'hitler-k8s'.
Dec 26 18:19:17 hitler-k8s systemd[1]: Started Network Name Resolution.
Dec 26 18:19:18 hitler-k8s systemd-resolved[52988]: Server returned error NXDOMAIN, mitigating potential DNS >
Dec 26 18:19:18 hitler-k8s systemd-resolved[52988]: Server returned error NXDOMAIN, mitigating potential DNS >
Dec 26 18:19:18 hitler-k8s systemd-resolved[52988]: Server returned error NXDOMAIN, mitigating potential DNS >
Dec 26 18:19:50 hitler-k8s systemd-resolved[52988]: Using degraded feature set (UDP) for DNS server 10.211.55>
lines 1-24/24 (END)
```

$systemctl stop systemd-resolved.service 
$systemctl disable systemd-resolved.service

╰─ sudo nano /etc/resolv.conf                                                                   
```shell=
$ cat /etc/resolv.conf                                                                                    ─╯
# This file is managed by man:systemd-resolved(8). Do not edit.
#
# This is a dynamic resolv.conf file for connecting local clients to the
# internal DNS stub resolver of systemd-resolved. This file lists all
# configured search domains.
#
# Run "resolvectl status" to see details about the uplink DNS servers
# currently in use.
#
# Third party programs must not access this file directly, but only through the
# symlink at /etc/resolv.conf. To manage man:resolv.conf(5) in a different way,
# replace this symlink by a static file or a different symlink.
#
# See man:systemd-resolved.service(8) for details about the supported modes of
# operation for /etc/resolv.conf.
nameserver 114.114.114.114
nameserver 127.0.0.53
options edns0
search localdomain
```

```shell=
╰─ nslookup                                                                                                ─╯
> bing.com
Server:		114.114.114.114
Address:	114.114.114.114#53

Non-authoritative answer:
Name:	bing.com
Address: 13.107.21.200
Name:	bing.com
Address: 204.79.197.200
Name:	bing.com
Address: 2620:1ec:c11::200
```