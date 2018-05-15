
from pytube import YouTube
from get_list import crawl

# list=[
#
# 'https://www.youtube.com/watch?v=_V7MntH_Tu8',
# ]

list = crawl('https://www.youtube.com/watch?v=Ol4w4E7XIUI&list=PL2F44B2F76C6A9B44')
for file in list:
    try:
        video = YouTube(file)
        streams = video.streams
        stream = streams.get_by_itag(18)
        stream.download()
        print(video.title)
    except:
        print("Failed to get {}".format(file))
        raise
