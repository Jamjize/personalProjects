@echo off
msg * Abriendo app en el navegador, espera un momento
timeout /t 5 /nobreak>nul 
start http://localhost:5000
