from types import ClassMethodDescriptorType
from pytube import YouTube

link = input('Link: ')
yt = YouTube(link)

ys = yt.streams.get_highest_resolution()
ys.download('path/for/directory')
