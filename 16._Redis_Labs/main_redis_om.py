from redis_om import get_redis_connection, HashModel
from dotenv import load_dotenv
import os 

load_dotenv()

redis_connection = get_redis_connection(
    host=os.environ["REDIS_HOST"],
    port=os.environ["REDIS_PORT"],
    password=os.environ["REDIS_PASSWORD"],
    decode_responses=True
)

class Animal(HashModel):
    name: str
    weight: float

    class Meta:
        redis = redis_connection

dog = Animal(name='dog', weight=10.5)

print(dog.save())

primary_key = dog.pk
saved_dog = Animal.get(primary_key)

print(saved_dog)
