import asyncio
import time


# Synchronous code
def sync_f():
    print("one", end="")
    time.sleep(1)
    print("two", end="")


# Asynchronous code
async def async_f():
    print("one", end="")
    await asyncio.sleep(1)
    print("two", end="")


async def main():
    tasks = [async_f() for _ in range(3)]

    await asyncio.gather(*tasks)


asyncio.run(main())
