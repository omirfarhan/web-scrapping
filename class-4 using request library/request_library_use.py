from bs4 import BeautifulSoup
import requests
html_text = requests.get('https://bdjobs.com/h/jobs?qOT=&txtsearch=flutter%20developer&lang=en')
print(html_text)