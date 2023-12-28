from model.Writer import Writer
from model.Reader import Reader


class Downloader:
    __writer = None
    __reader = None
    __analyser = None

    def __init__(self, read_file_name, read_file_path, write_file_name, write_file_path):
        self.__writer = Writer(write_file_name, write_file_path)
        self.__reader = Reader(read_file_name, read_file_path)

    def download(self):
        pass
        # threading.Thread(target=self.writer.write())
