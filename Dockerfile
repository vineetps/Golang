FROM python:3
MAINTAINER "Vineet Pal Singh"
RUN git clone https://github.com/vineetps/django.git
RUN pip install -r requirements.txt
#RUN python django/first_project/manage.py runserver
EXPOSE 8000:8000
