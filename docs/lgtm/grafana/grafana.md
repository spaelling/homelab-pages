# Grafana

```bash
helm repo add grafana https://grafana.github.io/helm-charts
helm repo update
kubectl apply -f certificate.yaml
helm install grafana grafana/grafana --namespace lgtm -f grafana-values.yaml
```

Get your 'admin' user password by running:

```bash
kubectl get secret --namespace lgtm grafana -o jsonpath="{.data.admin-password}" | base64 --decode ; echo
```

And test the installation by running:

```bash
curl -kv https://grafana.local.spaelling.xyz/
```

# Upgrade

```bash
helm upgrade grafana grafana/grafana --namespace lgtm -f grafana-values.yaml
```
