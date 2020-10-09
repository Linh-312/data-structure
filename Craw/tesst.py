import bs4
import pandas
import requests
url = 'https://www.it-swarm-vi.tech/vi/python/cai-dat-pyaudio-voi-pip-trong-virtualenv/823954782'
def get_page_content(url):
   page = requests.get(url,headers={"Accept-Language":"en-US"})
   return bs4.BeautifulSoup(page.text,"html.parser")
soup = get_page_content(url)
print(soup)