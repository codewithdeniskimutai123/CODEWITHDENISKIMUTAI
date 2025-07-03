#!/usr/bin/env bash

#  Exit immediately on errors
set -o errexit

# Install Python dependencies
pip install -r requirements.txt

# Collect static files (no prompts)
python manage.py collectstatic --no-input

# Apply database migrations
python manage.py migrate