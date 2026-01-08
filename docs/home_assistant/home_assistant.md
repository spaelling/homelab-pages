# Home Assistant

```bash
kubectl create namespace home-assistant
kubectl apply -f home_assistant.yaml
```

If `configmap` is updated then update the deployment

```bash
kubectl rollout restart deployment home-assistant -n home-assistant
kubectl rollout status  deployment home-assistant -n home-assistant
```

If this hangs we can force it by scaling down to 0 and back up again

```bash
kubectl -n home-assistant scale deploy/home-assistant --replicas=0
kubectl -n home-assistant get pods

kubectl -n home-assistant delete rs -l app=home-assistant

kubectl -n home-assistant scale deploy/home-assistant --replicas=1
kubectl -n home-assistant rollout status deploy/home-assistant
```

TODO. implement with kustomize

```yaml
spec:
  template:
    metadata:
      annotations:
        # Update this value when the ConfigMap changes.
        configmap.home-assistant.checksum: "{{ .Values or kustomize var with sha256 of the ConfigMap }}"
```

## Troubleshooting

Check the status of the certificate in the `traefik` namespace:

```bash
kubectl get certificates -n home-assistant --no-headers -o custom-columns=":metadata.name" | xargs -I {} kubectl describe certificates {} -n home-assistant

kubectl get certificaterequests -n home-assistant --no-headers -o custom-columns=":metadata.name" | xargs -I {} kubectl describe certificaterequests {} -n home-assistant

kubectl get order -n home-assistant --no-headers -o custom-columns=":metadata.name" | xargs -I {} kubectl describe order {} -n home-assistant

kubectl get challenges -n home-assistant --no-headers -o custom-columns=":metadata.name" | xargs -I {} kubectl describe challenges {} -n home-assistant
```

```bash
kubectl exec -n home-assistant -it deploy/home-assistant -- sh
```

## Matter Server

```bash
kubectl apply -f matter_server.yaml
```

```bash
kubectl logs -f deployment/matter-server -n home-assistant
```

Look for these entries in the log:

```text
INFO [matter_server.server.server] Starting the Matter Server...
INFO [matter_server.server.helpers.paa_certificates] Fetching the latest PAA root certificates...
INFO [matter_server.server.server] Matter Server successfully initialized.
```

Just like with Home Assistant updates may get stuck on old replicas.

```bash
kubectl -n home-assistant scale deploy/matter-server --replicas=0
kubectl -n home-assistant get pods

kubectl -n home-assistant delete rs -l app=matter-server

kubectl -n home-assistant scale deploy/matter-server --replicas=1
kubectl -n home-assistant rollout status deploy/matter-server
```

### Testing Matter Server Connectivity

```bash
kubectl get pod -n home-assistant -l app=matter-server -o jsonpath='{.items[0].status.hostIP}'
tcping -f 4 -t 5 192.168.1.12 5580
```
