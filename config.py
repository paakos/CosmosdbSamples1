import os

settings = {
    'host': os.environ.get('ACCOUNT_HOST', 'https://paakoscosmosdb.documents.azure.com:443/'),
    'master_key': os.environ.get('ACCOUNT_KEY', 'fakekeylsdfkñsldkfñlskdf=='),
    'database_id': os.environ.get('COSMOS_DATABASE', 'FarmerStatistics'),
    'container_id': os.environ.get('COSMOS_CONTAINER', 'Protest'),
}
