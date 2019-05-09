import pandas as pd

print("Empty data frame:");
df = pd.DataFrame();
print(df);

print("Data frame with list: ")
data = [1,2,3,4,5];
df = pd.DataFrame(data);
print(df);

print("Data frame with list: ");
data = [['PPA', 4], ['LB', 3], ['Angular', 3], ['Python', 3]];
df = pd.DataFrame(data, columns=['Name', 'Duration']);
print(df);

data = {'Name': ['PPA', 'LB', 'Angular', 'Python'], 'Duration': [4,3,3,3]};
df = pd.DataFrame(data);
print(df);

data = [{'Name': 'PPA', 'Duration': '4', 'Fees': '10000'},
        {'Name': 'LB', 'Duration': '3'},
        {'Name': 'Angular', 'Fees': '5000'},
        {'Name': 'Python', 'Duration': '4', 'Fees': '5000'}];
df = pd.DataFrame(data);
print(df);

data = {'one': pd.Series([1,2,3], index=['a','b','c']),
        'two': pd.Series([1,2,3,4], index=['x','y','z','w'])};
df = pd.DataFrame(data);
print(df);

