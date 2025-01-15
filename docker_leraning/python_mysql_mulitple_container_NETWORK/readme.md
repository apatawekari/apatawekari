use Docker to link containers together using the Docker network

Step 1 :  Create a network
    $ docker network create my_network
    $ docker network ls

Step 2 : Run the MySQL container and connect it to the network:
    $ docker run --name <container_name> --network <network_name> -e MYSQL_ROOT_PASSWORD=<password> -e MYSQL_DATABASE=testdb -e MYSQL_USER=admin -e MYSQL_PASSWORD=admin -p 3306:3306 -d mysql

Step 3 : Create a Dockerfile for your Python application:

Step 4 : Create a Python script (app.py) to connect to the MySQL database:
    1. Provide 'container_name' in host part in python code as it will be sharing same netwrok 

Step 5 : Build the Python application Docker image:
    $ docker build -t <tag_name> .
    $ docker build -t python-code-image .

Step 6 : Run the Python container and connect it to the network:
    $ docker run --name <python-container> --network <my_network> -p <loca_port>:<cnt_port> <image_name>
    $ docker run --name python-container -it --network my_network -p 5000:5000 python-code-image:latest