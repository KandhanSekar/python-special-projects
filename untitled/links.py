from bs4 import BeautifulSoup
import urllib.request
import re

html_page = urllib.request.urlopen("http://www.asu.edu")
soup = BeautifulSoup(html_page)
links = []
for link in soup.findAll('a'):
    links.append(link.get('href'))

print(links)
