# Spot Ocean CD 



Ocean CD focuses on the most painful aspects of modern application delivery, giving developers the freedom to push code with confidence while DevOps easily maintain governance and SLOs.

Ocean CD provides DevOps and Infrastructure teams with out of the box processes to reimplement and share complex and mission critical pieces of CD across different environments, such as progressive delivery and verification of the software deployments. Service owners are able to promote service changes to production without code or re-inventing deployment strategies. Developers are able to commit with confidence, now that the deployment phases are managed and visible.

https://docs.spot.io/ocean-cd/

## Table of Contents

- [Operator Installation](#Operator-installation)
- [Quick Start](#quick-start)

## Operator Installation

Prerequisites:
- Kubernetes cluster up and running (Azure,GCP,AWS)
- Workstation with the Kubernetes cluster context and kubectl installed
- Have an installed operator lifecycle manager (‘OLM’)
- [A Spot API token](https://docs.spot.io/administration/api/create-api-token)

The Ocean CD Operator detects every applied SpotDeployment, monitors all of your resources, and manages rollouts based on the SaaS logic. Whenever the SpotDeployment is applied, the SaaS will trigger a rollout. 

You may install your operator via API, UI or HELM.

No matter which method you will choose, during the installation, you will be required to update whether your cluster has an already installed Argo Rollout installation.
Indeed Ocean CD recognizes the advantages of Argo rollouts as an engine for CD strategies and uses it accordingly to manage and enable it as a scalable CD product. 


**Helm Option** : We invite you to reach to the "charts/spot-oceancd-operator" directory, and follow the tutorial provided. 

**API & UI Options**: We invite you to reach out to [our documentation](https://docs.spot.io/ocean-cd/getting-started/install-operator-using-API-or-helm) for further details on the process and the commands.


## Quick Start

After installing the Ocean CD Operator in your cluster, you will set up three basic types of entities:

- Create a SpotDeployment CRD  - Ocean CD replacement of a Deployment Resource
- Define Strategy - An entity including a definition of phases that manage
the way your workload changes are being exposed in the desired
cluster and namespace
- Define RolloutSpec - An entity including the CD strategy and traffic definitions 
for the selected SpotDeployment.
  
### Note

Any **first** Apply to your SpotDeployments will not trigger a rollout. Only the creation of the pods will be accomplished.
To trigger a rollout with the entities of your choice, you will need to apply any additional change to the SpotDeployment in question. 

  
**To easily get started with OceanCD, you may make use of the 'Quick Start & Examples' section found above.**
Through such files, you will find a series of examples which will accompany you through the process of a simplified and quick Canary Deployment. 



