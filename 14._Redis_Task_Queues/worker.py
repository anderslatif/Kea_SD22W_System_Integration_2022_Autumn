from redis import Redis
from rq import Worker, Queue

redis = Redis()

queue = Queue(name="mainqueue", connection=redis)
worker = Worker(queues=[queue], connection=redis)

worker.work()
