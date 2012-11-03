xhprof Profiled Data Extraction Script
======================================

Extracts profiling data from xhprof details table. The script populates new
table `parent_child` with parent->child relationship along with profile
information.

Usage
=====
Change `config.py` and execute `run.py`. Sample config file is:
    config = {
        "db": {
            "name": "xhprof",    #database name
            "host": "localhost", #database host
            "port": 3306,        #database port
            "user": "root",      #database user
            "pass": ""           #password for db user
        },
        "logs": {
            "dir": os.getcwd() + "/logs", #directory where logs should be written
            "prefix": "xhprofextract"     #prefix for log files
        }
    }
