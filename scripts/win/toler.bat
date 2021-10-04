::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:: Run toler.py script
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
@echo off

:: pyacademic parent path
set SCRIPTPATH="%~dp0..\..\toler\toler.py"

:: run newtex.py
python %SCRIPTPATH%
