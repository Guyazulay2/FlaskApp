FROM ubuntu:latest


RUN apt-get update
RUN apt-get install python3-pip -y
RUN pip3 install flask

WORKDIR /root


COPY . .


ENTRYPOINT [ "python3" ]
CMD [ "./app.py" ]