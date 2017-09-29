#!/bin/bash

echo '#### Create Virtual Environment ####'
VIRTUAL_ENV_NAME='env'
virtualenv $VIRTUAL_ENV_NAME

echo '#### Activate Virtual Environment ####'
source $VIRTUAL_ENV_NAME/bin/activate

echo '#### Install requirements ####'
pip install -r requirements.txt

echo '#### Run tests ####'

echo "print('hello world')" > test.py
python test.py

echo "********* Running github selenium script now **************"
python github.py

echo '### deactivate virtual environment ###'
deactivate
