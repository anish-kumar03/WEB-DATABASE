"""
Custom Web Scraper - Interactive tool to scrape data from websites
Author: Anish
Date: November 4, 2025
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
import json
from datetime import datetime
import time

def scrape_website(url, scrape_type='basic'):
    """
    Scrape data from a given URL
    
    Args:
        url: Website URL to scrape
        scrape_type: Type of scraping - 'basic', 'detailed', 'tables', 'links'
    """
    print(f"\n{'='*70}")
    print(f"🌐 Scraping: {url}")
    print(f"{'='*70}\n")
    
    try:
        # Send HTTP request
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        # Parse HTML
        soup = BeautifulSoup(response.content, 'html.parser')
        
        print("✅ Successfully connected and parsed HTML!\n")
        
        results = {}
        
        if scrape_type == 'basic':
            # Basic text extraction
            results['title'] = soup.title.string if soup.title else "No title found"
            results['all_text'] = soup.get_text()[:500]  # First 500 chars
            
            # Count elements
            results['paragraphs'] = len(soup.find_all('p'))
            results['links'] = len(soup.find_all('a'))
            results['images'] = len(soup.find_all('img'))
            results['headings'] = len(soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6']))
            
            print(f"📄 Page Title: {results['title']}")
            print(f"\n📊 Page Statistics:")
            print(f"   • Paragraphs: {results['paragraphs']}")
            print(f"   • Links: {results['links']}")
            print(f"   • Images: {results['images']}")
            print(f"   • Headings: {results['headings']}")
            
        elif scrape_type == 'links':
            # Extract all links
            links = []
            for link in soup.find_all('a', href=True):
                links.append({
                    'text': link.get_text().strip(),
                    'url': link['href']
                })
            
            results['links'] = links
            print(f"🔗 Found {len(links)} links:\n")
            for i, link in enumerate(links[:10], 1):  # Show first 10
                print(f"   {i}. {link['text'][:50]} → {link['url'][:50]}")
            
            if len(links) > 10:
                print(f"   ... and {len(links)-10} more links")
                
        elif scrape_type == 'tables':
            # Extract tables
            tables = soup.find_all('table')
            results['tables'] = []
            
            print(f"📋 Found {len(tables)} tables:\n")
            
            for i, table in enumerate(tables, 1):
                try:
                    df = pd.read_html(str(table))[0]
                    results['tables'].append(df)
                    print(f"   Table {i}: {df.shape[0]} rows × {df.shape[1]} columns")
                    print(df.head())
                    print()
                except:
                    print(f"   Table {i}: Could not parse")
                    
        elif scrape_type == 'detailed':
            # Detailed extraction
            results['title'] = soup.title.string if soup.title else "No title"
            results['meta_description'] = ''
            
            meta = soup.find('meta', attrs={'name': 'description'})
            if meta:
                results['meta_description'] = meta.get('content', '')
            
            # Extract all headings
            headings = {}
            for level in ['h1', 'h2', 'h3']:
                headings[level] = [h.get_text().strip() for h in soup.find_all(level)]
            results['headings'] = headings
            
            # Extract paragraphs
            paragraphs = [p.get_text().strip() for p in soup.find_all('p')]
            results['paragraphs'] = paragraphs[:10]  # First 10
            
            print(f"📄 Title: {results['title']}")
            print(f"\n📝 Meta Description: {results['meta_description']}")
            print(f"\n📑 Headings Structure:")
            for level, heads in headings.items():
                if heads:
                    print(f"   {level.upper()}: {len(heads)} found")
                    for h in heads[:3]:
                        print(f"      • {h}")
            
            print(f"\n📄 First Few Paragraphs:")
            for i, p in enumerate(results['paragraphs'][:3], 1):
                print(f"   {i}. {p[:100]}...")
        
        return results, soup
        
    except requests.exceptions.RequestException as e:
        print(f"❌ Error connecting to website: {e}")
        return None, None
    except Exception as e:
        print(f"❌ Error parsing website: {e}")
        return None, None


def save_results(results, filename=None):
    """Save scraped results to file"""
    if filename is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"scraped_data_{timestamp}.json"
    
    with open(filename, 'w', encoding='utf-8') as f:
        # Convert any DataFrames to dictionaries for JSON serialization
        serializable_results = {}
        for key, value in results.items():
            if isinstance(value, pd.DataFrame):
                serializable_results[key] = value.to_dict()
            elif isinstance(value, list) and len(value) > 0 and isinstance(value[0], pd.DataFrame):
                serializable_results[key] = [df.to_dict() for df in value]
            else:
                serializable_results[key] = value
        
        json.dump(serializable_results, f, indent=2, ensure_ascii=False)
    
    print(f"\n💾 Results saved to: {filename}")


def main():
    """Main interactive function"""
    print("""
╔════════════════════════════════════════════════════════════════════╗
║           🕷️  CUSTOM WEB SCRAPER - INTERACTIVE MODE 🕷️            ║
╚════════════════════════════════════════════════════════════════════╝
    """)
    
    # Example websites to try
    print("\n📌 Example websites you can scrape:")
    print("   1. https://quotes.toscrape.com - Practice scraping site")
    print("   2. https://books.toscrape.com - Books catalog")
    print("   3. https://en.wikipedia.org/wiki/Python_(programming_language)")
    print("   4. https://news.ycombinator.com - Tech news")
    print("   5. Any other website (be respectful of robots.txt)\n")
    
    url = input("🌐 Enter website URL to scrape: ").strip()
    
    if not url:
        print("❌ No URL provided. Using default example...")
        url = "https://quotes.toscrape.com"
    
    print("\n📋 Choose scraping type:")
    print("   1. Basic - Quick overview (paragraphs, links, images count)")
    print("   2. Links - Extract all links from page")
    print("   3. Tables - Extract all tables (if any)")
    print("   4. Detailed - Full extraction (headings, paragraphs, metadata)")
    
    choice = input("\nEnter choice (1-4): ").strip()
    
    scrape_types = {
        '1': 'basic',
        '2': 'links',
        '3': 'tables',
        '4': 'detailed'
    }
    
    scrape_type = scrape_types.get(choice, 'basic')
    
    # Scrape the website
    results, soup = scrape_website(url, scrape_type)
    
    if results:
        # Ask if user wants to save
        save = input("\n💾 Save results to file? (y/n): ").strip().lower()
        if save == 'y':
            save_results(results)
        
        print("\n✅ Scraping completed successfully!")
    else:
        print("\n❌ Scraping failed. Please check the URL and try again.")
    
    print(f"\n{'='*70}\n")


if __name__ == "__main__":
    main()
