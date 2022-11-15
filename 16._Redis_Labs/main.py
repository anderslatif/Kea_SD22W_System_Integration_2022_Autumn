from redis import Redis
from dotenv import load_dotenv
import os 

load_dotenv()

redis_connection = Redis(
    host=os.environ["REDIS_HOST"],
    port=os.environ["REDIS_PORT"],
    password=os.environ["REDIS_PASSWORD"],
    decode_responses=True
)

# redis_connection.set('test_key', 'test_value')

print(redis_connection.get('test_key'))
