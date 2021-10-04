::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:: Create tex folder from template
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
@echo off

:: pyacademic parent path
set SCRIPTPATH="%~dp0..\..\misc\newtex\newtex.py"

:: run newtex.py
python %SCRIPTPATH%
