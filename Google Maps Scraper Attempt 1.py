# google maps LAT and LON data for Chicago IL - @41.8336479,-87.8720465

import requests
from bs4 import BeautifulSoup

URL = 'https://www.google.com/maps/search/Dog+Daycare/@41.8334777,-87.8720468,11z/data=!3m1!4b1'
#main get request
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(id="section-layout section-scrollbox scrollable-y scrollable-show section-layout-flex-vertical")

#status or request
response = requests.get(URL)
if response.status_code == 200:
    print('Success')
    print()
elif response.status_code == 404:
    print('Error 404 - Not Found')
    print()
    
print(results.text.strip())