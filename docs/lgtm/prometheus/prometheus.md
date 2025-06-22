# prometheus

[prometheus-community](https://github.com/prometheus-community/helm-charts/blob/main/charts/kube-prometheus-stack/README.md)

```bash
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update
helm install prometheus prometheus-community/kube-prometheus-stack --values prometheus-values.yaml -n lgtm

kubectl --namespace lgtm get pods -l "release=prometheus"
```

Server url for the Grafana connection is: `http://prometheus-kube-prometheus-prometheus.lgtm.svc.cluster.local:9090`
