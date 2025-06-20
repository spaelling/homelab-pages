# Longhorn

[Installation Requirements](https://longhorn.io/docs/1.9.0/deploy/install/#installation-requirements)

Checking Prerequisites Using Longhorn Command Line Tool

```bash
sudo mkdir -p ~/.kube
sudo cp /etc/rancher/k3s/k3s.yaml ~/.kube/config
```

```bash
curl -sSfL -o longhornctl https://github.com/longhorn/cli/releases/download/v1.9.0/longhornctl-linux-arm64

sudo chmod +x longhornctl
sudo KUBECONFIG=/etc/rancher/k3s/k3s.yaml ./longhornctl check preflight
```

We can attempt to have Longhorn install prerequisites. This will install prerequisites on all nodes in the cluster.

```bash
sudo ./longhornctl --kube-config ~/.kube/config --image longhornio/longhorn-cli:v1.9.0 install preflight
```

## Helm Installation

[Install with Helm](https://longhorn.io/docs/1.9.0/deploy/install/install-with-helm/)

```bash
brew install helm
```

And then install Longhorn using Helm.

```bash
helm repo add longhorn https://charts.longhorn.io
helm repo update
helm install longhorn longhorn/longhorn --namespace longhorn-system --create-namespace --version 1.9.0
kubectl -n longhorn-system get pod
```

## Proxy

When Traefik is up and running we can create an ingress and certificate for Longhorn.

The existing frontend service is already behind a load balancer, so we delete that and create our own.

```bash
kubectl delete service longhorn-frontend -n longhorn-system
kubectl apply -f longhorn-frontend.yaml
kubectl apply -f certificate.yaml
kubectl apply -f ingress.yaml
```

Wait for the certificate to be ready.

```bash
kubectl describe certificate longhorn-web-ui-tls -n longhorn-system
```
