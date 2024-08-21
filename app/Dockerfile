FROM python:3.12-slim

# Set the working directory
COPY . /usr/app
WORKDIR /usr/app

# Install python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port
EXPOSE 5000

# Run the application
CMD ["python", "server.py"]