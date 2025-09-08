# 🏛️ VenueScraper AI

**An intelligent web scraper for wedding venues using AI-powered data extraction**

VenueScraper AI is a Python-based web scraping tool that uses Crawl4AI and Groq's LLM to intelligently extract wedding venue information from venue listing websites. It automatically navigates through paginated results and saves structured venue data to CSV files.

## ✨ Features

- 🤖 **AI-Powered Extraction**: Uses Groq's DeepSeek R1 model for intelligent data parsing
- 🌐 **Smart Web Crawling**: Built on Crawl4AI with Playwright for robust navigation
- 📄 **Automatic Pagination**: Handles multi-page venue listings automatically
- 💾 **CSV Export**: Saves extracted venue data in structured CSV format
- 🛡️ **Anti-Detection**: Configured with realistic browser headers and stealth features
- ⚡ **Async Processing**: High-performance asynchronous web scraping

## 🎯 Supported Sites

- **Venuelook.com** - Mumbai banquet halls (currently configured)
- **Weddingz.in** - Wedding venues across India
- **The Knot** - Wedding venues (configurable)

## 📋 Prerequisites

- Python 3.8+
- Windows 10/11 (tested on Windows)
- Groq API key

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/venuescraper-ai.git
cd venuescraper-ai
```

### 2. Set Up Virtual Environment

```bash
python -m venv .venv
```

**Windows:**
```bash
.\.venv\Scripts\Activate.ps1
```

**macOS/Linux:**
```bash
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### 4. Install Playwright Browser

```bash
playwright install chromium --with-deps
```

### 5. Configure API Key

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key_here
```

**Get your Groq API key:**
1. Visit [Groq Console](https://console.groq.com/)
2. Sign up/Login
3. Go to [API Keys](https://console.groq.com/keys)
4. Create a new API key
5. Copy and paste it into your `.env` file

### 6. Run the Scraper

```bash
python main.py
```

## 📊 Output

The scraper generates CSV files with venue data:

- `venue.csv` - Main output file with extracted venues
- `venues.csv` - Alternative output file

**Sample CSV Structure:**
```csv
name,price,capacity,rating,reviews,description,location
Venue Name 1,Price 1,Capacity 1,1,1,Description of Venue 1,Location 1
Venue Name 2,Price 2,Capacity 2,2,2,Description of Venue 2,Location 2
```

## ⚙️ Configuration

### Target Website

Edit `config.py` to change the target website:

```python
BASE_URL = "https://www.venuelook.com/mumbai/banquet-halls"
CSS_SELECTOR = "body"
REQUIRED_KEYS = [
    "name",
    "location",
]
```

### Pagination

The scraper automatically handles pagination:
- **Venuelook**: Uses `?page={n}` format
- **Weddingz**: Uses `/page/{n}/` format
- **The Knot**: Uses `?page={n}` format

### Browser Settings

Modify `utils/scraper_utils.py` for browser configuration:

```python
def get_browser_config() -> BrowserConfig:
    return BrowserConfig(
        browser_type="chromium",
        headless=False,  # Set to True for headless mode
        verbose=True,
        # ... other settings
    )
```

## 🏗️ Project Structure

```
venuescraper-ai/
├── main.py                 # Main entry point
├── config.py              # Configuration settings
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables (create this)
├── models/
│   ├── __init__.py
│   └── venue.py          # Venue data model
├── utils/
│   ├── __init__.py
│   ├── scraper_utils.py  # Scraping utilities
│   └── data_utils.py     # Data processing utilities
├── venue.csv             # Generated output
└── README.md             # This file
```

## 🔧 Advanced Usage

### Custom Venue Fields

Modify `models/venue.py` to add custom fields:

```python
class Venue(BaseModel):
    name: str
    price: str
    capacity: str
    rating: int
    reviews: int
    description: str
    location: str
    # Add your custom fields here
    amenities: str = ""
    contact: str = ""
```

### Multiple Cities

To scrape different cities, update the base URL:

```python
# For Delhi venues
BASE_URL = "https://www.venuelook.com/delhi/banquet-halls"

# For Bangalore venues  
BASE_URL = "https://www.venuelook.com/bangalore/banquet-halls"
```

### Proxy Support

Add proxy configuration in `utils/scraper_utils.py`:

```python
def get_browser_config() -> BrowserConfig:
    return BrowserConfig(
        # ... other settings
        proxy="http://username:password@proxy-server:port",
    )
```

## 🐛 Troubleshooting

### Common Issues

**1. Navigation Errors (ERR_ABORTED)**
- The target site may be blocking automated requests
- Try using a proxy or switching to headless mode
- Consider adding delays between requests

**2. No Venues Extracted**
- Check if the CSS selector is correct
- Verify the target website structure hasn't changed
- Ensure the LLM extraction is working (check GROQ_API_KEY)

**3. Playwright Browser Issues**
- Reinstall Playwright: `playwright install chromium --force`
- Check if antivirus is blocking browser execution

**4. API Key Issues**
- Verify your Groq API key is valid and has sufficient credits
- Check the `.env` file is in the project root
- Ensure no extra spaces in the API key

### Debug Mode

Enable verbose logging by setting `verbose=True` in browser config and check the console output for detailed information.

## 📈 Performance

- **Speed**: ~2-3 venues per minute (depends on LLM processing time)
- **Memory**: ~200MB RAM usage
- **Network**: Respects rate limits with 2-second delays between pages

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes
4. Add tests if applicable
5. Commit your changes: `git commit -m "Add feature"`
6. Push to the branch: `git push origin feature-name`
7. Submit a pull request


## 🙏 Acknowledgments

- [Crawl4AI](https://github.com/unclecode/crawl4ai) - Web crawling framework
- [Groq](https://groq.com/) - AI inference platform
- [Playwright](https://playwright.dev/) - Browser automation
- [Pydantic](https://pydantic.dev/) - Data validation

