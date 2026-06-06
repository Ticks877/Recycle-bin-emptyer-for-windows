import ctypes
from ctypes import wintypes

# Constants for SHEmptyRecycleBin
SHERB_NOCONFIRMATION = 0x00000001  # No confirmation dialog
SHERB_NOPROGRESSUI = 0x00000002    # No progress dialog
SHERB_NOERRORUI = 0x00000004       # No error dialog

# Empty the Recycle Bin
ctypes.windll.shell32.SHEmptyRecycleBinW(None, None, SHERB_NOCONFIRMATION | SHERB_NOPROGRESSUI | SHERB_NOERRORUI)

# Print message 5 times
for _ in range(5):
    print("Recycle Bin emptied!")