
FROM continuumio/anaconda3:latest
#FROM python:3
#RUN apt-get install gcc
RUN apt-get update  --fix-missing && apt-get install -y libmysqlclient-dev \
gcc
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
RUN pip install -i https://pypi.anaconda.org/pypi/simple django-bootstrap3
RUN pip install -U django-bootstrap3
#RUN pip install -i https://pypi.anaconda.org/pypi/simple mysqlclient
ADD . /code/


# install django, normally you would remove this step because your project would already
# be installed in the code/app/ directory
##run django-admin.py startproject website /home/docker/code/app/ 