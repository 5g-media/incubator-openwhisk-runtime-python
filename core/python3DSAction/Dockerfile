FROM ubuntu:xenial

ENV FLASK_PROXY_PORT 8080
ENV PYTHONIOENCODING "UTF-8"

RUN apt-get update && apt-get upgrade -y && apt-get install -y \
        python3-pip \
        vim \
        wget \
        sox \
        && rm -rf /var/lib/apt/lists/*

RUN pip3 install --no-cache-dir deepspeech==0.4.1 \
        && pip3 install --no-cache-dir gevent==1.2.1 \
        && pip3 install --no-cache-dir flask==0.12 \
        && pip3 install --no-cache-dir requests==2.13.0

# Download pre-trained model
RUN wget https://github.com/mozilla/DeepSpeech/releases/download/v0.4.1/deepspeech-0.4.1-models.tar.gz
RUN tar xvfz deepspeech-0.4.1-models.tar.gz

RUN mkdir -p /actionProxy
ADD https://raw.githubusercontent.com/apache/incubator-openwhisk-runtime-docker/dockerskeleton%401.3.3/core/actionProxy/actionproxy.py /actionProxy/actionproxy.py

RUN mkdir -p /pythonAction
COPY pythonrunner.py /pythonAction/pythonrunner.py

CMD ["/bin/bash", "-c", "cd /pythonAction && python3 -u pythonrunner.py"]
