import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import argparse

def scrape_webpage(url, file_name):
    """
    Scrape the links from a webpage and save them to a text file.

    Parameters:
    url (str): The URL of the webpage to scrape.
    file_name (str): The name of the file to save the links to.

    Returns:
    None
    """
    # Validate user input
    if not url.startswith('http'):
        print("Please enter a valid URL starting with 'http' or 'https'.")
        return

    # Make a request to the website
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Safari/605.1.15'}
    try:
        response = requests.get(url, headers)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print("An error occurred while making the request:", e)
        return

    # Parse the HTML content of the page
    soup = BeautifulSoup(response.content, "html.parser")
    
    # Find all the links on the page
    links = set()
    for tag in soup.find_all():
        if tag.name in ['a', 'img', 'link', 'script'] and 'href' in tag.attrs:
            url = tag.attrs['href']
            if not urlparse(url).scheme:
                url = urljoin(response.url, url) # Convert relative links to absolute links
            links.add(url)

    # Write the unique links to a text file
    try:
        with open(file_name, "w") as file:
            for url in links:
                file.write(url + "\n")
    except IOError as e:
        print("An error occurred while writing the file:", e)
        return

    # Print a summary of the links found
    print(f"Number of unique links found: {len(links)}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Scrape links from a webpage.")
    parser.add_argument("url", type=str, help="The URL of the webpage to scrape.")
    parser.add_argument("filename", type=str, help="The name of the file to write the links to.")
    args = parser.parse_args()

    scrape_webpage(args.url, args.filename)
