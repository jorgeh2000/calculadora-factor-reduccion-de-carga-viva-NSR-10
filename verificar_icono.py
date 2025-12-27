#!/usr/bin/env python3
"""
Verificador de icono para la aplicación
"""

import tkinter as tk
import os

def verificar_icono():
    """Verifica si el icono existe y se puede cargar"""
    icon_path = "E:\\PROYECTOS PYTHON\\LOGO 4D-ROTULO.ico"
    
    print("🔍 VERIFICANDO ICONO...")
    print(f"📁 Buscando: {icon_path}")
    
    if os.path.exists(icon_path):
        print("✅ Archivo encontrado!")
        
        # Probar cargar en tkinter
        try:
            root = tk.Tk()
            root.withdraw()  # No mostrar ventana
            root.iconbitmap(icon_path)
            root.destroy()
            print("✅ Icono compatible con tkinter")
            return True
        except Exception as e:
            print(f"❌ Error cargando icono: {e}")
            return False
    else:
        print("❌ Archivo NO encontrado")
        print("\n💡 SOLUCIONES:")
        print("1. Verificar que el archivo existe en E:\\PROYECTOS PYTHON\\")
        print("2. Verificar que se llama exactamente 'LOGO 4D-ROTULO.ico'")
        print("3. Verificar que es un archivo .ico válido")
        return False

def crear_icono_prueba():
    """Crea un icono de prueba simple"""
    try:
        import tkinter as tk
        from tkinter import Canvas
        
        # Crear ventana temporal para generar icono
        temp_root = tk.Tk()
        temp_root.withdraw()
        
        # Crear imagen simple usando tkinter
        canvas = Canvas(temp_root, width=32, height=32)
        canvas.create_rectangle(0, 0, 32, 32, fill='blue', outline='white', width=2)
        canvas.create_text(16, 16, text="4D", fill='white', font=("Arial", 10, "bold"))
        
        # Guardar como postscript y convertir
        canvas.postscript(file="temp_icon.ps")
        temp_root.destroy()
        
        print("💡 Se puede crear un icono de prueba si es necesario")
        
    except Exception as e:
        print(f"⚠️ No se pudo crear icono de prueba: {e}")

if __name__ == "__main__":
    print("🎨 VERIFICADOR DE ICONO LOGO 4D-ROTULO")
    print("=" * 50)
    
    if verificar_icono():
        print("\n🎉 ¡Todo listo! El icono funcionará correctamente.")
    else:
        print("\n⚠️ El icono no está disponible.")
        print("La aplicación usará el icono predeterminado (plumilla).")
        crear_icono_prueba()
    
    print("\n📋 INSTRUCCIONES:")
    print("1. Asegurase que LOGO 4D-ROTULO.ico esté en E:\\PROYECTOS PYTHON\\")
    print("2. El archivo debe ser formato .ico válido")
    print("3. Tamaño recomendado: 32x32 o 64x64 píxeles")
    print("4. Si no existe, la app funcionará con icono predeterminado")