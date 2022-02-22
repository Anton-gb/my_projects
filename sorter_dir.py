import os
import sys

if len(sys.argv) > 1:
    root_dir = sys.argv[1]
else:
    root_dir = r'C:\Users\User\Downloads'

os.chdir(root_dir)
print(os.getcwd())

dict_dir = {
    'docx': ['docx', 'doc'],
    'xlsx': ['xlsx'],
    'pdf': ['pdf', 'djvu'],
    'ppt': ['ppt', 'pptx'],
    'mp': ['mp4'],
    'png, jpeg': ['png', 'jpeg', 'jpg'],
    'rvt, dwg': ['dwg', 'rvt', 'rte', 'rfa', 'bak'],
    'exe': ['exe'],
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
