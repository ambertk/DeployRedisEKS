import sys
import math
import redis
import os.path

### CONSTANTS!
HOST='redis'
KEY='job2'

# Read command line...
cluster_size = int(sys.argv[1])
dataset_size = int(sys.argv[2])

# Calculate partition size...
partition_size = dataset_size/cluster_size
partitionDx = {host:{'start':'', 'end':''} for host in range(cluster_size)}

start = -1
for host in range(cluster_size):
    start += 1
    partitionDx[host]['start'] = start
    start += partition_size - 1
    start = int(start)
    partitionDx[host]['end'] = start
    if host == range(cluster_size)[-1]:
        partitionDx[host]['end'] = dataset_size

c = redis.Redis(host=HOST)
c.delete(KEY)
for i in partitionDx.keys():
    c.rpush(KEY, "{START}|{END}".format(START=partitionDx[i]['start'], END=partitionDx[i]['end']))



# python find_partitions_and_write_hostfiles.py $cluster_size $dataset_size
