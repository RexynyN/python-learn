import os
import unicodedata
import re
import colorama
import subprocess
from os.path import join as join_path
from pytube import YouTube, Playlist
from requests import get
from shutil import copyfileobj
from PIL import Image
from colorama import init
# import moviepy.editor as mp
# from musiccleaner import MusicCleaner

init()


# ============================== CONFIGS =========================================
# The video/playlist urls
urls = [
    "https://www.youtube.com/watch?v=FNYRTmXBAVY",
    "https://www.youtube.com/watch?v=BkDQI-W1Wh4",
    "https://www.youtube.com/watch?v=8km6wx0wRAI",
    "https://www.youtube.com/watch?v=Xg0dFud8kqM",
    "https://www.youtube.com/watch?v=rpqmDEBlTIc",
]

# Either "playlist" or "video"
mode = "video"

# Either "video" or "music"
file = "video"

# Either "thumbnail" or "custom", just if file = "music"
cover = "custom"

# if cover is "custom", uses this file path to retrieve the image, just if file = "music"
custom_cover = "source\\Quarentena Vibes Finale.jpg"

# to use ffmpeg converter, must install it; either True or False
ffmpeg_convert = True

# an array of arrays of tuples, to make clips 
clips = [
#     [("00:00:00", "00:00:00"), ("00:00:00", "00:00:00")], # clip 1
#     [("00:00:00", "00:00:00")], # clip 2
]

# ================================================================================
 
def moviepy_convert(path, file):
    mp4_path = os.path.join(path, file)
    mp3_path = os.path.join(path, os.path.splitext(file)[0] + ".mp4")
    file = mp.AudioFileClip(mp4_path)
    file.write_audiofile(mp3_path)
    os.remove(mp4_path)


def clean_filename(name):
    forbidden_chars = '"*\\/\'.|?:<>'
    filename = ''.join([x if x not in forbidden_chars else '' for x in name])
    if len(filename) >= 176:
        filename = filename[:170] + '...'
    return filename


def slugify(value, allow_unicode=False):
    value = str(value)
    if allow_unicode:
        value = unicodedata.normalize('NFKC', value)
    else:
        value = unicodedata.normalize('NFKD', value).encode(
            'ascii', 'ignore').decode('ascii')
    value = re.sub(r'[^\w\s-]', '', value.lower())
    return re.sub(r'[-\s]+', '-', value).strip('-_')


def crop_cover(filepath=""):
    # We'll be cropping the image to a 300x300 dimensions
    img = Image.open(filepath)

    width, height = img.size   # Get dimensions

    offset = 350
    if height < offset:
        offset = height

    left = (width - offset)/2
    top = (height - offset)/2
    right = (width + offset)/2
    bottom = (height + offset)/2

    # Crop the center of the image
    img = img.crop((left, top, right, bottom))

    img.save(filepath)


def progressbar(progress, total, message="", color=colorama.Fore.YELLOW):
    percent = 100 * (progress / float(total))

    # # A larger bar, if you need xD
    # bar = '█' * int(percent) + "-" * (100 - int(percent))

    bar = '█' * int(percent/2) + "-" * (50 - int(percent/2))
    print(color + f"\r|{bar}| {percent:.2f} {message}", end="\r")
    if progress == total:
        print(colorama.Fore.GREEN +
              f"\r|{bar}| {percent:.2f} {message}", end="\r")
        print("\n")

# Uses the img source to download the image


def handleImg(src, name=""):
    img_path = f"{os.getcwd()}\\__img_data__\\"

    if not os.path.isdir(img_path):
        os.mkdir(img_path)

    dir = os.listdir(img_path)

    image_url = src
    filename = image_url.split("?")[0].split(
        "/")[-1] if not name else f"{name}.jpg"

    if not filename in dir:
        response = get(image_url, stream=True)
        response.raw.decode_content = True

        with open(img_path + filename, 'wb') as f:
            copyfileobj(response.raw, f)

    return filename


