import os

home_dir = os.getcwd()

for i in range(1, 9):
    name_folder = f"{i} lesson"
    name_docx = f"{i}_les.docx"
    if not os.path.exists(name_folder):
        os.mkdir(name_folder)
    os.chdir(name_folder)
    if not os.path.exists(name_docx):
        with open(name_docx, 'w', encoding='utf-8') as f:
            pass
    os.chdir(home_dir)
