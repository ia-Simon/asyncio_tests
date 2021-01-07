import asyncio
import time

gen = (i for i in range(5))

async def count():
    await asyncio.sleep(1)
    print("1")
    await asyncio.sleep(1)
    print("2") 
    await asyncio.sleep(1)
    print("3")

async def main():
    return await asyncio.gather(count(), count(), count())

if __name__ == "__main__":
    print(asyncio.run(main()))