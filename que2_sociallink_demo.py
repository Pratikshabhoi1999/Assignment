import requests
from bs4 import BeautifulSoup

url = "https://stackoverflow.com/questions/tagged/python"
url1= "https://@gmail.com"
r = requests.get(url)
e = requests.get(url1)
sm_sites = ['facebook.com','linkedin.com']
sm_emails = ['support']
sm_sites_present = []
sm_emails_present = []

soup = BeautifulSoup(r.content, 'html5lib')
all_links = soup.find_all('a', href = True)

stop = BeautifulSoup(e.content, 'html5lib')
all_emails = stop.find_all('a', href = True)


for sm_site in sm_sites:
    for link in all_links:
        if sm_site in link.attrs['href']:
            sm_sites_present.append(link.attrs['href'])

print(sm_sites_present)

for sm_email in sm_emails:
    for link in all_emails:
        if sm_email in link.attrs['href']:
            sm_emails_present.append(link.attrs['href'])

print(sm_emails_present)