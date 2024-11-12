import requests
from bs4 import BeautifulSoup
import html
from datetime import datetime
import os

class WebScraper:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }

    def fetch_page(self, url):
        """Fetch a webpage and return its content"""
        try:
            response = requests.get(url.strip(), headers=self.headers)
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            print(f"Error fetching {url}: {str(e)}")
            return None

    def extract_content(self, html_content, url):
        """Extract relevant content from HTML"""
        if not html_content:
            return None

        soup = BeautifulSoup(html_content, 'html.parser')
        
        # Extract metadata
        metadata = {
            'title': soup.title.string if soup.title else 'No title',
            'meta_description': soup.find('meta', {'name': 'description'})['content'] if soup.find('meta', {'name': 'description'}) else 'No description',
            'url': url,
            'date_scraped': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }

        # Extract main content (looking for common content containers)
        main_content = soup.find('main') or soup.find('article') or soup.find('div', {'id': ['content', 'main-content']})
        if not main_content:
            main_content = soup.find('body')

        # Keep only desired HTML elements and their content
        allowed_tags = ['h1', 'h2', 'h3', 'h4', 'p', 'table', 'tr', 'td', 'th', 'strong', 'em', 'b', 'i']
        for tag in main_content.find_all():
            if tag.name not in allowed_tags:
                tag.unwrap()

        return {
            'metadata': metadata,
            'content': str(main_content)
        }

    def create_document(self, urls, output_file='scraped_content.html'):
        """Create a single HTML document from multiple URLs"""
        document_parts = []
        document_parts.append("""
            <!DOCTYPE html>
            <html>
            <head>
                <meta charset="UTF-8">
                <title>Scraped Content</title>
                <style>
                    body { font-family: Arial, sans-serif; line-height: 1.6; max-width: 800px; margin: 0 auto; padding: 20px; }
                    .page-section { border: 1px solid #ccc; margin: 20px 0; padding: 20px; border-radius: 5px; }
                    .metadata { background: #f5f5f5; padding: 10px; margin-bottom: 15px; border-radius: 3px; }
                    .content { margin-top: 15px; }
                    h1 { color: #2c3e50; }
                    table { border-collapse: collapse; width: 100%; }
                    th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
                </style>
            </head>
            <body>
            <h1>Scraped Content Report</h1>
            <p>Generated on: """ + datetime.now().strftime('%Y-%m-%d %H:%M:%S') + """</p>
        """)

        for url in urls:
            print(f"Scraping {url}...")
            html_content = self.fetch_page(url)
            if html_content:
                extracted = self.extract_content(html_content, url)
                if extracted:
                    document_parts.append(f"""
                        <div class="page-section">
                            <div class="metadata">
                                <h2>{html.escape(extracted['metadata']['title'])}</h2>
                                <p><strong>URL:</strong> {html.escape(extracted['metadata']['url'])}</p>
                                <p><strong>Description:</strong> {html.escape(extracted['metadata']['meta_description'])}</p>
                                <p><strong>Scraped:</strong> {extracted['metadata']['date_scraped']}</p>
                            </div>
                            <div class="content">
                                {extracted['content']}
                            </div>
                        </div>
                    """)

        document_parts.append("""
            </body>
            </html>
        """)

        with open(output_file, 'w', encoding='utf-8') as f:
            f.write('\n'.join(document_parts))

        print(f"\nScraped content has been saved to {output_file}")

def get_urls_from_user():
    """Get URLs from user input"""
    print("\nPlease paste your URLs (one per line).")
    print("When you're done, press Enter twice (i.e., leave a blank line):\n")
    
    urls = []
    while True:
        line = input().strip()
        if not line:  # Empty line
            break
        if line.startswith(('http://', 'https://')):
            urls.append(line)
        else:
            print(f"Warning: Skipping invalid URL format: {line}")
    
    return urls

def get_output_filename():
    """Get desired output filename from user"""
    while True:
        filename = input("\nEnter the desired output filename (e.g., output.html): ").strip()
        if filename.endswith('.html'):
            return filename
        else:
            print("Filename must end with .html")

def main():
    print("Welcome to the Web Content Scraper!")
    
    # Get URLs from user
    urls = get_urls_from_user()
    if not urls:
        print("No valid URLs provided. Exiting...")
        return
    
    # Get output filename
    output_file = get_output_filename()
    
    # Create scraper and process URLs
    print(f"\nStarting to scrape {len(urls)} URLs...")
    scraper = WebScraper()
    scraper.create_document(urls, output_file)
    
    print("\nDone! You can find your scraped content in:", output_file)

if __name__ == "__main__":
    main()
