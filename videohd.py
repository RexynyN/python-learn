from pytube import YouTube
import os 

def download_videos(urls):
    resolutions = ["1080p", "720p", "480p", "360p", "240p", "144p"]
    audio_quality = ["160kbps", "128kbps", "70kbps", "50kbps", "48kbps"]
    for url in urls:
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
            stream = yt.streams.filter(progressive=True, resolution=best_res).first()
            stream.download("", yt.title)
            print(f"{yt.title} foi baixado com sucesso!")
        else:
            # If not, downloads the audio and video separatedly
            print("O vídeo não possui uma stream progressiva, o áudio e o vídeo serão baixados separadamente.")
            video_stream = yt.streams.filter(resolution="720p", mime_type="video/mp4", only_video=True).first()
            

            # Finds the best audio quality to download from
            best_res = ""
            for audio in audio_quality:
                if yt.streams.filter(only_audio=True, abr=audio):
                    best_res = audio
                    break

            audio_stream = yt.streams.filter(only_audio=True, abr=best_res).first()

            # Downloads video
            print("Eu tô baixando o video...")
            video_stream.download("", "video.mp4")

            # Downloads audio
            print("Eu tô baixando o audio...")
            audio_stream.download("", "audio.mp3")

            # Using ffmpeg, merge the video and audio
            print("Eu tô juntando os dois... (pode demorar um pouquinho dependendo do tamanho do vídeo, segura aí)")
            status = os.system(f"ffmpeg -i video.mp4 -i audio.mp3 -c:v copy -c:a aac \"{yt.title}.mp4\" -hide_banner -loglevel error")

            # Remove the individual files
            os.remove(f"video.mp4")
            os.remove(f"audio.mp3")

            print(f"{yt.title} foi baixado com sucesso!")

        print("\n")


if __name__ == "__main__":
    urls = [
        # "https://www.youtube.com/watch?v=MVj3eC5Q1Og",
        # "https://www.youtube.com/watch?v=9iFKJ8_EUA8",
        "https://www.youtube.com/watch?v=w7Legsnb7KQ",
        "https://www.youtube.com/watch?v=ukU2WZ_lbbI",
        "https://www.youtube.com/watch?v=TMF49V9i__o"
        # "",
    ]

    download_videos(urls)