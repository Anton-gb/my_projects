
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


import json

with open('test.json', 'r', encoding='utf-8') as file:
    link = json.load(file)

print(link)

# link = [
#   {
#     'href': 'products_all',
#     'title': 'все'
#   },
#   {
#     'href': 'products_home',
#     'title': 'дом'
#   },
#   {
#     'href': 'products_office',
#     'title': 'офис'
#   },
#   {
#     'href': 'products_modern',
#     'title': 'модерн'
#   },
#   {
#     'href': 'products_classic',
#     'title': 'классика'
#   }
# ]
#
# with open('test.json', 'w', encoding='utf-8') as file:
#     json.dump(link, file, indent=4, ensure_ascii=False)
