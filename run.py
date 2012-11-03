#!/usr/bin/python

import __builtin__
from config import config
from lib import logger
from lib.db import mysql
from lib import sql
from third_party.progressbar import ProgressBar
import time
import math
import zlib
import json

#shutdown hook
import atexit
@atexit.register
def _on_shutdown():
    print "FINISHED"

print "Extracting data from xhprof details"

#Global variables
__builtin__.logger = logger
__builtin__.xhprof_config = config

print "Creating tables"
mysql.write(sql.DROP_TBL_PERFDATA)
mysql.write(sql.CREATE_TBL_PERFDATA)
mysql.write(sql.CREATE_TBL_PARENT_CHILD)
print "Tables created"

print "Getting profiler data"
(num_rows, res) = mysql.query(sql.SELECT_DETAILS)
print "%d Requests profiled" % (num_rows)
p = ProgressBar()

print "Analyzing Runs"
i = 0
row = res.fetchone()
while row:
    p.render((i*100/num_rows), "Run-%d#%s" % (i +1, row["id"]))
    data = row["perfdata"]
    data_hash = json.loads(zlib.decompress(data))
    for k, v in data_hash.iteritems():
        parent = child = None
        try:
            (parent, child) = k.split("==>")
        except ValueError as e:
            parent = ""
            child = k
        params = {
            "run_id": row["id"],
            "key": k,
            "parent": parent,
            "child": child,
            "callnum": v["ct"],
            "walltime": v["wt"],
            "proc": v["cpu"],
            "mem": v["mu"],
            "peakmem": v["pmu"],
            "rec_on": row["timestamp"]
        }
        mysql.write((sql.INSERT_INTO_PC, params))
    row = res.fetchone()
    i = i + 1
p.render(100, "Run-%d" % i)
