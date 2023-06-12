from os import times
from bs4 import BeautifulSoup
import urllib.error
from bs4 import BeautifulSoup  # 解析html的
from selenium import webdriver
import time
# from selenium.webdriver.common.keys import Keys  # 模仿键盘,操作下拉框的

def main():
    pa()


def pa():  # 爬取动态下滑加载网页
    options = webdriver.ChromeOptions()
    options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    driver = webdriver.Chrome(chrome_options=options)
    driver.get("https://www.relamanhua.com/comic/fenghuoliaoyuan/chapter/4f651236-12ef-11eb-976c-00163e0ca5bd")
    button=driver.find_element('xpath','/html/body/main/div[3]/a[1]')
    button.click()
    
    js = '''
                let height = 0
        let interval = setInterval(() => {
            window.scrollTo({
                top: height,
                behavior: "smooth"
            });
            height += 500
        }, 500);
        setTimeout(() => {
            clearInterval(interval)
        }, 15000);
    '''
    driver.execute_script(js)
    time.sleep(30)
    bs = BeautifulSoup(driver.page_source, "html.parser")
    driver.close()
    images = bs.find_all('img','lazyload')
    for img in images:
        src = img['data-src']
        print("%s\n" % src)


if __name__ == "__main__":
    main()

