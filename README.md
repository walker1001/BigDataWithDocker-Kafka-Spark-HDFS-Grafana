Utilize command
---
```bash
docker rm -f $(docker ps -a -q)
bin/kafka-topics.sh --create --topic quickstart-events --bootstrap-server localhost:9092
bin/kafka-topics.sh --describe --topic quickstart-events --bootstrap-server localhost:9092
bin/kafka-console-producer.sh --topic quickstart-events --bootstrap-server localhost:9092
bin/kafka-console-consumer.sh --topic quickstart-events --from-beginning --bootstrap-server localhost:9092
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
