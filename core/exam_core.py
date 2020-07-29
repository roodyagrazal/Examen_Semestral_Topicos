import os
import numpy as np
import pandas as pd


class ProcessData:

    def __init__(self, *args, **kwargs):
        self.pwd = os.path.dirname(os.path.realpath(__file__))
    
    def get_file_info(self):
        file = open("core/info.csv", "r")
        with file as csv:
            print(csv.readlines())

    def read_csv_panda(self):
        df = pd.read_csv("core/info.csv")
        data = df.iloc[:,0:3].values
        print(data)

    def run(self):
        self.get_file_info()
        self.read_csv_panda()