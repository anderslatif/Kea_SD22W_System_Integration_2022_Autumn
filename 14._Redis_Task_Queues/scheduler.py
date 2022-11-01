from redis import Redis
from rq import Queue
from scheduler_util import perform_task
import random

queue = Queue(name="mainqueue", connection=Redis())


for _ in range(20):
    sleep_time = random.randint(1, 5)
    queue.enqueue(perform_task, sleep_time)

# Additional cool options:
""" 
job = queue.enqueue(perform_task, retry=Retry(max=3, interval=[10, 30, 60]))
job = queue.enqueue_in(timedelta(seconds=1), perform_task)
job = queue.enqueue_at(datetime(2019, 10, 8, 9, 15), perform_task)
"""
