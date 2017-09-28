#!/bin/bash

echo '#### Create Virtual Environment ####'
VIRTUAL_ENV_NAME='env'
virtualenv $VIRTUAL_ENV_NAME

echo '#### Activate Virtual Environment ####'
source $VIRTUAL_ENV_NAME/bin/activate

echo '#### Install requirements ####'
pip install selenium

echo '#### Run tests ####'

echo "print('hello world')" > test.py
xvfb-run python test.py

echo ### deactivate virtual environment ###
deactivate