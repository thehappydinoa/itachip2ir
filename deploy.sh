#!/usr/bin/env bash

rm dist/*
python3 setup.py sdist bdist_wheel
python2 setup.py sdist bdist_wheel

pip install -r dev-requirements.txt --user

twine upload dist/*
