FROM python:3.7
WORKDIR /app
COPY requirements.txt .
#RUN apt-get update && apt-get install -y python3-pip
COPY ./requirements.txt .
RUN pip3 install -r requirements.txt
COPY . .
EXPOSE :5000
ENTRYPOINT ["/usr/local/bin/python", "app.py"]
