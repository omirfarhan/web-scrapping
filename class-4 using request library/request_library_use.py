from bs4 import BeautifulSoup
import requests
html_text = requests.get('https://books.toscrape.com').text
soup = BeautifulSoup(html_text, 'lxml')

# product_list = soup.find_all('ol', class_ ='row')
# print(product_list)

first_book=soup.find_all('li',class_ = 'col-xs-6 col-sm-4 col-md-3 col-lg-3')
for books in first_book:
     title = books.find('h3').find('a').get('title')
     product_list_price = books.find('div', class_ = 'product_price')
     product_price = product_list_price.find('p').text
     rating_tag = books.find('p',class_='star-rating')
     product_rating = rating_tag.get('class')[-1]

     print(f'''
Book name = {title}
product price = {product_price}
product rating = {product_rating}
     ''')


# #ekhane ekta product er data gula dekhacche 
# first_book=soup.find('li',class_ = 'col-xs-6 col-sm-4 col-md-3 col-lg-3')
# product_price = soup.find('div', class_ = 'product_price')

# title = first_book.find('h3').find('a').get('title')
# book_price = product_price.find('p').text


# print(f'''
# Book name = {title}
# product price = {book_price}
# ''')
