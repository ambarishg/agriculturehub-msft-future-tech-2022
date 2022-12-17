from azure.cosmos import CosmosClient as cosmos_client
from azure.cosmos import PartitionKey, exceptions

from . import kvutils

# <method_populate_container_items>
def populate_container_items(container_obj, item_to_create):
    # Add items to the container
    inserted_item =  container_obj.create_item(body=item_to_create)
    # </create_item>
# </method_populate_container_items>

# <create_database_if_not_exists>
def get_or_create_db(client, database_name):
    try:
        database_obj  = client.get_database_client(database_name)
        return database_obj
    except exceptions.CosmosResourceNotFoundError:
        print("Creating database")
        return client.create_database(database_name)
# </create_database_if_not_exists>
    
# Create a container
# Using a good partition key improves the performance of database operations.
# <create_container_if_not_exists>
def get_or_create_container(database_obj, container_name):
    try:        
        todo_items_container = database_obj.get_container_client(container_name)
        return todo_items_container
    except exceptions.CosmosResourceNotFoundError:
        print("Creating container with lastName as partition key")
        return database_obj.create_container(
            id=container_name,
            partition_key=PartitionKey(path="/category"),
            offer_throughput=400)
    except exceptions.CosmosHttpResponseError:
        raise
# </create_container_if_not_exists>

def create_item(item_to_create):
    # <add_uri_and_key>
    endpoint = kvutils.cosmosdb_endpoint 
    key = kvutils.cosmosdb_key 
    # </add_uri_and_key>

    # <define_database_and_container_name>
    database_name = kvutils.cosmosdb_database_name 
    container_name = kvutils.cosmosdb_container_name 
    # </define_database_and_container_name>
    client = cosmos_client(endpoint, credential = key) 

    database_obj = get_or_create_db(client, database_name)
    # create a container
    container_obj = get_or_create_container(database_obj, container_name)
        
    # populate the family items in container
    populate_container_items(container_obj, item_to_create)  
        
def get_all_items():
    # <add_uri_and_key>
    endpoint = kvutils.cosmosdb_endpoint 
    key = kvutils.cosmosdb_key 
    # </add_uri_and_key>

    # <define_database_and_container_name>
    database_name = kvutils.cosmosdb_database_name 
    container_name = kvutils.cosmosdb_container_name 
    # </define_database_and_container_name>
    client = cosmos_client(endpoint, credential = key) 

    database_obj = get_or_create_db(client, database_name)
    # create a container
    container_obj = get_or_create_container(database_obj, container_name)

    allitems = []
    for item in container_obj.query_items(
    query="SELECT * FROM c WHERE c.category = 'cassava' ORDER BY c._ts DESC",
    enable_cross_partition_query=True):
        allitems.append(item)
    
    return(allitems)

def get_items(qry):
    # <add_uri_and_key>
    endpoint = kvutils.cosmosdb_endpoint 
    key = kvutils.cosmosdb_key 
    # </add_uri_and_key>

    # <define_database_and_container_name>
    database_name = kvutils.cosmosdb_database_name 
    container_name = kvutils.cosmosdb_container_name 
    # </define_database_and_container_name>
    client = cosmos_client(endpoint, credential = key) 

    database_obj = get_or_create_db(client, database_name)
    # create a container
    container_obj = get_or_create_container(database_obj, container_name)
     
    querystring = "SELECT * FROM c WHERE  c.category = 'cassava' AND c.filename LIKE '%" +  qry + "%'"
        
    allitems = []
    for item in container_obj.query_items(
    query=querystring,enable_cross_partition_query=True):
        allitems.append(item)
    
    return(allitems)
            