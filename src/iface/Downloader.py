import threading

import Writer


class Downloader:
    writer = None
    reader = None

    def __init__(self, file_name, path):
        self.writer = Writer.Writer("test", "/")
        # self.writer = Writer.Writer(file_name, path)

    def download(self):
        pass
        # threading.Thread(target=self.writer.write())
