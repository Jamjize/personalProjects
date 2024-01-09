# Verificar si Python está instalado
if (-not (python --version 2>$null)) {
    # Instalar Python usando winget si no está instalado
    winget install Python.Python.3.12
}

# Mostrar un mensaje de instalación completada
Write-Host "La instalación se ha completado exitosamente." -ForegroundColor Green

# Mostrar un mensaje de pop-up
[System.Reflection.Assembly]::LoadWithPartialName("System.Windows.Forms")
[System.Windows.Forms.MessageBox]::Show("La instalación se ha completado exitosamente.")

