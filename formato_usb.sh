#!/bin/bash

# Lanzador para FormatTool en Linux
# Este archivo ejecuta format_tool.py con Python3

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Colores para output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "\n${GREEN}========================================${NC}"
echo -e "${GREEN}   Iniciando FormatTool en Linux${NC}"
echo -e "${GREEN}========================================${NC}\n"

# Verificar si Python3 está instalado
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}ERROR: Python3 no está instalado${NC}"
    echo -e "\nInstala Python3 con:"
    echo -e "  Ubuntu/Debian: ${YELLOW}sudo apt-get install python3${NC}"
    echo -e "  Fedora: ${YELLOW}sudo dnf install python3${NC}"
    echo -e "  Arch: ${YELLOW}sudo pacman -S python${NC}"
    exit 1
fi

# Ejecutar la aplicación
python3 "$SCRIPT_DIR/format_tool.py"

# Verificar si hubo error
if [ $? -ne 0 ]; then
    echo -e "\n${RED}❌ Error al ejecutar FormatTool${NC}"
    echo -e "Intenta ejecutar con ${YELLOW}sudo${NC}:"
    echo -e "  ${YELLOW}sudo python3 $SCRIPT_DIR/format_tool.py${NC}"
fi
