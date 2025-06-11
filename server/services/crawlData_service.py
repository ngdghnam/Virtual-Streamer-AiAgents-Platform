from utils.crawl import scrape_content_areas

class CrawlDataService: 
    def getContextFromURL(url):
        return scrape_content_areas(url)