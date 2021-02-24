#   19. Any / all built-ins
#   https://docs.python.org/3/library/functions.html#all
languages = ['Java', 'Perl', 'PHP', 'Python', 'JS', 'C++', 'JS', 'Ruby']

print(f'{all(len(l) >= 2 for l in languages)}')

print(f'{any("++" in l for l in languages)}')
