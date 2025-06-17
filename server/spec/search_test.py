from googlesearch import search
from test import scrape_content_areas
import time

query = "Virtual Idol"
urls = []

try:
    # Fix: Use only supported parameters for googlesearch-python
    # Different versions have different parameter names
    
    # Try the most common parameter combinations
    try:
        # Version 1: Basic parameters only
        search_results = search(query, num=10, stop=10, pause=2)
    except TypeError:
        try:
            # Version 2: Even more basic
            search_results = search(query, num_results=10)
        except TypeError:
            # Version 3: Most basic version
            search_results = search(query)
    
    for url in search_results:
        urls.append(url)
        if len(urls) >= 10:  # Limit to 10 results
            break
        
except Exception as e:
    print(f"Search error: {e}")
    # Fallback: manual URLs for Virtual Idol
    urls = [
        "https://en.wikipedia.org/wiki/Virtual_idol",
        "https://virtualyoutuber.fandom.com/wiki/Virtual_YouTuber",
        "https://www.crunchyroll.com/news/features/2021/1/15/the-rise-of-virtual-idols",
    ]

print(f"Found {len(urls)} URLs to scrape")

i = 1
for url in urls:
    try:
        res = scrape_content_areas(url)
        print(f"Bai {i}")
        print(f"url: {url}")
        print(res)
        print()
        i += 1
        time.sleep(1)  # Be respectful with delays
    except Exception as e:
        print(f"Error scraping {url}: {e}")
        i += 1