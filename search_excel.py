# search_excel.py
# https://www.youtube.com/watch?v=EWIUWVsejWY

import numpy as np
import pandas as pd
import os

os.chdir('\\Users\\WRA1523\\Dropbox\\Yellow Folders\\Python')
print(f"{os.getcwd()}")

excel_file = 'Weight.xlsx'
df = pd.read_excel(excel_file)
# print(df)

print(df['Date'])
# programmers = df['Name'].where(df['Occupation'] == 'Programmer')
# print(programmers.dropna())

# excel_files = ['Pandas_Workbook.xlsx','Pandas_Workbook_copy.xlsx','Pandas_Workbook_copy_2.xlsx']

# for individual_excel_file in excel_files:
#     df = pd.read_excel(individual_excel_file)
#     programmers = df['Name'].where(df['Occupation'] == 'Programmer').dropna()
#     print("File Name" + individual_excel_file)
#     print(programmers)
