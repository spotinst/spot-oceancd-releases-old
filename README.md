# Spot Ocean CD 

Ocean CD focuses on the most painful aspects of modern application delivery, giving developers the freedom to push code with confidence while DevOps easily maintain governance and SLOs.

Ocean CD provides DevOps and Infrastructure teams with out of the box processes to reimplement and share complex and mission critical pieces of CD across different environments, such as progressive delivery and verification of the software deployments. Service owners are able to promote service changes to production without code or re-inventing deployment strategies. Developers are able to commit with confidence, now that the deployment phases are managed and visible.

https://docs.spot.io/ocean-cd/

## Table of Contents

- [Installation](#installation)
- [Quick Start](#quick-start)

## Installation

Prerequisites:
- Kubernetes cluster up and running ( Azure,GCP,AWS)
- Workstation with the Kubernetes cluster context and kubectl installed
- Have an installed operator lifecycle manager (‘OLM’)
- [A Spot API token](https://docs.spot.io/administration/api/create-api-token)

**Note: Please contact Ocean CD team to get a private preview access, for installing Ocean CD controller and for full documentation.**

After installing the Ocean CD Operator in your cluster, you will set up three basic types of entities:

- A SpotDeployment CRD: Ocean CD replacement of a Deployment Resource
- A Strategy: An entity including a definition of phases that manage the way your workload changes are being exposed in the desired cluster and namespace
- A RolloutSpec: An entity including the CD process description for the selected workload

## Quick Start

To easily get started with OceanCD, you may make use of the 'examples' section found above. 
Through such files, you will find a series of examples which will accompany you through the process of a simplified and quick Canary Deployment. 


Should you wish me to make use of specific traffic manager, we invite you to take a look at the ones we support and the way it should be used. 
