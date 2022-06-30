@echo off

if not "%1" == "max" start /MAX cmd /c %0 max & exit/b

py get_files.py
py analyze.py

pause >nul
exit 0
