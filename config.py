import os

config = {
    "db": {
        "name": "xhprof",
        "host": "localhost",
        "port": 3306,
        "user": "root",
        "pass": "lasvegas"
    },
    "logs": {
        "dir": os.getcwd() + "/logs",
        "prefix": "xhprofextract"
    }
}
