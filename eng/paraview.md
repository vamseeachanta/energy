## Introduction

## Summary

### Installation

**Search in Ubuntu Application software or Snap Store and install Paraview.**

### Installation Steps - Superseded

- Remove old version (if any)
- Download the latest version of Paraview from [here](https://www.paraview.org/download/)

- Extract and copy
  -

  - sudo gedit ~/.bashrc
  - Add the following line(s) to the end of the file:
    - export PATH=$PATH:/opt/ParaView-5.11/bin/
- Compile
- Terminal access
- Create a lancher icon
  - sudo gedit /usr/share/applications/paraview.desktop
  - Add the following line(s) to the end of the file:
<code>
[Desktop Entry]
Version=1.0
Name=ParaView 5.11
Exec=paraview
Terminal=false
Icon=/opt/ParaView-5.11/share/icons/hicolor/96X96/apps/paraview.png
Type=Application
x-Ayatana-Desktop-Shortcuts=NewWindow
[NewWindow Shortcut Group]
Name=New Window
Exec=paraview
TargetEnvironment=Unity
</code>

### References

<https://youtu.be/tWEGjWD8d2M>