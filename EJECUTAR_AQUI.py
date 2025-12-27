#!/usr/bin/env python3
"""
LANZADOR SIMPLE - Ejecutar este archivo directamente
"""
import os
import sys

# Cambiar al directorio del script
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

print("🚀 Lanzando Calculadora...")
print(f"📁 Directorio: {script_dir}")

# Intentar ejecutar la calculadora estable
try:
    exec(open('calculadora_estable.py').read())
except FileNotFoundError:
    print("❌ No se encuentra calculadora_estable.py")
    try:
        exec(open('calculadora_simple.py').read())
    except FileNotFoundError:
        print("❌ No se encuentra calculadora_simple.py")
        input("Presiona Enter para salir...")