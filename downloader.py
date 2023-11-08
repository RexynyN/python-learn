import internetdownloadmanager as idm 

URL = ""
OUTPUT = ""

down = idm.Downloader(worker=25, part_size=1024*1024*10, resumable=True)

down.download(URL, OUTPUT)