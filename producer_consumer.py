"""
Producer - Consumer (pub-sub) example
"""

import threading
from queue import Queue
from time import sleep


def producer(q, n):
    """Generates fibonacci number and put it in queue."""
    a, b = 0, 1
    while a <= n:
        q.put(a)
        print(f"Producer: {a}")
        sleep(0.25)
        a, b = b, a + b
    q.put(None)


def consumer(q):
    """Consumer, reads data from the queue."""
    while True:
        num = q.get()
        print(f"\nConsumer: {num}")
        sleep(0.4)
        q.task_done()
        if num is None:
            break


def main():
    q = Queue()
    threads = []
    threads.append(threading.Thread(target=producer, args=(q, 1000)))
    threads.append(threading.Thread(target=consumer, args=(q,)))
    for t in threads:
        t.start()

    for t in threads:
        t.join()


if __name__ == "__main__":
    main()
    print("DONE!!!")
