import pandas as pd
import numpy as np

s = pd.Series();
print(s);
print("-----------------------------");

data = np.array(['a','b','c','d']);
s = pd.array(data);
print(s);
print("-----------------------------");

data = np.array(['a', 'b', 'c', 'd']);
s = pd.Series(data, index=[100,101,102,103]);
print(s);
print("-----------------------------");

data = {'a':'0.1', 'b':'1.1', 'c':'2.1', 'd':'3.1'};
s = pd.Series(data);
print(s);
print("-----------------------------");

s = pd.Series([1,2,3,4], index=['a','b','c','d']);
print(s);