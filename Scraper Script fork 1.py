#First time web scrapin, kinda nervous
#following the tutorial on realpython.com
#https://realpython.com/beautiful-soup-web-scraper-python/#what-is-web-scraping

# test url:  https://www.monster.com/jobs/search/?q=Software-Developer&where=Australia

import requests
from bs4 import BeautifulSoup

URL = 'https://www.monster.com/jobs/search/?q=Software-Developer&where=Australia'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(id="ResultsContainer")

job_elems = results.find_all('section', class_='card-content')
python_jobs = results.find_all('h2', string='Python Developer')
for job_elem in job_elems:
    # Each job_elem is a new BeautifulSoup object.
    # You can use the same methods on it as you did before.
    title_elem = job_elem.find('h2', class_='title')
    company_elem = job_elem.find('div', class_='company')
    location_elem = job_elem.find('div', class_='location')
    if None in (title_elem, company_elem, location_elem):
        print()
        print(":: ERROR ::")
        print(title_elem, company_elem, location_elem)
        print()
        print()
        continue
    print(title_elem.text.strip())
    print(company_elem.text.strip())
    print(location_elem.text.strip())
    print()