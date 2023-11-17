#!/usr/bin/env python3
#
# Testing test_queue_Queue ...
# 1000000 2.2275411180016818
# Testing test_queue_deque1 ...
# 1000000 0.11330108199763345
# Testing test_queue_deque2 ...
# 1000000 0.11317988100199727

try:
    from Queue import Queue
except ImportError:   # Python 3
    from queue import Queue

import timeit
import collections

N = 1000

def test_queue_Queue(n):
    queue = Queue()
    for i in range(n):
        queue.put(i)
    while not queue.empty():
        queue.get()

def test_queue_deque1(n):
    queue = collections.deque()
    for i in range(n):
        queue.append(i)
    while len(queue) > 0:
        queue.popleft()

def test_queue_deque2(n):
    queue = collections.deque()
    for i in range(n):
        queue.appendleft(i)
    while len(queue) > 0:
        queue.pop()

print ("Testing test_queue_Queue ..." )
t1 = timeit.Timer(lambda: test_queue_Queue(N))
print ( "{} {}".format(N, t1.timeit(1)) )   # single run

print ("Testing test_queue_deque1 ..." )
t1 = timeit.Timer(lambda: test_queue_deque1(N))
print ( "{} {}".format(N, t1.timeit(1)) )   # single run

print ("Testing test_queue_deque2 ..." )
t1 = timeit.Timer(lambda: test_queue_deque2(N))
print ( "{} {}".format(N, t1.timeit(1)) )   # single run

# EOF
