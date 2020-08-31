cat << EOF | sudo tee -a /etc/systemd/system/gobgpd.service


[Unit]
Description=gobgpd
After=network.target syslog.target
[Service]
Type=simple
PermissionsStartOnly=yes
User=seaomi
ExecStartPre=/sbin/setcap 'cap_net_bind_service=+ep' /usr/local/sbin/gobgpd
ExecStart=/usr/local/sbin/gobgpd -f /etc/gobgpd.conf --cpus=1
ExecReload=/bin/kill -s HUP $MAINPID
ExecStop=/bin/kill -s TERM $MAINPID
[Install]
WantedBy=multi-user.target


EOF