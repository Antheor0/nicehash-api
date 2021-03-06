FROM ubuntu:18.04
RUN apt-get update && apt-get upgrade -y \
    && apt-get install python3.6 -y \
    && apt-get install python3-pip -y \
    && apt-get install git -y \
    && apt-get install vim -y
RUN git clone https://github.com/Antheor0/nicehash-api ~/app
COPY requirements.txt /tmp/
RUN pip3 install --upgrade -r /tmp/requirements.txt
WORKDIR /root/app
CMD python3 main.py