# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.
ARG BASE_CONTAINER=jupyter/scipy-notebook:c094bb7219f9
FROM $BASE_CONTAINER

LABEL maintainer="Jupyter Project <jupyter@googlegroups.com>"

# Fix DL4006
SHELL ["/bin/bash", "-o", "pipefail", "-c"]

USER root

# Spark dependencies
# Default values can be overridden at build time
# (ARGS are in lower case to distinguish them from ENV)
ARG spark_version="2.4.1"
ARG hadoop_version="2.7"
# ARG spark_checksum="E8B47C5B658E0FBC1E57EEA06262649D8418AE2B2765E44DA53AAF50094877D17297CC5F0B9B35DF2CEEF830F19AA31D7E56EAD950BBE7F8830D6874F88CFC3C"
ARG openjdk_version="8"

RUN wget https://downloads.apache.org/kafka/2.7.0/kafka_2.13-2.7.0.tgz && tar -xzf kafka_2.13-2.7.0.tgz && mv kafka_2.13-2.7.0 ~/kafka

ENV APACHE_SPARK_VERSION="${spark_version}" \
    HADOOP_VERSION="${hadoop_version}"

RUN apt-get -y update && \
    apt-get install --no-install-recommends -y \
    "openjdk-${openjdk_version}-jre-headless" \
    ca-certificates-java && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Spark installation
COPY spark-2.4.1-bin-hadoop2.7.tgz /tmp/
WORKDIR /tmp
# Using the preferred mirror to download Spark
# hadolint ignore=SC2046
# RUN wget https://archive.apache.org/dist/spark/spark-${APACHE_SPARK_VERSION}/spark-${APACHE_SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz && \
    # python -c "import sys, json; content=json.load(sys.stdin); print(content['preferred']+content['path_info'])") && \
    # echo "${spark_checksum} *spark-${APACHE_SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz" | sha512sum -c - && \
RUN tar xzf "spark-${APACHE_SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz" -C /usr/local --owner root --group root --no-same-owner && \
    rm "spark-${APACHE_SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz"

WORKDIR /usr/local

# Configure Spark
ENV SPARK_HOME=/usr/local/spark
ENV SPARK_OPTS="--driver-java-options=-Xms1024M --driver-java-options=-Xmx4096M --driver-java-options=-Dlog4j.logLevel=info" \
    PATH=$PATH:$SPARK_HOME/bin

RUN ln -s "spark-${APACHE_SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}" spark && \
    # Add a link in the before_notebook hook in order to source automatically PYTHONPATH
    mkdir -p /usr/local/bin/before-notebook.d && \
    ln -s "${SPARK_HOME}/sbin/spark-config.sh" /usr/local/bin/before-notebook.d/spark-config.sh

USER $NB_UID

# Install pyarrow
# RUN conda config --set allow_conda_downgrades true && \
#     conda install conda=4.6.11
RUN pip install pyarrow
    # conda install --yes --satisfied-skip-solve \
    # 'pyarrow=2.0.*' && \
RUN conda clean --all -f -y && \
    fix-permissions "${CONDA_DIR}" && \
    fix-permissions "/home/${NB_USER}"

WORKDIR $HOME




# # Copyright (c) Jupyter Development Team.
# # Distributed under the terms of the Modified BSD License.
# FROM jupyter/minimal-notebook


# USER root

# # Util to help with kernel spec later
# RUN apt-get -y update && apt-get -y install jq && apt-get clean && rm -rf /var/lib/apt/lists/*

# # Spark dependencies
# ENV APACHE_SPARK_VERSION 2.4.1
# RUN apt-get -y update && \
#     apt-get install -y --no-install-recommends openjdk-8-jre-headless && \
#     apt-get clean && \
#     rm -rf /var/lib/apt/lists/*

# COPY spark-2.4.1-bin-hadoop2.7.tgz /tmp/
# RUN cd /tmp && \
#         # wget -q http://d3kbcqa49mib13.cloudfront.net/spark-${APACHE_SPARK_VERSION}-bin-hadoop2.7.tgz && \
#         # echo "439fe7793e0725492d3d36448adcd1db38f438dd1392bffd556b58bb9a3a2601 *spark-${APACHE_SPARK_VERSION}-bin-hadoop2.7.tgz" | sha256sum -c - && \
#         tar xzf spark-${APACHE_SPARK_VERSION}-bin-hadoop2.7.tgz -C /usr/local && \
#         rm spark-${APACHE_SPARK_VERSION}-bin-hadoop2.7.tgz
# RUN cd /usr/local && ln -s spark-${APACHE_SPARK_VERSION}-bin-hadoop2.7 spark

# # Mesos dependencies
# # Currently, Mesos is not available from Debian Jessie.
# # So, we are installing it from Debian Wheezy. Once it
# # becomes available for Debian Jessie. We should switch
# # over to using that instead.
# RUN apt-key adv --keyserver keyserver.ubuntu.com --recv E56151BF && \
#     DISTRO=debian && \
#     CODENAME=wheezy && \
#     echo "deb http://repos.mesosphere.io/${DISTRO} ${CODENAME} main" > /etc/apt/sources.list.d/mesosphere.list && \
#     apt-get -y update && \
#     apt-get --no-install-recommends -y --force-yes install mesos=0.22.1-1.0.debian78 && \
#     apt-get clean && \
#     rm -rf /var/lib/apt/lists/*

# # Spark and Mesos config
# ENV SPARK_HOME /usr/local/spark
# ENV PYTHONPATH $SPARK_HOME/python:$SPARK_HOME/python/lib/py4j-0.9-src.zip
# ENV MESOS_NATIVE_LIBRARY /usr/local/lib/libmesos.so
# ENV SPARK_OPTS --driver-java-options=-Xms1024M --driver-java-options=-Xmx4096M --driver-java-options=-Dlog4j.logLevel=info

# USER jovyan

# # Install Python 3 packages
# RUN conda install --quiet --yes \
#     'ipywidgets=4.1*' \
#     'pandas=0.17*' \
#     'matplotlib=1.5*' \
#     'scipy=0.17*' \
#     'seaborn=0.7*' \
#     'scikit-learn=0.17*' \
#     && conda clean -tipsy

# # Install Python 2 packages and kernel spec
# RUN conda create --quiet --yes -p $CONDA_DIR/envs/python2 python=2.7 \
#     'ipython=4.1*' \
#     'ipywidgets=4.1*' \
#     'pandas=0.17*' \
#     'matplotlib=1.5*' \
#     'scipy=0.17*' \
#     'seaborn=0.7*' \
#     'scikit-learn=0.17*' \
#     pyzmq \
#     && conda clean -tipsy

# # Install Python 2 kernel spec into the Python 3 conda environment which
# # runs the notebook server
# RUN bash -c '. activate python2 && \
#     python -m ipykernel.kernelspec --prefix=$CONDA_DIR && \
#     . deactivate'
# # Set PYSPARK_HOME in the python2 spec
# RUN jq --arg v "$CONDA_DIR/envs/python2/bin/python" \
#         '.["env"]["PYSPARK_PYTHON"]=$v' \
#         $CONDA_DIR/share/jupyter/kernels/python2/kernel.json > /tmp/kernel.json && \
#         mv /tmp/kernel.json $CONDA_DIR/share/jupyter/kernels/python2/kernel.json
