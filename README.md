# Spot OceanCD

Ocean CD makes Kubernetes an afterthought for application teams. Commit code and Ocean CD takes care of operations, automation and monitoring to ensure SLOs and production health.

https://spot.io/products/ocean-cd

## Table of Contents

- [Installation](#installation)
- [Getting Started](#getting-started)
- [Documentation](#documentation)
- [Getting Help](#getting-help)
- [Community](#community)

## Installation


## Getting Started

```console
chmod +x oceancdGetStarted.py

python3 oceancdGetStarted.py -h
usage: oceancdGetStarted [-h] -t TOKEN -e ENVIRONMENT_NAME -c CLUSTER_ID -m
                         MICROSERVICE_NAME -l [LABELS [LABELS ...]]
                         [-n NOTIFICATION_PROVIDER] [-w WEBHOOK]

oceancdGetStarted

optional arguments:
  -h, --help            show this help message and exit
  -t TOKEN, --token TOKEN
                        Api token to spot api
  -e ENVIRONMENT_NAME, --environment_name ENVIRONMENT_NAME
                        Environment name
  -c CLUSTER_ID, --cluster_id CLUSTER_ID
                        Cluster id for environment
  -m MICROSERVICE_NAME, --microservice_name MICROSERVICE_NAME
                        Microservice name
  -l [LABELS [LABELS ...]], --labels [LABELS [LABELS ...]]
                        Set of k8s labels that are exisitng on the wanted
                        workload
  -n NOTIFICATION_PROVIDER, --notification_provider NOTIFICATION_PROVIDER
                        The name identifier of the Ocean CD notification
                        provider
  -w WEBHOOK, --webhook WEBHOOK
                        Webhook url

 example:
    ./oceancd_baker.py -t 1234 -e test-environment -c test-cluster -m test-microservice -l app=test -n test-notification -w https://webhook.site
```

## Documentation

If you're new to Spot and want to get started, please checkout our [Getting Started](https://help.spot.io/getting-started-with-spotinst/) guide, available on the [Spot Documentation](https://help.spot.io/) website.


## Getting Help

We use GitHub issues for tracking bugs and feature requests. Please use these community resources for getting help:

- Ask a question on [Stack Overflow](https://stackoverflow.com/).
- Join our Spot community on [Slack](http://slack.spot.io/).
- Open an [issue](https://github.com/spotinst/spot-oceancd-releases/issues/new/choose/).

## Community

- [Slack](http://slack.spot.io/)
- [Twitter](https://twitter.com/spot_hq/)
