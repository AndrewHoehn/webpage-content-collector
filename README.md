# Multi-Webpage Content Collector

Paste in a list of URLs from multiple webpages, get out a single, well-formatted HTML document. Perfect for getting specific web content into a LLM and more. 

## Features

- Scrapes multiple web pages from provided URLs
- Preserves essential HTML formatting (H1-H4, paragraphs, tables, emphasis)
- Extracts and organizes metadata (title, description, URL)
- Creates a clean, readable HTML output
- Interactive command-line interface for URL input
- Error handling for failed requests
- Mobile-friendly output styling
- Custom CSS for better readability
- Progress tracking during scraping

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/webpage-content-aggregator.git
```

2. Install required packages:
```bash
pip install requests beautifulsoup4
```

## Usage

1. Run the script:
```bash
python webpage_content_aggregator.py
```

2. When prompted, paste your URLs (one per line). Press Enter twice when done.

3. Enter your desired output filename (must end with .html)

4. The script will process each URL and create a single HTML document containing all the scraped content.

## Example Output

See an example [here](sample_output.html). 

The script creates a well-structured HTML document with:

- A header section showing generation timestamp
- Individual sections for each webpage containing:
  - Title
  - Original URL
  - Meta description
  - Scraped timestamp
  - Main content with preserved formatting

Example of output structure:
```html
<div class="page-section">
    <div class="metadata">
        <h2>What is Bluesky? Everything to know about the X competitor.</h2>
        <p><strong>URL:</strong> https://techcrunch.com/example-url</p>
        <p><strong>Description:</strong> Bluesky is the latest app users are flocking to...</p>
        <p><strong>Scraped:</strong> 2024-11-12 12:51:34</p>
    </div>
    <div class="content">
        <!-- Preserved HTML content -->
    </div>
</div>
```

## Features in Detail

### Content Preservation
- Maintains heading hierarchy (H1-H4)
- Preserves paragraph structure
- Keeps tables intact
- Retains text formatting (bold, italic, emphasis)
- Maintains basic HTML structure

### Metadata Extraction
- Page title
- Meta description
- Original URL
- Timestamp of scraping
- Additional metadata when available

### Styling
- Responsive design
- Clean typography
- Clear content separation
- Mobile-friendly layout
- Consistent spacing and margins

## Error Handling

The script includes robust error handling for:
- Invalid URLs
- Failed requests
- Missing content
- Network timeouts
- Invalid HTML structure

## Limitations

- Does not save images
- Doesn't preserve complex JavaScript functionality
- Some dynamic content may not be captured
- CSS styling is simplified
- Does not handle password-protected pages

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- BeautifulSoup4 for HTML parsing
- Requests library for HTTP handling
