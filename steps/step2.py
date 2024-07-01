import pandas as pd

def step1(data):
    data.num += 1
    data.df1 = pd.DataFrame.sub(data.df1, data.df2)