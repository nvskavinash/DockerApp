FROM python:3

ADD cloudDocker.py /
ADD . /home/data

CMD [ "python", "./cloudDocker.py" ]
