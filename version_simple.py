import tkinter as tk
from tkinter import ttk, messagebox, filedialog, Menu
from datetime import datetime
import os
import threading
import time


def calcular_factor_reduccion(i, n):
    """
    Calcula el factor de reducción para el piso i de un edificio de n pisos
    
    Algoritmo:
    - Para i = n-4 a i = n (5 pisos superiores): r_i = 1.0
    - Para i = n-5 a i = n-8 (4 pisos): r_i = 1.0 + 0.1*(i - n + 4)  
    - Para i = 1 a i = n-9 (resto): r_i = 0.5
    """
    if i >= n - 4:  # Los 5 pisos superiores
        return 1.0
    elif i >= n - 8:  # Zona intermedia (4 pisos)
        return 1.0 + 0.1 * (i - n + 4)
    else:  # Pisos inferiores
        return 0.5


def exportar_a_txt():
    try:
        n = int(entry_pisos.get())
        
        if n < 1:
            messagebox.showerror("Error", "El número de pisos debe ser mayor a 0")
            return
        
        # Selector de carpeta
        carpeta_destino = filedialog.askdirectory(
            title="Seleccionar carpeta para guardar el reporte",
            initialdir="e:\\PROYECTOS PYTHON\\SCRIPTS\\REDUCCION DE CARGA VIVA"
        )
        
        if not carpeta_destino:  # Usuario canceló
            return
        
        # Generar contenido del archivo
        contenido = []
        contenido.append("="*60)
        contenido.append("         REPORTE DE FACTORES DE REDUCCIÓN")
        contenido.append("              DE CARGA VIVA")
        contenido.append("="*60)
        contenido.append(f"Fecha: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
        contenido.append(f"Número de pisos del edificio: {n}")
        contenido.append("")
        
        # Algoritmo
        contenido.append("ALGORITMO UTILIZADO:")
        contenido.append("-" * 20)
        contenido.append("Para un edificio de 'n' pisos, el factor de reducción r_i")
        contenido.append("para el piso 'i' se calcula según:")
        contenido.append("")
        contenido.append("• Pisos superiores (i = n-4 a i = n):")
        contenido.append("  r_i = 1.0 (aplicado a los 5 pisos superiores)")
        contenido.append("")
        contenido.append("• Zona intermedia (i = n-5 a i = n-8):")
        contenido.append("  r_i = 1.0 + 0.1*(i - n + 4)")
        contenido.append("")
        contenido.append("• Pisos inferiores (i = 1 a i = n-9):")
        contenido.append("  r_i = 0.5")
        contenido.append("")
        
        # Resultados
        contenido.append("RESULTADOS:")
        contenido.append("-" * 11)
        contenido.append(f"{'Piso':<6} | {'Factor':<8} | {'Criterio':<20} | {'Cálculo':<25}")
        contenido.append("-" * 70)
        
        for i in range(n, 0, -1):  # De arriba hacia abajo
            factor = calcular_factor_reduccion(i, n)
            
            # Determinar criterio y cálculo
            if i >= n - 4:
                criterio = "Piso superior"
                calculo = "r = 1.0"
            elif i >= n - 8:
                criterio = "Zona intermedia"
                calculo = f"r = 1.0+0.1*({i}-{n}+4) = {factor:.3f}"
            else:
                criterio = "Piso inferior"
                calculo = "r = 0.5"
            
            contenido.append(f"{i:<6} | {factor:<8.3f} | {criterio:<20} | {calculo:<25}")
        
        contenido.append("")
        contenido.append("="*60)
        contenido.append("Reporte generado por: Calculadora de Factor de Reducción v2.0")
        
        # Guardar archivo
        filename = f"reporte_factores_{n}_pisos_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        filepath = os.path.join(carpeta_destino, filename)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write('\n'.join(contenido))
        
        messagebox.showinfo("Éxito", f"Reporte exportado exitosamente:\n{filepath}")
        
    except ValueError:
        messagebox.showerror("Error", "Por favor ingrese un número válido")
    except Exception as e:
        messagebox.showerror("Error", f"Error al exportar: {str(e)}")


def calcular_y_mostrar():
    try:
        n = int(entry_pisos.get())
        
        if n < 1:
            messagebox.showerror("Error", "El número de pisos debe ser mayor a 0")
            return
        
        # Limpiar tabla
        for item in tree.get_children():
            tree.delete(item)
        
        # Calcular y mostrar factores
        for i in range(n, 0, -1):  # De arriba hacia abajo
            factor = calcular_factor_reduccion(i, n)
            
            # Determinar criterio
            if i >= n - 4:
                criterio = "5 pisos superiores"
            elif i >= n - 8:
                criterio = "Zona intermedia"
            else:
                criterio = "Pisos inferiores"
            
            tree.insert('', 'end', values=(i, f"{factor:.3f}", criterio))
            
    except ValueError:
        messagebox.showerror("Error", "Por favor ingrese un número válido")
    except Exception as e:
        messagebox.showerror("Error", f"Error: {str(e)}")


def mostrar_splash_screen():
    """Muestra la pantalla de splash con disclaimer"""
    splash = tk.Toplevel()
    splash.title("")
    splash.geometry("500x400")
    splash.configure(bg='#2c3e50')
    splash.resizable(False, False)
    
    # Centrar la ventana
    splash.transient()
    splash.grab_set()
    
    # Frame principal
    main_frame = tk.Frame(splash, bg='#2c3e50', padx=30, pady=30)
    main_frame.pack(fill=tk.BOTH, expand=True)
    
    # Título
    title_label = tk.Label(main_frame, text="CALCULADORA DE FACTOR\nDE REDUCCIÓN DE CARGA VIVA", 
                          font=("Arial", 16, "bold"), fg='white', bg='#2c3e50', justify='center')
    title_label.pack(pady=(0, 20))
    
    # Versión
    version_label = tk.Label(main_frame, text="Versión 2.0", 
                            font=("Arial", 12), fg='#ecf0f1', bg='#2c3e50')
    version_label.pack(pady=(0, 30))
    
    # Disclaimer
    disclaimer_frame = tk.Frame(main_frame, bg='#e74c3c', relief='solid', bd=2)
    disclaimer_frame.pack(fill=tk.X, pady=(0, 20))
    
    disclaimer_title = tk.Label(disclaimer_frame, text="⚠️ IMPORTANTE - DISCLAIMER", 
                               font=("Arial", 12, "bold"), fg='white', bg='#e74c3c')
    disclaimer_title.pack(pady=(10, 5))
    
    disclaimer_text = """Es responsabilidad del usuario verificar que los datos 
generados por este software son correctos y aplicables 
a su caso específico. El desarrollador no se hace 
responsable por errores en cálculos o decisiones 
basadas en los resultados de este programa."""
    
    disclaimer_label = tk.Label(disclaimer_frame, text=disclaimer_text, 
                               font=("Arial", 10), fg='white', bg='#e74c3c', 
                               justify='center', wraplength=400)
    disclaimer_label.pack(pady=(0, 10), padx=10)
    
    # Información
    info_text = "Desarrollado para cálculo de factores de reducción\nen edificaciones según normativas técnicas."
    info_label = tk.Label(main_frame, text=info_text, 
                         font=("Arial", 10), fg='#bdc3c7', bg='#2c3e50', 
                         justify='center')
    info_label.pack(pady=(0, 20))
    
    # Botón continuar
    continue_btn = tk.Button(main_frame, text="Continuar", 
                            font=("Arial", 12, "bold"), 
                            command=splash.destroy,
                            bg='#27ae60', fg='white', 
                            relief='flat', padx=30, pady=10)
    continue_btn.pack()
    
    # Auto-cerrar después de 5 segundos
    splash.after(5000, splash.destroy)
    
    return splash


def mostrar_ayuda():
    """Muestra ventana de ayuda con funcionalidad y uso"""
    ayuda_window = tk.Toplevel()
    ayuda_window.title("Ayuda y Funcionalidad")
    ayuda_window.geometry("700x500")
    ayuda_window.configure(bg='white')
    
    # Intentar configurar icono
    try:
        ayuda_window.iconbitmap("E:\\PROYECTOS PYTHON\\LOGO 4D-ROTULO.ico")
    except:
        pass
    
    # Frame principal con scroll
    canvas = tk.Canvas(ayuda_window, bg='white')
    scrollbar = ttk.Scrollbar(ayuda_window, orient="vertical", command=canvas.yview)
    scrollable_frame = ttk.Frame(canvas)
    
    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )
    
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)
    
    # Contenido de ayuda
    help_text = """
🏗️ CALCULADORA DE FACTOR DE REDUCCIÓN DE CARGA VIVA

📋 FUNCIONALIDAD:
Esta aplicación calcula los factores de reducción de carga viva para edificios 
según el algoritmo específico implementado.

📐 ALGORITMO:
• Pisos Superiores (n-4 a n): Factor = 1.0
  - Se aplica a los 5 pisos más altos
  - Sin reducción de carga

• Zona Intermedia (n-5 a n-8): Factor = 1.0 + 0.1*(i-n+4)
  - Se aplica a los siguientes 4 pisos
  - Reducción gradual según altura

• Pisos Inferiores (1 a n-9): Factor = 0.5
  - Se aplica al resto de pisos
  - Máxima reducción permitida

🎯 CÓMO USAR:
1. Ingrese el número total de pisos del edificio
2. Haga clic en "Calcular" para ver los resultados
3. Use "Exportar TXT" para generar reporte completo
4. Seleccione la carpeta donde guardar el archivo

📊 RESULTADOS:
• Tabla con factor para cada piso
• Criterio aplicado (Superior/Intermedio/Inferior)
• Cálculo detallado de la fórmula

💾 EXPORTACIÓN:
• Reporte en formato TXT legible
• Incluye algoritmo y resultados completos
• Fecha y hora de generación
• Selección libre de carpeta destino

⚠️ IMPORTANTE:
Verifique siempre que los resultados son aplicables a su caso específico.
Consulte las normativas locales vigentes.

📞 SOPORTE:
Este software es una herramienta de cálculo. Para dudas técnicas,
consulte con un ingeniero estructural calificado.
"""
    
    text_label = tk.Label(scrollable_frame, text=help_text, 
                         font=("Arial", 11), justify='left', 
                         bg='white', padx=20, pady=20)
    text_label.pack(fill=tk.BOTH, expand=True)
    
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")


