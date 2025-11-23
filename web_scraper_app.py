"""
Web Scraper - Flask Web Application
Interactive web interface for scraping websites
Author: Anish
Date: November 23, 2025
"""

from flask import Flask, render_template, request, jsonify, send_file
import requests
from bs4 import BeautifulSoup
import pandas as pd
import json
from datetime import datetime
import os

app = Flask(__name__)

# Create results directory if it doesn't exist
RESULTS_DIR = 'scraping_results'
if not os.path.exists(RESULTS_DIR):
    os.makedirs(RESULTS_DIR)


def scrape_website(url, scrape_type='basic'):
    """
    Scrape data from a given URL
    
    Args:
        url: Website URL to scrape
        scrape_type: Type of scraping - 'basic', 'detailed', 'tables', 'links'
    
    Returns:
        dict: Scraped results with status
    """
    try:
        # Send HTTP request
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        # Parse HTML
        soup = BeautifulSoup(response.content, 'html.parser')
        
        results = {
            'status': 'success',
            'url': url,
            'scrape_type': scrape_type,
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        
        if scrape_type == 'basic':
            # Basic text extraction
            results['data'] = {
                'title': soup.title.string if soup.title else "No title found",
                'paragraphs_count': len(soup.find_all('p')),
                'links_count': len(soup.find_all('a')),
                'images_count': len(soup.find_all('img')),
                'headings_count': len(soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])),
                'preview_text': soup.get_text()[:500].strip()
            }
            
        elif scrape_type == 'links':
            # Extract all links
            links = []
            for link in soup.find_all('a', href=True):
                links.append({
                    'text': link.get_text().strip()[:100],
                    'url': link['href']
                })
            
            results['data'] = {
                'title': soup.title.string if soup.title else "No title",
                'total_links': len(links),
                'links': links[:100]  # Limit to 100 links for display
            }
                
        elif scrape_type == 'tables':
            # Extract tables
            tables = soup.find_all('table')
            table_data = []
            
            for i, table in enumerate(tables[:10], 1):  # Limit to 10 tables
                try:
                    df = pd.read_html(str(table))[0]
                    table_data.append({
                        'table_number': i,
                        'rows': df.shape[0],
                        'columns': df.shape[1],
                        'data': df.head(20).to_dict('records')  # First 20 rows
                    })
                except:
                    table_data.append({
                        'table_number': i,
                        'error': 'Could not parse table'
                    })
            
            results['data'] = {
                'title': soup.title.string if soup.title else "No title",
                'total_tables': len(tables),
                'tables': table_data
            }
                    
        elif scrape_type == 'detailed':
            # Detailed extraction
            meta = soup.find('meta', attrs={'name': 'description'})
            meta_description = meta.get('content', '') if meta else ''
            
            # Extract all headings
            headings = {
                'h1': [h.get_text().strip() for h in soup.find_all('h1')],
                'h2': [h.get_text().strip() for h in soup.find_all('h2')],
                'h3': [h.get_text().strip() for h in soup.find_all('h3')]
            }
            
            # Extract paragraphs
            paragraphs = [p.get_text().strip() for p in soup.find_all('p') if p.get_text().strip()]
            
            results['data'] = {
                'title': soup.title.string if soup.title else "No title",
                'meta_description': meta_description,
                'headings': headings,
                'paragraphs': paragraphs[:20],  # First 20 paragraphs
                'total_paragraphs': len(paragraphs)
            }
        
        return results
        
    except requests.exceptions.RequestException as e:
        return {
            'status': 'error',
            'message': f'Connection error: {str(e)}',
            'url': url
        }
    except Exception as e:
        return {
            'status': 'error',
            'message': f'Parsing error: {str(e)}',
            'url': url
        }


@app.route('/')
def index():
    """Render the main page"""
    return render_template('index.html')


@app.route('/scrape', methods=['POST'])
def scrape():
    """Handle scraping request"""
    data = request.get_json()
    url = data.get('url', '').strip()
    scrape_type = data.get('scrape_type', 'basic')
    
    if not url:
        return jsonify({
            'status': 'error',
            'message': 'Please provide a URL'
        })
    
    # Add http:// if not present
    if not url.startswith(('http://', 'https://')):
        url = 'https://' + url
    
    # Scrape the website
    results = scrape_website(url, scrape_type)
    
    # Save results to file if successful
    if results.get('status') == 'success':
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{RESULTS_DIR}/scraped_{timestamp}.json"
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(results, f, indent=2, ensure_ascii=False)
        
        results['saved_file'] = filename
    
    return jsonify(results)


@app.route('/download/<filename>')
def download(filename):
    """Download scraped results"""
    filepath = os.path.join(RESULTS_DIR, filename)
    if os.path.exists(filepath):
        return send_file(filepath, as_attachment=True)
    return jsonify({'status': 'error', 'message': 'File not found'})


if __name__ == '__main__':
    print("""
╔════════════════════════════════════════════════════════════════════╗
║              🕷️  WEB SCRAPER - WEB INTERFACE 🕷️                   ║
╚════════════════════════════════════════════════════════════════════╝

Starting Flask server...
Open your browser and go to: http://localhost:5000

Press CTRL+C to stop the server
    """)
    
    app.run(debug=True, host='0.0.0.0', port=5000)
