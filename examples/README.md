Getting Started - 

Here you will find all of the relevant templates to get started with OceanCD and apply a Canary Deployment. 

Prerequisite: 
```sh
1. Have a running Kubernetes cluster (Amazon/Azure/Google)
2. Have a running and fully installed operator
```

Steps towards your Canary deployment:

1. Create and apply your SpotDeployment
   
    Do not forget to change accordingly the namespace. It will be found relevant for the rest of the procedure. 
    
    Please note that your first apply will not create a Canary Deployment. 
   

2. Create and Apply your entities : Strategy & RolloutSpec

    Please note that if you decide to make use of a traffic manager OceanCD supports many of them which can be found in the traffic manager
   
3. Apply changes to your SpotDeployment and Apply


You are now all set to get working with OceanCD. 
   