#!/bin/bash

#remove last build result
sudo rm -rf /build/*
sudo rm -rf /dist/*

#edit version
newv=$(git describe --exact-match --tags)
echo ">>>>>>>>>>>>>>>>>>>>>> tag=${newv}"
echo ">>>>>>>>>>>>>>>>>>>>>> old setup.py"
cat setup.py
echo ">>>>>>>>>>>>>>>>>>>>>> new setup.py"
sudo sed -i 's/version="[0-9\.]*"/version="'$newv'"/g' setup.py
cat setup.py

echo ">>>>>>>>>>>>>>>>>>>>>> old README.md"
cat README.md
sudo sed -i 's/branch=master/label='$newv'/g' README.md
echo ">>>>>>>>>>>>>>>>>>>>>> new README.md"
cat README.md

#build new packages
sudo python3 setup.py sdist bdist_wheel