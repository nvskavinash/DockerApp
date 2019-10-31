FROM python:3

ADD cloudDocker.py /

CMD [ "python", "./cloudDocker.py" ]
