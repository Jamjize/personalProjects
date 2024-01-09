@echo off
if not exist installed (call :install) else (call :execute)
exit

:install
msg * Instalando requerimientos
echo nashe >> installed
PowerShell.exe -File "installer.ps1"

:execute
::Está instalado
PowerShell.exe -File "play.ps1"
:: eso ejecuta init.bat