# Kubevip

Following instructions on [k3s](https://kube-vip.io/docs/usage/k3s/). Full script towards the end.

Create Manifests Folder

```bash
mkdir -p /var/lib/rancher/k3s/server/manifests/
```

K3s has an optional manifests directory that will be searched to auto-deploy any manifests found within.

Upload kube-vip RBAC Manifest

```bash
curl https://kube-vip.io/manifests/rbac.yaml > /var/lib/rancher/k3s/server/manifests/kube-vip-rbac.yaml
```

## Generate a kube-vip DaemonSet Manifest

```bash
export VIP=192.168.1.10
export INTERFACE=eth0
apt install -y jq curl
KVVERSION=$(curl -sL https://api.github.com/repos/kube-vip/kube-vip/releases | jq -r ".[0].name")
alias kube-vip="ctr image pull ghcr.io/kube-vip/kube-vip:$KVVERSION; ctr run --rm --net-host ghcr.io/kube-vip/kube-vip:$KVVERSION vip /kube-vip"
```

Generate manifest and save to `kube-vip.yaml`:

```bash
kube-vip manifest daemonset \
    --interface $INTERFACE \
    --address $VIP \
    --inCluster \
    --taint \
    --controlplane \
    --services \
    --arp \
    --leaderElection | tee /var/lib/rancher/k3s/server/manifests/kube-vip.yaml
```

```bash
mkdir -p /var/lib/rancher/k3s/server/manifests/
curl https://kube-vip.io/manifests/rbac.yaml > /var/lib/rancher/k3s/server/manifests/kube-vip-rbac.yaml
export VIP=192.168.1.10
export INTERFACE=eth0
apt install -y jq curl
KVVERSION=$(curl -sL https://api.github.com/repos/kube-vip/kube-vip/releases | jq -r ".[0].name")
alias kube-vip="ctr image pull ghcr.io/kube-vip/kube-vip:$KVVERSION; ctr run --rm --net-host ghcr.io/kube-vip/kube-vip:$KVVERSION vip /kube-vip"
kube-vip manifest daemonset \
    --interface $INTERFACE \
    --address $VIP \
    --inCluster \
    --taint \
    --controlplane \
    --services \
    --arp \
    --leaderElection | tee /var/lib/rancher/k3s/server/manifests/kube-vip.yaml
```

This is now automatically deployed by k3s, and you can check the status of the kube-vip pods:

```bash
kubectl get pods -n kube-system
```

Add a DNS entry for the VIP in the DNS server, in this case A-record `k3s.local.spaelling.xyz=192.168.1.10`

edit kubeconfig `sudo nano ~/.kube/config` and change the server address to `k3s.local.spaelling.xyz`.

## Install the kube-vip Cloud Provider

```bash
kubectl apply -f https://raw.githubusercontent.com/kube-vip/kube-vip-cloud-provider/main/manifest/kube-vip-cloud-controller.yaml
```

We will create kube-vip Cloud Provider ConfigMap later when Traefik is up and running as we want it handle all ingress traffic.
