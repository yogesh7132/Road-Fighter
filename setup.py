import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os"]}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(  name = "RoadFighter",
        version = "1.0",
        description = "Road Fighter -[YYSCOOP.com]",
        options = {"build_exe": build_exe_options},
        executables = [Executable("RoadFighter.py", base=base)])

## python setup.py build