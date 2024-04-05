import os

folder_path = "C:/Users/student/Desktop/pyjpmcadv_1.4/pyjpmcadv/examples"

print(os.path.exists(folder_path))

for entry in os.scandir(folder_path):
    if entry.is_file():
        print(entry.name)

