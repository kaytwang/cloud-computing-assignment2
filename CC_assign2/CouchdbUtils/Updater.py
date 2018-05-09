# Created by Yuan Wang (yuanw8)
# Cloud and Cluster Computing Assignment 2
# Semester 1, 2018


from Connector import Connector
import time


class Updater:

    def __init__(self):
        self.dest_doc = '/mnt/results/twitterInfo.json'
        self.conn = Connector()

    def update_document(self):


        try:
            docs = self.conn.select_full_docs(self.conn.twitterdb_demo_results_pub)
            with open(self.dest_doc, 'w') as dest:
                for doc in docs:
                    dest.write(doc)
                    dest.write('\n')

        except BaseException:
            try:
                docs = self.conn.select_full_docs(self.conn.twitterdb0_demo_results_pub)
                with open(self.dest_doc, 'w') as dest:
                    for doc in docs:
                        dest.write(doc)
                        dest.write('\n')
            except BaseException:
                docs = self.conn.select_full_docs(self.conn.twitterdb1_demo_results_pub)
                with open(self.dest_doc, 'w') as dest:
                    for doc in docs:
                        dest.write(doc)
                        dest.write('\n')

        return

if __name__ == "__main__":

    updater = Updater()

    while True:
        updater.update_document()
        time.sleep(604800)








