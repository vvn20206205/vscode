# # import subprocess

# # command = "code --list-extensions > ../.vscode/extensions.txt"
# # # command = "code --list-extensions > extensions.txt"

# # subprocess.run(command, shell=True, check=True)

# # # 
# # # "formulahendry.auto-rename-tag"

# # # "dracula-theme.theme-dracula"
# # # "pkief.material-icon-theme"

# # # "xabikos.ReactSnippets"
# # # "mengrbatinov.json-snippet-to-md-documentation"
# # # "blackboxapp.blackbox"
# # # "ritwickdey.LiveServer"
# # # "ritwickdey.liveserver"
# # # "steoates.autoimport"
# # # "kamikillerto.vscode-colorize"
# # # "ms-vscode.cpptools-themes"
# # # "ms-vscode.cpptools-extension-pack"
# # # "AMiner.codegeex"
# # # "ChakrounAnas.turbo-console-log"
# # # "mikestead.dotenv"
# # # "humao.rest-client"
# # # "aminer.codegeex"
# # # "ms-vscode.cpptools"
# # # "ms-vscode-remote.remote-wsl"
# # # "EditorConfig.EditorConfig"
# # # "archsense.architecture-view-nestjs"
# # # "dbaeumer.vscode-eslint"
# # # "Blackboxapp.blackbox"
# # # "xabikos.reactsnippets"
# # # "twxs.cmake"
# # # "ms-kubernetes-tools.vscode-kubernetes-tools"
# # # "Codeium.codeium"
# # # "MEngRBatinov.json-snippet-to-md-documentation"
# # # "hediet.vscode-drawio"
# # # "ms-vscode-remote.remote-containers"
# # # "ms-vscode.cmake-tools"
# # # "redhat.vscode-yaml"
# # # "austenc.tailwind-docs"
# # # "alefragnani.bookmarks"
# # # "editorconfig.editorconfig"
# import subprocess

# command = "code --list-extensions"
    
# extensions = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, text=True).stdout.splitlines()

# content = {
#     "recommendations": extensions
# }
    
# # sửa '' trong content thành ""
# content=content.
# print("🚀 Giá trị của content:", content)
# # with open('../.vscode/extensions.json', 'w') as file:
# #     file.write(str(content))
import subprocess
import json

# Define the command to list extensions
command = "code --list-extensions"

# Run the command and capture the output
extensions = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, text=True).stdout.splitlines()

# Create content dictionary
content = {
    "recommendations": extensions
}

# Write the content to a JSON file
with open("recommended_extensions.json", "w") as json_file:
    json.dump(content, json_file, indent=4)

print("Recommended extensions saved to recommended_extensions.json")
