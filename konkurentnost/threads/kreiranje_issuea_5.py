import logging
import threading
import time
from random import randint
from tdd.modules.projekat import Projekat
from tdd.modules.yaml_and_issues import loadIssues

# klijent pravi issue, a senior i vodja ih uzimaju cim budu u situaciji

def kreiranje_issuea():
    name = "Klijent"
    global projekat
    global semaphore
    logging.info("Thread  : Startovanje kreiranja issuea %s", name)
    issues = loadIssues()
    for i in issues:
        logging.info("Thread  : %s kreira issue %s", name, i)
        time.sleep(randint(1,2))
        try:
            projekat.addIssue(i)
            semaphore.release()
            logging.info("Thread  : %s kreirao issue %s", name, i)
        except ValueError:
            pass
    logging.info("Thread  : Zavrsavanje %s", name)


def koristenje_issuea(name, sleep_time):
    global projekat
    global semaphore
    global counters
    global klijent_zavrsio
    logging.info("Thread  : Startovanje koristenja issuea %s", name)

    while True:
        logging.info("Thread  : %s pokusava da uzme neki issue", name)
        semaphore.acquire()  # -1
        if len(projekat.issues) > 0:
            i = projekat.issues.pop(0)
            counters[name] += 1
            logging.info("Thread  : %s uzeo sebi issue %s", name, i)
            time.sleep(sleep_time)
        else:
            if klijent_zavrsio:
                break

    logging.info("Thread  : Zavrsavanje %s", name)

def get_other_thread_name(name):
    if name == "senior":
        return "vodja projekta"
    return "senior"

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    exit_when_empty = False
    projekat = Projekat("Naziv Projekta")

    semaphore = threading.Semaphore()
    klijent_zavrsio = False
    klijent_thread = threading.Thread(target=kreiranje_issuea)
    klijent_thread.start()

    osobe = [
        ("senior", 2),
        ("vodja projekta",1)]
    threads = {}
    counters = {}
    for osoba in osobe:
        logging.info("Main    : startovanje rada %s.", osoba[0])
        x = threading.Thread(target=koristenje_issuea, args=osoba)
        threads[osoba[0]] = x
        counters[osoba[0]] = 0

        x.start()

    klijent_thread.join()
    klijent_zavrsio = True
    logging.info("Main    : završen klijent")

    for osoba in threads:
        logging.info("Main    : prije joina %s", osoba)
        semaphore.release()
        threads[osoba].join()
        logging.info("Main    : zavrsen %s ", osoba)

    print("NEPREUZETI isuei:")
    for i in projekat.issues:
        print("\t", i)

    for osoba in counters:
        print(osoba, counters[osoba])