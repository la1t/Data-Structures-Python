from .queue import Queue


def round_queue(queue, n):
    if n < 0:
        raise ValueError('Items num must be positive')

    if queue.size() == 0:
        return
        
    for _ in range(n):
        queue.enqueue(queue.dequeue())
