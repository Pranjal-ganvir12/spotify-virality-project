#data cleaning will happen here

import pandas as pd

class Datahandler:
    def __init__(self, path):
        self.path = path 
        
    def load(self, cols=None):
        pd.read_csv()
