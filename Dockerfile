FROM python:3.9

COPY . /myproject

# Install OpenJDK-11
RUN apt-get update && \
    apt-get install -y openjdk-11-jre-headless && \
    apt-get clean;

RUN pip install -r myproject/requirements.txt

WORKDIR /myproject

CMD ["python", "/myproject/Main.py"]