import os 
from azure.identity import ManagedIdentityCredential
from azure.keyvault.secrets import SecretClient


keyVaultName = os.environ["kvname"] #""
KVUri = f"https://{keyVaultName}.vault.azure.net"


credential = ManagedIdentityCredential()
client = SecretClient(vault_url=KVUri, credential=credential)

account_url = client.get_secret("accounturl").value 
container_name = client.get_secret("containername").value 
ENDPOINT = client.get_secret("endpoint").value
prediction_key = client.get_secret("predictionkey").value
prediction_resource_id = "paddy"
project_id = client.get_secret("projectid").value
publish_iteration_name = client.get_secret("publishiterationname").value

# <add_uri_and_key>
cosmosdb_endpoint = client.get_secret("cosmosdbendpoint").value 
cosmosdb_key = client.get_secret("cosmosdbkey").value 
# </add_uri_and_key>


# <define_database_and_container_name>
cosmosdb_database_name = 'predictions'
cosmosdb_container_name = 'predictions'
