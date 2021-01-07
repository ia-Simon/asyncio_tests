import settings
import sys
from web_scraping import (
    sync_scrape,
     async_scrape
)

if __name__ == "__main__":
    if "scrape" in sys.argv:
        if "--sync" in sys.argv:
            sync_scrape.run()
        if "--async" in sys.argv:
            async_scrape.run()