#!/bin/bash

sudo apt update
sudo apt-get install python3-pip
sudo python3 -m pip install --upgrade pip setuptools wheel

virtualenv -p /usr/bin/python3 venv/py3 --verbose --no-setuptools
python3 -m pip install --upgrade 'setuptools; python_version >= "3.6"' 'setuptools<51.3.0; python_version < "3.6" and python_version >= "3.0"'