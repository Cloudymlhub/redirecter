# Redirecter API

A minimal FastAPI project for URL redirection, specifically designed for redirecting QR codes to WhatsApp links.

## Features

- FastAPI-based REST API
- QR code redirection endpoint
- WhatsApp link generation
- Health check endpoint

## Setup

1. Install Poetry (if not already installed):
```bash
curl -sSL https://install.python-poetry.org | python3 -
```

2. Install PM2 globally (if not already installed):
```bash
npm install -g pm2
```

3. Install dependencies:
```bash
make install
# or
poetry install
```

## Running the Application

### Using PM2 (Production):
```bash
# Start the API
make start

# Check status
make status

# View logs
make logs

# Restart
make restart

# Stop
make stop

# Clean (stop and delete)
make clean
```

### Development mode (with auto-reload):
```bash
make dev
```

### Manual run:
```bash
poetry run python main.py
```

## API Endpoints

- `GET /` - Root endpoint
- `GET /health` - Health check
- `GET /qr/solarbox-energy/{bike_id}` - Redirect to WhatsApp for SolarBox bike verification

## Usage Example

Visit: `http://localhost:8000/qr/solarbox-energy/BIKE123`

This will redirect to a WhatsApp chat with the configured phone number and a pre-filled message.

## Configuration

Update the phone number in `src/app_config.py` to match your requirements.