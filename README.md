# TaskDialog-Python

> [!NOTE]
> This script, as you can guess, only works on Windows-based systems. <br>
> Running this script on non-NT systems (i.e. Linux, macOS, etc) will return an error. <br>
> **This includes those running Cygwin.**

This repository contains the script `taskdialog.py`, a "wrapper" for comctl32's TaskDialog in Python. <br>
<sup>(This script is not meant to be a wrapper for the TaskDialog function, just some sample code on its implementation and how to use it.)</sup> <br>

# Extra
This repository also comes with one text file - `icons.txt`. <br>
This text file contains hexadecimal indexes for a lot of the icons from the DLL file `imageres.dll`. <br>
There wasn't any existing documentation online, and so I decided to create one myself. <br>
<br>
The text file in this repository is based on Windows 10 21H2. If you would like to see what the indexes of your system's icons are, there is [this repository](https://github.com/commandcontrolQ/getwinicons). <br>

# What about `TaskDialogIndirect`?
I have tried for a good few days to get TaskDialogIndirect working properly and all I get is (at least) one of the following:
- Getting an access violation OSError exception (e.g. `OSError: exception: access violation reading 0x0000000000010033`)
- Having the script run without exceptions but the function itself returns an error

If you can get TaskDialogIndirect working properly on Python, please let me know!
