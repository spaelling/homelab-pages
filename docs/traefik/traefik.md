# Traefik

Add Traefik Labs chart repository to Helm and install it with the Helm command line. All traefik helm chart values can be found [here](https://github.com/traefik/traefik-helm-chart/blob/master/traefik/values.yaml)

```bash
helm repo add traefik https://traefik.github.io/charts
helm repo update
kubectl create ns traefik
helm install --namespace=traefik --values=./traefik-values.yml traefik traefik/traefik
kubectl get pods --namespace traefik
```

Get pods in the Traefik namespace and describe them to check their status:

```bash
kubectl get pods -n traefik --no-headers -o custom-columns=":metadata.name" | xargs -I {} kubectl describe pod {} -n traefik
```

We can upgrade a helm release with the following command (if ex. changing values in the `traefik-values.yml` file):

```bash
helm upgrade --namespace=traefik --values=./traefik-values.yml traefik traefik/traefik
```

Create a ConfigMap for the Traefik Cloud Provider:

```bash
kubectl create configmap -n kube-system kubevip --from-literal cidr-traefik=192.168.1.20/32
```

This allows kubevip to assign an external IP address to the Traefik service.

## Troubleshooting

Check the status of the Traefik IngressRoute and secrets:

```bash
kubectl describe ingressroute traefik-dashboard -n traefik
kubectl describe secrets traefik-dashboard-tls -n traefik
```

Check the logs of the Traefik pods to see if there are any errors:

```bash
kubectl logs -n traefik -l app.kubernetes.io/name=traefik > traefik.log
```

## Authentik

Setup authentication forwarding to the authentik service.

```bash
kubectl apply -f authentik-middleware.yaml
```
