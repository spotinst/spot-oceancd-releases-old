## Installation

1. Install OLM

```sh
curl -sL https://github.com/operator-framework/operator-lifecycle-manager/releases/download/v0.20.0/install.sh | bash -s v0.20.0
```

2. Add the OceanCD Helm chart repository:

```sh
helm repo add oceancd https://charts.oceancd.io
```

3. Update your local Helm chart repository cache:

```sh
helm repo update
```

4. Install `spot-oceancd-operator`:

```sh
helm install my-release oceancd/spot-oceancd-operator \
  --set token=REDACTED \
  --set clusterId=REDACTED \
  # [...]
```

> NOTE: Please configure all required chart values using the `set` command line argument or a `values.yaml` file.


5. Uninstall `spot-oceancd-operator`:

```sh
helm uninstall my-release 
kubectl get csv -A | grep spot-oceancd-operator | awk '{system("kubectl delete csv " $2 " -n " $1)}'
kubectl delete apiservices v1.packages.operators.coreos.com
kubectl delete -f https://github.com/operator-framework/operator-lifecycle-manager/releases/download/v0.20.0/crds.yaml
kubectl delete -f https://github.com/operator-framework/operator-lifecycle-manager/releases/download/v0.20.0/olm.yaml
```

## Values


![Version: 1.0.0](https://img.shields.io/badge/Version-1.0.0-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square) ![AppVersion: 1.0.0](https://img.shields.io/badge/AppVersion-1.0.0-informational?style=flat-square)

A Helm chart for spot-oceancd-operator

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| affinity | object | `{}` | (Optional) Node affinity |
| apiUrl | string | `"https://api.spotinst.io"` | (Optional) Spot Api URL |
| channel | string | `"stable"` | (Optional) Operator Catalog channel |
| clusterId | string | `""` | (Required) Cluster ID |
| nodeSelector | object | `{}` | (Optional) Node selector |
| podAnnotations | object | `{}` | (Optional) Pod annotations |
| resources | object | `{"limits":{"cpu":"500m","memory":"128Mi"}}` | (Optional) Resource requests and limits |
| saasUrl | string | `"https://operator.oceancd.io"` | (Optional) Saas URL |
| token | string | `""` | (Required) Spot Token |
| tolerations | list | `[]` | (Optional) Tolerations for nodes that have taints on them |

----------------------------------------------
Autogenerated from chart metadata using [helm-docs v1.7.0](https://github.com/norwoodj/helm-docs/releases/v1.7.0)