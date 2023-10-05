# Redis client library for Python
import redis
from redis.commands.search.indexDefinition import (
    IndexDefinition,
    IndexType
)
from redis.commands.search.query import Query
from redis.commands.search.field import (
    TextField,
    VectorField
)

# Constants
REDIS_HOST =  "localhost"
REDIS_PORT = 6379
REDIS_PASSWORD = "" # default for passwordless Redis

# Ignore unclosed SSL socket warnings - optional in case you get these errors
import warnings
warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)
warnings.filterwarnings("ignore", category=DeprecationWarning) 

def connect():
    # Connect to Redis
    redis_client = redis.Redis(
        host=REDIS_HOST,
        port=REDIS_PORT,
        password=REDIS_PASSWORD
    )
    if redis_client.ping():
        print('Successfully connected to Redis')
        return redis_client
    else:
        raise('Unable to connect to Redis')
