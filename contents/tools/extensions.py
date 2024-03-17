import json
import subprocess


command = "code --list-extensions"

extensions = subprocess.run(
    command,
    shell=True,
    check=True,
    stdout=subprocess.PIPE,
    text=True
).stdout.splitlines()

content = {
    "recommendations": extensions
}


with open("../../.vscode/extensions.json", "w") as json_file:
    json.dump(content, json_file, indent=4)



#@@ "editorconfig.editorconfig",
#@ "fedricknishant.turbo-python-print",
    
#@ "chakrounanas.turbo-console-log",
#@ "mikestead.dotenv",
#@ "archsense.architecture-view-nestjs",
# "formulahendry.auto-rename-tag"
# "xabikos.ReactSnippets"
# "ritwickdey.liveserver"
    
#@@ "redhat.vscode-yaml",


#@@ "ms-vscode-remote.remote-wsl",
#@@ "ms-azuretools.vscode-docker",
#@@ "ms-kubernetes-tools.vscode-kubernetes-tools",
#@@ "ms-vscode-remote.remote-containers",

# "mengrbatinov.json-snippet-to-md-documentation"

# "kamikillerto.vscode-colorize"
    
# "blackboxapp.blackbox"
    
# "ms-vscode.cpptools-themes"
# "ms-vscode.cpptools-extension-pack"
# "ms-vscode.cpptools"
    
# "AMiner.codegeex"

# "humao.rest-client"
    
# "dbaeumer.vscode-eslint"
# "Blackboxapp.blackbox"
# "xabikos.reactsnippets"
# "twxs.cmake"
# "ms-kubernetes-tools.vscode-kubernetes-tools"
# "Codeium.codeium"
# "MEngRBatinov.json-snippet-to-md-documentation"
# "hediet.vscode-drawio"
# "ms-vscode-remote.remote-containers"
# "ms-vscode.cmake-tools"
# "redhat.vscode-yaml"
# "austenc.tailwind-docs"
# "alefragnani.bookmarks"
