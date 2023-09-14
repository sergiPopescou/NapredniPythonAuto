import logging
import concurrent.futures
from lista_issuea import ListaIssuea
import random

KRAJ = object()

def klijent(pipeline):
    for index in range(10):
        issue_ = random.randint(1, 101)
        logging.info("Klijent napravio issue: %s", issue_)
        pipeline.set_issue(issue_)

    # Kad je kraj, podesava se ova
    pipeline.set_issue(KRAJ)

def tehnicar(pipeline):
    issue_ = None
    while issue_ is not KRAJ:
        issue_ = pipeline.get_issue()
        if issue_ is not KRAJ:
            logging.info("Tehnicar na issuu: %s", issue_)

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    pipeline = ListaIssuea()
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(klijent, pipeline)
        executor.submit(tehnicar, pipeline)

import asyncio
async def unutrasnja_funkcija():
    # simuliramo neko cekanje
    await asyncio.sleep(1)
    return 1  # ovo je mjesto
async def vanjska_fja():
    # ovdje ide neki kod koji je sinhron

    # ovdje mozes da ides i radis nesto korisno
    # jer je ova unutrasnja funkcija spora
    # vrati se kada unutrasnja funkcija zavrsi
    retval = await unutrasnja_funkcija()

    # ovdje opet moze biti nekog koda
    return retval # ovo je mjesto