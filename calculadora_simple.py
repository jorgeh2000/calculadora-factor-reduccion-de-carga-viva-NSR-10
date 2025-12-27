import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from datetime import datetime
import os

def calcular_factor(i, n):
    if i >= n - 4:
        return 1.0
    elif i >= n - 8:
        return 1.0 + 0.1 * (i - n + 4)
    else:
        return 0.5

def exportar():
    try:
        n = int(entry.get())
        if n < 1:
            messagebox.showerror("Error", "Número debe ser mayor a 0")
            return
        
        carpeta = filedialog.askdirectory(title="Seleccionar carpeta")
        if not carpeta:
            return
        
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
        contenido.append("")
        contenido.append("")
        contenido.append("ALGORITMO Y ECUACIONES UTILIZADAS")
        contenido.append("="*35)
        contenido.append("")
        contenido.append("ECUACIONES DEL FACTOR DE REDUCCIÓN:")
        contenido.append("")
        contenido.append("1. PISOS SUPERIORES (i >= n-4):")
        contenido.append("   Ecuación: r_i = 1.0")
        contenido.append("   Aplicación: Los 5 pisos más altos")
        contenido.append("   Justificación: Carga viva completa")
        contenido.append("")
        contenido.append("2. ZONA INTERMEDIA (n-8 <= i < n-4):")
        contenido.append("   Ecuación: r_i = 1.0 + 0.1 × (i - n + 4)")
        contenido.append("   Aplicación: Siguientes 4 pisos hacia abajo")
        contenido.append("   Justificación: Reducción gradual por altura")
        contenido.append("")
        contenido.append("3. PISOS INFERIORES (i < n-8):")
        contenido.append("   Ecuación: r_i = 0.5")
        contenido.append("   Aplicación: Resto de pisos hacia cimentación")
        contenido.append("   Justificación: Máxima reducción permitida")
        contenido.append("")
        
        contenido.append("")
        contenido.append("=" * 60)
        contenido.append("⚠️  NOTA IMPORTANTE - APLICACIÓN ESPECÍFICA:")
        contenido.append("-" * 45)
        contenido.append("Los factores de reducción calculados en este reporte")
        contenido.append("APLICAN ÚNICAMENTE para el diseño de:")
        contenido.append("")
        contenido.append("✓ COLUMNAS")
        contenido.append("✓ CIMENTACIONES (zapatas, pilotes, etc.)")
        contenido.append("✓ EDIFICIOS DE 5 PISOS O MÁS")
        contenido.append("")
        contenido.append("❌ NO APLICABLE para:")
        contenido.append("   • Vigas")
        contenido.append("   • Losas")
        contenido.append("   • Muros estructurales")
        contenido.append("   • Edificios de menos de 5 pisos")
        contenido.append("   • Otros elementos estructurales")
        contenido.append("")
        contenido.append("Esta limitación está establecida en la norma NSR-10 B.5.4.2")
        contenido.append("y debe ser respetada estrictamente en el diseño.")
        contenido.append("")
        contenido.append("Reporte generado por: Calculadora de Factor de Reducción v2.0")
        contenido.append("Referencia normativa: NSR-10 B.5.4.2")
        
        archivo = os.path.join(carpeta, f"reporte_{n}_pisos.txt")
        with open(archivo, 'w', encoding='utf-8') as f:
            f.write('\\n'.join(contenido))
        
        messagebox.showinfo("Éxito", f"Archivo guardado en:\\n{archivo}")
        
    except ValueError:
        messagebox.showerror("Error", "Ingrese un número válido")

def calcular():
    try:
        n = int(entry.get())
        if n < 1:
            messagebox.showerror("Error", "Número debe ser mayor a 0")
            return
        
        for item in tree.get_children():
            tree.delete(item)
        
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
        messagebox.showerror("Error", "Ingrese un número válido")

# Ventana principal
root = tk.Tk()
root.title("Calculadora Factor Reducción NSR-10 B.5.4.2")
root.geometry("550x500")

# Intentar cargar icono
try:
    icon_paths = [
        "LOGO 4D-ROTULO.ico",
        "E:\\PROYECTOS PYTHON\\LOGO 4D-ROTULO.ico"
    ]
    for path in icon_paths:
        if os.path.exists(path):
            root.iconbitmap(path)
            print(f"✅ Icono cargado: {path}")
            break
except:
    print("ℹ️ Usando icono predeterminado")

# Interface
frame = ttk.Frame(root, padding="10")
frame.pack(fill=tk.BOTH, expand=True)

ttk.Label(frame, text="🏗️ Calculadora Factor Reducción v2.0", 
         font=("Arial", 14, "bold")).pack(pady=(0, 5))

ttk.Label(frame, text="NSR-10 B.5.4.2 - Solo Columnas/Cimentaciones (5+ pisos)", 
         font=("Arial", 10, "italic"), foreground="red").pack(pady=(0, 15))

# Input
input_frame = ttk.Frame(frame)
input_frame.pack(fill=tk.X, pady=(0, 15))

ttk.Label(input_frame, text="Número de pisos:").pack(side=tk.LEFT)
entry = ttk.Entry(input_frame, width=10)
entry.pack(side=tk.LEFT, padx=(5, 10))
entry.insert(0, "10")

ttk.Button(input_frame, text="Calcular", command=calcular).pack(side=tk.LEFT, padx=(0, 5))
ttk.Button(input_frame, text="Exportar TXT", command=exportar).pack(side=tk.LEFT)

# Tabla
tree = ttk.Treeview(frame, columns=('Piso', 'Factor', 'Criterio'), show='headings', height=15)
for col in ('Piso', 'Factor', 'Criterio'):
    tree.heading(col, text=col)
    tree.column(col, width=120, anchor='center')
tree.pack(fill=tk.BOTH, expand=True, pady=(0, 10))

# Info
ttk.Label(frame, text="⚠️ Verificar resultados con profesional calificado", 
         foreground="red").pack()

# Calcular inicial
calcular()

print("🚀 Aplicación lista")
root.mainloop()