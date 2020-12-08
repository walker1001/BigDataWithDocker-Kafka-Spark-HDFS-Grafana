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
```
Build images
---
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
bin/kafka-topics.sh --create --topic tweets --partitions 2 --replication-factor 1 --bootstrap-server localhost:9092,kafka:9093
```
