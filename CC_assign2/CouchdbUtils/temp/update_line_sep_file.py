from Connector import Connector
conn = Connector()

conn.insert_file_pro_res('employ2006.json', conn.vic_suburbs_info)

conn.insert_file_pro_res('504target.json', conn.twitterdb_info)

conn.insert_file_pro('twitterdocs504.json', conn.twitterdb504_3)



