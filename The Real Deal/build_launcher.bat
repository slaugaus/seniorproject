@echo off
del dist\*
rmdir /S dist\data
pyinstaller -F -w -i data\assets\icon\combined.ico launcher.py
xcopy /E data dist\data\
rmdir /S dist\data\__pycache__
rmdir /S dist\data\assets\models
move dist\launcher.exe "dist\Bullet Heck.exe"
copy controllertest.py dist\controllertest.py
pause
