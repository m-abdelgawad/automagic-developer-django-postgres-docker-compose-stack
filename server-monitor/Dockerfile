FROM python:3.10

# Install crontab
RUN apt-get update && apt-get -y install cron

# Create and step in the project directory inside the container
WORKDIR /server-monitor

# Copy the requirements to the container
COPY requirements.txt .

# Install all the requirements
RUN pip install -r requirements.txt

# Copy all project contents to the project directory inside the container
COPY . .

# Make the script executable (optional, only if not done in Step 2)
RUN chmod +x /server-monitor/entrypoint.sh

# Set the entrypoint to the bash script
ENTRYPOINT ["/server-monitor/entrypoint.sh"]
