#!/usr/bin/env python
# -*- coding: utf-8 -*-
# import sqlite3
#
# sql = sqlite3.connect("sg1.db", check_same_thread=False)

import dataset

# connecting to a SQLite database
db = dataset.connect('sqlite:///sg1.db')

if __name__ == '__main__':
    with open("c:/sg1/sg1/data/TIMES1.INI", "r", -1) as fp:
        lines = fp.readlines()
        table, row = None, None
        for line in lines:
            line = line.strip().decode("big5")
            if line == "" or line.startswith(";"):
                continue
            line = line.split(";")[0]
            if line.startswith("["):
                if table is not None:
                    print row
                    db[table].insert(row)
                    table, row = None, None
                if line.startswith("[SYSTEM"):
                    table, row = "SYSTEM", dict(INDEX=line[1:-1])
                if line.startswith("[KING"):
                    table, row = "KING", dict(INDEX=line[1:-1])
                if line.startswith("[CITY"):
                    table, row = "CITY", dict(INDEX=line[1:-1])
                if line.startswith("[PATH"):
                    table, row = "PATH", dict(INDEX=line[1:-1])
                if line.startswith("[GENERAL"):
                    table, row = "GENERAL", dict(INDEX=line[1:-1])
            else:
                [key, value] = line.split("=")
                row[key.strip()] = value.strip()
        if table is not None:
            print row
            db[table].insert(row)
