# Cassava Leaf Disease Detection         

## Problem Statement
We would implement a Cassava Leaf Disease detection system.
Cassava is a rich, affordable source of carbohydrates. It can provide more calories per acre of the crop than cereal grain crops, which makes it a very useful crop in developing nations.          
              

As the 2nd largest provider of carbohydrates in Africa, cassava is a key food security crop grown by small-holder farmers because it can withstand harsh conditions. At least 80% of small-holder farmer households in Sub-Saharan Africa grow cassava and viral diseases are major sources of poor yields.              
             

We have taken 105 images for 4 leaf disease categories and a healthy category. Therefore, we have 5 categories of leaves.            
The Cassava Leaf Disease detection system would help the farmers to detect the disease correctly and take preventive measures for the same.       

## Images of the **Cassava Disease Detection Application** 
    
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


## Images of the **Azure Container App**          
The images are in the `docs\images\ContainerApp\` folder     

| Category |  FileName  |  Description |
|---|---|---|
| Managed Identity | SystemIdentitySetting.png |    Images of the System identity configuration of the Container App which is turned ON            |   
| Storage account Access | StorageBlobDataContributorRole.png |     Images of the Storage Account  - Storage Data Blob Contributor Role             |       
| KeyVault Access | KeyVaultAccess.png |    Key Vault - Access Polices to acess the Key Vault Secrets             |      
| RevisionManagement - Container App | RevisionManagement.png  |    Revision Management Settings   - Container App         |     
| Scale - Container App | Scale.png  |    Scale Settings   - Container App         |   
| Secrets - Container App | Secrets.png  |    Secrets Settings   - Container App. The KeyVault Name is stored as a Secret         |   
| Continuous Deployment - Container App | CD.png  |    Continuous Deployment Settings   - Container App.          |   
           

### Images of the Key Vault Secrets  
| Category |  FileName  |  Description |
|---|---|---|
| Key Vault Secrets  | docs\images\KeyVault\KVSecrets.png |    Images of the Key Vault Secrets            |        

### Images of the Storage Account    
| Category |  FileName  |  Description |
|---|---|---|
| Storage Account | docs\images\StorageAccount\StorageAccount.png |    Images of the Storage Account            |        

### Images of the Cosmos DB    
| Category |  FileName  |  Description |
|---|---|---|
| Database and Container | docs\images\CosmosDB\cosmos-db-container.png |    Images of  Database and Container of Cosmos DB            |        
| Partition | cosmos-db-container.png |    Images of  Cosmos DB container           |        


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


          




