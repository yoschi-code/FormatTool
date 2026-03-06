# Guía de Instalación de FormatTool

## Requisitos Previos

### Windows
- **Python 3.7+** instalado
- Derechos de Administrador
- Windows 7 o superior

### Linux
- **Python 3.7+** instalado
- Acceso a sudo (para operaciones de formateo)
- Cualquier distribución Linux

## Instalación Paso a Paso

### OPCIÓN 1: Ejecución Rápida (Recomendado)

#### Windows
```
1. Abre CMD o PowerShell
2. Navega a la carpeta: cd C:\Users\mrcri\mis scripts\FormatTool
3. Ejecuta: python format_tool.py
4. O haz doble clic en: formato_usb.bat
```

#### Linux
```bash
1. Abre terminal
2. Navega a la carpeta: cd ~/mis\ scripts/FormatTool
3. Ejecuta: python3 format_tool.py
4. O ejecuta: bash formato_usb.sh
```

### OPCIÓN 2: Instalación en el Sistema

#### Windows - Crear Acceso Directo en Menú Inicio

```batch
1. Abre CMD como Administrador
2. Ejecuta:
   cd C:\Users\mrcri\mis scripts\FormatTool
   tipo format_tool.py | find "python" >nul
3. Crea un acceso directo:
   - Click derecho en format_tool.py
   - "Enviar a" > "Escritorio"
   - O arrastra a Menú Inicio
```

#### Windows - Crear Variable de Entorno

```batch
1. Presiona Windows + X
2. Selecciona "Sistema"
3. "Configuración avanzada del sistema"
4. "Variables de entorno"
5. Click "Nueva" (Variables del sistema)
   - Nombre: FORMATOOL_PATH
   - Valor: C:\Users\mrcri\mis scripts\FormatTool
6. Aplica y aceptar
7. Ahora puedes correr desde cualquier CMD:
   python %FORMATOOL_PATH%\format_tool.py
```

#### Linux - Crear Alias

```bash
# Opción 1: Alias temporal (solo esta sesión)
alias formato_usb='python3 ~/mis\ scripts/FormatTool/format_tool.py'

# Opción 2: Alias permanente (agregar al ~/.bashrc)
echo "alias formato_usb='python3 ~/mis\ scripts/FormatTool/format_tool.py'" >> ~/.bashrc
source ~/.bashrc

# Luego puedes usar:
formato_usb
```

#### Linux - Crear Comando Global

```bash
# Como administrador (sudo)
sudo bash

# Copia el script a /usr/local/bin
cp ~/mis\ scripts/FormatTool/format_tool.py /usr/local/bin/formatool
chmod +x /usr/local/bin/formatool

# Ahora puedes usar desde cualquier carpeta:
formatool
```

### OPCIÓN 3: Instalación Manual en Carpetas del Sistema

#### Windows

```batch
REM Copiar a carpeta de sistemas de Windows
copy format_tool.py C:\Windows\System32\
REM Luego ejecuta desde CMD:
format_tool.py

REM O copia a carpeta de programas:
mkdir "C:\Program Files\FormatTool"
copy * "C:\Program Files\FormatTool\"
```

#### Linux

```bash
# Copiar a /usr/local/bin
sudo cp format_tool.py /usr/local/bin/formatool
sudo chmod +x /usr/local/bin/formatool

# O a /opt (para aplicaciones)
sudo mkdir -p /opt/formatool
sudo cp -r * /opt/formatool/
sudo chmod +x /opt/formatool/format_tool.py

# Crear enlace simbólico
sudo ln -s /opt/formatool/format_tool.py /usr/local/bin/formatool
```

## Verificación de Instalación

### Windows
```batch
python --version
python -c "import sys; print(sys.version)"
```

### Linux
```bash
python3 --version
python3 -c "import sys; print(sys.version)"
```

## Solución de Problemas de Instalación

### "Python no está instalado"

**Windows:**
1. Descarga desde: https://www.python.org/downloads/
2. Durante instalación: ☑️ Marca "Add Python to PATH"
3. Reinicia la computadora
4. Abre CMD nuevo y verifica: `python --version`

**Linux:**
```bash
# Ubuntu/Debian
sudo apt-get update
sudo apt-get install python3 python3-pip

# Fedora
sudo dnf install python3 python3-pip

# Arch
sudo pacman -S python python-pip

# Verificar
python3 --version
```

### "Permiso denegado" en Linux

```bash
# Dar permisos de ejecución
chmod +x format_tool.py
chmod +x formato_usb.sh

# Para operaciones de formateo, necesitas sudo
sudo python3 format_tool.py

# O agregar permisos sudo sin contraseña (avanzado):
sudo visudo
# Agrega al final:
# %sudo ALL=(ALL) NOPASSWD: /usr/bin/python3
```

### "El script no se ejecuta desde cualquier carpeta"

**Windows:**
```batch
REM Verifica que Python esté en PATH
python -c "import sys; print('\n'.join(sys.path))"

REM Si no ve Python, reinstala con "Add to PATH"
```

**Linux:**
```bash
# Verifica que el script esté en PATH
echo $PATH

# Copia el script a un lugar en PATH
sudo cp format_tool.py /usr/local/bin/formatool
sudo chmod +x /usr/local/bin/formatool
```

## Uso después de Instalación

### Instalación Rápida (sin alias)
```bash
# Windows
python C:\Users\mrcri\mis scripts\FormatTool\format_tool.py

# Linux
python3 ~/mis\ scripts/FormatTool/format_tool.py
```

### Con Alias/Comando Global
```bash
# Windows (si agregaste variable de entorno)
python %FORMATOOL_PATH%\format_tool.py

# Linux (si creaste alias)
formato_usb

# Linux (si lo copiaste a /usr/local/bin)
formatool
```

## Dependencias Opcionales

Para más características, instala:

```bash
# Windows
pip install psutil

# Linux
pip3 install psutil
```

Esto mostrará información adicional del sistema (CPU, RAM, etc)

## Desinstalación

### Para remover la herramienta:

**Windows:**
- Elimina la carpeta `FormatTool`
- Si creaste un alias en PATH, elimínalo también

**Linux:**
```bash
# Si la copiaste a /usr/local/bin
sudo rm /usr/local/bin/formatool

# Si la copiaste a /opt
sudo rm -rf /opt/formatool

# Si editaste ~/.bashrc
nano ~/.bashrc
# (elimina la línea del alias)
```

## Próximos Pasos

1. Lee el [README.md](README.md) para entender todas las funciones
2. Practica con un USB de prueba primero
3. Usa siempre el formateo con cuidado
4. Mantén backups de datos importantes

¡Estás listo para usar FormatTool! 🎉
