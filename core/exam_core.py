class ProcessData:

    def __init__(self, *args, **kwargs):
        self.pwd = os.path.dirname(os.path.realpath(__file__))
    
    def run(self):
        print(self.pwd)