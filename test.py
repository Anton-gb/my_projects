with open('PR.txt', 'r', encoding='utf-8') as f:
    a = f.read()
    print(a)

a = a.replace('\n', ' ')

with open('new.txt', 'w', encoding='utf-8') as f:
    f.write(a)
