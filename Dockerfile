FROM python:3

ADD cloudDocker.py /
ADD C:\Users\Assignment /home/data

CMD [ "python", "./cloudDocker.py" ]
