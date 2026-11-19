FROM python:3.12-slim
#set folder within container as workdir
WORKDIR /app
#copy files in local folder
COPY . .
#RUN - pip install requirments/dependencies
RUN pip install -r requirements.txt
#when container starts it will do the following
ENTRYPOINT ["python3","cleanup_v1.py"]

##when building images always build from the images where the file is locaked