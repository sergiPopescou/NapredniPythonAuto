import logging
import threading
import time
from random import randint
from tdd.modules.projekat import Projekat
from tdd.modules.yaml_and_issues import loadIssues

# pazim da niko nikome ne udje u posao pomocu muteksa

def kreiranje_issuea(name, issues):
    global projekat
    global pointer_mutex
    global pointer_
    logging.info("Thread  : Startovanje kreiranja issuea %s", name)
    while pointer_ < len(issues):

        with pointer_mutex:
            i = issues[pointer_]
            pointer_ += 1

        logging.info("Thread  : %s kreira issue %s", name, i)
        time.sleep(randint(1,2))
        try:
            projekat.addIssue(i)
            logging.info("Thread  : %s kreirao issue %s", name, i)
        except ValueError:
            pass

    logging.info("Thread  : Zavrsavanje %s", name)


if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    projekat = Projekat("Naziv Projekta")
    issues = loadIssues()

    nazivi = ["senior", "vodja projekta", "klijent"]
    threads = {}
    pointer_ = 0
    pointer_mutex = threading.Lock()
    for osoba in nazivi:
        logging.info("Main    : startovanje rada %s.", osoba)
        x = threading.Thread(target=kreiranje_issuea, args=(osoba, issues))
        threads[osoba] = x
        x.start()

    for osoba in threads:
        logging.info("Main    : prije joina %s", osoba)
        threads[osoba].join()
        logging.info("Main    : zavrsen %s ", osoba)

    print("Uneseni isuei:")
    for i in projekat.issues:
        print("\t", i)