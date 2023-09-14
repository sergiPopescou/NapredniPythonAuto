import logging
import threading
import time
from random import randint
from tdd.modules.projekat import Projekat
from tdd.modules.yaml_and_issues import loadIssues

# odrzavanje redoslijeda sa semaforom

def kreiranje_issuea():
    name = "Klijent"
    global projekat
    logging.info("Thread  : Startovanje kreiranja issuea %s", name)
    issues = loadIssues()
    for i in issues:
        logging.info("Thread  : %s kreira issue %s", name, i)
        # time.sleep(randint(1,10))
        try:
            projekat.dodajIssue(i)
            logging.info("Thread  : %s kreirao issue %s", name, i)
        except ValueError:
            pass
    logging.info("Thread  : Zavrsavanje %s", name)


def koristenje_issuea(name, sleep_time):
    global projekat
    global semaphores
    global counters
    logging.info("Thread  : Startovanje koristenja issuea %s", name)

    while True:
        logging.info("Thread  : %s pokusava da uzme neki issue", name)
        semaphores[name].acquire()  # -1
        if len(projekat.issues) > 0:
            i = projekat.issues.pop(0)
            counters[name] += 1
        else:
            break
        logging.info("Thread  : %s uzeo sebi issue %s", name, i)
        time.sleep(sleep_time)
        semaphores[get_other_thread_name(name)].release()

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

    klijent_thread = threading.Thread(target=kreiranje_issuea)
    klijent_thread.start()
    klijent_thread.join()
    logging.info("Main    : završen klijent")

    osobe = [
        ("senior", 2),
        ("vodja projekta",0)]
    threads = {}
    semaphores = {}
    counters = {}
    for osoba in osobe:
        logging.info("Main    : startovanje rada %s.", osoba[0])
        x = threading.Thread(target=koristenje_issuea, args=osoba)
        threads[osoba[0]] = x
        semaphores[osoba[0]] = threading.Semaphore()
        counters[osoba[0]] = 0

        semaphores["senior"].release()

        x.start()

    for osoba in threads:
        logging.info("Main    : prije joina %s", osoba)
        threads[osoba].join()
        logging.info("Main    : zavrsen %s ", osoba)

    print("NEPREUZETI isuei:")
    for i in projekat.issues:
        print("\t", i)

    for osoba in counters:
        print(osoba, counters[osoba])