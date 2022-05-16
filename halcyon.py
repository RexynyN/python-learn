from pytube import YouTube, Playlist, Search
import os 
import unicodedata
import re
import colorama
from requests import get
from shutil import copyfileobj
from musiccleaner import MusicCleaner
from PIL import Image
from colorama import init
init()


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
        value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore').decode('ascii')
    value = re.sub(r'[^\w\s-]', '', value.lower())
    return re.sub(r'[-\s]+', '-', value).strip('-_')

def crop_cover(filepath=""):
    # We'll be cropping the image to a 300x300 dimensions
    img = Image.open(filepath)
    print(img.size)

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
        print(colorama.Fore.GREEN + f"\r|{bar}| {percent:.2f} {message}", end="\r")
        print("\n")

# Uses the img source to download the image
def handleImg(src, name=""):
    img_path = f"{os.getcwd()}\\__img_data__\\"

    if not os.path.isdir(img_path):
        os.mkdir(img_path)

    dir = os.listdir(img_path)

    image_url = src
    filename = image_url.split("?")[0].split("/")[-1] if not name else f"{name}.jpg"

    if not filename in dir:
        response = get(image_url, stream=True)
        response.raw.decode_content = True

        with open(img_path + filename, 'wb') as f:
            copyfileobj(response.raw, f)

    return filename


# ============================== CONFIGS =========================================
# The video/playlist url
url = "https://www.youtube.com/playlist?list=PL9inGG514dORjBGs3JWlK-3oa44Gdv7c7"

# Either "playlist" or "video"
mode = "playlist"

# Either "thumbnail" or "custom"
cover = "custom"

# if cover is "custom", uses this file path to retrieve the image
custom_cover = "Quarentena Vibes Finale.jpg"

# ================================================================================


cleaner = MusicCleaner()

if mode == "playlist":
    yt = Playlist(url)
    queue = yt.videos
    if queue == []:
        print("A playslist é privada ou não existe")
        quit()
else:
    yt = YouTube(url)
    queue = [yt]

# If there is no subfolder for the songs, create a new one
songs_path = f"{os.getcwd()}\\music"
if not os.path.isdir(songs_path):
    os.mkdir(songs_path)

prog = 0
total = (len(queue) * 5) + 1
for yt in queue:
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
        cover_path=f"{os.getcwd()}\\__img_data__\\{song}.jpg"
        crop_cover(cover_path)

    prog += 1
    progressbar(prog, total, message="Downloading the video...")
    # This one is for getting the music in the webm format in 160kbps - Prefer this, but the other is a fallback
    yt.streams.get_by_itag(251).download(output_path=songs_path, filename=f"{song}.mp4")

    # # This one is for getting the music in the mp4 format in 128kbps
    # yt.streams.get_by_itag(140).download(output_path=songs_path, filename=f"{song}.mp3")

    prog += 1
    progressbar(prog, total, message="Converting to MP3...")
    this_song = f"{songs_path}\\{song}"
    status = os.system(f"ffmpeg -i \"{this_song}.mp4\" \"{this_song}.mp3\" -hide_banner -loglevel error")
    os.remove(f"{this_song}.mp4")

    prog += 1
    progressbar(prog, total, message="Writing metadata...")
    cleaner.set_metadata(f"{songs_path}", f"{song}.mp3", author=author, title=title, cover_path=cover_path, album="", check=False)


prog += 1
progressbar(prog, total, message="Done!")


# # For testing the streams
# print(yt.streams.filter())
# for i in yt.streams:
#     print(i)

# # For downloading the video and audio separately then merging them together
# yt = YouTube("https://www.youtube.com/watch?v=Oz6x10vRbOY")
# for i in yt.streams.filter(file_extension='mp4'):
#     print(i)
# yt.streams.get_by_itag(137).download("", "video.mp3")
# yt.streams.get_by_itag(251).download("", "audio.mp3")
# status = os.system(f"ffmpeg -i video.mp4 -i audio.mp3 -c:v copy -c:a aac grease.mp4")

