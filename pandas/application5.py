import pandas as pd
import numpy as np

df1 = {'one': pd.Series([1,2,3], index=['a','b','c']),
       'two': pd.Series([1,2,3,4], index=['a','b','c','d'])};

df2 = {'one': pd.Series([1,2,3], index=['a','b','c']),
       'two': pd.Series([1,2,3,4], index=['a','b','c','d'])};

data = {'item1': df1, 'item2': df2};

p = pd.Panel(data);
print(p);
