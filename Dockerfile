FROM python:3

ADD cloudDocker.py /
ADD . /home/data
ADD result.txt /home/output/result.txt

CMD [ "python", "./cloudDocker.py" ]
