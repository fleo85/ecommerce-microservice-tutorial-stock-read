# Commands to run the environment:

## MongoDB:
$sudo docker run -d --network mongo-network -v /home/federico/Documents/MongoDB/data/:/data/db -p 27017:27017 --name mongodb -h mongodbhost mongo

## RabbitMQ:
### First run the RabbitMQ container
$sudo docker run -d --rm -h rabbitmqhost --network mongo-network --name rabbitmqueue rabbitmq

### Second build the consumer docker image
$sudo docker build -t consumer .

### Then run the consumer container with the following command:
$sudo docker run --rm -it --network mongo-network consumer

### Testing the queue:
$sudo docker run -it --network mongo-network --rm -v $(pwd):/home python bash

Run the program 'send.py'

## REST API:
### First build the restapi docker image
$sudo docker build -t restapi .

### Then run the restapi container with the following command:
$sudo docker run -it --rm --name restapi_server -h restapihost --network mongo-network -p 8080:8080 restapi

To test the APIs, navigate to:
http://localhost:8080/v1/ui/

