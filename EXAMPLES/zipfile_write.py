from zipfile import ZipFile, ZIP_DEFLATED
import shutil
import os.path

file_names = ["parrot.txt", "tyger.txt", "knights.txt", "alice.txt", "poe_sonnet.txt", "spam.txt"]
file_folder = "../DATA"

# creating new, empty, zip file
zip_out = ZipFile("example.zip", mode="w", compression=ZIP_DEFLATED)  # Create new zip file

# add files to zip file
for file_name in file_names:
    file_path = os.path.join(file_folder, file_name)
    zip_out.write(file_path, file_name)  # Add member to zip file
zip_out.close()

zip_in = ZipFile("example.zip")
print(f"{zip_in.namelist() = }")

shutil.make_archive("answers", "zip", "../ANSWERS")
shutil.make_archive("answers", "gztar", "../ANSWERS")


