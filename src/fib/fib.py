import time
import asyncio

def fib(n):
    if n == 0:
        return 0
    elif 0 < n <= 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

async def a_fib(n):
    if n == 0:
        return 0
    elif 0 < n <= 2:
        return 1
    else:
        return sum(await asyncio.gather(a_fib(n - 1), a_fib(n - 2)))

t = time.perf_counter()
result = fib(40)
tf = time.perf_counter() - t
print(f"Total time elapsed: {tf} seconds; Result: {result}")

# t = time.perf_counter()
# result = asyncio.run(a_fib(40))
# tf = time.perf_counter() - t
# print(f"Total time elapsed: {tf} seconds; Result: {result}")
