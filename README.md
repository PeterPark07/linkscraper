# link Scraper

This is a Python command-line tool that scrapes links from a webpage and saves them to a text file. It uses the Requests and BeautifulSoup libraries to make an HTTP request to the specified URL and parse the HTML content of the page to find all the links on the page. The links are then written to a file, with one link per line, and the number of unique links found is printed as a summary.

# Installation
To use this tool, you need to have Python 3 and the Requests and BeautifulSoup libraries installed. You can install them using pip:

```
pip install requests beautifulsoup4
```

# Usage
To use this tool, open a terminal or command prompt and navigate to the directory where the Scrape_Webpage.py file is located. Then, run the following command:

```
python Scrape_webpage.py [url] [filename]
```
