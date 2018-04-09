# This script installs all dependencies and configures the Raspberry PI
# to execute the ledcontrol app.

sudo apt update
sudo apt upgrade -y

# Install apt packages
sudo apt install -y python3
sudo apt install -y python3-pip

# Update pip3 and install the required python libraries
sudo pip3 install -U setuptools
sudo pip3 install -U pip