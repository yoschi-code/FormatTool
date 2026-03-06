# Solución de Problemas - FormatTool

## Errores Comunes

### "Python no está instalado"

#### Windows
```
Síntoma: 'python' is not recognized as an internal or external command
Solución:
1. Descarga Python desde https://www.python.org/downloads/
2. Durante la instalación:
   ☑️ IMPORTANTE: Marca "Add Python to PATH"
3. Reinicia tu computadora
4. Abre CMD nuevo y verifica:
   python --version
```

#### Linux
```
Síntoma: command not found: python3
Solución:
# Ubuntu/Debian
sudo apt-get update
sudo apt-get install python3

# Fedora
sudo dnf install python3

# Arch
sudo pacman -S python

# Verificar
python3 --version
```

---

### "Acceso denegado" al formatear

#### Windows
```
Síntoma: Access Denied, Permission Denied
Solución:
1. Ejecuta CMD como Administrador
   - Windows 10/11: Presiona Win+X → Selecciona "Terminal (Administrador)"
   - Windows 7/8: Click derecho en CMD → "Ejecutar como administrador"
2. Navega a la carpeta del programa
3. Ejecuta: python format_tool.py
```

#### Linux
```
Síntoma: Permission denied
Solución:
# Para ver dispositivos, usa:
sudo python3 format_tool.py

# O con lsblk primero:
lsblk

# Dar permisos de ejecución al script:
chmod +x format_tool.py
```

---

### "El dispositivo está en uso" (No se puede formatear)

#### Windows
```
Síntoma: Device is in use, The disk is write protected
Solución:
1. Cierra el Explorador de archivos
2. Expulsa el USB de forma segura (click derecho → Expulsar)
3. Espera 5 segundos
4. Inserta nuevamente
5. Intenta de nuevo
6. Si persiste, reinicia Windows

Alternativa: Usa Administración de Discos
1. Windows+X → "Administración de Discos"
2. Localiza el USB
3. Click derecho → "Formatear"
4. Elige NTFS o FAT32
```

#### Linux
```
Síntoma: Device busy, Operation not permitted
Solución:
1. Lista dispositivos:
   lsblk

2. Desmonta el dispositivo:
   sudo umount /dev/sdXX
   (reemplaza XX con la letra del dispositivo)

3. Intenta formatear de nuevo:
   sudo python3 format_tool.py

4. Si sigue en uso:
   sudo lsof | grep /dev/sdXX
   (para ver qué procesos lo usan)
```

---

### "USB protegido contra escritura"

```
Síntoma: Write protected, Read-only file system
Causas: 
- Switch físico de protección en el USB
- Protección por software
- Corrupción del dispositivo

Solución Windows:
1. Si el USB tiene switch: muévelo
2. Opción 3 en FormatTool: "Remover protección de archivo"
3. O usa Instalación Limpia:
   - Descarga "HP USB Disk Storage Format Tool"
   - Ejecuta como administrador
   - Formatea internamente

Solución Linux:
1. Verifica si está comprometido:
   sudo fdisk -l /dev/sdXX

2. Intenta limpiar:
   sudo hdparm -r0 /dev/sdXX

3. Si sigue protegido:
   sudo shred -vfz -n 3 /dev/sdXX
   (CUIDADO: destroza completamente)
```

---

### "El archivo no se puede modificar" (Read-only)

#### Windows
```
Síntoma: "Cannot modify, file is read-only"
Solución:
1. Opción 3 en FormatTool: "Remover protección de archivo"
2. O manualmente:
   - Click derecho en archivo → Propiedades
   - Desactiva ☑️ "Solo lectura"
   - Aplica → Aceptar
3. Si sigue sin funcionar:
   - Ejecuta como administrador
   - En CMD: attrib -r "ruta del archivo"
```

#### Linux
```
Síntoma: "Permission denied" al editar archivo
Solución:
1. Opción 3 en FormatTool: "Remover protección de archivo"
2. O en terminal:
   chmod 644 archivo.txt        # Lectura/escritura

3. Para carpetas:
   chmod -R 755 /ruta/carpeta   # Recursivo
```

---

### "No encuentro mi USB" (No aparece en la lista)

#### Windows
```
Síntoma: El USB no aparece con opción 1
Solución:
1. Verifica en Administración de Discos:
   - Windows+X → "Administración de Discos"
   - Busca un disco sin asignar

2. Si aparece sin asignar:
   - Click derecho → "Nuevo volumen simple"
   - Sigue el asistente

3. Si no aparece:
   - Prueba otro puerto USB
   - Prueba otro USB (podría estar roto)
   - Reinicia el equipo

4. Comprueba drivers:
   - Windows+X → "Administrador de dispositivos"
   - Busca "Controladores de almacenamiento masivo"
```

#### Linux
```
Síntoma: El USB no aparece con opción 1
Solución:
1. Abre otra terminal y verifica:
   lsblk

2. Ten en cuenta la ruta exacta (ej: /dev/sdb1)

3. Si no aparece:
   dmesg | tail    # Ver últimos eventos
   
4. Intenta:
   sudo blkid       # Lista todos los dispositivos

5. Si necesitas montar:
   sudo mkdir -p /mnt/usb
   sudo mount /dev/sdb1 /mnt/usb
```

