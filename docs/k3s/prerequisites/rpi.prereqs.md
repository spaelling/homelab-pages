# Raspberry Pi

To run K3s on a Raspberry Pi, we need to ensure that the system is properly configured. Below are the steps to prepare Raspberry Pi for K3s installation.

On the Raspberry Pi modify `/boot/firmware/cmdline.txt` to include `cgroup_enable=cpuset cgroup_memory=1 cgroup_enable=memory`

```bash
nano /boot/firmware/cmdline.txt
```

edit `/etc/dphys-swapfile` and set `CONF_SWAPSIZE=0`

```bash
nano /etc/dphys-swapfile
```

then run the following commands to disable and reconfigure swap

```bash
dphys-swapfile swapoff
dphys-swapfile setup
```

## Static IP address

A static IP address is recommended for the Raspberry Pi to ensure consistent connectivity.

```bash
nano /etc/hosts
```

and change 127.0.0.1 to desired static IP address

This should return the static IP address

```bash
hostname --ip-address
```

Next use `nmcli` to set a static IP address.

```bash
nmcli connection add type ethernet ifname eth0 con-name static-eth0 ipv4.addresses 192.168.1.11/24 ipv4.gateway 192.168.1.1 ipv4.dns 192.168.1.60 ipv4.method manual
nmcli connection up static-eth0
```

use `ip a` to verify the static IP address is set correctly
