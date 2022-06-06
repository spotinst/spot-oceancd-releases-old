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

After installing the Ocean CD Operator in your cluster, you will create the following Ocean CD entities:
- SpotDeployment
- Strategy
- RolloutSpec


## Quick Start

You may make use of the examples section to efficiently get started with OceanCD.
Such examples will accompany you through a simplified and quick Canary Deployment. 

Should you wish me to make use of specific traffic manager, we invite you to take a look at the ones we support and the way it should be used. 
