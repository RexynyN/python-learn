from torrentp import TorrentDownloader

magnet = "magnet:?xt=urn:btih:8c81edeba688c6b9658032db5ba6e5b4771bc922&tr=http%3A%2F%2Fbt.uniondht.org%3A777%2Fannounce&tr=http%3A%2F%2Fretracker.local%2Fannounce&tr=http%3A%2F%2Fbt.rutor.org%3A2710%2Fannounce&tr=http%3A%2F%2Fpubt.net%3A2710%2Fannounce&tr=http%3A%2F%2Ftracker.publicbt.com%2Fannounce&tr=udp%3A%2F%2Ftracker.publicbt.com%3A80%2Fannounce&tr=udp%3A%2F%2Ftracker.openbittorrent.com%3A80%2Fannounce&tr=udp%3A%2F%2Ftracker.prq.to%3A80%2Fannounce&tr=http%3A%2F%2Ftracker.prq.to%2Fannounce"


torrent_file = TorrentDownloader(magnet, '.')
torrent_file.start_download()


