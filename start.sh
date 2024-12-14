#!/bin/bash

# Use PORT from environment variable or default to 8000
PORT="${PORT:-8000}"

# Start the application
exec uvicorn src.main:app --host 0.0.0.0 --port "$PORT"