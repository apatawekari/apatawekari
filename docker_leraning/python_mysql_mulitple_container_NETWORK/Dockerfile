# --> Please See below Step to use one docker with other docker (to/from Communication)
FROM python

# Set the working directory in the container
WORKDIR /code


# Copy the current directory contents into the container at /code dir
COPY ./script.py /code/

# Install any needed packages specified
RUN pip install mysql-connector-python
RUN pip install mysql


# Run app.py when the container launches
CMD [ "python", "script.py" ]

# Make port 80 available to the world outside this container 
# EXPOSE 80






