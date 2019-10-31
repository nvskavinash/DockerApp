FROM python:3

ADD cloudDocker.py /
ADD Assignment /home/data

CMD [ "python", "./cloudDocker.py" ]
