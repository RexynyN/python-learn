from pytube import YouTube
import os 

def download_hd(urls):
    for url in urls:
        yt = YouTube(url)

        print("Eu tô baixando o video...")
        yt.streams.get_by_itag(137).download("", "video.mp4")
        print("Eu tô baixando o audio...")
        yt.streams.get_by_itag(251).download("", "audio.mp3")

        status = os.system(f"ffmpeg -i video.mp4 -i audio.mp3 -c:v copy -c:a aac \"{yt.title}.mp4\"")

        os.remove(f"video.mp4")
        os.remove(f"audio.mp3")

if __name__ == "__main__":
    urls = [
        "https://www.youtube.com/watch?v=jKnUcsUAkwI",
        "https://www.youtube.com/watch?v=acdvGJOt9wQ",
        "https://www.youtube.com/watch?v=1VR2I0HFFtk",
        # "",
        # "",
        # "",
    ]

    download_hd(urls)