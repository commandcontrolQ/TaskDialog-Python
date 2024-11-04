import sys
sys.dont_write_bytecode = True

import ctypes
from ctypes import wintypes

# Check if the user is not running Windows
__NOT_NT_MSG = f"Expected sys.platform to return 'win32', got '{sys.platform}'"
if [False, True][sys.platform == "win32"]:
    pass
else:
    raise OSError(__NOT_NT_MSG)

# Valid icons
# For some reason comctl32.TaskDialog uses icons from imageres.dll
icons = {
    "info": 0x0051,
    "warning": 0x0054,
    "error": 0x0062,
    "question": 0x0063,
    "x": 0x0059,
    "deny": 0x0403,
    "shield_question": 0x0068,
    "shield_error": 0x0069,
    "shield_ok": 0x006a,
    "shield_warning": 0x006b,
    "shield_uac": 0x004e
}

# Constants for buttons
TD_BUTTON = {
    "OK": 0x0001,
    "YES": 0x0002,
    "NO": 0x0004,
    "CANCEL": 0x0008,
    "RETRY": 0x0010,
    "CLOSE": 0x0020
}

# Load comctl32
comctl32 = ctypes.windll.comctl32

# Define a function to check if all of the items in list A are in list B (i.e. if list A is a subset of list B)
def is_subset(listA, listB):
    return set(listA) <= set(listB)

# Define a function to get a variable amount of numbers and perform a bitwise or operation on all of them
def bitwise(*args):
    from functools import reduce
    return reduce(lambda x, y: x | y, args)


# Define a function to run the TaskDialog function
def taskDialog(title, instruction, content, icon, buttons):
    # Prepare parameters
    hwnd_owner = None  # No owner window
    pwsz_title = ctypes.c_wchar_p(title)
    pwsz_instructions = ctypes.c_wchar_p(instruction)
    pwsz_content = ctypes.c_wchar_p(content)
    
    # Handle buttons
    
    # Check if the buttons provided are valid
    if is_subset(list(buttons), list(TD_BUTTON.keys())):
        button_values = [TD_BUTTON[b] for b in buttons]
        if len(buttons) > 1:
            button_type = bitwise(*button_values)
        else:
            button_type = button_values[0]
    else:
        raise ValueError(f"Button(s) {list(buttons)} not in {list(TD_BUTTON.keys())}")
            

    # Prepare result variable
    button_result = wintypes.INT()

    # Get the icon handle
    if icon in icons.keys():
        icon_handle = icons[icon]
    elif isinstance(icon, int):
        icon_handle = icon
    else:
        icon_handle = 0x0000 # Default, no icon

    # Call TaskDialog function
    result = comctl32.TaskDialog(
        hwnd_owner,
        None,
        pwsz_title,
        pwsz_instructions,
        pwsz_content,
        button_type,
        icon_handle,
        ctypes.byref(button_result)
    )

    return button_result.value

# Example usage
if __name__ == "__main__":
    result = taskDialog(
        title = "TaskDialog Sample",
        instruction = "This is a sample TaskDialog window.",
        content = """TaskDialog is a function for creating dialog boxes. 
Introduced in Windows Vista, it serves as a more modern alternative to the MessageBox* functions introduced in Windows 2000.
One major difference is the increase in customization, including a 'instruction' section (see blue text above).""",
        icon = 'info',
        buttons = ("OK",) # Due to how Python recognizes tuples, if you want only one button MAKE SURE THE BUTTONS TUPLE ENDS WITH A COMMA
    )
    print(f"TaskDialog returned {result}")
