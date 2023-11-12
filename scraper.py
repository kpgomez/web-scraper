# from playwright.sync_api import sync_playwright
# from bs4 import BeautifulSoup
#
# def main():
#     with sync_playwright() as playwright:
#         # Open chrome and navigate to target page
#         browser = playwright.chromium.launch(headless=False)

import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/History_of_Mexico"
response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

missing_citations = soup.find_all("p")

print(type(missing_citations))








#
# if __name__ == "__main__":
#     main()