import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
from multiprocessing.dummy import Pool as ThreadPool
def getHTMLText(target):
    req=requests.get(url=target)
    req.encoding=req.apparent_encoding
    bs=BeautifulSoup(req.text,'html.parser')
    texts=bs.find('div',id='content')
    return texts.text.strip().split('\xa0'*4)
    # print(texts.text.strip().split('\xa0'*4))
server='https://www.62zw.com/book_55697/'
req=requests.get(url=server)
bs=BeautifulSoup(req.text,'html.parser')
chapter=bs.find(class_='zjlist')
chapter=chapter.find_all('a')
def downbook(chapter):
    print(chapter)
    for i in tqdm( chapter ):

        book_name='诡秘2'
        chapter_name=i.text
        url=server+'/'+i.get('href')
        content=getHTMLText(url)
        with open(book_name, 'a', encoding='utf-8') as f:
                f.write(chapter_name)
                f.write('\n')
                f.write('\n'.join(content))
                f.write('\n')
# 开8个线程池
pool = ThreadPool(8)
results = pool.map(downbook, chapter)
pool.close()
pool.join()