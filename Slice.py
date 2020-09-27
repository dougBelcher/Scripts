# initial data
data = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
# populate variable with the position of @
atpos = data.find('@')
print(f'{atpos}')
# populate variable with the position of the next blank after @
sppos = data.find(' ',atpos)
print(f'{sppos}')
# populate variable with contents of the position after the @
host = data[atpos+1:sppos]
print(f'{host}')
