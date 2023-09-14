import logging
import threading
import time
from random import randint
from tdd.modules.projekat import Projekat
from tdd.modules.yaml_and_issues import loadIssues

# podijeli issue pa vladaj

def kreiranje_issuea(name, _issues):
    global projekat
    logging.info("Thread  : Startovanje kreiranja issuea %s", name)
    for i in _issues:
        logging.info("Thread  : %s kreira issue %s", name, i)
        # time.sleep(randint(1,2))
        try:
            projekat.addIssue(i)
            logging.info("Thread  : %s kreirao issue %s", name, i)
        except ValueError:
            pass

    logging.info("Thread  : Zavrsavanje %s", name)


if __name__ == "__main__":
    _format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=_format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    projekat = Projekat("Naziv Projekta")
    issues = loadIssues()

    osoba_issue = {"senior": issues[:2],
                   "vodja projekta": issues[2:5],
                   "klijent": issues[5:]}
    threads = {}
    for osoba in osoba_issue:
        logging.info("Main    : startovanje rada %s.", osoba)
        x = threading.Thread(target=kreiranje_issuea, args=(osoba, osoba_issue[osoba]))
        threads[osoba] = x
        x.start()

    for osoba in threads:
        logging.info("Main    : prije joina %s", osoba)
        threads[osoba].join()
        logging.info("Main    : zavrsen %s ", osoba)

    print("Uneseni isuei:")
    for i in projekat.issues:
        print("\t", i)
