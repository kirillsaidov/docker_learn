# use python3.10 as the base image
# it is built upon a simplified os container
# which usually is a linux os system
FROM python:3.10

# create base folder that we will use for our program
WORKDIR /app

# python file to our docker container
COPY ./print_fibonacci.py ./

# command to run
ENTRYPOINT ["python3", "print_fibonacci.py"]

