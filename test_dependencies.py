"""
Test script to verify all dependencies are installed and working correctly
"""

import sys

def test_imports():
    """Test all required package imports"""
    print("Testing package imports...")
    print("-" * 60)
    
    packages = [
        ('numpy', 'NumPy'),
        ('pandas', 'Pandas'),
        ('requests', 'Requests'),
        ('bs4', 'BeautifulSoup4'),
        ('matplotlib', 'Matplotlib'),
        ('seaborn', 'Seaborn'),
        ('scipy', 'SciPy'),
        ('statsmodels', 'Statsmodels'),
        ('nltk', 'NLTK'),
        ('wordcloud', 'WordCloud'),
        ('openpyxl', 'OpenPyXL'),
        ('xlsxwriter', 'XlsxWriter'),
        ('jupyter', 'Jupyter'),
        ('notebook', 'Notebook'),
        ('IPython', 'IPython')
    ]
    
    failed = []
    for module, name in packages:
        try:
            __import__(module)
            print(f"✓ {name:20s} - OK")
        except ImportError as e:
            print(f"✗ {name:20s} - FAILED: {e}")
            failed.append(name)
    
    print("-" * 60)
    if failed:
        print(f"\n❌ {len(failed)} package(s) failed to import:")
        for pkg in failed:
            print(f"   - {pkg}")
        return False
    else:
        print("\n✅ All packages imported successfully!")
        return True

def test_basic_functionality():
    """Test basic functionality of key packages"""
    print("\n\nTesting basic functionality...")
    print("-" * 60)
    
    try:
        # Test NumPy
        import numpy as np
        arr = np.array([1, 2, 3, 4, 5])
        print(f"✓ NumPy array creation: {arr.mean()}")
        
        # Test Pandas
        import pandas as pd
        df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
        print(f"✓ Pandas DataFrame: {df.shape}")
        
        # Test Requests
        import requests
        print(f"✓ Requests library version: {requests.__version__}")
        
        # Test BeautifulSoup
        from bs4 import BeautifulSoup
        soup = BeautifulSoup("<html><body><p>Test</p></body></html>", "html.parser")
        print(f"✓ BeautifulSoup parsing: {soup.p.text}")
        
        # Test NLTK
        import nltk
        print(f"✓ NLTK version: {nltk.__version__}")
        
        print("-" * 60)
        print("\n✅ All basic functionality tests passed!")
        return True
        
    except Exception as e:
        print(f"\n❌ Functionality test failed: {e}")
        return False

def check_files():
    """Check if required files exist"""
    print("\n\nChecking required files...")
    print("-" * 60)
    
    import os
    files = [
        ('requirements.txt', 'Dependencies file'),
        ('stopwords.txt', 'Stopwords file'),
        ('APIkeys.json', 'API keys file'),
        ('SETUP_GUIDE.md', 'Setup guide')
    ]
    
    for filename, description in files:
        if os.path.exists(filename):
            print(f"✓ {description:25s} - {filename}")
        else:
            print(f"✗ {description:25s} - {filename} (MISSING)")
    
    print("-" * 60)

def main():
    """Main test function"""
    print("\n" + "=" * 60)
    print("Web-Database-Analytics Dependency Test")
    print("=" * 60 + "\n")
    
    # Test imports
    imports_ok = test_imports()
    
    # Test functionality
    if imports_ok:
        functionality_ok = test_basic_functionality()
    else:
        functionality_ok = False
    
    # Check files
    check_files()
    
    # Final summary
    print("\n" + "=" * 60)
    if imports_ok and functionality_ok:
        print("✅ ALL TESTS PASSED - Repository is ready to use!")
        print("\nYou can now run:")
        print("  - Python scripts: python script_name.py")
        print("  - Jupyter notebooks: jupyter notebook")
    else:
        print("❌ SOME TESTS FAILED - Please check the errors above")
        sys.exit(1)
    print("=" * 60 + "\n")

if __name__ == "__main__":
    main()