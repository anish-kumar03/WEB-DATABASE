# Setup Guide for Web-Database-Analytics

This guide will help you set up the environment and run all programs without errors.

## Prerequisites

- Python 3.5 or higher (Python 3.7+ recommended)
- pip (Python package installer)

## Installation Steps

### 1. Install Required Dependencies

Run the following command in your terminal (PowerShell on Windows):

```powershell
pip install -r requirements.txt
```

This will install all necessary packages including:
- numpy, pandas (data manipulation)
- requests, beautifulsoup4 (web scraping)
- matplotlib, seaborn (visualization)
- scipy, statsmodels (statistical analysis)
- nltk (natural language processing)
- wordcloud (word cloud generation)
- openpyxl, xlsxwriter (Excel support)
- jupyter, notebook (Jupyter notebooks)

### 2. Download NLTK Data (Required for text mining notebooks)

After installing the packages, you need to download NLTK data:

```python
import nltk
nltk.download('popular')
```

Or run this command:

```powershell
python -c "import nltk; nltk.download('popular')"
```

### 3. Set Up API Keys (Optional - for API-based notebooks)

Some notebooks require API keys. To use them:

1. Copy `APIkey_Bogus_example.json` to `APIkeys.json`
2. Replace the bogus keys with your actual API keys:
   - **Weather API**: Get from [OpenWeatherMap](https://openweathermap.org/api)
   - **OMDB API**: Get from [OMDb API](http://www.omdbapi.com/apikey.aspx)

```powershell
Copy-Item APIkey_Bogus_example.json APIkeys.json
```

Then edit `APIkeys.json` with your actual keys.

## Running the Programs

### Python Scripts

To run any Python script:

```powershell
python script_name.py
```

Examples:
```powershell
python Word_count_from_web.py
python Top100_Book_numbers_Gutenberg.py
python GeoLocation-GoogleAPI-XML.py
```

### Jupyter Notebooks

To run Jupyter notebooks:

1. Start Jupyter:
```powershell
jupyter notebook
```

2. Your browser will open automatically
3. Navigate to any `.ipynb` file and click to open
4. Run cells using Shift+Enter

## Troubleshooting

### Common Issues

1. **Import Error**: If you get "ModuleNotFoundError", install the missing package:
   ```powershell
   pip install package_name
   ```

2. **API Key Error**: Make sure you've created `APIkeys.json` with valid keys for notebooks that require them (WeatherAPI.ipynb, Movie_Database_Build.ipynb)

3. **NLTK Data Error**: Run the NLTK download command mentioned in step 2

4. **Stopwords File Missing**: The `stopwords.txt` file has been created in the repository root

### Verify Installation

Run this command to verify all packages are installed:

```powershell
python -c "import numpy, pandas, requests, bs4, matplotlib, seaborn, scipy, statsmodels, nltk, wordcloud, openpyxl, xlsxwriter; print('All packages installed successfully!')"
```

## What Each Program Does

- **Word_count_from_web.py**: Counts words from Project Gutenberg books
- **Top100_Book_numbers_Gutenberg.py**: Scrapes top 100 ebook numbers from Gutenberg
- **GeoLocation-GoogleAPI-XML.py**: Gets latitude/longitude using Google Maps API
- **CIA-Factbook-Analytics2.ipynb**: Analyzes CIA World Factbook data
- **Movie_Database_Build.ipynb**: Builds a movie database using OMDB API
- **Yelp_Review/**: Yelp restaurant review analysis and word clouds
- **WeatherAPI.ipynb**: Weather data analysis using OpenWeatherMap API
- And many more...

## Notes

- Some scripts may take time to run as they fetch data from the web
- API-based scripts require internet connection and valid API keys
- The repository includes both standalone Python scripts and Jupyter notebooks
- All dependencies are now properly documented in requirements.txt

## Support

If you encounter any issues, please check:
1. Python version (should be 3.5+)
2. All packages are installed correctly
3. API keys are set up (if needed)
4. Internet connection is active (for web scraping scripts)