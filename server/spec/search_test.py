from googlesearch import search 
from test import scrape_content_areas

query = "Virtual Idol"

urls = []

for j in search(query, lang="kr" , num=10, stop=10, pause=2, country="kr"):
    urls.append(j)

i = 1
for url in urls:
    res = scrape_content_areas(url)
    print("Bai ", i)
    print("url: ", url)
    print(res)
    print()
    i = i + 1
