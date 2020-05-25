FROM python:3
MAINTAINER "Vineet Pal Singh"

RUN git clone https://github.com/vineetps/django.git 

WORKDIR /django

RUN cat requirements.txt && pip install -r requirements.txt

# EXPOSE 8000
CMD ["python", "first_project/manage.py", "runserver"]
