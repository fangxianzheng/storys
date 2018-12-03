# -*- coding:UTF-8 -*-
from urllib import request
from bs4 import BeautifulSoup
import pymongo

if __name__ == "__main__":
    download_url = 'http://www.biqukan.com/1_1094/5403177.html'
    head = {}
    head['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
    download_req = request.Request(url = download_url, headers = head)
    download_response = request.urlopen(download_req)
    download_html = download_response.read().decode('gbk','ignore')
    soup_texts = BeautifulSoup(download_html, 'html.parser')
    texts = soup_texts.find_all(id = 'content', class_ = 'showtxt')
    soup_text = BeautifulSoup(str(texts), 'html.parser')

    content = soup_text.div.text.replace('\xa0','')
    data = {
        'content': content
    }
    client = pymongo.MongoClient('localhost', 27017)
    database = client['小说']
    table =database['玄幻']
    table.insert(data)