#FROM tells Docker which image you base your image on
FROM python:3.7.2-alpine3.8

RUN mkdir -p /home/data/

#ADD Script
COPY ./main.py /

#CMD tells Docker to execute the command when the image loads
CMD ["python", "./main.py"]
