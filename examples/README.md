Getting Started

Prerequisites:
```sh
- Have a running Kubernetes cluster 
- Have an installed operator lifecycle manager (‘OLM’)
- An installed Ocean CD operator. Use the following API: https://api.spotinst.io/ocean/cd/clusterInstaller?clusterId=CLUSTER_ID or create using the UI.
```
Steps towards your Canary deployment

**Note**: Here you will find all the relevant templates to get started with Ocean CD and apply a Canary Deployment strategy for a demo NGINX application.

1. Migrate your Deployment.yaml into a ‘SpotDeployment’ CRD by copying your deployment and change its ‘Kind’ to SpotDeployment (see ‘SpotDeployment.yaml). 

**Note**: Do not forget to update the namespace in which you plan to do the rollouts. 

2. Apply and create your SpotDeployment .Please note that your first apply will create the new SpotDeployment pods (can be tracked via the console UI, ‘Workloads’ page).
3. Create Canary and Stable services that will be used to expose your canary and stable pods with the respective traffic. 
4. Create Ocean CD entities that manage your SpotDeployment rollout logic: Strategy & RolloutSpec. See entities formats that can be used via API inside the entities folder.
Make sure to use your Spot API token for authorization. 
   
    API Routes: 

    https://api.spotinst.io/ocean/cd/rolloutSpec
    https://api.spotinst.io/ocean/cd/strategy
   
**Notes for RolloutSpec**:
Make sure to use the same namespace and Cluster ID to which your SpotDeployment is applied.

Make sure to use the canary and stable services you have defined 
(exception when using Istio with subsets, no need to mention the services).

RolloutSpec can include your traffic manager details. If you decide to make use of a traffic manager, Ocean CD supports many of them. See RolloutSpec examples with traffic manager templates inside the traffic manager folder.

5. Perform changes to your SpotDeployment containers spec and Apply.

**You are now all set to get working with Ocean CD!**
   
You can read more on Ocean CD architecture and functionality in our documentation:
https://docs.spot.io/ocean-cd/