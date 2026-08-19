from bs4 import BeautifulSoup

with open('scraping usages and local file/home.html', 'r') as html_file:
    content = html_file.read()
    soup = BeautifulSoup(content, 'lxml')
    #just find the first tag
    #tags = soup.find('h5')
    #it will find all the h5 tags
    course_html_tags = soup.find_all('h5')

    for course in course_html_tags:
        print(course.text)