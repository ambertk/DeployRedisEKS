FROM python
RUN pip install redis
COPY ./worker.py /worker.py
COPY ./rediswq.py /rediswq.py
COPY ./redis_wq.py /redis_wq.py

CMD  python worker.py





# # $ docker run -it -p 8888:8888 tensorflow/tensorflow
# FROM intelpython/intelpython2_core

# # Set user...
# USER root

# # Creat directories...
# RUN mkdir illumina
# RUN mkdir illumina/Models

# # Install python bits...
# ### Don't need to install these on intel-optimized aws... 
# RUN pip install tensorflow keras sklearn h5py redis
# RUN apt-get install -y unzip numactl

# # Set function aliases...
# RUN echo 'alias ll="ls -lah"' >> ~/.bashrc

# # Copy data, decompress, clean up...
# COPY Code.zip /illumina/Code.zip
# # RUN aws s3 cp s3://inference-data-kyle/Code.zip .; mv Code.zip /illumina/
# RUN cd /illumina
# RUN unzip /illumina/Code.zip
# RUN rm /illumina/Code.zip

# # Set working directory...
# # WORKDIR /illumina/Code

# # Set environment variables...
# # ENV master_node_hostfile=/home/ubuntu/src/hostfile_dir
# COPY ./worker.py /worker.py
# COPY ./rediswq.py /rediswq.py
# CMD python worker.py

# # To run:
# # kubectl exec -it illumina-pod -- /bin/bash
# # sudo docker run -it --privileged b827fa3fef55 /bin/bash
# # taskset -c 0,1,2 numactl --membind=0 python test.py 10000 1
