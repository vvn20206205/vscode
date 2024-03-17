import os
import shutil


def get_settings_path():
    if os.name == 'nt':
        return os.path.expanduser('~/AppData/Roaming/Code/User/settings.json')
    # else:
    #     return os.path.expanduser('~/.config/Code/User/settings.json')


source_path = "../../.vscode/settings.json"
settings_path = get_settings_path()


shutil.copy2(source_path,    settings_path)
