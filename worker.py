#!/usr/bin/env python
import sys
import time
import rediswq
# from redis_wq import RedisWQ

HOST="redis"
JOBNAME="job2"
# Uncomment next two lines if you do not have Kube-DNS working.
# import os
# host = os.getenv("REDIS_SERVICE_HOST")
# 197441620132.dkr.ecr.us-west-2.amazonaws.com/redis-test
print("oh hey!")

q = rediswq.RedisWQ(name=b"job2")
# conn = RedisWQ(host=HOST)
print("oh hey!!")
print(q._main_qsize())
print(q._db.brpoplpush(q._main_q_key, q._processing_q_key, timeout=60))
print(q._main_qsize())

# wq = conn.get(JOBNAME)
# print(wq)


"""
print("Worker with sessionID: " +  q.sessionID())
print("Initial queue state: empty=" + str(q.empty()))
while not q.empty():
  item = q.lease(lease_secs=10, block=True, timeout=2) 
  if item is not None:
    itemstr = item.decode("utf=8")
    print("Working on " + itemstr)
    time.sleep(10) # Put your actual work here instead of sleep.
    q.complete(item)
  else:
    print("Waiting for work")
print("Queue empty, exiting")
"""