# hackathon-rabbitmq
A small and simple hackathon project to explore streaming messages to/from different services using Python and RabbitMQ.

## Background
This project is composed of three services: a producer service, a consumer service, and a RabbitMQ instance. 
The producer uses a client library to send messages to RabbitMQ, and the consumer receives them.

## Environment
This project requires a .env file added to the root directory in order for docker-compose to set the appropriate environment variables within the service containers.

## Commands
This project uses docker-compose to orchestrate building and running its services. Standard commands can be used.

To build and run the project:
```
docker-compose up --build -d
```

To stop a running project:
```
docker-compose down
```