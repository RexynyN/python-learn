from pydub import AudioSegment
import os

files_path = os.getcwd()
file_name = '\\aot-op'

startMin = 0
startSec = 0

endMin = 1
endSec = 45

# Time to miliseconds
startTime = startMin * 60 * 1000 + startSec * 1000
endTime = endMin * 60 * 1000 + endSec * 1000

# Opening file and extracting segment
song = AudioSegment.from_mp3("aot.mp3")
extract = song[startTime:endTime]

# Saving
extract.export(file_name+'-extract.mp3', format="mp3")
