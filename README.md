# Big data storage and processing pipeline
Authors:
 - Le Vu Loi
 - Vu Trung Nghia
 - Dang Lam San

In this project, we built a pipeline for storing and processing PNRs data 
Link data: (https://developers.amadeus.com/blog/free-fake-pnr-sample-data)

The pipeline support batch view and real-time view:
 - In batch view, user can using SQL api and python to query and visuzlie data in HDFS
 - For real-time view, we simple logs the number of recieved records every 10 seconds

![alt text](images/architecture.png)

Acknowledgement:
 - https://github.com/haiphucnguyen/BigDataDemo
 - http://www.diva-portal.org/smash/get/diva2:897808/FULLTEXT01.pdf

Prerequires:
---
 - java 8
 - python 3.8
 - pip install kafka-python==2.0.2
 - docker version 20.10.1, build 831ebea
 - docker-compose version 1.25.0
 - ubuntu 20.04
 - RAM: 12 GB

Create docker network name: bigdata
```
docker network create bigdata
```
Remove old containers
```
docker rm -f $(docker ps -a -q)
```
Start bigdata cluster
```bash
docker-compose -f docker-compose.yml up -d
```
Go to browser at: `localhost:8888` and enter `password`: `admin`

From notebook GUI, open a terminal and run the following commands to create `trips` and `real-time-statistic` topics
```
cd ~/kafka
bin/kafka-topics.sh --create --topic trips --partitions 2 --replication-factor 2 --bootstrap-server kafka-broker-1:9093,kafka-broker-2:9093
bin/kafka-topics.sh --create --topic real-time-statistic --partitions 2 --replication-factor 2 --bootstrap-server kafka-broker-1:9093,kafka-broker-2:9093

# decribe created topics (optional)
bin/kafka-topics.sh --describe --topic trips --bootstrap-server kafka-broker-1:9093,kafka-broker-2:9093
bin/kafka-topics.sh --describe --topic real-time-statistic --bootstrap-server kafka-broker-1:9093,kafka-broker-2:9093
# decribe created topics from local machine (optional, you computer must install kafka)
bin/kafka-topics.sh --describe --topic trips --bootstrap-server localhost:9092,localhost:9094
bin/kafka-topics.sh --describe --topic real-time-statistic --bootstrap-server localhost:9092,localhost:9094
```

Go to `localhost:8888` again and open 3 notebooks in folder `work`:
 - `batch-processing.ipynb`
 - `dashboard.ipynb`
 - `speed-processing.ipynb`

Run all:
 - `batch-processing.ipynb`: listen on topic `trips` => process data => save to hdfs
 - `speed-processing.ipynb`: listen on topic `trips` => process data => write to topic `real-time-statistic`

Take a look at spark master at: `localhost:8082`, `localhost:8083`, `localhost:8084`
Take a look at hdfs at: `localhost:50070`

To access graphite web UI, type `localhost:80` on your browser. The credentials are:
- `username`: `guest`
- `password`: `guest`

To access grafana web UI, type `localhost:3000` on your browser. The credentials are:
- `username`: `admin`
- `password`: `admin`

Add data source in grafana. On the left bar: `Configuration` => `Data Sources` => `Add data source`. Choose Graphite from the list. The configuration are:
- URL: `http://<graphite container ip>:80` (to get ip: `docker inspect graphite`)
- Basic auth: checked
- Basic auth details:
   - User: `guest`
   - Password: `guest`

Create dashboard in grafana


Run java app to consume topic `real-time-statistic` and write result to graphite
```
java -jar app/KafkafToGraphite.jar
```
Produce records from your local machine (you machine must install kafka-python==2.0.2)
```
python simulation/producer.py --n 10000 --delay 0.1
```
After run produce command, in `batch-processing.ipynb` you should see the logs which count the recieved records

![alt text](images/batch_processing.png)

Go to `dashboard.ipynb` and run all to see the statistics and anomaly detection results

![alt text](images/dashboard.png)

Go to grafana UI dashboard to see the graph which show the number of recieved records every 10 seconds

![alt text](images/real-time-dashboard.png)



Utilize command
---
```bash
docker ps --format "table {{.Image}}\t{{.Ports}}\t{{.Names}}"
```
