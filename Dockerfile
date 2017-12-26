
FROM gcr.io/tensorflow/tensorflow:latest-gpu

RUN apt-get update && apt-get install -y \
    protobuf-compiler \
    git \
    wget \
    python3-tk



RUN apt-get update \
  && apt-get install -y python3-pip python3-dev \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install --upgrade pip


ADD requirements.txt /tensorflow/requirements.txt

COPY models /tensorflow/models


ADD data/ssd_mobilenet_v1.config /tensorflow/models/research/object_detection/ssd_mobilenet_v1.config
ADD data/train.record /tensorflow/models/research/object_detection/data/train.record
ADD data/valid.record /tensorflow/models/research/object_detection/data/valid.record
ADD data/test.record /tensorflow/models/research/object_detection/data/test.record



WORKDIR /tensorflow

RUN pip3 install -r requirements.txt

RUN cd /tensorflow/models/research \
    && protoc object_detection/protos/*.proto --python_out=. \
    && python setup.py sdist \
    && (cd slim && python setup.py sdist)




# TensorBoard
# EXPOSE 6006
# Jupyter
EXPOSE 8888

ENV PYTHONPATH=$PYTHONPATH:/tensorflow/models/research:/tensorflow/models/research/slim
