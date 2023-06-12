import os
from pytube import YouTube
from pytube import Playlist
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
from selenium import webdriver
import time
from multiprocessing.dummy import Pool as ThreadPool
root='https://www.youtube.com'
def main():
    pa()


def pa():  # 爬取动态下滑加载网页
    options = webdriver.ChromeOptions()
    options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    driver = webdriver.Chrome(chrome_options=options)
    driver.get("https://www.youtube.com/playlist?list=PLMinhigDWz6emRKVkVIEAaePW7vtIkaIF")
    # button=driver.find_element('xpath','/html/body/main/div[3]/a[1]')
    # button.click()
    
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
        }, 20000);
    '''
    driver.execute_script(js)
    time.sleep(20)
    bs = BeautifulSoup(driver.page_source, "html.parser")
    driver.close()
    videos = bs.find_all(id='video-title')
    for video in videos:
        src = video['href']
        print("%s\n" % src)
        downvideo(root+src)
    # print(len(videos))
    # downvideo(videos)
def downvideo(url):
    yt=YouTube(url)
    yt.streams.filter(progressive=True).order_by('resolution').desc().first().download('./videos')

if __name__ == "__main__":
    main()


# playList='https://www.youtube.com/playlist?list=PLMinhigDWz6emRKVkVIEAaePW7vtIkaIF'
# src='https://www.youtube.com/watch?v=LtFujAtKM5I&list=PLMinhigDWz6emRKVkVIEAaePW7vtIkaIF&index=1&ab_channel=SketchpunkLabs'

# pl = Playlist("https://www.youtube.com/playlist?list=PLMinhigDWz6emRKVkVIEAaePW7vtIkaIFU")
# print(pl)


# create a Playlist object
# playlist = Playlist(playList)
# for video in playlist.videos:
#     print(f"Downloading video: {video.title}")
#     video.streams.get_highest_resolution().download('/funwebgl')