import Writer
import Reader
from iface.Downloader import Downloader
from iface.Analyser import Analyser


class M3U8Downloader(Downloader):
    def __init__(self, read_file_name, read_file_path, write_file_name, write_file_path):
        super().__init__(read_file_name, read_file_path, write_file_name, write_file_path)
        self.analyser = Analyser("test")

    def download(self):
        self.__reader.read()


