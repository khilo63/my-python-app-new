# Use a base Python image
FROM python:3.13.0-slim

# Set the working directory in the container
WORKDIR /app

# Copy the application file into the container
ADD issa0113-assignment4.py /app/

# Define the default command to run the app
CMD ["python", "issa0113-assignment4.py"]