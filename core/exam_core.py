import os

class ProcessData:

    def __init__(self, *args, **kwargs):
        self.pwd = os.path.dirname(os.path.realpath(__file__))
    
    def get_file_info(self):
        file = open("core/info.csv", "r")
        with file as csv:
            print(csv.readlines())

    def run(self):
        self.get_file_info()