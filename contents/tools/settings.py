 

# with open("../../.vscode/extensions.json", "w") as json_file:

import json

def read_vscode_workspace(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

file_path = r"C:\Users\vvn20206205\Desktop\vscode\vscode.code-workspace"
workspace_data = read_vscode_workspace(file_path)
print(workspace_data)
