class AbstractPersister():
    def persist(self, _object):
        pass

class PrintPersister(AbstractPersister):
    def persist(self, _object):
        print(_object)

class FilePersister(AbstractPersister):
    def __init__(self, filename):
        self.filename = filename
    def persist(self, _object):
        with open(self.filename, "w") as f:
            f.write(str(_object))


class DBPersister(AbstractPersister):
    def __init__(self, db_url, credentials):
        self.db_url = db_url
        self.credentials = credentials

    def persist(self, _object):
        print(f"open db on db_ulr {self.db_url} with credentials")
        print(_object)
        print("close db")
