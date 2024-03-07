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



#@ "almenon.arepl",
#@ "ms-python.python",
#@ "ms-python.vscode-pylance",
#@ "ms-python.autopep8",
#@ "fedricknishant.turbo-python-print",


#@ "chakrounanas.turbo-console-log",
#@ "mikestead.dotenv",
#@ "archsense.architecture-view-nestjs",

#@@ "foxundermoon.shell-format",
#@@ "redhat.vscode-yaml",
#@@ "editorconfig.editorconfig",
#@@ "ms-vscode-remote.remote-wsl",
#@@ "ms-azuretools.vscode-docker",
#@@ "ms-kubernetes-tools.vscode-kubernetes-tools",
#@@ "ms-vscode-remote.remote-containers",
#
# "formulahendry.auto-rename-tag"

# "dracula-theme.theme-dracula"
# "pkief.material-icon-theme"

# "xabikos.ReactSnippets"
# "mengrbatinov.json-snippet-to-md-documentation"
# "blackboxapp.blackbox"
# "ritwickdey.LiveServer"
# "ritwickdey.liveserver"
# "steoates.autoimport"
# "kamikillerto.vscode-colorize"
# "ms-vscode.cpptools-themes"
# "ms-vscode.cpptools-extension-pack"
# "AMiner.codegeex"
# "ChakrounAnas.turbo-console-log"
# "mikestead.dotenv"
# "humao.rest-client"
# "aminer.codegeex"
# "ms-vscode.cpptools"
# "ms-vscode-remote.remote-wsl"
# "EditorConfig.EditorConfig"
# "archsense.architecture-view-nestjs"
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
# "editorconfig.editorconfig"
