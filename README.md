Utilize command
---
```bash
docker rm -f $(docker ps -a -q)
bin/kafka-topics.sh --list --zookeeper zookeeper:2181
bin/kafka-topics.sh --create --topic tweets --partitions 2 --replication-factor 1 --bootstrap-server localhost:9092,kafka:9093
bin/kafka-topics.sh --describe --topic quickstart-events --bootstrap-server localhost:9092
bin/kafka-console-producer.sh --topic quickstart-events --bootstrap-server localhost:9092
bin/kafka-console-consumer.sh --topic quickstart-events --from-beginning --bootstrap-server localhost:9092
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
Go to gateway and create a topic
```bash
docker run --network bigdata -it wurstmeister/kafka:2.12-2.2.1 bash
cd /opt/kafka
bin/kafka-topics.sh --create --topic trips --partitions 2 --replication-factor 1 --bootstrap-server localhost:9092,kafka-broker-1:9093,localhost:9094,kafka-broker-2:9093
```
Producer to kafka topic
```bash
python simulation/producer.py
```