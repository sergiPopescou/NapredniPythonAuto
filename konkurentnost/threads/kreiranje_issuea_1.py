import logging
import threading
import time
from random import randint

# Nit samo pomocu funkcije

def kreiranje_issuea(name):
    print("Thread  : Startovanje kreiranja issuea %s" % name)
    time.sleep(randint(1,5))
    print("Thread  : Zavrsavanje %s" % name)


if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    nazivi = ["senior", "vodja projekta","klijent"]
    threads = {}
    for osoba in nazivi:
        print("Main    : startovanje rada %s." % osoba)
        x = threading.Thread(target=kreiranje_issuea, args=(osoba,))
        threads[osoba] = x
        x.start()

    for osoba in threads:
        print("Main    : prije joina %s" % osoba)
        threads[osoba].join()
        print("Main    : zavrsen %s " % osoba)

    # # drugi nacin startovanja:
    # import concurrent.futures
    # with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
    #     executor.map(kreiranje_issuea, nazivi)