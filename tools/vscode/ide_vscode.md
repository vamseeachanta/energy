## Introduction
The document describes the VS code usage, principles and best practices for projects:

## Keyboard Shortcuts

[https://code.visualstudio.com/shortcuts/keyboard-shortcuts-windows.pdf](https://code.visualstudio.com/shortcuts/keyboard-shortcuts-windows.pdf)


## Installation and General working

- Download visual studio code from below:
    https://code.visualstudio.com/
- Install extensions to suit programming needs
    - After installation, vs code will use intelligence to suggest what type of extension and tool a typical programmer needs. 
    - Install and experiment extensions as you see fit until one gets bored of all the fancy tools
    

### Settings 

### Overview

Settings can be accessed from Command Palette (Ctrl+Shift+P)

| Settings Type |   Short Description |  Comments |
|---|---|---|
| User | Settings that apply globally to any instance of VS Code you open.  | fallback properties. Located in user folder |
| Workspace | Settings stored inside your workspace and only apply when the workspace is opened.  | override user settings. Located in workspace folder|

### Sync from previous work

- Install Settings Sync
- Authorize access to Github
- Upload your current settings
- syncing your configuration to another environment
    - Install VS code
    - Install Settings Sync
    - Perform the github authentication 
    - Go to command pallette and search "Sync: Download Settings" and click on it
    - Perform the github authentication again if needed

https://www.freecodecamp.org/news/how-to-sync-vs-code-settings-between-multiple-devices-and-environments/
https://itnext.io/settings-sync-with-vs-code-c3d4f126989?gi=820f71c93d1e

## Automation


## Opening Settings.json

- Open the command palette (either with F1 or Ctrl+Shift+P)
- Type "open settings"
- You are presented with two options, choose "Open Settings (JSON)"
### On-Save, execute bash command


https://marketplace.visualstudio.com/items?itemName=fsevenm.run-it-on

https://betterprogramming.pub/automatically-execute-bash-commands-on-save-in-vs-code-7a3100449f63
https://stackoverflow.com/questions/68059778/auto-run-command-from-vscode-extension-on-file-save

## Remote Connections

Steps:


References:
https://code.visualstudio.com/docs/remote/remote-overview
https://code.visualstudio.com/docs/remote/ssh-tutorial

## Useful Extensions

[Spell checker](https://marketplace.visualstudio.com/items?itemName=streetsidesoftware.code-spell-checker)
[vscode-journal](https://marketplace.visualstudio.com/items?itemName=pajoma.vscode-journal)

https://www.reddit.com/r/vscode/comments/d36ni0/textbased_daily_journal_for_vscode/

**Run on Save**

https://stackoverflow.com/questions/68059778/auto-run-command-from-vscode-extension-on-file-save
