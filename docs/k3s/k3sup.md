# k3sup

[k3sup](https://github.com/alexellis/k3sup) is a light-weight utility to get from zero to KUBECONFIG with k3s on any local or remote VM.

Install k3sup using Homebrew:

```bash
brew install k3sup
```

**NOTE:**

Most commands in the following assume superuser privileges, so you may want to run them with `sudo` or switch to the root user (`su`)

## Install k3s Master Node

```bash
k3sup install \
    --user pi \
    --sudo true \
    --ip 192.168.1.11 \
    --cluster \
    --k3s-channel stable \
    --no-extras \
    --local-path ~/.kube/config \
    --merge \
    --tls-san 192.168.1.10 \
    --tls-san k3s.local.spaelling.xyz
```

validate that k3s is running

```bash
kubectl get nodes
```

and check the status of the k3s service

```bash
systemctl status k3s.service
```

Look specifically for `--tls-san k3s.local.spaelling.xyz --tls-san 192.168.10 --disable servicelb --disable traefik`. If any of these parameters are missing the installation did not go as planned.

## Join a new server to the cluster

```bash
k3sup join \
    --user pi \
    --ip 192.168.1.12 \
    --sudo true \
    --server \
    --server-ip 192.168.1.11 \
    --server-user pi \
    --k3s-channel stable \
    --no-extras
```

## Uninstall k3s

Simply run the uninstall script on each node:

```bash
sudo /usr/local/bin/k3s-uninstall.sh
```
