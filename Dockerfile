FROM python:3

ADD cloudDocker.py /
ADD Assignment 2 /home/data

CMD [ "python", "./cloudDocker.py" ]
