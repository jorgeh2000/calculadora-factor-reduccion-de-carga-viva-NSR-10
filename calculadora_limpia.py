#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Calculadora de Factor de Reducción de Carga Viva - Versión Simplificada
"""

import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from datetime import datetime
import os

def calcular_factor(piso, total_pisos):
    """Calcula el factor de reducción para un piso específico"""
    if piso >= total_pisos - 4:
        return 1.0
    elif piso >= total_pisos - 8:
        return 1.0 + 0.1 * (piso - total_pisos + 4)
    else:
        return 0.5

def exportar():
    """Exporta los resultados a archivo TXT"""
    try:
        n = int(entry.get())
        if n < 1:
            messagebox.showerror("Error", "Número debe ser mayor a 0")
            return
        
        carpeta = filedialog.askdirectory(title="Seleccionar carpeta")
        if not carpeta:
            return
        
        # Generar contenido con formato mejorado
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
            "para el piso 'i' se calcula según:",
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
        
        contenido.append("")
        contenido.append("=" * 60)
        contenido.append("Reporte generado por: Calculadora de Factor de Reducción v2.0")
        contenido.append("Referencia normativa: NSR-10 B.5.4.2")
        
        archivo = os.path.join(carpeta, f"reporte_{n}_pisos_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt")
        with open(archivo, 'w', encoding='utf-8') as f:
            f.write('\n'.join(contenido))
        
        messagebox.showinfo("Éxito", f"Archivo guardado:\n{archivo}")
        
    except ValueError:
        messagebox.showerror("Error", "Ingrese número válido")

def calcular():
    """Calcula y muestra los factores de reducción"""
    try:
        n = int(entry.get())
        if n < 1:
            messagebox.showerror("Error", "Número debe ser mayor a 0")
            return
        
        # Limpiar tabla
        for item in tree.get_children():
            tree.delete(item)
        
        # Llenar tabla
        for i in range(n, 0, -1):
            factor = calcular_factor(i, n)
            if i >= n - 4:
                criterio = "Superior"
            elif i >= n - 8:
                criterio = "Intermedio" 
            else:
                criterio = "Inferior"
            
            tree.insert('', 'end', values=(i, f"{factor:.3f}", criterio))
            
    except ValueError:
        messagebox.showerror("Error", "Ingrese número válido")

# Crear ventana principal
root = tk.Tk()
root.title("Calculadora Factor Reducción NSR-10 B.5.4.2")
root.geometry("500x400")

# Frame principal
frame = ttk.Frame(root, padding="10")
frame.pack(fill=tk.BOTH, expand=True)

# Título
ttk.Label(frame, text="Calculadora Factor Reducción", 
         font=("Arial", 14, "bold")).pack(pady=(0, 10))

# Input
input_frame = ttk.Frame(frame)
input_frame.pack(fill=tk.X, pady=(0, 10))

ttk.Label(input_frame, text="Número de pisos:").pack(side=tk.LEFT)
entry = ttk.Entry(input_frame, width=10)
entry.pack(side=tk.LEFT, padx=5)
ttk.Button(input_frame, text="Calcular", command=calcular).pack(side=tk.LEFT, padx=5)
ttk.Button(input_frame, text="Exportar", command=exportar).pack(side=tk.LEFT, padx=5)

# Tabla
columns = ('Piso', 'Factor', 'Criterio')
tree = ttk.Treeview(frame, columns=columns, show='headings', height=15)

for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=120)

tree.pack(fill=tk.BOTH, expand=True)

# Iniciar aplicación
print("✅ Iniciando aplicación...")
root.mainloop()