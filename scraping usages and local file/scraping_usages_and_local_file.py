from bs4 import BeautifulSoup

with open('scraping usages and local file/home.html', 'r') as html_file:
    content = html_file.read()
    #print(content)
    #print('--------------------------')
    soup = BeautifulSoup(content, 'lxml')
    tags = soup.find('h5')
    print(tags)