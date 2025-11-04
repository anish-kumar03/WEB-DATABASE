# Quick Start Guide

## ✅ Setup Complete!

All dependencies have been installed and verified. The repository is ready to use!

## Running Programs

### 1. Python Scripts

Run any Python script directly:

```powershell
# Example: Scrape top 100 Gutenberg books
python Top100_Book_numbers_Gutenberg.py

# Example: Get geolocation data
python GeoLocation-GoogleAPI-XML.py

# Example: Count words from web
python Word_count_from_web.py
```

### 2. Jupyter Notebooks

Start Jupyter Notebook server:

```powershell
jupyter notebook
```

This will:
- Start a local server
- Open your browser automatically
- Show all available notebooks

Popular notebooks to try:
- `CIA-Factbook-Analytics2.ipynb` - Analyze CIA World Factbook data
- `Movie_Database_Build.ipynb` - Build a movie database
- `Yelp_Review/Yelp_Reviews_Wordcloud.ipynb` - Generate word clouds from Yelp reviews
- `Countries-JSON-API.ipynb` - Work with country data APIs

### 3. Test Everything

Run the test script to verify all dependencies:

```powershell
python test_dependencies.py
```

## What's Installed

✅ All required packages:
- numpy, pandas (data manipulation)
- requests, beautifulsoup4 (web scraping)
- matplotlib, seaborn (visualization)
- scipy, statsmodels (statistics)
- nltk (natural language processing)
- wordcloud (word cloud generation)
- openpyxl, xlsxwriter (Excel support)
- jupyter, notebook (Jupyter notebooks)

✅ NLTK data downloaded
✅ Stopwords file created
✅ API keys template created

## Important Notes

### API Keys
Some notebooks require API keys. Edit `APIkeys.json` with your actual keys:
- **OpenWeatherMap API**: For WeatherAPI.ipynb
- **OMDB API**: For Movie_Database_Build.ipynb

Get free API keys from:
- Weather: https://openweathermap.org/api
- Movies: http://www.omdbapi.com/apikey.aspx

### Files Created
- `requirements.txt` - All Python dependencies
- `stopwords.txt` - Common English stopwords
- `APIkeys.json` - API key configuration
- `SETUP_GUIDE.md` - Detailed setup instructions
- `test_dependencies.py` - Dependency verification script

## Examples

### Example 1: Run a simple script
```powershell
python Top100_Book_numbers_Gutenberg.py
```
Output: List of top 100 ebook file numbers from Project Gutenberg

### Example 2: Start Jupyter
```powershell
jupyter notebook
```
Then navigate to any `.ipynb` file and run cells with Shift+Enter

### Example 3: Test setup
```powershell
python test_dependencies.py
```
Verifies all packages are working correctly

## Troubleshooting

If you encounter any issues:

1. **Import errors**: Run `pip install -r requirements.txt` again
2. **NLTK errors**: Run `python -c "import nltk; nltk.download('popular')"`
3. **API errors**: Make sure you've added valid API keys to `APIkeys.json`

## Next Steps

1. ✅ All dependencies installed
2. ✅ Test script passed
3. 🚀 Start exploring the notebooks!

Try running:
```powershell
jupyter notebook
```

Happy coding! 🎉