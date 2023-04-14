import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
from multiprocessing.dummy import Pool as ThreadPool

def getHTMLText(target):
    req=requests.get(url=target)
    req.encoding=req.apparent_encoding
    bs=BeautifulSoup(req.text,'html.parser')
    texts=bs.find('div',id='booktxt')
    return texts.text.strip().split('\xa0'*4)

def downbook(i):
    book_name='亵渎.txt'
    chapter_name=i.text
    url='https://www.biqugei.net'+i.get('href')
    content=getHTMLText(url)
    with open(book_name, 'a', encoding='utf-8') as f:
        f.write(chapter_name)
        f.write('\n')
        f.write('\n'.join(content))
        f.write('\n')

if __name__ == '__main__':
    server='https://www.biqugei.net/catalog/7268/1.html'
    req=requests.get(url=server)
    bs=BeautifulSoup(req.text,'html.parser')
    chapter=bs.find('dl').find_all('a')
    
    # 创建线程池
    pool = ThreadPool(8)
    
    # 下载小说
    for i in tqdm(chapter):
        pool.apply_async(downbook, args=(i,))
        
    # 关闭线程池
    pool.close()
    pool.join()
    
    print('下载完成！')
