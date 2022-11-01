from redis import Redis
from rq import Queue
from scheduler_util import perform_task

queue = Queue(name="mainqueue", connection=Redis())





for _ in range(20):
    queue.enqueue(perform_task)
