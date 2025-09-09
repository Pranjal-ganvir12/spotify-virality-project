#data cleaning will happen here

import pandas as pd

class Datahandler:
    def __init__(self, path):
        self.path = path 
        self.df = None
        
    def load(self, cols=None):
        if cols:
            self.df = pd.read_csv(self.path, usecols= cols)
        else :
            self.df = pd.read_csv(self.path)

        return self.df
    
    def drop_missing(self,cols = None):
        if cols:
            self.df = self.df.dropna(subset = cols)
        else:
            self.df = self.df.dropna()

        return self.df
    
    def get_df(self):
        return self.df
    
    def save(self, output_path):
        self.df.to_csv(output_path, index=False )



