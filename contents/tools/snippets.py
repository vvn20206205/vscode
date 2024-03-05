import os
import shutil


def get_snippets_path():
    if os.name == 'nt':
        return os.path.expanduser('~/AppData/Roaming/Code/User/snippets')
    # else:
    #     return os.path.expanduser('~/.config/Code/User/snippets')


source_folder = "../snippets"
destination_folder = get_snippets_path()


for root, dirs, files in os.walk(source_folder):
    for file in files:
        source_path = os.path.join(root, file)
        destination_path = os.path.join(destination_folder, file)

        shutil.copy2(source_path, destination_path)
