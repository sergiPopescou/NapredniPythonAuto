import time

def levat(i):
    print(f"Levat {i}")
    time.sleep(1)


if __name__ == "__main__":
    s = time.perf_counter()
    for i in range(12):
        levat(i)
    elapsed = time.perf_counter() - s
    print(f"Izvrseno za {elapsed:0.2f} sekundi.")