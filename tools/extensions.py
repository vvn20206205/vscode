# import subprocess

# command = "code --list-extensions > ../.vscode/extensions.txt"
# # command = "code --list-extensions > extensions.txt"

# subprocess.run(command, shell=True, check=True)

# # 
# # "formulahendry.auto-rename-tag"

# # "dracula-theme.theme-dracula"
# # "pkief.material-icon-theme"

# # "xabikos.ReactSnippets"
# # "mengrbatinov.json-snippet-to-md-documentation"
# # "blackboxapp.blackbox"
# # "ritwickdey.LiveServer"
# # "ritwickdey.liveserver"
# # "steoates.autoimport"
# # "kamikillerto.vscode-colorize"
# # "ms-vscode.cpptools-themes"
# # "ms-vscode.cpptools-extension-pack"
# # "AMiner.codegeex"
# # "ChakrounAnas.turbo-console-log"
# # "mikestead.dotenv"
# # "humao.rest-client"
# # "aminer.codegeex"
# # "ms-vscode.cpptools"
# # "ms-vscode-remote.remote-wsl"
# # "EditorConfig.EditorConfig"
# # "archsense.architecture-view-nestjs"
# # "dbaeumer.vscode-eslint"
# # "Blackboxapp.blackbox"
# # "xabikos.reactsnippets"
# # "twxs.cmake"
# # "ms-kubernetes-tools.vscode-kubernetes-tools"
# # "Codeium.codeium"
# # "MEngRBatinov.json-snippet-to-md-documentation"
# # "hediet.vscode-drawio"
# # "ms-vscode-remote.remote-containers"
# # "ms-vscode.cmake-tools"
# # "redhat.vscode-yaml"
# # "austenc.tailwind-docs"
# # "alefragnani.bookmarks"
# # "editorconfig.editorconfig"
import subprocess

def main():
    # Command to get the list of installed extensions in VSCode
    command = "code --list-extensions"
    
    # Thực hiện câu lệnh và lưu kết quả vào biến extensions
    extensions = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, text=True).stdout.splitlines()
    
    # Tạo nội dung cho tệp extensions.json
    content = {
        "recommendations": extensions
    }
    
    # Ghi nội dung vào tệp extensions.json
    with open('../.vscode/extensions.json', 'w') as file:
        file.write(str(content))

if __name__ == "__main__":
    main()
