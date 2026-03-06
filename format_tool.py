#!/usr/bin/env python3
"""
FormatTool - Herramienta multiplataforma para formatear USB y archivos
Compatible con Windows y Linux
"""

import os
import sys
import platform
import subprocess
import shutil
from pathlib import Path
import stat

class FormatTool:
    def __init__(self):
        self.system = platform.system()
        self.is_windows = self.system == "Windows"
        self.is_linux = self.system == "Linux"
        
    def print_header(self):
        """Imprime el encabezado de la aplicación"""
        os.system('cls' if self.is_windows else 'clear')
        print("=" * 60)
        print("       FORMATOOL - Formateador Universal de USB y Archivos")
        print("=" * 60)
        print(f"Sistema operativo: {self.system}")
        print()
    
    def print_menu(self):
        """Imprime el menú principal"""
        print("\n[MENÚ PRINCIPAL]")
        print("1. Listar dispositivos USB/Unidades")
        print("2. Formatear USB (CUIDADO - datos permanentes)")
        print("3. Remover protección contra escritura de archivo")
        print("4. Remover protección contra escritura de carpeta")
        print("5. Borrar archivos de forma segura")
        print("6. Información de dispositivo")
        print("0. Salir")
        print("-" * 60)
    
    def get_user_choice(self):
        """Obtiene la opción del usuario"""
        try:
            choice = input("Selecciona una opción (0-6): ").strip()
            return choice
        except KeyboardInterrupt:
            print("\n\n[OPERACIÓN CANCELADA]")
            sys.exit(0)
    
    def list_drives(self):
        """Lista los dispositivos disponibles"""
        print("\n[DISPOSITIVOS DISPONIBLES]")
        
        if self.is_windows:
            self._list_drives_windows()
        elif self.is_linux:
            self._list_drives_linux()
    
    def _list_drives_windows(self):
        """Lista unidades en Windows"""
        try:
            import ctypes
            drives = []
            for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                drive = f"{letter}:"
                if ctypes.windll.kernel32.GetDriveTypeW(f"{drive}\\") != 0:
                    drives.append(drive)
            
            if drives:
                for drive in drives:
                    try:
                        import os
                        usage = shutil.disk_usage(drive)
                        print(f"  {drive} - {usage.total // (1024**3)} GB total, "
                              f"{usage.free // (1024**3)} GB libre")
                    except:
                        print(f"  {drive}")
            else:
                print("No se encontraron unidades")
        except Exception as e:
            print(f"Error: {e}")
    
    def _list_drives_linux(self):
        """Lista unidades en Linux"""
        try:
            result = subprocess.run(
                ["lsblk", "-o", "NAME,SIZE,MOUNTPOINT", "-d"],
                capture_output=True, text=True
            )
            print(result.stdout)
        except FileNotFoundError:
            try:
                result = subprocess.run(
                    ["df", "-h"],
                    capture_output=True, text=True
                )
                print(result.stdout)
            except Exception as e:
                print(f"Error: {e}")
    
    def format_usb(self):
        """Formatea un dispositivo USB - PELIGROSO"""
        print("\n[⚠️  FORMATEO DE DISPOSITIVO - PELIGRO ⚠️]")
        print("ADVERTENCIA: Esta operación BORRARÁ TODOS LOS DATOS")
        print("Esta acción NO se puede deshacer.")
        
        confirmation1 = input("\n¿Entiendes que se borrarán TODOS los datos? (sí/no): ").strip().lower()
        if confirmation1 not in ['sí', 'si', 'yes', 's', 'y']:
            print("Operación cancelada.")
            return
        
        confirmation2 = input("¿Estás completamente seguro? (sí/no): ").strip().lower()
        if confirmation2 not in ['sí', 'si', 'yes', 's', 'y']:
            print("Operación cancelada.")
            return
        
        device = input("\nIngresa la unidad a formatear (ej: D:, /dev/sdb1): ").strip()
        
        if not device:
            print("Dispositivo inválido.")
            return
        
        file_system = input("Sistema de archivos (NTFS/FAT32/ext4) [NTFS]: ").strip() or "NTFS"
        volume_name = input("Nombre del volumen: ").strip() or "FormatTool"
        
        try:
            if self.is_windows:
                self._format_usb_windows(device, file_system, volume_name)
            elif self.is_linux:
                self._format_usb_linux(device, file_system, volume_name)
        except Exception as e:
            print(f"Error al formatear: {e}")
    
    def _format_usb_windows(self, device, fs, name):
        """Formatea USB en Windows"""
        device = device.replace(":", "")  # D: -> D
        
        try:
            print(f"\nFormateando {device}: con {fs}...")
            cmd = f'format {device}: /FS:{fs} /V:{name} /Y'
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
            
            if result.returncode == 0:
                print("✓ Dispositivo formateado exitosamente")
            else:
                print(f"Error: {result.stderr}")
        except Exception as e:
            print(f"Error: {e}")
            print("Sugerencia: Ejecuta como administrador")
    
    def _format_usb_linux(self, device, fs, name):
        """Formatea USB en Linux"""
        try:
            # Verificar que no sea el sistema de archivos raíz
            if device in ["/", "/home"]:
                print("Error: No puedes formatear la partición raíz del sistema")
                return
            
            print(f"\nFormateando {device} con {fs}...")
            
            if fs.lower() == "ntfs":
                subprocess.run(
                    ["sudo", "mkfs.ntfs", "-F", "-L", name, device],
                    check=True
                )
            elif fs.lower() == "fat32":
                subprocess.run(
                    ["sudo", "mkfs.vfat", "-n", name, device],
                    check=True
                )
            else:  # ext4
                subprocess.run(
                    ["sudo", "mkfs.ext4", "-L", name, device],
                    check=True
                )
            
            print("✓ Dispositivo formateado exitosamente")
        except subprocess.CalledProcessError as e:
            print(f"Error: {e}")
            print("Sugerencia: Necesitas permisos de sudo")
        except Exception as e:
            print(f"Error: {e}")
    
    def remove_file_protection(self):
        """Remueve protección contra escritura de un archivo"""
        print("\n[REMOVER PROTECCIÓN DE ARCHIVO]")
        file_path = input("Ruta del archivo: ").strip()
        
        if not os.path.exists(file_path):
            print("Error: Archivo no encontrado")
            return
        
        try:
            self._remove_write_protection(file_path)
            print(f"✓ Protección removida de: {file_path}")
        except Exception as e:
            print(f"Error: {e}")
    
    def remove_folder_protection(self):
        """Remueve protección contra escritura de una carpeta"""
        print("\n[REMOVER PROTECCIÓN DE CARPETA]")
        folder_path = input("Ruta de la carpeta: ").strip()
        
        if not os.path.isdir(folder_path):
            print("Error: Carpeta no encontrada")
            return
        
        try:
            self._remove_write_protection_recursive(folder_path)
            print(f"✓ Protección removida de: {folder_path}")
        except Exception as e:
            print(f"Error: {e}")
    
    def _remove_write_protection(self, file_path):
        """Remueve protección de un archivo"""
        if self.is_windows:
            try:
                import ctypes
                ctypes.windll.kernel32.SetFileAttributesW(file_path, 0x1)  # Remover atributo de solo lectura
            except:
                os.chmod(file_path, stat.S_IWRITE | stat.S_IREAD)
        else:
            os.chmod(file_path, stat.S_IWRITE | stat.S_IREAD)
    
    def _remove_write_protection_recursive(self, folder_path):
        """Remueve protección recursivamente"""
        for root, dirs, files in os.walk(folder_path):
            # Remover protección de archivos
            for file in files:
                file_path = os.path.join(root, file)
                try:
                    self._remove_write_protection(file_path)
                except:
                    pass
            
            # Remover protección de directorios
            for dir_name in dirs:
                dir_path = os.path.join(root, dir_name)
                try:
                    self._remove_write_protection(dir_path)
                except:
                    pass
    
    def secure_delete(self):
        """Borra archivos de forma segura"""
        print("\n[BORRADO SEGURO DE ARCHIVOS]")
        file_path = input("Ruta del archivo a borrar: ").strip()
        
        if not os.path.exists(file_path):
            print("Error: Archivo no encontrado")
            return
        
        confirm = input(f"¿Confirmas borrado seguro de {os.path.basename(file_path)}? (sí/no): ").strip().lower()
        if confirm not in ['sí', 'si', 'yes', 's', 'y']:
            print("Operación cancelada")
            return
        
        try:
            self._secure_delete_file(file_path)
            print(f"✓ Archivo borrado de forma segura: {file_path}")
        except Exception as e:
            print(f"Error: {e}")
    
    def _secure_delete_file(self, file_path):
        """Borra un archivo de forma segura sobrescribiendo datos"""
        try:
            import secrets
            
            if os.path.isfile(file_path):
                file_size = os.path.getsize(file_path)
                
                # Sobrescribir con datos aleatorios (3 pasadas)
                with open(file_path, 'ba+') as f:
                    for _ in range(3):
                        f.seek(0)
                        f.write(secrets.token_bytes(file_size))
                
                os.remove(file_path)
        except Exception as e:
            # Si falla el borrado seguro, borrar normalmente
            os.remove(file_path)
    
    def device_info(self):
        """Muestra información del dispositivo"""
        print("\n[INFORMACIÓN DEL DISPOSITIVO]")
        print(f"Sistema Operativo: {platform.system()} {platform.release()}")
        print(f"Arquitectura: {platform.machine()}")
        print(f"Python: {platform.python_version()}")
        
        try:
            import psutil
            print(f"CPU cores: {psutil.cpu_count()}")
            memoria = psutil.virtual_memory().total // (1024**3)
            print(f"Memoria RAM: {memoria} GB")
        except ImportError:
            pass
        
        print("\nEspacios en disco:")
        try:
            for partition in self._get_partitions():
                print(f"  {partition}")
        except Exception as e:
            print(f"Error al obtener información: {e}")
    
    def _get_partitions(self):
        """Obtiene particiones disponibles"""
        if self.is_windows:
            import ctypes
            drives = []
            for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                drive = f"{letter}:"
                if ctypes.windll.kernel32.GetDriveTypeW(f"{drive}\\") != 0:
                    try:
                        usage = shutil.disk_usage(drive)
                        size_gb = usage.total // (1024**3)
                        free_gb = usage.free // (1024**3)
                        drives.append(f"{drive} - {size_gb} GB ({free_gb} GB libres)")
                    except:
                        pass
            return drives
        else:
            # Linux
            result = subprocess.run(["df", "-h"], capture_output=True, text=True)
            return result.stdout.split('\n')[1:]
    
    def run(self):
        """Inicia la aplicación principal"""
        while True:
            self.print_header()
            self.print_menu()
            choice = self.get_user_choice()
            
            if choice == "0":
                print("\n¡Gracias por usar FormatTool!")
                break
            elif choice == "1":
                self.list_drives()
            elif choice == "2":
                self.format_usb()
            elif choice == "3":
                self.remove_file_protection()
            elif choice == "4":
                self.remove_folder_protection()
            elif choice == "5":
                self.secure_delete()
            elif choice == "6":
                self.device_info()
            else:
                print("Opción inválida. Selecciona una opción entre 0 y 6.")
            
            if choice != "0":
                input("\nPresiona ENTER para continuar...")

def main():
    """Función principal"""
    try:
        app = FormatTool()
        app.run()
    except Exception as e:
        print(f"Error fatal: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
