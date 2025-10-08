.PHONY: install start stop restart status logs clean

# Install dependencies
install:
	poetry install

# Start the API with PM2
start:
	pm2 start "poetry run uvicorn main:app --host 0.0.0.0 --port 8000" --name redirecter

# Stop the API
stop:
	pm2 stop redirecter

# Restart the API
restart:
	pm2 restart redirecter

# Check status
status:
	pm2 status redirecter

# View logs
logs:
	pm2 logs redirecter

# Stop and delete the process
clean:
	pm2 delete redirecter

# Development mode (with auto-reload)
dev:
	poetry run uvicorn main:app --host 0.0.0.0 --port 8081 --reload

# Show all PM2 processes
list:
	pm2 list


connect-adita:
	ssh ubuntu@ec2-52-47-172-168.eu-west-3.compute.amazonaws.com
