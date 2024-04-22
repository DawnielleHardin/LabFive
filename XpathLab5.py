import requests
from bs4 import BeautifulSoup
from lxml import etree

# List of URLs
urls = [
    "https://www.gutenberg.org/cache/epub/580/pg580-images.html",
    "https://www.gutenberg.org/cache/epub/730/pg730-images.html",
    "https://www.gutenberg.org/cache/epub/967/pg967-images.html",
    "https://www.gutenberg.org/cache/epub/700/pg700-images.html",
    "https://www.gutenberg.org/cache/epub/917/pg917-images.html",
    "https://www.gutenberg.org/cache/epub/968/pg968-images.html",
    "https://www.gutenberg.org/cache/epub/821/pg821-images.html",
    "https://www.gutenberg.org/cache/epub/766/pg766-images.html",
    "https://www.gutenberg.org/cache/epub/1023/pg1023-images.html",
    "https://www.gutenberg.org/cache/epub/786/pg786-images.html",
    "https://www.gutenberg.org/cache/epub/963/pg963-images.html",
    "https://www.gutenberg.org/cache/epub/98/pg98-images.html",
    "https://www.gutenberg.org/cache/epub/1400/pg1400-images.html",
    "https://www.gutenberg.org/cache/epub/883/pg883-images.html",
    "https://www.gutenberg.org/cache/epub/564/pg564-images.html"
]

# Loop through each URL
for url in urls:
    # Get the webpage content
    response = requests.get(url)
    html_content = response.text

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html_content, "html.parser")

    # Convert the soup object to an lxml etree object
    dom = etree.HTML(str(soup))

    # XPath expression for the body excluding specific elements
    body_xpath = "/html/body"

    # Extract the content of the body using XPath
    body_content = dom.xpath("string(" + body_xpath + ")")

    # Print the content of the body along with the URL
    print(f"URL: {url}")
    print(body_content)
