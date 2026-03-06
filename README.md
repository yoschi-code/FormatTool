# FormatTool - Herramienta Multiplataforma de Formateo

Una aplicación de terminal simple pero poderosa para formatear USB y manejar archivos con protección contra escritura en Windows y Linux.

## Características

✅ **Formateo de USB** - Formatea dispositivos USB con múltiples sistemas de archivos
✅ **Remover Protección** - Quita protección contra escritura de archivos y carpetas
✅ **Borrado Seguro** - Borra archivos sobrescribiendo datos (3 pasadas)
✅ **Listar Dispositivos** - Muestra unidades disponibles y espacio
✅ **Información del Sistema** - Detalles del hardware y particiones
✅ **Multiplataforma** - Funciona en Windows y Linux
✅ **Interfaz Amigable** - Menú interactivo fácil de usar

## Requisitos

### Windows
- Python 3.7+
- Derechos de Administrador (para formateo)

### Linux
- Python 3.7+
- Permisos de sudo
- `lsblk` o `df` instalado (generalmente preinstalado)

## Instalación

### Opción 1: Ejecución Directa

```bash
# Windows
python format_tool.py

# Linux
python3 format_tool.py
```

### Opción 2: Crear Script Ejecutable

#### Windows (crear formato_usb.bat)
```batch
@echo off
python "%~dp0format_tool.py" %*
pause
```

#### Linux (crear formato_usb.sh)
```bash
#!/bin/bash
python3 "$(dirname "$0")/format_tool.py" "$@"
```

Hacer ejecutable:
```bash
chmod +x formato_usb.sh
./formato_usb.sh
```

## Uso

### Menú Principal

```
1. Listar dispositivos USB/Unidades
   Muestra todos los dispositivos disponibles

2. Formatear USB
   ⚠️  PELIGROSO - Borra TODO de la unidad
   Requiere confirmación doble

3. Remover protección contra escritura de archivo
   Desbloquea archivos de solo lectura

4. Remover protección contra escritura de carpeta
   Desbloquea carpetas y su contenido

5. Borrar archivos de forma segura
   Sobrescribe datos antes de eliminar

6. Información de dispositivo
   Muestra estado del sistema
```

## Ejemplos de Uso

### Formatear un USB en Windows
1. Selecciona opción 2
2. Ingresa: `D:`
3. Sistema: `FAT32` o `NTFS`
4. Nombre: `MiUSB`

### Formatear un USB en Linux
1. Selecciona opción 2
2. Ingresa: `/dev/sdb1` (verificar con `lsblk`)
3. Sistema: `ext4` o `fat32`
4. Nombre: `MiUSB`

### Remover protección de archivo
1. Selecciona opción 3
2. Ingresa ruta: `C:\Users\Usuario\archivo.txt`
3. ✓ Listo

### Remover protección de carpeta
1. Selecciona opción 4
2. Ingresa ruta: `D:\MiCarpeta`
3. Se procesa recursivamente
4. ✓ Listo

## Advertencias Importantes

⚠️ **FORMATEO DE DISPOSITIVOS**
- Esta operación BORRA PERMANENTEMENTE todos los datos
- No hay forma de recuperar los datos después
- Verifica el dispositivo antes de confirmar
- ¡CUIDADO CON DISCOS DEL SISTEMA!

⚠️ **LINUX**
- Necesitas permisos de `sudo` para formatear
- NUNCA formatees `/` o `/home`
- Usa `lsblk` para identificar el dispositivo correcto

⚠️ **WINDOWS**
- Ejecuta como Administrador para formatear
- Algunos antivirus pueden bloquear operaciones de bajo nivel

## Solución de Problemas

### No puedo formatear en Windows
```
Solución: Ejecuta como Administrador
- Click derecho en CMD/PowerShell → "Ejecutar como administrador"
- Luego ejecuta: python format_tool.py
```

### No puedo formatear en Linux
```
Solución: Usa sudo
sudo python3 format_tool.py
```

### El dispositivo está en uso
```
Solución: Desmonta primero
Linux: sudo umount /dev/sdb1
Windows: Cierra el Explorador de archivos
```

### Error "Permiso denegado"
```
Solución Windows: Ejecuta como administrador
Solución Linux: usa sudo
```

## Estructura del Proyecto

```
FormatTool/
├── format_tool.py          # Aplicación principal
├── README.md               # Este archivo
├── INSTALL.md              # Guía de instalación (opcional)
├── formato_usb.bat         # Lanzador para Windows (opcional)
└── formato_usb.sh          # Lanzador para Linux (opcional)
```

## Características Técnicas

### Sistemas de Archivos Soportados
- **Windows**: NTFS, FAT32
- **Linux**: ext4, FAT32, NTFS

### Métodos de Protección
- Atributos de archivo Windows
- Permisos Unix (chmod)
- Sobrescritura segura de datos

### Borrado Seguro
- 3 pasadas de sobrescritura
- Datos aleatorios criptográficos
- Eliminación fisica del archivo

## Opciones Avanzadas

Para usuarios avanzados, puedes modificar el código:
- Aumentar pasadas de borrado seguro (línea en `_secure_delete_file`)
- Cambiar sistemas de archivos por defecto
- Agregar más opciones de menú

## Seguridad

✓ No se envían datos a ningún servidor
✓ Todas las operaciones son locales
✓ Código abierto - ¡Revísalo!
✓ No instala nada en el sistema
✓ Requiere confirmación para operaciones destructivas

## Licencia

Esta herramienta se proporciona "tal cual". El usuario es responsable de cualquier pérdida de datos.
Úsala bajo tu propio riesgo.

## Actualización Futura

Características planeadas:
- [ ] Interfaz gráfica (GUI)
- [ ] Restauración de datos
- [ ] Diagnóstico de discos
- [ ] Cifrado de dispositivos
- [ ] Clonación de discos

## Contacto / Soporte

Si encuentras problemas:
1. Verifica los requisitos
2. Ejecuta con permisos de administrador/sudo
3. Revisa los mensajes de error
4. Intenta desmontar el dispositivo primero

---

**Versión**: 1.0
**Última actualización**: 2026
**Compatibilidad**: Python 3.7+, Windows 7+, Linux (cualquier distribución)
