@echo off
REM Lanzador para FormatTool en Windows
REM Este archivo ejecuta format_tool.py con Python

setlocal enabledelayedexpansion

REM Obtener la carpeta donde está este script
set "SCRIPT_DIR=%~dp0"

REM Verificar si Python está instalado
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo.
    echo ERROR: Python no está instalado o no está en la ruta del sistema
    echo.
    echo Descarga Python desde: https://www.python.org/downloads/
    echo Durante la instalación, MARCA: "Add Python to PATH"
    echo.
    pause
    exit /b 1
)

REM Ejecutar la aplicación
echo.
echo ========================================
echo Iniciando FormatTool...
echo ========================================
echo.

python "%SCRIPT_DIR%format_tool.py"

if %errorlevel% neq 0 (
    echo.
    echo ❌ Error al ejecutar FormatTool
    echo.
    pause
)

endlocal
