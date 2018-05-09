import couchdb
import json

class Connector:

    def __init__(self):
        self.user = 'admin'
        self.pw = 'password'
        self.localhost = '127.0.0.1'
        self.ip0 = '115.146.84.191'
        self.ip2 = '115.146.86.111'
        self.ip3 = '115.146.86.90'

        self.couchdbserver0 = couchdb.Server("http://%s:%s@%s:5984/" % (self.user, self.pw, self.ip0))
        self.couchdbserver2 = couchdb.Server("http://%s:%s@%s:5984/" % (self.user, self.pw, self.ip2))
        self.couchdbserver3 = couchdb.Server("http://%s:%s@%s:5984/" % (self.user, self.pw, self.ip3))
        self.couchdbserver_pub = couchdb.Server("http://%s:%s@%s:80/" % (self.user, self.pw, self.ip2))

        self.SUCCEED = 'SUCCEED'
        self.DBEXISTED = 'DB EXISTED'
        self.DBNOTEXISTED = 'DB NOT EXISTED'
        self.RESOURCENOTFOUND = 'ResourceNotFound'
        self.PRECONDITIONFAILED = 'PreconditionFailed'

        self.TWITTERDB_NAME = 'twitterdb'
        self.testingDBName = 'testingdb'

        self.testingDB_pub = self.create_select_db(self.testingDBName, self.couchdbserver_pub)

        self.twitterdb0 = self.create_select_db(self.TWITTERDB_NAME, self.couchdbserver0)
        self.twitterdb2 = self.create_select_db(self.TWITTERDB_NAME, self.couchdbserver2)
        self.twitterdb3 = self.create_select_db(self.TWITTERDB_NAME, self.couchdbserver3)
        self.twitterdb_pub = self.create_select_db(self.TWITTERDB_NAME, self.couchdbserver_pub)

    def show_all_dbs(self, dbs):
        dbNames = []
        for dbname in dbs:
            dbNames.append(dbname)
        return dbNames

    def create_select_db(self, dbname, dbs):
        try:
            return dbs.create(dbname)
        except couchdb.http.PreconditionFailed:
            return dbs[dbname]

    def delete_select_db(self, dbname, dbs):
        try:
            dbs.delete(dbname)
            return self.SUCCEED
        except couchdb.http.ResourceNotFound:
            return self.DBNOTEXISTED

    def insert(self, doc, dbs):
        doc_id, doc_rev = dbs.save(self, doc)
        return doc_id, doc_rev

    def insert_update_with_id_key(self, id, doc, updateKey, updateValue, db):
        try:
            doc_rev = db[id] = doc
        except couchdb.http.ResourceConflict:
            doc = db.get(id)
            doc[updateKey] = updateValue
            doc_rev = db.save(doc)
        return doc_rev

    def insert_update_with_id(self, id, doc, db):
        json_d = json.loads(doc)
        try:
            db[id] = json_d
        except couchdb.http.ResourceConflict:
            pass
        return self.SUCCEED

    def insert_raw_twitter(self, doc, db):
        json_d = json.loads(doc)
        json_id = json_d['id_str']
        try:
            db[json_id] = json_d
        except couchdb.http.ResourceConflict:
            pass
        return self.SUCCEED

    def insert_with_id(self, id, doc, db):
        doc_rev = db[id] = doc
        return doc_rev

    def insert_file(self, path, db):
        with open(path) as json_file:
            collection = json_file.readlines()
            for line in collection:
                self.insert_raw_twitter(line, db)

    def select_doc(self, id, db):
        doc = db.get(id)
        return doc

    def select_all_docs(self, db):
        full_docs = []
        docs = db.view('_all_docs')
        for doc in docs:
            full_docs.append(self.select_doc(doc.id, db))
        return full_docs




