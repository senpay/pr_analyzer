#!/usr/bin/env bash
set -e
$(command -v python3.6) -m venv .env

source .env/bin/activate

pip install --upgrade wheel
pip install --upgrade -r requirements.txt
