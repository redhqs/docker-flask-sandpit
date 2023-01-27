# base python image
FROM python:3.11.1

# set working directory
WORKDIR /opt/app

# copy files to working directory
COPY . .

# install dependencies
RUN pip install -r requirements.txt

# on container start
CMD ["python", "/opt/app/src/app.py"]