import os
import sys
from pathlib import Path
from dotenv import load_dotenv


dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

if len(sys.argv) > 1:
    root_dir = sys.argv[1]
else:
    root_dir = rf'{os.getenv("path_to_telegram")}'

os.chdir(root_dir)
print(os.getcwd())

dict_dir = {
    'docx': ['docx', 'doc'],
    'xlsx': ['xlsx'],
    'pdf': ['pdf', 'djvu'],
    'ppt': ['ppt', 'pptx'],
    'mp': ['mp4'],
    'png, jpeg': ['png', 'jpeg', 'jpg'],
    'rvt, dwg': ['dwg', 'rvt', 'rte', 'rfa', 'bak', 'dyn'],
    'exe, msi': ['exe', 'msi'],
    'zip': ['zip']
}

for name_dict in dict_dir.keys():
    path_to_dir = os.path.join(root_dir, name_dict)
    if not os.path.exists(path_to_dir):
        os.mkdir(path_to_dir)

for file in os.listdir(root_dir):
    if os.path.isfile(file):
        a = file.split('.')[-1]
        for key, val in dict_dir.items():
            if a in val:
                os.replace(file, fr".\{key}\{file}")
                print(fr"{file} был перемещен в .\{key}")

for file in os.listdir(root_dir):
    if os.path.isdir(file):
        if not any(Path(fr".\{file}").iterdir()):
            os.rmdir(file)
            print(f"{file} - пустая папка")
