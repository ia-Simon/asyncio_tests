import requests
import time
from settings import BASE_DIR

def download_file(url):
    print(f'Started downloading {url}')
    response = requests.get(url)
    print(f'Finished downloading {url}')
    return response.content

def write_file(n, content):
    filename = BASE_DIR / f"web_scraping/sync/f_{n}.html"
    with open(filename, "wb") as f:
        print(f'Started writing {filename}')
        f.write(content)
        print(f'Finished writing {filename}')

def run():
    t = time.perf_counter()
    with open(BASE_DIR / f"web_scraping/urls.txt") as f:
        for n, url in enumerate(f.readlines()):
            content = download_file(url)
            write_file(n, content)
    tf = time.perf_counter() - t
    print(f'Total time elapsed: {tf:.2f} seconds')
