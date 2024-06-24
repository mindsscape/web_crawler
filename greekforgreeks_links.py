import requests
from bs4 import BeautifulSoup

# URL to scrape
url = "https://www.geeksforgeeks.org/difference-between-structured-semi-structured-and-unstructured-data/?ref=header_search"

# Perform the request
response = requests.get(url)
response.raise_for_status()  # Ensure we notice bad responses

# Parse the page content
soup = BeautifulSoup(response.text, 'html.parser')

# Extract all the links
links = []
for a_tag in soup.find_all('a', href=True):
    links.append(a_tag['href'])

# Print all the links
for link in links:
    print(link)
