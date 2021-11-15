# Spot Ocean CD (private preview)

Ocean CD makes Kubernetes an afterthought for application teams. Commit code and Ocean CD takes care of operations, automation and monitoring to ensure SLOs and production health.

https://spot.io/products/ocean-cd

## Table of Contents

- [Installation](#installation)
- [Quick Start](#quick-start)

## Installation

Prerequisites:
- Kubernetes cluster up and running
- Workstation with the Kubernetes cluster context and kubectl installed
- [A Spot API token](https://docs.spot.io/administration/api/create-api-token)

**Note: Please contact Ocean CD team to get a private preview access, for installing Ocean CD controller and for full documentation.**

After installing the Ocean CD controller in your cluster, you will create the following Ocean CD entities:
- Environment
- Microservice
- Notification Provider
- Rollout Spec

## Quick Start

For quick start you can use [oceancd_baker](oceancd_baker.py) script to create a basic configuration. (That you can easily modified later via API)

Use any 'Example' deployment YAML (which is installed in your connected cluster) to get a quick overview of Ocean CD capabilities.

Run the following commands on your local machine:
- wget https://raw.githubusercontent.com/spotinst/spot-oceancd-releases/main/oceancd_baker.py
- pip3 install requests (if not already installed)
- chmod +x oceancd_baker.py

```console
chmod +x oceancd_baker.py

./oceancd_baker.py -h
usage: oceancd_baker [-h] -t TOKEN -e ENVIRONMENT_NAME -c CLUSTER_ID -m MICROSERVICE_NAME -l [LABELS [LABELS ...]] [-n NOTIFICATION_PROVIDER] [-w WEBHOOK]

oceancd_baker

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
                        Set of k8s labels that are exisitng on the wanted workload
  -n NOTIFICATION_PROVIDER, --notification_provider NOTIFICATION_PROVIDER
                        The name identifier of the Ocean CD notification provider
  -w WEBHOOK, --webhook WEBHOOK
                        Webhook url

 example:
    ./oceancd_baker.py -t 1234 -e test-environment -c test-cluster -m test-microservice -l app=test -n test-notification -w https://webhook.site
```

Expected outcome:
- Confirmation has been received, Ocean CD entities has been created.
- You can now run your 'Example' deployment (make sure to do some changes in the spec template to demonstrate the update), and see Ocean CD in action!

You can use the getting started script to create more rollout objects,
or go to Spot API documentation and use your favorite API tool.
