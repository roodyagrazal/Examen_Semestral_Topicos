FROM python:3
LABEL MAINTAINER="Roody Agrazal roody@agrazal.com"
WORKDIR /src

COPY ./requirements.txt /src/requirements.txt
RUN pip install -r requirements.txt

COPY ./app.py /src/app.py
COPY ./core /src/core

CMD ["python", "app.py"]