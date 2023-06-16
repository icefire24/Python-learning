import os
from youtube_dl import YoutubeDL
# from test import srcs
srcs=['https://www.youtube.com/watch?v=LtFujAtKM5I&list=PLMinhigDWz6emRKVkVIEAaePW7vtIkaIF&index=1&pp=iAQB']

def main():
    for src in srcs:
        index=srcs.index(src)
        downvideo(src)

def downvideo(url):
    ydl_opts = {
        'outtmpl': './test/%(title)s.%(ext)s',
        'format': 'bestvideo+bestaudio/best',
        'noplaylist': True,
        'progress_hooks': [my_hook],
    }
    cmd='youtube-dl --write-auto-sub --sub-lang en --sub-format "ass/srt/best"  --skip-download -i '+url
    print(cmd)
    os.system(cmd) 
    # with YoutubeDL(ydl_opts) as ydl:
    #     ydl.download([url])


def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now converting ...')

if __name__ == "__main__":
    main()