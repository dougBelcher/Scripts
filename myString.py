# Remove whitespace from strings

string1 = "     Filet Mignon"
string2 = "Brisket     "
string3 = "     Cheesburger     "

print(string1.lstrip())
print(string2.rstrip())
print(string3.strip())

string1a = "Becomes"
string2a = "becomes"
string3a = "BEAR"
string4a = " bEautiful"
string1a = string1a.lower()
string3a = string3a.lower()
string4a = string4a.lstrip().lower()

print(string1a.startswith("be"))
print(string2a.startswith("be"))
print(string3a.startswith("be"))
print(string4a.startswith("be"))
