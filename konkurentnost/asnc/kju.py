import asyncio
import itertools as it
import os
import random
import time
import yaml
from tdd.modules.issue import Issue, Nivo

async def loadIssues(producer_name, q, filePath=None):
    if filePath is None:
        filePath = os.sep.join([os.getcwd(), "..", "klijent_issues.yaml"])
    with open(filePath, 'r') as f:
        issues = list(yaml.load_all(f, Loader=yaml.SafeLoader))
        for issue_ in issues[0]["issues"]:
            await randsleep(caller=f"Producer {producer_name}")
            nivo = Nivo.createNivo(issue_['nivo'])
            i = Issue(issue_['naziv'], nivo=nivo)
            t = time.perf_counter()
            await q.put((i, t))
            print(f"Producer {producer_name} added issue <{i}> to queue.")
        return len(issues[0])

async def randsleep(caller=None):
    i = random.randint(0, 10)
    if caller:
        print(f"{caller} sleeping for {i} seconds.")
    await asyncio.sleep(i)

async def produce(name, q, filePath=None):
    count = await loadIssues(name, q, filePath)
    print(f"Producer {name} added {count} issues to queue.")

async def consume(name, q):
    while True:
        await randsleep(caller=f"Consumer {name}")
        i, t = await q.get()
        now = time.perf_counter()
        print(f"Consumer {name} got issue <{i}>"
              f" in {now-t:0.5f} seconds.")
        q.task_done()

async def main():
    q = asyncio.Queue()
    files = ["issues.yml", "klijent_issues.yaml"]
    producers = [asyncio.create_task(produce(file, q,
                                             os.sep.join([os.getcwd(), "..", file])))
                 for file in files]
    consumers = [asyncio.create_task(consume(n, q)) for n in range(3)]
    await asyncio.gather(*producers)
    await q.join()  # Implicitly awaits consumers, too
    for c in consumers:
        c.cancel()

if __name__ == "__main__":
    random.seed(123)
    start = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - start
    print(f"Program completed in {elapsed:0.5f} seconds.")