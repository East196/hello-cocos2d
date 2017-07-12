#!/usr/bin/env python
# -*- coding: utf-8 -*-
import dataset

# connecting to a SQLite database
db = dataset.connect('sqlite:///sg1.db')
print db['GENERAL'].find_one()