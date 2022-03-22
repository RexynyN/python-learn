from pytube import YouTube, Playlist, Search

def main():
    type_of_content = str(input(
        "Which type of content you want:\n-v for video\n-m for audio\n-p for playlist\n-s to search for a video\n-q to quit the program\n-h for help\n"))

    while type_of_content != 'q':

        if type_of_content == 'v':
            path = str(input("What is the url for the video: "))
            yt = YouTube(path)
            yt.streams.get_by_itag(22).download(output_path="../../Downloads")
            print("Download successful")

        elif type_of_content == 'm':
            path = str(input("What is the url for the music: "))
            yt = YouTube(path)
            yt.streams.get_by_itag(140).download(output_path="../../Downloads")
            print("Download successful")

        elif type_of_content == 'p':
            path = str(input("What is the url for the playlist: "))
            tmp = str(input("it's a music playlist or a video one: "))
            p = Playlist(path)
            while True:
                if tmp == 'music':
                    for video in p.videos:
                        video.streams.get_by_itag(140).download(
                            output_path="../../Downloads")
                    break
                elif tmp == 'video':
                    for video in p.videos:
                        video.streams.get_by_itag(22).download(
                            output_path="../../Downloads")
                    break
                else:
                    print("error, choose a valid type of playlist, music or video: ")
                    tmp = str(input(""))
            print("Download successful")
        elif type_of_content == 's':
            blob = str(input("What you wanna search: "))
            tmp = str(input("it's a music or a video: "))
            sc = Search(blob)
            while True:
                if tmp == 'music':
                    s = sc.results[1].streams.get_by_itag(
                        140).download(output_path="../../Downloads")
                    break
                elif tmp == 'video':
                    s = sc.results[1].streams.get_by_itag(
                        22).download(output_path="../../Downloads")
                    break
                else:
                    print("error, choose a valid type of playlist, music or video ")
                    tmp = str(input(""))
            print("Download successful")

        else:
            print("This command does not exist, type h for help")
        type_of_content = str(input("What you want to do now? "))


if __name__ == "__main__":
    main()