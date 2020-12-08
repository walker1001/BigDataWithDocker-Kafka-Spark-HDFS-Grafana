# FROM bde2020/spark-base:2.4.1-hadoop2.7
FROM vutrungnghia99/pyspark-notebook:2.4.1-2.7-3.7

LABEL maintainer="Gezim Sejdiu <g.sejdiu@gmail.com>, Giannis Mouchakis <gmouchakis@gmail.com>"

COPY worker.sh /
USER root

RUN sudo mv /usr/local/spark-2.4.1-bin-hadoop2.7 /spark
RUN chown jovyan /spark
USER jovyan

ENV SPARK_WORKER_WEBUI_PORT 8081
ENV SPARK_WORKER_LOG /spark/logs
ENV SPARK_MASTER "spark://spark-master:7077"
ENV SPARK_HOME /spark

# RUN \
#    echo 'alias python="/usr/bin/python3"' >> /root/.bashrc && \
#    echo 'alias pip="/usr/bin/pip3"' >> /root/.bashrc && \
#    source /root/.bashrc

EXPOSE 8081

CMD ["/bin/bash", "/worker.sh"]
