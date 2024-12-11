import requests as rq

from bs4 import BeautifulSoup
import pandas as pd

from getBook import extractBook

bookurl = 'https://books.toscrape.com/'

bookHeader = {
    'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
    
    }
bookResq = rq.get(url=bookurl , headers=bookHeader)

bookSoup = BeautifulSoup (bookResq.content,'html.parser')

books = [extractBook (book) for book in bookSoup.find_all('article',{'class':"product_pod"})]   

booksDf = pd.DataFrame(books)

booksDf.to_csv('books.csv')

