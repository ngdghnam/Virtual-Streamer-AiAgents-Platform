from bs4 import BeautifulSoup
import requests
import re

def scrape_content_areas(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    
    title = soup.title.string
    
    # Try to find main content areas (adjust selectors based on website structure)
    content_selectors = [
        'article', 'main', '.content', '#content', 
        '.post-content', '.article-content', 'div.content',
        'p'  # fallback to all paragraphs
    ]
    
    content_text = ""
    
    for selector in content_selectors:
        elements = soup.select(selector)
        if elements:
            for element in elements:
                # Remove images from each content element
                for img in element.find_all('img'):
                    img.decompose()
                content_text += element.get_text(separator=' ', strip=True) + " "
            break  # Use first successful selector
    
    # Clean the text
    clean_text = re.sub(r'\s+', ' ', content_text).strip()

    data = {
        "title": title,
        "content": clean_text
    }
    
    return data
