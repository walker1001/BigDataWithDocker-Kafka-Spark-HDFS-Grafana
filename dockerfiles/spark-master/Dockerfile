FROM vutrungnghia99/pyspark-notebook:2.4.1-2.7-3.7

LABEL maintainer="Gezim Sejdiu <g.sejdiu@gmail.com>, Giannis Mouchakis <gmouchakis@gmail.com>"

COPY master.sh /
USER root
RUN sudo mv /usr/local/spark-2.4.1-bin-hadoop2.7 /spark

RUN chown jovyan /spark

USER jovyan

ENV SPARK_MASTER_PORT 7077
ENV SPARK_MASTER_WEBUI_PORT 8080
ENV SPARK_MASTER_LOG /spark/logs
ENV SPARK_HOME /spark
# RUN \
#    echo 'alias python="/usr/bin/python3"' >> /root/.bashrc && \
#    echo 'alias pip="/usr/bin/pip3"' >> /root/.bashrc && \
#    source /root/.bashrc
EXPOSE 8080 7077 6066

CMD ["/bin/bash", "/master.sh"]
