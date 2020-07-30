import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pytesseract



class ProcessData:

    def __init__(self, *args, **kwargs):
        self.pwd = os.path.dirname(os.path.realpath(__file__))
        self.csv_14_july = "core/info2.csv"
        self.csv_12_july = "core/info.csv"
        self.data_raw = []

    def read_csv_panda(self):
        df = pd.read_csv(self.csv_14_july)
        self.data_raw = df.iloc[:,0:3].values

    def data_analisis(self):
        print(self.data_raw)

    def run(self):
        self.read_csv_panda()
        self.data_analisis()
        