---

### Errores de Formateo

#### "Invalid device specified"
```
Causa: La ruta del dispositivo está mal

Windows: Usa D:, E:, F: (letra de unidad)
Linux: Usa /dev/sdb1, /dev/sdc1 (verifica con lsblk)

Solución:
1. En FormatTool, opción 1: lista dispositivos
2. Copia la ruta exacta
3. Intenta de nuevo
```

#### "File system not supported"
```
Causa: Sistema de archivos no válido

Windows soporta: NTFS, FAT32
Linux soporta: ext4, FAT32, NTFS

Solución:
1. Cuando pida el sistema
2. Ingresa: FAT32 (compatible con ambos)
3. O NTFS (recomendado para Windows)
```

#### "Formatting cancelled"
```
Causa: La operación fue interrumpida

Solución:
1. Desconecta el USB
2. Espera 30 segundos
3. Reconecta
4. Intenta de nuevo
5. Si persiste, reinicia
```

---

### Problemas de Protección de Carpeta

#### "Cannot modify nested directories"
```
Problema: No se puede cambiar permisos en subcarpetas

Windows:
1. Opción 4 en FormatTool: "Remover protección de carpeta"
2. Ingresa la ruta raíz
3. Espera a que procese todo

Linux:
1. Opción 4
2. O manualmente: chmod -R 755 /ruta/
```

#### Carpetas del sistema protegidas
```
NO intentes cambiar permisos de:
Windows: C:\Windows, C:\Program Files, C:\Users\[Usuario]\AppData
Linux: /root, /etc, /sys, /proc

Riesgo: Puedes dañar el sistema operativo
```

---

### Problemas de Rendimiento

#### "El programa responde lentamente"
```
Soluciones:
1. Cierra otros programas
2. Desactiva antivirus temporalmente
3. Espera a que terminen operaciones de fondo
4. Para carpetas grandes: ten paciencia
   (procesa recursivamente)
```

#### "Se congela en 0% de progreso"
```
Soluciones:
1. Espera 2-3 minutos
2. Si no cambia, presiona Ctrl+C
3. Desconecta/reconecta el dispositivo
4. Intenta con dispositivo diferente
5. Es posible que el hardware esté dañado
```

---

### Problemas de Borrado Seguro

#### "Archivo muy grande tarda mucho"
```
Esperado: Los archivos grandes tardan
         Depende de la velocidad del disco

Estimación:
- Archivo 1GB: ~30-60 segundos
- Archivo 10GB: ~5-10 minutos

Recomendación:
- No interrumpas la operación
- Ten paciencia
```

#### "No puedo borrar archivo en uso"
```
Solución:
1. Cierra la aplicación que lo usa
2. Busca qué programa lo abre:
   Windows: Taskmgr (Ctrl+Shift+Esc) → busca en "detalles"
   Linux: lsof | grep archivo
3. Cierra ese programa
4. Intenta de nuevo
```

---

## Cuando Todo Falla

Si nada funciona:

### Opción 1: Usa herramientas alternativas

**Windows:**
- DiskPart (en CMD): `diskpart`
- Administración de Discos (Windows+X)
- Instalación del fabricante del USB

**Linux:**
- `sudo fdisk /dev/sdX` (avanzado)
- `sudo gparted` (interfaz gráfica)
- Herramientas de fabricante

### Opción 2: Reinicia todo

```
1. Cierra FormatTool (Ctrl+C)
2. Desconecta el USB
3. Reinicia tu computadora
4. Reconecta el USB
5. Intenta de nuevo
```

### Opción 3: Verifica el hardware

```
Posibles problemas físicos:
- USB dañado
- Puerto USB no funciona
- Cable USB dañado
- Conexión suelta

Prueba:
- Otro puerto USB
- Otro equipo
- Otro USB (para verificar)
```

### Opción 4: Si es crítico

```
WINDOWS:
1. Restaura desde backups
2. O contacta a centro de servicio

LINUX:
1. La mayoría de problemas se resuelven con sudo
2. O usa Live USB con herramientas especializadas
```

---

## Contacto / Soporte

Este proyecto es de código abierto.
Si encuentras un bug:

1. Reproduce el error
2. Anota el mensaje exacto
3. Tu sistema operativo y versión
4. Python version (python --version)

---

## Consejos Finales

✅ **Siempre:**
- Haz backup antes de formatear
- Verifica el dispositivo correcto
- Lee las advertencias DOS VECES
- Ejecuta como administrador/sudo

❌ **Nunca:**
- Formatees la unidad del sistema
- Interrumpas durante la operación  
- Dejes conectado durante reinicio
- Ignores mensajes de error

🔧 **Mantenimiento:**
- Actualiza Python regularmente
- Verifica disponible espacio en disco
- Mantén antivirus actualizado
- Limpia puertos USB de polvo/suciedad

---

**Última actualización:** 2026
**Versión:** 1.0
