import multiprocessing
import threading


class Writer:
    __task_queue = multiprocessing.Queue(10)

    def __init__(self, file_name, path):
        self.__path = path + file_name
        self.__file_name = file_name

    def write(self):
        with open(self.__path, mode="a") as f:
            f.write(self.__task_queue.get())

    def add(self, content):
        self.__task_queue.put(content)
        thread = threading.Thread(target=self.write())
        thread.start()
        thread.join()

