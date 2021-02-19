#!/bin/bash

virtualenv -p /usr/bin/python3 venv/py3 --verbose --no-setuptools
python3 -m pip install --upgrade 'setuptools; python_version >= "3.6"' 'setuptools<51.3.0; python_version < "3.6" and python_version >= "3.0"'

#remove last build result
sudo rm -rf /build/*
sudo rm -rf /dist/*

#edit version
newv=$(git describe --exact-match --tags)
sudo sed -i 's/version="[0-9\.]*"/version="'$newv'"/g' setup.py

#build new packages
sudo python3 setup.py sdist bdist_wheel