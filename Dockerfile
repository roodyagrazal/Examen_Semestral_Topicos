FROM python:3
LABEL MAINTAINER="Roody Agrazal roody@agrazal.com"
WORKDIR /src

COPY ./requirements.txt /src/requirements.txt
RUN pip install -r requirements.txt

RUN apt-get update \
    && apt-get install tesseract-ocr -y \
    python3 \
    python-setuptools \
    python3-pip \
    && apt-get clean \
    && apt-get autoremove

COPY ./app.py /src/app.py
COPY ./core /src/core

CMD ["python", "app.py"]