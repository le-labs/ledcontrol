#!/usr/bin/env bash

# This script creates a Python virtual environment and installs the
# project's dependencies.

sudo apt update
sudo apt upgrade -y

# install apt packages
sudo apt install -y python3
sudo apt install -y python3-dev
sudo apt install -y python3-pip

# install pip packages
sudo pip3 install -U setuptools
sudo pip3 install -U pip
sudo pip3 install -U virtualenv

# create and activate the Python virtual environment
virtualenv -p /usr/bin/python3.5 venv
source venv/bin/activate

# install pip packages
pip install -r requirements.txt