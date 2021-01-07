import time
import asyncio

async def async_print():
    for i in "ab":
        print(i)
        await asyncio.sleep(1)
    print("Hello")


async def run():
    result = asyncio.create_task(async_print())
    result2 = asyncio.create_task(async_print())
    await asyncio.sleep(1)
    print("World")
    resp = await result, await result2
    print("O")
    return resp
    
    
event_loop = asyncio.get_event_loop()
try:
    resp = event_loop.run_until_complete(run())
    print(resp)
finally:
    event_loop.close()

