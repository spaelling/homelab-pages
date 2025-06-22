# Grafana

```bash
helm repo add grafana https://grafana.github.io/helm-charts
helm repo update
kubectl apply -f certificate.yaml
kubectl apply -f grafana-oauth-secret.yaml
helm install grafana grafana/grafana --namespace lgtm -f grafana-values.yaml
```

Get your 'admin' user password by running:

```bash
kubectl get secret --namespace lgtm grafana -o jsonpath="{.data.admin-password}" | base64 --decode ; echo
```

We will need it to make other users admin.

And test the installation by running:

```bash
curl -kv https://grafana.local.spaelling.xyz/
```

## Upgrade

```bash
helm upgrade grafana grafana/grafana --namespace lgtm -f grafana-values.yaml
```

Sometimes the previous pods are not delete, and the new gets stuck in an error state. Just delete some pods and it should resolve itself.

# Authentik

Follow the instructions in the [authentik documentation](https://docs.goauthentik.io/integrations/services/grafana/) to set up Grafana. The helm values are already configured.
