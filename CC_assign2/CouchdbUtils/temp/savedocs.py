# Created by Yuan Wang (yuanw8)
# Cloud and Cluster Computing Assignment 2
# Semester 1, 2018

from Connector import Connector
from json import dumps, loads

conn = Connector()

docs = conn.select_full_docs(conn.testingDB_pub)
with open('~/cloud_data/cloud_data_vic.json', 'w') as f:
    for doc in docs:
        f.write(dumps(doc))
        f.write('\n')


with open('cloud_data_doc_vic.json', 'r') as r:
    with open('cloud_data_doc_vic_line.json', 'w') as w:
        d = r.readline()
        json_d = loads(d)
        for twi in json_d["rows"]:
            w.write(dumps(twi))
            w.write('\n')

