with open('PR.txt', 'r', encoding='utf-8') as f:
    a = f.read()
    print('Файл прочитан!')

a = a.replace('\n', ' ')

with open('new.txt', 'w', encoding='utf-8') as f:
    f.write(a)
    print('Файл записан!')

# for i in range(1080, 1080*3, 1080):
#     print(i)

# for i in range(1, 4):
#     print(i)
