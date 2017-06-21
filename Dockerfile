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
RUN apt-get install -y python python-dev python-distribute python-pip
RUN pip install numpy
RUN pip install pandas
RUN pip install matplotlib
RUN pip install ipython
ADD ./989527.csv /src
ADD ./config.json /src
ADD ./commands.py /