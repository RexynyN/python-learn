from torrentp import TorrentDownloader
torrent_file = TorrentDownloader("test.torrent", '.')
torrent_file.start_download()
