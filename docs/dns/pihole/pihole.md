https://github.com/MoJo2600/pihole-kubernetes/tree/main/classic

Apply the ConfigMap for the Traefik Cloud Provider (`kubevip-configmap.yaml` is in the `k3s/kubevip` directory):

```bash
kubectl apply -f kubevip-configmap.yaml
kubectl apply -f pihole.yaml
kubectl create secret -n pihole generic pihole-webpassword --from-literal="password=$(openssl rand -base64 64)"
```

It has a dedicated IP for the Pihole namespace, `192.168.1.21`.

When pods are running test `tcping -f 4 -t 5 192.168.1.21 53` and `nslookup google.com 192.168.1.21`

## TODO

- Expose API
- Deploy Nebula sync
  - sync with main pihole instance
- Access to web ui via authentik
