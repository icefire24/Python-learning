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
    driver.get("https://www.youtube.com/playlist?list=PLMinhigDWz6emRKVkVIEAaePW7vtIkaIF")
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
        }, 7000);
    '''
    driver.execute_script(js)
    time.sleep(30)
    bs = BeautifulSoup(driver.page_source, "html.parser")
    driver.close()
    list = bs.find_all(id='video-title')
    print(list)
    for i in range(len(list)):
        list[i] = list[i].__getattribute__('href')
        print("%s\n" % list[i])


if __name__ == "__main__":
    main()

