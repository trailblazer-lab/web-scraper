import requests
from bs4 import BeautifulSoup

# Step 1: Fetch the web page
url = 'https://en.wikipedia.org/wiki/Web_scraping'
response = requests.get(url)

# Step 2: Check if the request was successful
if response.status_code == 200:
    print('Successfully fetched the web page')

# Step 3: Parse the HTML
    soup = BeautifulSoup(response.content, 'html.parser')

# Step 4: Extract data
    headings = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
    for heading in headings:
        print(heading.get_text(strip=True))
else:
    print('Failed to fetch the web page')