def download_videos(urls, path):
    resolutions = ["2160p", "1440p", "1080p",
                   "720p", "480p", "360p", "240p", "144p"]
    audio_quality = ["160kbps", "128kbps", "70kbps", "50kbps", "48kbps"]
    for url in urls:
        if not url:
            continue

        yt = YouTube(url)

        print(f"Trabalhando com o vídeo: \"{yt.title}\"")

        # Finds the best video quality to download from
        best_res = ""
        for res in resolutions:
            if yt.streams.filter(resolution=res):
                best_res = res
                break

        print(f"Melhor resolução encontrada para este vídeo é {best_res}")
        # Checks if it has a progressive stream
        if yt.streams.filter(progressive=True, resolution=best_res):
            # If there is, downloads it
            print("Stream progressiva encontrada, baixando...")
            stream = yt.streams.filter(
                progressive=True, resolution=best_res).first()
            stream.download(path, f"{clean_filename(yt.title)}.mp4")
            print(f"{yt.title} foi baixado com sucesso!")
        else:
            # If not, downloads the audio and video separatedly
            print(
                "O vídeo não possui uma stream progressiva, o áudio e o vídeo serão baixados separadamente.")
            video_stream = yt.streams.filter(
                resolution="720p", mime_type="video/mp4", only_video=True).first()

            # Finds the best audio quality to download from
            best_res = ""
            for audio in audio_quality:
                if yt.streams.filter(only_audio=True, abr=audio):
                    best_res = audio
                    break

            audio_stream = yt.streams.filter(
                only_audio=True, abr=best_res).first()

            # Downloads video
            print("Eu tô baixando o video...")
            video_stream.download("", "video.mp4")

            # Downloads audio
            print("Eu tô baixando o audio...")
            audio_stream.download("", "audio.mp3")

            # Using ffmpeg, merge the video and audio
            print("Eu tô juntando os dois... (pode demorar um pouquinho dependendo do tamanho do vídeo, segura aí)")
            subprocess.call(f"ffmpeg -i video.mp4 -i audio.mp3 -c:v copy -c:a aac \"{join_path(path, clean_filename(yt.title))}.mp4\" -hide_banner -loglevel error")

            # Remove the individual files
            os.remove(f"video.mp4")
            os.remove(f"audio.mp3")

            print(f"{yt.title} foi baixado com sucesso!")

        print("\n")


def download_songs(urls, songs_path):
    cleaner = MusicCleaner()
    audio_quality = ["160kbps", "128kbps", "70kbps", "50kbps", "48kbps"]
    prog = 0
    total = (len(urls) * 5) + 1
    for url in urls:
        yt = YouTube(url)

        prog += 1
        progressbar(prog, total, message="Cleaning the metadata...")

        # Clears the file name and brings metadata
        clean_title = cleaner.check_name(yt.title)
        separators = ["-", "–", "—"]
        # If the title of the video is not the full song title (author - title), uses the channel name as the song author
        if not any(x in clean_title for x in separators):
            # if there is " - Topic" in the name of the channel, strips it
            song = yt.author.replace(" - Topic", "")
            author = song
            song += f" - {clean_title}"
            title = clean_title
        else:
            song = clean_title
            # split all chars in the title, and find the first occurence of one of the separators, then split the string using it, to separate the title from the artist
            for char in [char for char in song]:
                if char in separators:
                    name = song.split(char)
                    break

            author = name[0].strip()
            title = name[1].strip()

        song = clean_filename(song)

        prog += 1
        progressbar(prog, total, message="Taking care of the cover...")
        if cover == "custom":
            cover_path = custom_cover
        else:
            # Retrieve the thumbnail, if chosen to
            handleImg(yt.thumbnail_url, name=song)
            cover_path = f"{os.getcwd()}\\__img_data__\\{song}.jpg"
            crop_cover(cover_path)

        prog += 1
        progressbar(prog, total, message="Downloading the video...")
        best_res = ""
        for audio in audio_quality:
            if yt.streams.filter(only_audio=True, abr=audio):
                best_res = audio
                break

        audio_stream = yt.streams.filter(only_audio=True, abr=best_res).first()
        audio_stream.download(output_path=songs_path, filename=f"{song}.mp4")

        prog += 1
        progressbar(prog, total, message="Converting to MP3...")
        this_song = join_path(songs_path, song)

        subprocess.call(["ffmpeg", "-i", this_song + ".mp4", "-i", this_song + ".mp3", "-hide_banner -loglevel error"])
        
        os.remove(f"{this_song}.mp4")

        prog += 1
        progressbar(prog, total, message="Writing metadata...")
        cleaner.set_metadata(f"{songs_path}", f"{song}.mp3", author=author,
                             title=title, cover_path=cover_path, album="", check=False)

    prog += 1
    progressbar(prog, total, message="Done!")

def create_clips(clips, files):

    for clip in clips:
        for chunk in clip:
            start_time = chunk[0]
            end_time = chunk[1]

            subprocess.call(['ffmpeg', '-i', input_file, '-ss', start_time, '-to', end_time, '-c', 'copy', output_file])

            # # Usa duração
            # duration = "10"
            # subprocess.call(['ffmpeg', '-i', input_file, '-ss', start_time, '-t', duration, '-c', 'copy', output_file])

def download_playlists(urls, path, mode):
    for url in urls:
        playlist = Playlist(url)

        urls = playlist.video_urls
        if not urls:
            print("A playlist é privada ou não existe")
            continue

        if mode == "video":
            download_videos(urls, path)
        elif mode == "music":
            download_songs(urls, path)
        else:
            print("Nenhuma opção de playlist foi escolhida")
            break


if __name__ == '__main__':
    if clips and len(clips) != len(urls):
        print("The clips array is missing arguments for all the videos")
        exit()

    # If there is no subfolder for the videos/songs, create a new one
    path = os.path.join(os.getcwd(), file)
    if not os.path.isdir(path):
        os.mkdir(path)

    
    if mode == "playlist":
        download_playlists(urls, path, file)
    elif mode == "video" and file == "video":
        download_videos(urls, path)
    elif mode == "video" and file == "music":
        pass
    else:
        print("Nenhuma opção foi selecionada.")

