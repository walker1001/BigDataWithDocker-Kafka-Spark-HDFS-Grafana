docker build dockerfiles/pyspark -t vutrungnghia99/pyspark:spark2.4.1-python3.7-hadoop2.7
docker build dockerfiles/spark-master -t vutrungnghia99/spark-master:spark2.4.1-python3.7-hadoop2.7
docker build dockerfiles/spark-worker -t vutrungnghia99/spark-worker:spark2.4.1-python3.7-hadoop2.7
docker build dockerfiles/system-manager -t vutrungnghia99/system-manager:spark2.4.1-python3.7-hadoop2.7-kafka2.7.0
docker build dockerfiles/graphite -t vutrungnghia99/graphite:1.1.7-6