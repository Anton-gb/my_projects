"""
Попробовать реализовать рекурсию
"""

import os
import openpyxl


def new_file(file_name):
    if not os.path.exists(file_name):
        with open(file_name, 'w', encoding='utf-8') as f:
            pass


subjects = [
    'Отопление',
    'Теплоснабжение'
]

files = {
    'ПЗ': '.docx',
    # Без дополнительной библиотеки создать exel файл невозможно
    'Расчеты': '.xlsx'
}

home_dir = os.getcwd()

for subject in subjects:
    if not os.path.exists(subject):
        os.mkdir(subject)
    os.chdir(subject)
    for key, val in files.items():
        if val == '.xlsx':
            wb = openpyxl.Workbook()
            wb.save(f"{key}_{subject.lower()}{val}")
        else:
            new_file(f"{key}_{subject.lower()}{val}")
    os.chdir(home_dir)
