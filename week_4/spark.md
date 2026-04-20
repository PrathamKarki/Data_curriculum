# Apache Spark
Apache spark is an open source analytical data engine, that works on large-scale of dataset, is fast and applicalbe for pyspark
It is mostly used for machine learning and AI applications

Apache spark is about 10 to 100 times faster and is a great alternative for hadoop.

It also includes API for programming languages that are popular for data analysts, data scientist and more

## How apache spark works?
In context of MapReduce model in apache hadoop, large scale of data is stored in HDFS, which is broken down into mulitple chunks (called blocks), well each of these blocks are replicated 3 times to prevent fault tolerance, these block are stored in different cluster of machine, and hence now mapReduce comes to the play, where
mapReduce perform parallel processing of these data,  mapReduce requires sequential multi-step process to do a job , with every step first it reads data from the cluster, write it to the disk , then cluster performs operation again it's write to the disk this process heavily relies of I/O disk and makes it slower

SO, apache spark comes to the rescue here, instead of using of I/O disk, it processes data directly to the memory (RAM), it means spark can laod data once, peform multiple operation without saving it again and again like we did in hadoop.


### Distributed computing with spark
Distributed computing is technique, well we just learned like in hadoop, where large scale of data is divided or broken down into multiple chunks,
processed simultaneoulsy across multiple machine(cluster) and instead of I/0 disk , here processed result are stored in memory

## what is pyspark now?
pyspark is Python API, if we think of apache spark as engine, pyspark is like a translator or way to connect/talk to that engine using python