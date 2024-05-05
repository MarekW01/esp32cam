@echo off

REM Check if .credentials folder exists, create if not
if not exist .credentials mkdir .credentials

REM Check if credentials.txt exists in .credentials folder
if exist .credentials\credentials.txt (
    choice /M "Credentials file already exists. Overwrite? "
    if errorlevel 2 (
        goto :skip_overwrite
    ) else (
        del .credentials\credentials.txt
    )
)

REM Prompt for name
set /p name="Enter username: "

REM Prompt for lastName
set /p lastName="Enter remote IP address: "

REM Prompt for lastlastName
set /p lastlastName="Enter local IP address: "

REM Write to credentials.txt in .credentials folder
echo name=%name%>.credentials\credentials.txt
echo lastName=%lastName%>>.credentials\credentials.txt
echo lastlastName=%lastlastName%>>.credentials\credentials.txt

:skip_overwrite
for /f "tokens=1,2 delims==" %%a in (.credentials\credentials.txt) do (
    if %%a==name set %%a=%%b
    if %%a==lastName set %%a=%%b
    if %%a==lastlastName set %%a=%%b
)

ssh -R 8000:%lastlastName%:80 -t %name%@%lastName% python3 host.py
