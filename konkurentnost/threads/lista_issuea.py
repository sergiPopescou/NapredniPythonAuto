import threading
class ListaIssuea:
    """
    Queue issuea
    """
    def __init__(self):
        self.issues = []
        self.klijent_lock = threading.Lock()
        self.tehnicar_lock = threading.Lock()
        self.tehnicar_lock.acquire()

    def get_issue(self):
        self.tehnicar_lock.acquire()
        i = self.issues.pop(0)
        self.klijent_lock.release()
        return i

    def set_issue(self, issue_):
        self.klijent_lock.acquire()
        self.issues.append(issue_)
        self.tehnicar_lock.release()