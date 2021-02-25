from requests import get
from bs4 import BeautifulSoup

# getting html from site

def get_html_from_url(url):
    req = get(url).content
    html = BeautifulSoup(req, 'lxml')
    return html