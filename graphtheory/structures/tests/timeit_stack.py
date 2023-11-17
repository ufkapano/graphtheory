#!/usr/bin/env python3
#
# Testing test_stack_LifoQueue ...
# 1000000 2.437962128999061
# Testing test_stack_list ...
# 1000000 0.138347371997952
# Testing test_stack_deque1 ...
# 1000000 0.1228583490010351
# Testing test_stack_deque2 ...
# 1000000 0.12487589500233298

try:
    from Queue import LifoQueue
except ImportError:   # Python 3
    from queue import LifoQueue

import timeit
import collections

N = 1000

def test_stack_LifoQueue(n):
    queue = LifoQueue()
    for i in range(n):
        queue.put(i)
    while not queue.empty():
        queue.get()

def test_stack_list(n):
    stack = []
    for i in range(n):
        stack.append(i)
    while len(stack) > 0:
        stack.pop()

def test_stack_deque1(n):
    stack = collections.deque()
    for i in range(n):
        stack.append(i)
    while len(stack) > 0:
        stack.pop()

def test_stack_deque2(n):
    stack = collections.deque()
    for i in range(n):
        stack.appendleft(i)
    while len(stack) > 0:
        stack.popleft()

print ("Testing test_stack_LifoQueue ..." )
t1 = timeit.Timer(lambda: test_stack_LifoQueue(N))
print ( "{} {}".format(N, t1.timeit(1)) )   # single run

print ("Testing test_stack_list ..." )
t1 = timeit.Timer(lambda: test_stack_list(N))
print ( "{} {}".format(N, t1.timeit(1)) )   # single run

print ("Testing test_stack_deque1 ..." )
t1 = timeit.Timer(lambda: test_stack_deque1(N))
print ( "{} {}".format(N, t1.timeit(1)) )   # single run

print ("Testing test_stack_deque2 ..." )
t1 = timeit.Timer(lambda: test_stack_deque2(N))
print ( "{} {}".format(N, t1.timeit(1)) )   # single run

# EOF
