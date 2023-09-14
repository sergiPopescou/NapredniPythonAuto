import logging
import threading
import time
from random import randint

# nit pomocu klase Thread

class Kreator(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        logging.info("Thread  : Startovanje kreiranja issuea %s", self.name)
        time.sleep(randint(1,5))
        logging.info("Thread  : Zavrsavanje %s", self.name)


if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    nazivi = ["senior", "vodja projekta","klijent"]
    threads = {}
    for osoba in nazivi:
        logging.info("Main    : startovanje rada %s.", osoba)
        x = Kreator(osoba)
        threads[osoba] = x

    for osoba in threads:
        threads[osoba].start()

    for osoba in threads:
        logging.info("Main    : prije joina %s", osoba)
        threads[osoba].join()
        logging.info("Main    : zavrsen %s ", osoba)