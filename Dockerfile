FROM python:3.9
ENV PYTHONUNBUFFERED 1
RUN mkdir app1
WORKDIR /app1
COPY requirements.txt  /app1/requirements.txt
RUN pip install -r requirements.txt
COPY . /app1/

#CMD python manage.py runserver 0.0.0.0:8000