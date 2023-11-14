from bs4 import BeautifulSoup
import requests

url = "https://en.wikipedia.org/wiki/Laos"


def get_citations_needed_count(url_address: str) -> int:
    response = requests.get(url_address)
    soup = BeautifulSoup(response.content, "html.parser")
    # https://chat.openai.com/c/67fb1e11-a1bc-40dc-9410-71b1f27933a2
    missing_citations = soup.find_all(
        lambda tag: tag.name == 'p' and tag.find('a', href="/wiki/Wikipedia:Citation_needed") is not None)
    count = 0
    # https://chat.openai.com/c/4eac8099-d441-4e4e-880c-1715b3990bd3
    for citation in missing_citations:
        if "citation needed" in citation.text:
            count += 1
    return count


def get_citations_needed_report(url_address: str) -> str:
    response = requests.get(url_address)
    report = ""
    soup = BeautifulSoup(response.content, "html.parser")
    missing_citations = soup.find_all(
        lambda tag: tag.name == 'p' and tag.find('a', href="/wiki/Wikipedia:Citation_needed") is not None)
    for citation in missing_citations:
        if "citation needed" in citation.text:
            report += f'{citation.text}\n'
    return report


print(get_citations_needed_count(url))
print(get_citations_needed_report(url))
