# Apache kafka
apache kafka is a distributed real-time data streaming system , built to transport large volumes of data in real-time between the system.
It is used to send, store and pass data (events) between system in real time.

## How does apache kafka works?
Apache kafka is real-time data streaming and message processing platform. Think of kafka as fast "post office" that receives messages (data) from various sources and sends them to their respective destinations.

- Producer: sends the message

- Kafka broker :  behave like postal staff: sorting, storing and controlling the flow

- consumer: get the message (such as individual opening mailbox)

## Kafka architecture

1. Kafka producers: these are the data/event senders to the kafka topics
                    eg: users places an order, then producer sends "order_created" to kafka topics


2. Kafka broker:  kafka broker is a server that recieves message from producers, and decides where to store them in topics/partitions and serves them to consumers.



3. Kafka Topics:    Stores those data/event send by producer, groups those message by category
                    eg: orders payments, user-activity

4. Kafka Partitions: 
Partitions divide a topic into smaller parts to handle high data volume.
Messages are distributed across partitions, and order is preserved within each partition only.
now suppose that "order_created" gets lot of traffic so kafka splits them as   order_created :  partition_0,  partition_1, partition_2 ...
                    eg: orders topic
                        ├── Partition 0 → order1, order4 
                        ├── Partition 1 → order2, order5
                        └── Partition 2 → order3

4. Kafka broker:  kafka broker is a server that recieves message from producers, store them in topics/partitions and serves them to consumers.


5. kafka consumers: kafka consumers are applications that read and process message from kafka partitions, they process the data
eg: "order_created" events comes in 
    consumer reads it and update database, sends confirmation email, triggers payment flow


Final flow: Producer -> broker -> (topics and partitions) --> consumer