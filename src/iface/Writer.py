import multiprocessing
import threading
import queue
class Writer:
    task_queue = queue.Queue(10)

    def __init__(self, file_name):
        pass

    def write(self, content):
        self.task_queue.put(content)

    def finish(self):
        pass
