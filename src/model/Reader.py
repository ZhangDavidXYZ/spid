class Reader:
    def __init__(self, file_name, path):
        self.__path = path + file_name
        self.__file_name = file_name

    def read(self):
        with open(self.__path, mode="r") as f:
            return f.read()

