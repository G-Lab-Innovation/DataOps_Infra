# Use an official Airflow image as a parent image
FROM apache/airflow:2.1.2-python3.6

# Set the PATH environment variable to include /home/airflow/.local/bin
ENV PATH="/home/airflow/.local/bin:${PATH}"

# Install any needed packages specified in requirements.txt
COPY ./docker/requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r /usr/src/app/requirements.txt

RUN pip install apache-airflow

# Copy the rest of your Airflow project
COPY . /usr/src/app/
