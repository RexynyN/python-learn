import moviepy
import moviepy.editor as mpe

# Redondinho, pode usar 
my_clip = mpe.VideoFileClip("aot.mp4")
audio_background = mpe.AudioFileClip("aot.mp3")
final_clip = my_clip.set_audio(audio_background)
final_clip.write_videofile("aot2.mp4",fps=60)