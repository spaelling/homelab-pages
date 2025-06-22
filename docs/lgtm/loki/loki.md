# Loki

```bash
helm repo add grafana https://grafana.github.io/helm-charts
helm repo update
helm install loki grafana/loki -f loki-values.yaml -n lgtm
kubectl get pods -n lgtm
```

## Upgrade Loki

```bash
helm upgrade loki grafana/loki --values loki-values.yaml -n lgtm
```

You can send logs from inside the cluster using the cluster DNS:

http://loki-gateway.lgtm.svc.cluster.local/loki/api/v1/push

If Grafana operates within the cluster, you'll set up a new Loki datasource by utilizing the following URL:

http://loki-gateway.lgtm.svc.cluster.local/

## Kubernetes Monitoring

https://grafana.com/docs/loki/latest/send-data/k8s-monitoring-helm/

```bash
helm install k3smon grafana/k8s-monitoring --values k3s-monitoring-values.yml -n lgtm
```

https://github.com/grafana/alloy/blob/main/operations/helm/charts/alloy/values.yaml

Check logs to validate that it is sending logs to Loki

```bash
helm upgrade k3smon grafana/k8s-monitoring --values k3s-monitoring-values.yml -n lgtm
```
