import aiohttp
import asyncio
import time
from settings import BASE_DIR

async def download_file(url):
    print(f'Started downloading {url}')
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            content = await response.read()
            print(f'Finished downloading {url}')
            return content

def write_file(n, content):
    filename = BASE_DIR / f"web_scraping/async/f_{n}.html"
    with open(filename, "wb") as f:
        print(f'Started writing {filename}')
        f.write(content)
        print(f'Finished writing {filename}')

async def scrape_page(n, url):
    content = await download_file(url)
    await asyncio.to_thread(write_file, n, content)

async def main():
    tasks = []
    with open(BASE_DIR / f"web_scraping/urls.txt") as f:
        for n, url in enumerate(f.readlines()):
            tasks.append(asyncio.create_task(scrape_page(n, url)))
    await asyncio.wait(tasks)


def run():
    t = time.perf_counter()
    asyncio.run(main())
    tf = time.perf_counter() - t
    print(f'Total time elapsed: {tf:.2f} seconds')
