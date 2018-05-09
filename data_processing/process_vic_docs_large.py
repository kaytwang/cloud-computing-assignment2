# from Connector import Connector
from json import dumps, loads

with open('cloud_data_doc_vic.json', 'r') as r:
    with open('cloud_data_doc_vic_line.json', 'w') as w:
        for line in r:
            try:
                target = line[:-3]
                json = loads(target)
                w.write(target)
                w.write('\n')
                # print(target)
            except ValueError:
                print(target)
                pass
        print(target)







