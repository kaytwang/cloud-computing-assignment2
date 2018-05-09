# Created by Yuan Wang (yuanw8)
# Cloud and Cluster Computing Assignment 2
# Semester 1, 2018

from Connector import Connector
conn = Connector()

conn.insert_file_pro_res('D:\\fatFiles\projectdata.json', conn.twitterdbpro_pub_result)

conn.insert_file('\home\kate\python.json', conn.twitterdb1)

conn.insert_file('\home\kate\python.json', conn.twitterdb2)

conn.insert_file_pro('cloud_data_doc_vic_line.json', conn.twitterdbpro2)
