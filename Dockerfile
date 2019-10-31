FROM python:3

ADD cloudDocker.py /
ADD . /home/data
ADD empty.txt /home/output/result.txt

CMD [ "python", "./cloudDocker.py" ]