# Crear ventana principal
root = tk.Tk()
root.withdraw()  # Ocultar mientras se muestra splash
root.title("Factor de Reducción de Carga Viva - Versión Simple v2.0")
root.geometry("650x600")

# Configurar icono
try:
    root.iconbitmap("E:\\PROYECTOS PYTHON\\LOGO 4D-ROTULO.ico")
except:
    pass  # Si no se encuentra el icono, usar el predeterminado

# Mostrar splash screen
splash = mostrar_splash_screen()

def mostrar_ventana_principal():
    """Mostrar la ventana principal después del splash"""
    root.deiconify()  # Mostrar ventana principal
    
# Auto mostrar ventana principal después de 5 segundos
root.after(5000, mostrar_ventana_principal)

# Crear menú ribbon
menubar = Menu(root)
root.config(menu=menubar)

# Menú Ayuda
help_menu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="📚 Ayuda", menu=help_menu)
help_menu.add_command(label="📖 Funcionalidad y Uso", command=mostrar_ayuda)
help_menu.add_separator()
help_menu.add_command(label="ℹ️ Acerca de", command=lambda: messagebox.showinfo(
    "Acerca de", 
    "Calculadora de Factor de Reducción de Carga Viva v2.0\n\n" +
    "Desarrollado para cálculo de factores según normativas.\n\n" +
    "⚠️ Verificar siempre la aplicabilidad de los resultados."
))

