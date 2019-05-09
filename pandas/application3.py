import pandas as pd;

data = [{'Name': 'PPA', 'Duration': '4', 'Fees': '10000'},
        {'Name': 'LB', 'Duration': '3'},
        {'Name': 'Angular', 'Fees': '5000'},
        {'Name': 'Python', 'Duration': '4', 'Fees': '5000'}];

df = pd.DataFrame(data);
print(df);

writer = pd.ExcelWriter('MarvellousBatch.xlsx', engine='xlsxwriter');

df.to_excel(writer, sheet_name='sheet1');

writer.save();