Utilize command
---
```bash
docker rm -f $(docker ps -a -q)
bin/kafka-topics.sh --list --zookeeper zookeeper:2181
bin/kafka-topics.sh --create --topic trips --partitions 2 --replication-factor 1 --bootstrap-server localhost:9092,kafka:9093
bin/kafka-topics.sh --describe --topic trips --bootstrap-server localhost:9092,localhost:9094,localhost:9095
bin/kafka-console-producer.sh --topic trips --bootstrap-server localhost:9092,localhost:9094,localhost:9095
bin/kafka-console-consumer.sh --topic trips --from-beginning --bootstrap-server localhost:9092,localhost:9094,localhost:9095
docker ps --format "table {{.Image}}\t{{.Ports}}\t{{.Names}}"
sudo rm -rf /tmp/*
```
Build images
---
Download spark at: https://archive.apache.org/dist/spark/spark-2.4.1/spark-2.4.1-bin-hadoop2.7.tgz

Save to: dockerfiles/pyspark-notebook/spark-2.4.1-bin-hadoop2.7.tgz
```bash
./build.sh
```
Start bigdata cluster
```bash
docker-compose -f docker-compose.yml up -d
```
Create a topic
```bash
bin/kafka-topics.sh --create --topic trips --partitions 3 --replication-factor 3 --bootstrap-server localhost:9092,localhost:9094,localhost:9095
```
Producer to kafka topic
```bash
python simulation/producer.py
```
