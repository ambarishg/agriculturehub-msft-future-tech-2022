# Paddy Disease Detection         

## Problem Statement



    
The images are in the `docs\images\ContainerApp\` folder     

|  FileName  |  Description |
|---|---|
| Predict.png  |    Prediction UI - Cassava Application          |     
| PredictionResult.png  |    Prediction Result - Cassava Application          |     
| AllPredictions.png  |    All Predictions - Cassava Application          |     
| FilterPredictions.png  |    Search Predictions by Filename - Cassava Application          |    
 

### Deployment Instructions [ Steps ]     
1.  Create the Custom Vision AI project for training the Cassava Leaf images            
2.  Steps for building the Docker Image [ `docs/01-DockerSteps.md` ]   
3.  Steps for deploying the image as a Container App in Azure [ `docs/2-AzureContainerAppsSteps.md` ]  
4.  Turn the Managed identity [System Assigned] for the deployed Container App[ `docs\images\ContainerApp\SystemIdentitySetting.png` ]        
5.  Create the Storage Account and the Container   [ `docs\images\StorageAccount\StorageAccount.png`]       
6.  Create the CosmosDB account , database and container. The partition of the container is **category** [`Section : Images of the Cosmos DB`]               
7. Assign Storage Data Blob Contributor Role to the Container App  for the Storage Account so that the Container App can read,write and delete the images in the Storage Account [ `docs\images\ContainerApp\StorageBlobDataContributorRole.png` ]                           
8. Assign Access Policies for the Container App so that the Container App can acess the secrets in the KeyVault[ `docs\images\ContainerApp\KeyVaultAccess.png` ]                          
9. Create the secrets in the KeyVault[ `docs\images\KeyVault\KVSecrets.png`]     
10. Configure Continuous Deployment for the Container App[ `docs\images\KeyVault\KVSecrets.png`]      


### Files     


|  FileName  |  Description |
|---|---|
| Dockerfile |   Docker file for the Container Image        |       
| requirements.txt |   Has the dependencies required for the Container Image        |        
|  app.py | Has the code for running the Flask app |    
| flaskr / cosmosdbwithoutasync.py |   Has the code for connecting the Container App with **CosmosDB**        |        
|  flaskr / kvutils.py | Has the code for reading the secrets from the **KeyVault** by the Container App   |          
|  flaskr / predictions.py | Has the code for getting the **predictions** for the Cassava Leaf by the Container App   |      
|  flaskr / __init__.py | Has the code for initialization for the **Flask** App |      
|  flaskr / templates folder | Folder containing the Views of the Container App   |        
|  flaskr / static folder | Folder containing the CSS file   |     


          




