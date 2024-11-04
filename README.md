# TaskDialog-Python

> [!NOTE]
> This script, as you can guess, only works on Windows-based systems. <br>
> Running this script on non-NT systems (i.e. Linux, macOS, etc) will return an error. <br>
> **This includes those running Cygwin.**

This repository contains the script `taskdialog.py`, a "wrapper" for comctl32's TaskDialog in Python. <br>
<sup>(This "wrapper" is a bit poorly made, as there are stuff still not implemented properly (or at all) )</sup> <br>

### Todo (from most to least important):
- [ ] Modify the script to use any other DLL other than `imageres.dll` (i.e. implement LoadImageW/LoadIconW)
- [ ] Implement TaskDialogIndirect (properly)
  - [ ] Have custom button text
- [ ] Modify the script to use local icons rather than DLL files

# Extra
This repository also comes with two files - `icons.txt` and `example.py`. <br>

### `icons.txt`
The text file contains hexadecimal indexes for a lot of the icons from the DLL file `imageres.dll`. <br>
There wasn't any existing documentation online, and so I decided to create one myself. <br>
<br>
The text file in this repository is based on Windows 10 21H2. If you would like to see what the indexes of your system's icons are, there is [this repository](https://github.com/commandcontrolQ/getwinicons), or [this piece of software](https://www.angusj.com/resourcehacker). <br>

### `example.py`
As you can guess by its name, this Python script provides example usage of the TaskDialog wrapper. <br>
It contains multiple different icons as well as a basic implementation of *branching dialogues*. <br>
Feel free to use the script as a template!
