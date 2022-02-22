import os

dir_name = r'C:\Users\aoioh\Мой диск\Учеба\7 сем\Теплоснабжение\КП'

os.chdir(dir_name)

start_name = 'Тимошков А.Д._'

for file in os.listdir():
    file_extension = file.split('.')[-1]
    if file_extension == 'docx':
        new_file_name = start_name + 'ПЗ.' + file_extension
        os.rename(file, new_file_name)
    elif file_extension == 'xlsx':
        new_file_name = start_name + 'Расчеты.' + file_extension
        os.rename(file, new_file_name)
    elif file_extension == 'pdf':
        new_file_name = start_name + 'КП.' + file_extension
        os.rename(file, new_file_name)
    elif file_extension == 'dwg':
        new_file_name = start_name + 'ГЧ.' + file_extension
        os.rename(file, new_file_name)

for file in os.listdir():
    print(file)