# Authentik

```bash
# Create a namespace and generate secrets
kubectl create namespace authentik
# could not get it to work with these secrets, so using the authentik-credentials.yaml file instead
# kubectl create secret generic authentik-secret-key --namespace authentik --from-literal=secret-key=$(openssl rand -base64 48)
# kubectl create secret generic authentik-postgresql-password --namespace authentik --from-literal=secret-key=$(openssl rand -base64 48)
# create certificate for authentik
kubectl apply -f authentik-certificate.yaml
# kubectl apply -n authentik -f authentik-secrets.yaml
helm repo add authentik https://charts.goauthentik.io
helm repo update
# Install authentik - authentik-credentials.yaml is found in password vault
helm upgrade --install authentik authentik/authentik --namespace=authentik -f authentik-values.yaml,authentik-credentials.yaml
```

First check the database is healthy:

```bash
kubectl describe pods -n authentik -l app.kubernetes.io/name=postgresql
```

Next, check the authentik server and worker pods:

```bash
kubectl describe pods -n authentik -l app.kubernetes.io/name=authentik,app.kubernetes.io/component=server
kubectl describe pods -n authentik -l app.kubernetes.io/name=authentik,app.kubernetes.io/component=worker
```

And finally, check the Redis pod:

```bash
kubectl describe pods -n authentik -l app.kubernetes.io/name=redis
```

Also check the certificate status, tls secret, and ingress configuration:

```bash
kubectl describe certificates authentik-tls -n authentik
kubectl get secret authentik-tls -n authentik -o yaml
kubectl get ingress -n authentik -o yaml
```

Can also try and restart the authentik server:

```bash
kubectl rollout restart deployment authentik-server -n authentik
```

If it looks good and pods are running we can check the service:

```bash
curl -kv https://authentik.local.spaelling.xyz/
```

If it says:

```text
* Server certificate:
*  subject: CN=TRAEFIK DEFAULT CERT
```

then the certificate is not in use. Likely an issue with Traefik. Check the Traefik dashboard if TLS is configured.

## First Login

Go to [https://authentik.local.spaelling.xyz/if/flow/initial-setup/](https://authentik.local.spaelling.xyz/if/flow/initial-setup/)

Create a new user and add it to the admins group.

Go to `settings` and under `MFA devices` register a passkey. Deactivate the `akadmin` user.

## Logs

```bash
kubectl logs -n authentik -l app.kubernetes.io/name=authentik,app.kubernetes.io/component=server --tail=-1 > authentik-server.log
kubectl logs -n authentik -l app.kubernetes.io/name=postgresql --tail=-1 > authentik-postgresql.log
```

## Uninstall

Persistent Volume Claims (PVCs) are not installed by `helm uninstall`, so you may need to delete them manually if you want to clean up completely:

```bash
helm uninstall authentik --namespace=authentik
kubectl get pvc -n authentik -o jsonpath="{.items[*].metadata.name}" | tr ' ' '\n' | xargs -I {} kubectl delete pvc {} -n authentik
```

```bash
kubectl delete secret authentik-secret-key --namespace authentik
kubectl delete secret authentik-postgresql-password --namespace authentik
```

## Certificates

We need both a certificate for the authentik service, but also for the outpost.