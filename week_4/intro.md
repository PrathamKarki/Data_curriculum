# Hadoop 
Hadoop is a open source software framework that works on large volume of big data, which is based on map reduce model and supports paralle processing of large dataset. Hadoop doesn't rely on single machine for processing of the data

## Hadoop architecture
Hadoop has two main components
- **Hadoop Distrubuted File System (HDFS)**
- **MapReduce**


### HDFS:
HDFS breaks down large volume of files into blocks (128mb or 256mb), and spread them across cluster of machines. Each block is replicated 3 times to ensure that fail in machine doesn't affect / for fault tolerance.

why break down large file into blocks and spread them?
- because to ensure that if any faul-tolerance or fail in machine occurs the data is replicated, and can be easily accessible

### MapReduce
MapReduce breaks down the large tasks into smaller chunks (map) and then merge them together (reduce) to quickly process massive dataset


## How does Hadoop work?

**step 1**: Large dataset is divided into chunks (size of: 128mb into blocks) which is then distributed across datanodes , and each block is replicated 3 times

**step 2**: MetaData is managed , let's say the master node , the "brain" called  Namenode keeps track of these datanodes

**Step 3** : Processing request comes in, handled by MapReduce

**Step 4**: Map phase(paralle processing) here hadoop sends computation to data, each dataNode processes its own block

**Step 5**: shuffle and sorting , result from nodes are grouped (groups similar data together) , sorted and transfereed to reducers.

**step 6** Reducers combines these results

**Step 7**: result is stored back to HDFS


flow:  store -> split -> distribute(cluster) -> manage metaData -> parallel processing(map) -> combine(reduct) -> store