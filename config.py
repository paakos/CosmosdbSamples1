import os

settings = {
    'host': os.environ.get('ACCOUNT_HOST', 'https://paakoscosmosdb.documents.azure.com:443/'),
    'master_key': os.environ.get('ACCOUNT_KEY', 'MCWIri1ucikvEGMPQ4UVTCZtB4YxeKeGuSIUQN7YP6pGczoQ6Bon05fvIeR7K23HIQB5SOxotwSiACDbIljAPA=='),
    'database_id': os.environ.get('COSMOS_DATABASE', 'FarmerStatistics'),
    'container_id': os.environ.get('COSMOS_CONTAINER', 'Protest'),
}