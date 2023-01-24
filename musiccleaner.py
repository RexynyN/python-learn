from shutil import move as replace_file
from mutagen.easyid3 import EasyID3
from mutagen.id3 import APIC, ID3
from mutagen.mp3 import MP3
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import askdirectory
from io import BytesIO
from PIL import Image
import os
import mutagen

class MusicCleaner:
    def __init__ (self):
        self.path = ""
        self.__get_blacklist()
        self.blacklist = self.__blacklist_iterator(self.keywords, self.separators)

    def __init__(self, path="", all_subfolders=False):
        self.all_subfolders = all_subfolders
        self.path = path
        if path != "":
            self.files = os.listdir(path)
        self.__get_blacklist()
        self.blacklist = self.__blacklist_iterator(self.keywords, self.separators)

    def __blacklist_iterator(self, keywords, separators):
        blacklist = []
        for word in keywords:
            for sep in separators:
                blacklist.append(f"{sep[0]}{word}{sep[1]}")
                blacklist.append(f"{sep[0]}{word.upper()}{sep[1]}")
                blacklist.append(f"{sep[0]}{word.lower()}{sep[1]}")

        return blacklist

    def __get_blacklist(self):
        self.separators = [("(", ")"), ("[", "]"), ("<", ">"), ("【", "】")]
        self.keywords = ["CC", "Lyrics", "Lyric", "𝙻𝚈𝚁𝙸𝙲𝚂", "With Subtitles", "With Lyrics" "Official Video", "Official Music Video", "Music Video", "Official Lyrics Video", "Lyric Video", "Lyrics Video"
                    "Official Lyric Video", "Extended", "Extended Audio", "Audio", "Official Audio", "Clean", "Clean Audio", "Visualizer", "Official Visualizer", "MV", "AMV",
                    "Free Download", "Download", "Link in Description", "Premiere", "New Release", "HD"]


    def override_blacklist(self, keywords, separators=[("", "")]):
        self.blacklist = []

        if separators == [("", "")]:
            separators = self.separators

        self.blacklist = self.__blacklist_iterator(keywords, separators)
        
    def check_name(self, filename, path=""):
        sentinel = False
        old = filename

        for term in self.blacklist:
            if filename.find(term) != -1:
                filename = filename.replace(term, "")
                sentinel = True

        if sentinel and path != "":
            cleaner = filename.split(".")
            filename = f"{cleaner[0].strip()}.{cleaner[-1].strip()}"
            replace_file(f"{path}\\{old}", f"{path}\\{filename}")

        return filename

    def set_folder_cover(self, image="", scheme=[("", "")]):
        '''
        The "scheme" variable is a list of tuples that work in the following way: 

        (<subfolder of the self.path>, <path of the image associated with the folder>)

        If you wish to set the cover to the root of self.path, use a empty string.
        '''
        if self.all_subfolders:
            for pair in scheme:
                path = f"{self.path}\\{pair[0]}"
                for file in os.listdir(path):
                    self.set_cover(f"{path}\\{file}", pair[1])
        else:
            for file in os.listdir(self.path):
                self.set_cover(f"{self.path}\\{file}", image)


    def set_cover(self, audio_path="", image_path=""):
        # Set the track cover to a specified image:
        audio = ID3(audio_path)

        image_file = image_path.split("\\")[-1]
        print(image_file)


        if audio.getall('APIC') != []:
            audio.delall("APIC")

        with open(image_path, 'rb') as albumart:
            audio.add(APIC(
                encoding=3,
                mime=f'image/{image_file.split(".")[-1]}',
                type=3,
                desc=u'Cover',
                data=albumart.read()
            ))

            
        audio.save(v2_version=3)


    def get_cover(self, path):
        # get the album cover from the track itself

        path = os.path.join(
            "E:\\Mídia\\musictest\\Quarentena Vibes Parte 1\\again&again – Eighty-Five.mp3")
        track = MP3(path)
        tags = ID3(path)
        print("ID3 tags included in this song ------------------")
        print(tags)
        print("-------------------------------------------------")
        pict = tags.get("APIC:").data
        print(pict)

        im = Image.open(BytesIO(pict))
        im.save("a.jpg")
        print('Picture size : ' + str(im.size))

    def get_metadata(self, path):
        try:
            metadata = EasyID3(path)
            return metadata
        except mutagen.id3._util.ID3NoHeaderError:
            try:
                mp3 = MP3(path)
                mp3.tags = ID3()
                mp3.save(v1=0, v2_version=3)

                metadata = EasyID3(path)
                return metadata

            except mutagen.id3.ID3NoHeaderError:
                try:
                    tags = ID3()
                    tags.save(path)
                    metadata = EasyID3(path)
                    return metadata

                except mutagen.id3.ID3NoHeaderError:
                    print("Não foi possível ler os metadados")

                    
    def strip_all_covers(self):
        "How to remove all covers from the tracks of the directory"

    def check_metadata(self, path="", file=""):
        # split all chars in the title, and find the first occurence of one of the separators, then split the string using it, to separate the title from the artist
        meta = self.get_metadata(f"{path}\\{file}")
        
        if not meta: 
            return

        separators = ["-", "–", "—"]
        file = file.split(".")[0]

        name = file
        for char in [char for char in name]:
            if char in separators:
                name = name.split(char)
                break

        if name != file.split(".")[0]:
            meta["artist"] = name[0].strip()
            meta["title"] = name[1].strip()
        else:
            meta["title"] = name.strip()

        meta.save()

    def clean_music(self):
        folders = self.path if not self.all_subfolders else [
            x[0] for x in os.walk(self.path)]

        for dire in folders:
            for file in os.listdir(dire):
                if file.find(".") != -1:
                    file = self.check_name(dire, file)
                    self.check_metadata(dire, file)

    def clean_file(self, path):
        "mesmo que o clean_music, só que no caso é com uma arquivo só"
        pass

    def set_metadata(self, path, filename, author="", title="", cover_path="", album="", check=False):
        self.set_cover(f"{path}\\{filename}", cover_path)

        meta = self.get_metadata(f"{path}\\{filename}")

        meta["artist"] = self.check_name(author) if check else author 
        meta["title"] = title
        meta["album"] = album
        meta.save()

    def refresh_path(self, path, all_subfolders=False):
        self.path = path
        self.files = os.listdir(path)
        self.all_subfolders = all_subfolders


if __name__ == "__main__":
    # base_dir = "E:\\Mídia\\musictest\\Quarentena Vibes Parte 2"
    base_dir = askdirectory()
    # filename = askopenfilename()

    cleaner = MusicCleaner(path=base_dir, all_subfolders=False)
    # cleaner.clean_music()

    cleaner.set_folder_cover("Quarentena Vibes Parte 1.jpg")

    # cleaner.set_folder_cover([
    #     ("Quarentena Vibes Parte 5", "reacao.jpg"),
    #     ("Quarentena Vibes Parte 3","reacao.jpg")
    # ])


