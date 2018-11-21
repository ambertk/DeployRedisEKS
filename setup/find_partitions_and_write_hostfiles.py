import sys
import math
import os.path


# python find_partitions_and_write_hostfiles.py $hostfile_dir $hosts $cluster_size $dataset_size

# Read command line...
hostfile_dir = sys.argv[1]
hosts = [i.strip() for i in sys.argv[2].split('\n')]
cluster_size = int(sys.argv[3])
dataset_size = int(sys.argv[4])


# Calculate partition size...
partition_size = dataset_size/cluster_size
partitionDx = {host:{'start':'', 'end':'', 'path':''} for host in hosts}

def write_config(start, end, path):
    if not os.path.exists(os.path.dirname(os.path.abspath(os.path.dirname(path)))):
        os.mkdir(os.path.abspath(os.path.dirname(path)))
    F = open(path, 'w')
    F.write("{START} {END}\n".format(START=start, END=end))
    F.close()

start = -1
for host in hosts:
    start += 1
    partitionDx[host]['start'] = start
    start += partition_size - 1
    start = int(start)
    partitionDx[host]['end'] = start
    if host == hosts[-1]:
        partitionDx[host]['end'] = dataset_size
    partitionDx[host]['path'] = os.path.join(hostfile_dir, host + ".config")
    write_config(start=partitionDx[host]['start'], end=partitionDx[host]['end'], path=partitionDx[host]['path'])
