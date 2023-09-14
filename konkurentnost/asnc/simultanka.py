import asyncio

async def levat(i):
    print(f"Levat {i}")
    await asyncio.sleep(1)

async def main():
    retval = await asyncio.gather(*(levat(i) for i in range(12)))
    return retval

if __name__ == "__main__":
    import time
    s = time.perf_counter()
    # nova definicija kreiranja event loop-a
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print(f"Izvrseno za {elapsed:0.2f} sekundi.")


## stara definicija kreiranja event loop-a
# loop = asyncio.get_event_loop() # ova linija je nekad zamijenjena sa create+set
# try:
#     loop.run_until_complete(main())
# finally:
#     loop.close()