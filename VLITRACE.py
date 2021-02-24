# Use pandas to extract data from Excel and write to SQL text file for VLITRACE
import pandas as pd


# df = pd.read_excel('/Users/WRA1523/OneDrive - Emerson/Varsity/!Archive/SP 743 - Why Orders with a Stop Code of 900/Derby Orders - 2020.10.19(0).xlsx')
df = pd.read_excel('/Users/WRA1523/OneDrive - Emerson/Varsity/!Archive/SP 743 - Why Orders with a Stop Code of 900/Derby Orders - 2020.10.19(0).xlsx', usecols='K:K')
print(df)

# Open the SQL text file
# file1 = open("/Users/WRA1523/OneDrive - Emerson/Varsity/SQL/WR - VLITRACE.sql", "w+")

# Start writing SQL statements to file
# file1.write("Select *\n\tfrom shp4dta/vlitrace"
#            \n\twhere trordr in (\'")

for psn in df:
    print(psn)
    # file1.write(SDPSN + "\', \'")
    # print(f'{psn["SDPSN"]}')


# file1.write(")")

# file1.close()