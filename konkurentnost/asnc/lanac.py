import asyncio
import random
import time
class Event(object):

    def __init__(self):
        self.__eventhandlers = []

    def __iadd__(self, handler):
        self.__eventhandlers.append(handler)
        return self

    def __isub__(self, handler):
        self.__eventhandlers.remove(handler)
        return self

    async def chain(self):
        start = time.perf_counter()
        first_call = True
        for eventhandler in self.__eventhandlers:
            if first_call:
                first_call = False
                x = await eventhandler()
            else:
                x = await eventhandler(x)
        end = time.perf_counter() - start
        print(f"-->Chained result (took {end:0.2f} seconds).")

    def __call__(self, *args, **keywargs):
        asyncio.run(self.chain())


class Police(object):
    def __init__(self, policeTelephoneNo):
        self._telephone = policeTelephoneNo

    async def callPolice(self, call):
        print(f"police is calling on {self._telephone}")
        await asyncio.sleep(1)
        i = random.randint(6, 10)
        print(f"police is comming... For {i} minutes")
        return i


class Owner(object):
    def __init__(self, ownerMobile):
        self.__mobile = ownerMobile

    async def messageAndCall(self, police_response):
        print(f"owner has been messaged on {self.__mobile}: Police responses for {police_response}")
        print(f"owner has been called on {self.__mobile}")
        await asyncio.sleep(1)
        print("owner called")
        i = random.randint(0, 10)
        print(f"real threat: {i>2}")
        return i > 2  # if False, then false alarm


class Alarm(object):

    async def setAlarm(self):
        await asyncio.sleep(0.01)
        print("Alarm has started")
        return True
    async def clearAlarm(self, realThreat):
        if not realThreat:
            await asyncio.sleep(0.01)
            print("Alarm cleared")
        else:
            print("Alarm not cleared")


class House(object):

    def __init__(self):
        self.OnLockBroken = Event()

    def lockBroken(self):
        self.OnLockBroken()

    def addSubscriber(self, method):
        self.OnLockBroken += method

    def removeSubscriber(self, method):
        self.OnLockBroken -= method


def main():
    random.seed(123)

    house = House()
    police = Police(122)
    owner = Owner(387656565)
    alarm = Alarm()

    house.addSubscriber(alarm.setAlarm)
    house.addSubscriber(police.callPolice)
    house.addSubscriber(owner.messageAndCall)
    house.addSubscriber(alarm.clearAlarm)

    house.lockBroken()


if __name__ == "__main__":
    main()
