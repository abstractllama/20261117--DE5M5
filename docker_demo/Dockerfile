FROM python:3.12-slim
#set folder within container as workdir
WORKDIR /app
#copy files in local folder
COPY . /app
#when container starts it will do the following
ENTRYPOINT ["python3","hello.py"]

##when building images always build from the images where the file is locaked