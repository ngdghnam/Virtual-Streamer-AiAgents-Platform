from bs4 import BeautifulSoup
import requests
import re

url = 'https://vnexpress.net/tong-bi-thu-tinh-lam-dong-moi-du-suc-hut-nguon-luc-chien-luoc-4896551.html'

# Method 1: Remove images before extracting text
def scrape_without_images_method1(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    
    
    
    # Remove all img tags
    for img in soup.find_all('img'):
        img.decompose()  # completely removes the tag
    
    # Remove other elements that might cause spacing issues
    for element in soup.find_all(['script', 'style', 'meta', 'link']):
        element.decompose()
    
    text = soup.get_text()
    
    # Clean up the text
    clean_text = re.sub(r'(?<![\.\?!])\n', ' ', text)
    clean_text = re.sub(r'\s+', ' ', clean_text).strip()
    
    return clean_text

# Method 3: Target specific content areas (recommended) ==> CHOOSE
def scrape_content_areas(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    
    
    
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
    
    return clean_text

# Method 4: Advanced cleaning with multiple filters
def scrape_advanced_cleaning(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    
    
    
    # Remove all unwanted elements
    unwanted_elements = [
        'img', 'script', 'style', 'meta', 'link', 'noscript',
        'header', 'footer', 'nav', 'aside', 'advertisement',
        '.ad', '.advertisement', '.sidebar'
    ]
    
    for selector in unwanted_elements:
        for element in soup.select(selector):
            element.decompose()
    
    # Extract text with proper spacing
    text = soup.get_text(separator='\n', strip=True)
    
    # Multiple cleaning steps
    lines = text.split('\n')
    cleaned_lines = []
    
    for line in lines:
        line = line.strip()
        if line and len(line) > 2:  # Filter out very short lines
            cleaned_lines.append(line)
    
    # Join lines with single space
    clean_text = ' '.join(cleaned_lines)
    
    # Final cleanup
    clean_text = re.sub(r'\s+', ' ', clean_text)
    clean_text = re.sub(r'[\r\n\t]+', ' ', clean_text)
    
    return clean_text.strip()
