#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Calculadora de Factor de Reducción de Carga Viva NSR-10 B.5.4.2
Versión Estable - Sin problemas de rutas
"""

import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from datetime import datetime
import os
import sys

def calcular_factor(piso, total_pisos):
    """Calcula el factor de reducción para un piso específico según NSR-10 B.5.4.2"""
    if piso >= total_pisos - 4:
        return 1.0
    elif piso >= total_pisos - 8:
        return 1.0 + 0.1 * (piso - total_pisos + 4)
    else:
        return 0.5

def exportar():
    """Exporta los resultados a archivo TXT en la carpeta seleccionada"""
    try:
        n = int(entry_pisos.get())
        if n < 1:
            messagebox.showerror("Error", "El número de pisos debe ser mayor a 0")
            return
        
        # Seleccionar carpeta donde guardar
        carpeta = filedialog.askdirectory(title="Seleccionar carpeta donde guardar el reporte")
        if not carpeta:
            return
        
        # Generar contenido del reporte
        contenido = [
            "=" * 60,
            "         REPORTE DE FACTORES DE REDUCCIÓN",
            "              DE CARGA VIVA",
            "=" * 60,
            f"Fecha: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}",
            f"Número de pisos del edificio: {n}",
            "",
            "ALGORITMO UTILIZADO:",
            "-" * 20,
            "Para un edificio de 'n' pisos, el factor de reducción r_i",
            "para el piso 'i' se calcula según NSR-10 B.5.4.2:",
            "",
            "• Pisos superiores (i = n-4 a i = n):",
            "  r_i = 1.0 (aplicado a los 5 pisos superiores)",
            "",
            "• Zona intermedia (i = n-5 a i = n-8):",
            "  r_i = 1.0 + 0.1*(i - n + 4)",
            "",
            "• Pisos inferiores (i = 1 a i = n-9):",
            "  r_i = 0.5",
            "",
            "RESULTADOS:",
            "-" * 11,
            "Piso   | Factor   | Criterio             | Cálculo",
            "-" * 70
        ]
        
        # Generar tabla de resultados
        for i in range(n, 0, -1):
            factor = calcular_factor(i, n)
            if i >= n - 4:
                criterio = "Piso superior"
                calculo = "r = 1.0"
            elif i >= n - 8:
                criterio = "Zona intermedia"
                calculo = f"r = 1.0+0.1*({i}-{n}+4) = {factor:.3f}"
            else:
                criterio = "Piso inferior"
                calculo = "r = 0.5"
            
            linea = f"{i:<7}| {factor:<9.3f}| {criterio:<21}| {calculo}"
            contenido.append(linea)
        
        # Pie del reporte
        contenido.extend([
            "",
            "=" * 60,
            "⚠️  NOTA IMPORTANTE - APLICACIÓN ESPECÍFICA:",
            "-" * 45,
            "Los factores de reducción calculados en este reporte",
            "APLICAN ÚNICAMENTE para el diseño de:",
            "",
            "✓ COLUMNAS",
            "✓ CIMENTACIONES (zapatas, pilotes, etc.)",
            "",
            "❌ NO APLICABLE para:",
            "   • Vigas", 
            "   • Losas",
            "   • Muros estructurales",
            "   • Otros elementos estructurales",
            "",
            "Esta limitación está establecida en la norma NSR-10 B.5.4.2",
            "y debe ser respetada estrictamente en el diseño.",
            "",
            "=" * 60,
            "Reporte generado por: Calculadora de Factor de Reducción v2.0",
            "Referencia normativa: NSR-10 B.5.4.2"
        ])
        
        # Guardar archivo
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        nombre_archivo = f"reporte_reduccion_carga_viva_{n}p_{timestamp}.txt"
        ruta_completa = os.path.join(carpeta, nombre_archivo)
        
        with open(ruta_completa, 'w', encoding='utf-8') as archivo:
            archivo.write('\n'.join(contenido))
        
        messagebox.showinfo("Exportación Exitosa", 
                          f"Reporte guardado exitosamente:\\n\\n{ruta_completa}")
        
    except ValueError:
        messagebox.showerror("Error", "Por favor ingrese un número válido de pisos")
    except Exception as e:
        messagebox.showerror("Error", f"Error al guardar el archivo:\\n{str(e)}")

def calcular():
    """Calcula y muestra los factores de reducción en la tabla"""
    try:
        n = int(entry_pisos.get())
        if n < 1:
            messagebox.showerror("Error", "El número de pisos debe ser mayor a 0")
            return
        
        # Limpiar tabla anterior
        for item in tabla.get_children():
            tabla.delete(item)
        
        # Llenar tabla con resultados
        for i in range(n, 0, -1):
            factor = calcular_factor(i, n)
            
            if i >= n - 4:
                criterio = "Superior"
                observacion = "Sin reducción"
            elif i >= n - 8:
                criterio = "Intermedio"
                observacion = f"Reducción gradual ({factor:.1%})"
            else:
                criterio = "Inferior"
                observacion = "Reducción máxima (50%)"
            
            tabla.insert('', 'end', values=(i, f"{factor:.3f}", criterio, observacion))
            
    except ValueError:
        messagebox.showerror("Error", "Por favor ingrese un número válido de pisos")

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Calculadora Factor Reducción NSR-10 B.5.4.2")
ventana.geometry("700x500")
ventana.resizable(True, True)

# Cargar icono personalizado 4D
try:
    ventana.iconbitmap("LOGO 4D-ROTULO.ico")
    print("✅ Icono 4D-ROTULO cargado exitosamente")
except Exception as e:
    print(f"⚠️ No se pudo cargar el icono: {e}")
    # Intentar con ruta absoluta
    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        icon_path = os.path.join(script_dir, "LOGO 4D-ROTULO.ico")
        ventana.iconbitmap(icon_path)
        print("✅ Icono 4D-ROTULO cargado desde ruta absoluta")
    except:
        print("ℹ️ Usando icono predeterminado del sistema")

# Frame principal con padding
frame_principal = ttk.Frame(ventana, padding="15")
frame_principal.pack(fill=tk.BOTH, expand=True)

# Título
titulo = ttk.Label(frame_principal, 
                   text="🏗️ CALCULADORA FACTOR REDUCCIÓN CARGA VIVA",
                   font=("Arial", 14, "bold"))
titulo.pack(pady=(0, 10))

subtitulo = ttk.Label(frame_principal, 
                      text="Según NSR-10 B.5.4.2", 
                      font=("Arial", 10, "italic"))
subtitulo.pack(pady=(0, 20))

# Frame para entrada de datos
frame_entrada = ttk.LabelFrame(frame_principal, text="Datos de Entrada", padding="10")
frame_entrada.pack(fill=tk.X, pady=(0, 15))

# Input número de pisos
ttk.Label(frame_entrada, text="Número de pisos del edificio:").pack(side=tk.LEFT)
entry_pisos = ttk.Entry(frame_entrada, width=10, font=("Arial", 12))
entry_pisos.pack(side=tk.LEFT, padx=(10, 10))

# Botones
boton_calcular = ttk.Button(frame_entrada, text="🔢 Calcular", command=calcular)
boton_calcular.pack(side=tk.LEFT, padx=(5, 5))

boton_exportar = ttk.Button(frame_entrada, text="📄 Exportar TXT", command=exportar)
boton_exportar.pack(side=tk.LEFT, padx=(5, 0))

# Frame para tabla de resultados
frame_tabla = ttk.LabelFrame(frame_principal, text="Resultados", padding="10")
frame_tabla.pack(fill=tk.BOTH, expand=True)

# Configurar tabla
columnas = ('Piso', 'Factor', 'Criterio', 'Observaciones')
tabla = ttk.Treeview(frame_tabla, columns=columnas, show='headings', height=15)

# Configurar encabezados y ancho de columnas
tabla.heading('Piso', text='Piso')
tabla.heading('Factor', text='Factor')
tabla.heading('Criterio', text='Criterio') 
tabla.heading('Observaciones', text='Observaciones')

tabla.column('Piso', width=80, anchor='center')
tabla.column('Factor', width=100, anchor='center')
tabla.column('Criterio', width=120, anchor='center')
tabla.column('Observaciones', width=300, anchor='center')

# Scrollbar para la tabla
scrollbar = ttk.Scrollbar(frame_tabla, orient=tk.VERTICAL, command=tabla.yview)
tabla.configure(yscrollcommand=scrollbar.set)

# Empaquetar tabla y scrollbar
tabla.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Frame inferior con información
frame_info = ttk.Frame(frame_principal)
frame_info.pack(fill=tk.X, pady=(10, 0))

# Nota importante sobre aplicación
frame_nota_importante = ttk.LabelFrame(frame_info, text="⚠️ NOTA IMPORTANTE", padding="10")
frame_nota_importante.pack(fill=tk.X, pady=(0, 10))

nota_importante = ("APLICACIÓN ESPECÍFICA: Los factores de reducción calculados por esta herramienta " +
                  "APLICAN ÚNICAMENTE para el diseño de COLUMNAS y CIMENTACIONES. " +
                  "NO deben utilizarse para el diseño de vigas, losas u otros elementos estructurales.")

label_nota = ttk.Label(frame_nota_importante, text=nota_importante, wraplength=650, 
                       font=("Arial", 9, "bold"), foreground="red")
label_nota.pack()

info_texto = ("💡 Información: Esta calculadora implementa los factores de reducción " +
              "según la norma NSR-10 B.5.4.2. Los resultados deben ser revisados " +
              "por un profesional calificado.")

label_info = ttk.Label(frame_info, text=info_texto, wraplength=650, 
                       font=("Arial", 9), foreground="blue")
label_info.pack()

# Enfocar en el campo de entrada
entry_pisos.focus()

# Permitir calcular con Enter
entry_pisos.bind('<Return>', lambda event: calcular())

# Iniciar aplicación
if __name__ == "__main__":
    print("✅ Iniciando Calculadora Factor Reducción NSR-10 B.5.4.2")
    print("📁 Directorio actual:", os.getcwd())
    ventana.mainloop()