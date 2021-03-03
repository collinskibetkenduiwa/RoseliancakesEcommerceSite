#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __init__ import py, virtualenv


def fixture():
    "Django Syncdb"
    with virtualenv():
        py('python3 manage.py dumpdata --format=json >fixtures/initial_data.json')

def fixture_load():
    with virtualenv():
        py('python3 manage.py loaddata fixtures/initial_data.json')