import os

dir_name = r'C:\Users\User\Google Диск\Учеба\7 сем\!_Серых_тепло'

os.chdir(dir_name)

start_name = 'Серых_2-Сб(ТГВ)-4_'

count_dwg = 1

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
        new_file_name = f'{start_name}ГЧ{count_dwg}.{file_extension}'
        if os.path.exists(new_file_name):
            count_dwg += 1
            new_file_name = f'{start_name}ГЧ{count_dwg}.{file_extension}'
        os.rename(file, new_file_name)

for file in os.listdir():
    print(file)
