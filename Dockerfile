From ubuntu:22.04
RUN apt-get update -y  &&\
    apt-get install -y python-pip python-dev
WORKDIR /app
COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
CMD [ "python", "./Bot_Discord.py" ]