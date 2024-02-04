# scraper.py
import requests
from bs4 import BeautifulSoup

def get_citations_needed_count(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    citations = soup.find_all('sup', class_='noprint Inline-Template Template-Fact')

    return len(citations)

def get_citations_needed_report(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    citations = soup.find_all('sup', class_='noprint Inline-Template Template-Fact')

    report = ""
    for citation in citations:
        passage = citation.find_next('p').text
        report += f'{passage.strip()}[citation needed]\n'

    return report

# Example usage:
url = 'https://en.wikipedia.org/wiki/Hydrogen_vehicle'
count = get_citations_needed_count(url)
report = get_citations_needed_report(url)

print(f'Number of citations needed: {count}')
print('Citations:')
print(report)
