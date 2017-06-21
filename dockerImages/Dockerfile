FROM ubuntu:latest

RUN apt-get update -q && apt-get install -yqq \
    apt-utils \
    git \
    vim \
    nano \
    ssh \
    gcc \
    make \
    build-essential \
    libkrb5-dev \
    sudo
RUN apt-get install -y python-pip3
RUN pip3 numpy
RUN pip3 pandas
RUN pip3 matplotlib
RUN pip3 ipython
RUN pip3 scipy
ADD ./FL_150617_12832.csv /src
ADD ./commands.py /