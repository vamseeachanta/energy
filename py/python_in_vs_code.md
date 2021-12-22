# Introduction


## Running python in VS Code


## Summary


For general VS code settings, refer to https://github.com/vamseeachanta/energy/blob/d6a5aeb896ecbbe355fde45a2c6016843c7cef3a/ide_vscode.md

Knownn Issues:
- Sometimes the selected python environment is not recognized inspite of following the instructions in this page. Need to collect more data on this.

### Key value pairs

The following settings will help set the python environments appropriately for a project or workspace in VS Code. 

| key |   Value (sample) |  Setting |  Comments |
|---|---|---|---|
| python.condaPath | C:\\Data\\Continuum\\Miniconda3\\Scripts\\conda.exe  | User settings | 
| python.pythonPath | Settings that apply globally to any instance of VS Code you open.  | fallback properties |

For User settings JSON
<pre>
    "python.terminal.activateEnvironment": true,
    "python.condaPath": "C:\\Data\\Continuum\\Miniconda3\\Scripts\\conda.exe",
    "python.defaultInterpreterPath": "C:\\Data\\Continuum\\Miniconda3\\envs\\flask\\python.exe",
</pre>
For Workspace settings JSON
<pre>
    "python.pythonPath": "C:\\Data\\Continuum\\Miniconda3\\envs\\flask\\python.exe",
</pre>




## References

https://code.visualstudio.com/docs/getstarted/settings

https://code.visualstudio.com/docs/python/environments

https://medium.com/analytics-vidhya/efficient-way-to-activate-conda-in-vscode-ef21c4c231f2