# 5. sword_fish
while True:
    print(f'Who are you?')
    name = input()
    if name != 'Joe':
        continue
    print(f'Hello, {name}. What is the password? (It is a fish)')
    password = input()
    if password == 'swordfish':
        break
print(f'Access granted.')