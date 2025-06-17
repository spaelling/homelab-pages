# cert-manager

```bash
brew install helm
```

[Installing with Helm](https://cert-manager.io/docs/installation/helm/)

```bash
helm repo add jetstack https://charts.jetstack.io --force-update
helm install \
  cert-manager jetstack/cert-manager \
  --namespace cert-manager \
  --create-namespace \
  --version v1.18.0 \
  --set crds.enabled=true
kubectl -n cert-manager get pod
```

## Issuer Configuration

Create a secret in Kubernetes containing the Cloudflare API token.

Go to [Cloudflare dashboard](https://dash.cloudflare.com/profile/api-tokens) - click Create Token and use the `Edit zone DNS` template. Pick the specific zone resource. Restrict the client IP.

For details on yaml configuration, see:

[Cloudflare API tokens](https://cert-manager.io/docs/configuration/acme/dns01/cloudflare/)

[Creating a ACME ClusterIssuer](https://cert-manager.io/docs/configuration/acme/#creating-a-basic-acme-issuer)

```bash
cd ~/git/Privat/homelab-pages/docs/traefik
kubectl apply -n kube-system -f cloudflare_api_token.yaml
kubectl apply -f acme_clusterissuer.yaml
```

## Troubleshooting

Check the status of the certificate in the `traefik` namespace:

```bash

kubectl get certificates -n traefik --no-headers -o custom-columns=":metadata.name" | xargs -I {} kubectl describe certificates {} -n traefik

kubectl get certificaterequests -n traefik --no-headers -o custom-columns=":metadata.name" | xargs -I {} kubectl describe certificaterequests {} -n traefik

kubectl get order -n traefik --no-headers -o custom-columns=":metadata.name" | xargs -I {} kubectl describe order {} -n traefik

kubectl get challenges -n traefik --no-headers -o custom-columns=":metadata.name" | xargs -I {} kubectl describe challenges {} -n traefik
```
