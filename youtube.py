from pytube import YouTube
import sys

yt = YouTube("https://www.youtube.com/watch?v=w2y715XAmso")

# print(yt.streams.filter(file_extension='mp4', resolution="1080p"))

print(yt.streams.filter(only_audio=True))

# stream = yt.streams.get_by_itag(299)
stream = yt.streams.get_by_itag(299)

stream.download()

args = sys.argv

if("-h" in args or "-help" in args):
    print_help()
    exit()


if("-folder" in args[1]):
    print(sexo)




