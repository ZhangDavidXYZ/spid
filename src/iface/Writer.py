import multiprocessing
import threading


class Writer:
    task_queue = multiprocessing.Queue(10)
    path = "/"
    file_name = "undefined"

    def __init__(self, file_name, path):
        self.path = path + file_name
        self.file_name = file_name

    def write(self):
        with open(self.path, mode="a") as f:
            f.write(self.task_queue.get())

    def add(self, content):
        self.task_queue.put(content)
        thread = threading.Thread(target=self.write())
        thread.start()
        thread.join()

