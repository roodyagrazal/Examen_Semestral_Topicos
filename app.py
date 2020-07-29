from core import ProcessData

class Procees_Data(ProcessData):
    pass

if __name__ == "__main__":
    ctx = {}
    process = ProcessData(**ctx)
    process.run()