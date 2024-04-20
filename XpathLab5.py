import requests
from bs4 import BeautifulSoup
from lxml import etree
from urllib.parse import urljoin


url = "https://www.gutenberg.org/cache/epub/786/pg786-images.html"

webpage = requests.get(url)
soup = BeautifulSoup(webpage.content, "html.parser")
dom = etree.HTML(str(soup))

base_xpath = '//*[@id="mainaside"]/html/body'

# Find all elements matching the base XPath pattern with any index
for index in range(1, 10):  # Adjust the range as needed based on the expected maximum index
    # Construct the full XPath for each iteration
    full_xpath = f"{base_xpath}[{index}]/a/text()"

    # Use XPath to extract data from each element
    res = dom.xpath(full_xpath)

    # Check if the result is not empty before printing
    if res:
        for i in res:
            print(i)
for index in range(1, 10):  # Adjust the range as needed based on the expected maximum index
    # Construct the full XPath for each iteration
    full_xpath = f"{base_xpath}[{index}]/a/@href"

    # Use XPath to extract href attributes from each element
    res = dom.xpath(full_xpath)

    # Check if the result is not empty before printing
    if res:
        for href in res:
            print(href)

base_xpath_href = '//*[@id="mainaside"]/html/body'

# Find all href attributes under the base XPath pattern with any index
for index in range(1, 10):  # Adjust the range as needed based on the expected maximum index
    full_xpath_href = f"{base_xpath_href}[{index}]/a/@href"
    res_href = dom.xpath(full_xpath_href)

    if res_href:
        for link in res_href:
            # Construct the absolute URL from the relative href
            absolute_url = urljoin(url, link)

            linked_page = requests.get(absolute_url)
            linked_soup = BeautifulSoup(linked_page.content, "html.parser")

            base_css_selector_p = '#mainaside article div:nth-child(2) div:nth-child(2) p'
            all_p_tags = linked_soup.select(base_css_selector_p)

            # Print the text of the first two <p> elements from each linked page
            for p_tag in all_p_tags[:2]:
                print(p_tag.text.strip())
                print()


