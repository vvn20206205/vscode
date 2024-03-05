# pip install json5
import json5
import json


def read_json_with_comments():
    with open("../vscode.code-workspace", 'r', encoding="utf-8") as file:
        json_with_comments = file.read()
        json_data = json5.loads(json_with_comments)
    return json_data


content = read_json_with_comments()


with open("../.vscode/aaaaaa.json", "w") as json_file:
    # with open("../.vscode/aaaaaa.json", "w") as json_file:
    json.dump(content["settings"], json_file, indent=4)
