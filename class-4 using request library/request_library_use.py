from bs4 import BeautifulSoup
import requests
html_text = requests.get('https://books.toscrape.com').text
soup = BeautifulSoup(html_text, 'lxml')

domainlink='https://books.toscrape.com/'

# product_list = soup.find_all('ol', class_ ='row')
# print(product_list)

# print('put your searching book.... ')
# unfamilier_book = input('>')
# print(f'Filtering out book {unfamilier_book}')

first_book=soup.find_all('li',class_ = 'col-xs-6 col-sm-4 col-md-3 col-lg-3')
for books in first_book:
     title = books.find('h3').find('a').get('title')
     product_list_price = books.find('div', class_ = 'product_price')
     product_price = product_list_price.find('p').text
     rating_tag = books.find('p',class_='star-rating')
     product_rating = rating_tag.get('class')[-1]
     product_description = books.find('div', class_ = 'image_container')
     product_link_des = product_description.find('a')['href']
     image_link = product_description.find('img')['src']

     print(f"Book name = {title.strip()}")
     print(f"product price = {product_price.strip()}")
     print(f"product rating = {product_rating.strip()}")
     print(f"Product description link = {product_link_des}")
     print(f"Product image link = {domainlink+image_link}")
     print(' ')

     # if unfamilier_book not in title:
          

     


     

#      print(f'''
# Book name = {title}
# product price = {product_price}
# product rating = {product_rating}
#      ''')


# #ekhane ekta product er data gula dekhacche 
# first_book=soup.find('li',class_ = 'col-xs-6 col-sm-4 col-md-3 col-lg-3')
# product_price = soup.find('div', class_ = 'product_price')

# title = first_book.find('h3').find('a').get('title')
# book_price = product_price.find('p').text


# print(f'''
# Book name = {title}
# product price = {book_price}
# ''')
