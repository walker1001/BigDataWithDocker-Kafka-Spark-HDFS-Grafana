docker build dockerfiles/pyspark-notebook -t pyspark-notebook:spark2.4.1-python3.7-hadoop2.7
docker build dockerfiles/spark-master -t spark-master:spark2.4.1-python3.7-hadoop2.7
docker build dockerfiles/spark-worker -t spark-worker:spark2.4.1-python3.7-hadoop2.7
docker build dockerfiles/dashboard-notebook -t dashboard-notebook:spark2.4.1-python3.7-hadoop2.7-hive
