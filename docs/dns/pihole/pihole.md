https://github.com/MoJo2600/pihole-kubernetes/tree/main/classic

Apply the ConfigMap for the Traefik Cloud Provider (`kubevip-configmap.yaml` is in the `k3s/kubevip` directory):

```bash
kubectl apply -f kubevip-configmap.yaml
kubectl create namespace pihole # causes a warning when running kubectl apply later
kubectl create secret -n pihole generic pihole-webpassword --from-literal="password=$(openssl rand -base64 64)"
kubectl apply -f pihole.yaml
```

It has a dedicated IP for the Pihole namespace, `192.168.1.21`.

When pods are running test `tcping -f 4 -t 5 192.168.1.21 53` and `nslookup google.com 192.168.1.21`

Check logs (for specific instance of the statefulset):

```bash
kubectl logs pihole-0 -n pihole
# stream logs
kubectl logs -f pihole-0 -n pihole
# see logs for ALL replicas at once
kubectl logs -l app=pihole -n pihole --all-containers
# check DNS query logs
kubectl exec -it pihole-0 -n pihole -- tail -f /var/log/pihole/pihole.log
```

When making changes check the statefulset status:

```bash
kubectl rollout status statefulset pihole -n pihole
```

## Pihole 0

```bash
kubectl apply -f pihole-0-ingress.yaml
```

## TODO

- Expose API
- Deploy Nebula sync
  - sync with main pihole instance
- Access to web ui via authentik
