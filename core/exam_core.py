import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import torch
import pytesseract
from PIL import Image


pytesseract.pytesseract.tesseract_cmd = r"/usr/bin/tesseract"


class ProcessData:

    def __init__(self, *args, **kwargs):
        self.pwd = os.path.dirname(os.path.realpath(__file__))
        self.csv_14_july = "core/info2.csv"
        self.csv_12_july = "core/info.csv"
        self.data_raw = []
        self.im = Image.open('core/12jul.jpeg')

    def read_csv_panda(self):
        df = pd.read_csv(self.csv_14_july)
        self.data_raw = df.iloc[:,0:3].values

    def data_analisis(self):
        #print(pytesseract.image_to_string(self.im))
        data_raw = pytesseract.image_to_string(self.im)
        data_split = data_raw.split()
        i = 13
        data_dict = {}
        #This creates a dictionary with the data from the image.
        for data in data_split[13:130]:
            temp = data
            data_dict[data + " " + temp] = i
        print(data_dict)

    def run(self):
        self.read_csv_panda()
        self.data_analisis()
        
        