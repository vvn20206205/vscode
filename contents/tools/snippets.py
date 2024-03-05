import os
import shutil

source_folder = "../snippets"
destination_folder = "c:/Users/vvn20206205/AppData/Roaming/Code/User/snippets"
# destination_folder = "/home/<tên người dùng>/.config/Code/User/snippets"

# if not os.path.exists(source_folder):
#     print(f"Thư mục nguồn '{source_folder}' không tồn tại.")
#     exit()

# if not os.path.exists(destination_folder):
#     os.makedirs(destination_folder)

for root, dirs, files in os.walk(source_folder):
    for file in files:
        source_path = os.path.join(root, file)
        destination_path = os.path.join(destination_folder, file)

        shutil.copy2(source_path, destination_path)
