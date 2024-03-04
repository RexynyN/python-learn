import sys
import os
import requests as r
import wget

filedir = os.path.join('C:/Users/admin/Downloads')

try:
    LINK = "https://www.facebook.com/peopleareawesome/videos/637730157348346/" #url of video to be downloaded
    html = r.get(LINK)
except r.ConnectionError as e:
    print("Error in connecting")
except r.Timeout as e:
    print("Timeout")
except r.RequestException as e:
    print("Invalid URL")
except (KeyboardInterrupt, SystemExit):
    print("System has quit")
    sys.exit(1)
except TypeError:
    print("Video seems to be private ")
else:
    print("\n")
    print("Video Quality:Normal " )
    print("[+] Starting Download")
    wget.download(LINK,filedir)
    print("\n")
    print("Video downloaded")