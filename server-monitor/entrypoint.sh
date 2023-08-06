#!/bin/bash

# Function to log messages with timestamps
log() {
    echo "$(date +'%Y-%m-%d %H:%M:%S') $1"
}

# Export environment variables to a file
log "Exporting environment variables..."
printenv > /server-monitor/env_vars.txt

# Add the desired crontab schedule using the exported env variables
log "Creating crontab schedule..."
echo "* * * * * /usr/local/bin/python3 /server-monitor/server_monitor/__main__.py >> /var/log/cron.log 2>&1" > /server-monitor/crontab

# Load the new crontab
log "Loading the crontab..."
crontab /server-monitor/crontab

# Create the log file to redirect cron job output
log "Create the cron.log file"
touch /var/log/cron.log

# Start the cron service in the foreground
log "Starting cron service..."
cron && tail -f /var/log/cron.log
