import Writer
import Reader
import iface.Downloader


class M3U8Downloader(iface.Downloader):
    def __init__(self, read_file_name, read_file_path, write_file_name, write_file_path):
        super().__init__(read_file_name, read_file_path, write_file_name, write_file_path)
        self.analyser =

    def download(self):
        self.__reader.read()