# Menú Archivo
file_menu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="📁 Archivo", menu=file_menu)
file_menu.add_command(label="📤 Exportar TXT", command=lambda: exportar_a_txt())
file_menu.add_separator()
file_menu.add_command(label="❌ Salir", command=root.quit)

# Frame principal
main_frame = ttk.Frame(root, padding="10")
main_frame.pack(fill=tk.BOTH, expand=True)

# Título
ttk.Label(main_frame, text="Calculadora de Factor de Reducción v2.0", 
          font=("Arial", 14, "bold")).pack(pady=(0, 15))

# Frame para input
input_frame = ttk.Frame(main_frame)
input_frame.pack(fill=tk.X, pady=(0, 15))

ttk.Label(input_frame, text="Número de pisos:").pack(side=tk.LEFT)
entry_pisos = ttk.Entry(input_frame, width=10)
entry_pisos.pack(side=tk.LEFT, padx=(5, 10))
entry_pisos.insert(0, "10")  # Valor por defecto

ttk.Button(input_frame, text="Calcular", command=calcular_y_mostrar).pack(side=tk.LEFT)
ttk.Button(input_frame, text="Exportar TXT", command=exportar_a_txt).pack(side=tk.LEFT, padx=(5, 0))

# Tabla de resultados
columns = ('Piso', 'Factor', 'Criterio')
tree = ttk.Treeview(main_frame, columns=columns, show='headings', height=15)

# Configurar columnas
tree.heading('Piso', text='Piso')
tree.heading('Factor', text='Factor (r_i)')
tree.heading('Criterio', text='Criterio')

tree.column('Piso', width=80, anchor='center')
tree.column('Factor', width=120, anchor='center')
tree.column('Criterio', width=200, anchor='center')

tree.pack(fill=tk.BOTH, expand=True, pady=(0, 15))

# Scrollbar
scrollbar = ttk.Scrollbar(tree, orient=tk.VERTICAL, command=tree.yview)
tree.configure(yscrollcommand=scrollbar.set)

# Información del algoritmo
info_frame = ttk.LabelFrame(main_frame, text="Algoritmo", padding="5")
info_frame.pack(fill=tk.X)

info_text = """Reglas del Factor de Reducción:
• Pisos superiores (n-4 a n): r = 1.0
• Zona intermedia (n-8 a n-5): r = 1.0 + 0.1*(i-n+4)
• Pisos inferiores (1 a n-9): r = 0.5"""

ttk.Label(info_frame, text=info_text, justify=tk.LEFT).pack(anchor=tk.W)

# Calcular automáticamente al inicio
calcular_y_mostrar()

# Ejecutar aplicación
root.mainloop()