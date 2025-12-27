import tkinter as tk
from tkinter import ttk, messagebox, filedialog, Menu
from datetime import datetime
import os


def buscar_y_cargar_icono(ventana):
    """Busca el icono en múltiples ubicaciones y lo carga"""
    posibles_rutas = [
        "E:\\PROYECTOS PYTHON\\LOGO 4D-ROTULO.ico",
        os.path.join(os.path.dirname(__file__), "LOGO 4D-ROTULO.ico"),
        os.path.join(os.getcwd(), "LOGO 4D-ROTULO.ico"),
        "LOGO 4D-ROTULO.ico"
    ]
    
    for ruta in posibles_rutas:
        if os.path.exists(ruta):
            try:
                ventana.iconbitmap(ruta)
                print(f"✅ Icono cargado desde: {ruta}")
                return True
            except Exception as e:
                print(f"⚠️ Error cargando icono de {ruta}: {e}")
                continue
    
    print("⚠️ No se encontró LOGO 4D-ROTULO.ico")
    print("   🖼️ Se usará el icono predeterminado de tkinter")
    return False


def mostrar_splash_screen():
    """Muestra splash screen con disclaimer"""
    splash = tk.Tk()
    splash.title("")
    splash.geometry("500x400")
    splash.configure(bg='#2c3e50')
    splash.resizable(False, False)
    
    # Buscar y configurar icono del splash
    buscar_y_cargar_icono(splash)
    
    # Centrar ventana
    try:
        splash.eval('tk::PlaceWindow . center')
    except:
        # Si no funciona el centrado automático, centrar manualmente
        splash.update_idletasks()
        x = (splash.winfo_screenwidth() // 2) - (500 // 2)
        y = (splash.winfo_screenheight() // 2) - (400 // 2)
        splash.geometry(f"500x400+{x}+{y}")
    
    # Frame principal
    main_frame = tk.Frame(splash, bg='#2c3e50', padx=30, pady=30)
    main_frame.pack(fill=tk.BOTH, expand=True)
    
    # Título
    title_label = tk.Label(main_frame, text="CALCULADORA DE FACTOR\nDE REDUCCIÓN DE CARGA VIVA", 
                          font=("Arial", 16, "bold"), fg='white', bg='#2c3e50', justify='center')
    title_label.pack(pady=(0, 15))
    
    # Versión
    version_label = tk.Label(main_frame, text="Versión 2.0", 
                            font=("Arial", 12), fg='#ecf0f1', bg='#2c3e50')
    version_label.pack(pady=(0, 25))
    
    # Disclaimer
    disclaimer_frame = tk.Frame(main_frame, bg='#e74c3c', relief='solid', bd=2)
    disclaimer_frame.pack(fill=tk.X, pady=(0, 15))
    
    disclaimer_title = tk.Label(disclaimer_frame, text="⚠️ IMPORTANTE - DISCLAIMER", 
                               font=("Arial", 12, "bold"), fg='white', bg='#e74c3c')
    disclaimer_title.pack(pady=(10, 5))
    
    disclaimer_text = """Es responsabilidad del usuario verificar que 
los datos generados son correctos y aplicables. 
El desarrollador no se hace responsable por 
errores o decisiones basadas en los resultados."""
    
    disclaimer_label = tk.Label(disclaimer_frame, text=disclaimer_text, 
                               font=("Arial", 10), fg='white', bg='#e74c3c', 
                               justify='center', wraplength=400)
    disclaimer_label.pack(pady=(0, 10), padx=15)
    
    # Botón continuar
    continue_btn = tk.Button(main_frame, text="Acepto y Continuar", 
                            font=("Arial", 12, "bold"), 
                            command=splash.destroy,
                            bg='#27ae60', fg='white', 
                            relief='flat', padx=30, pady=8)
    continue_btn.pack(pady=(10, 0))
    
    # Auto-cerrar después de 8 segundos
    splash.after(8000, splash.destroy)
    
    # Mostrar splash
    splash.mainloop()


def calcular_factor_reduccion(i, n):
    """Calcula el factor de reducción para el piso i de un edificio de n pisos"""
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
            initialdir=os.path.dirname(__file__)
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
        contenido.append("• Pisos superiores (n-4 a n): r_i = 1.0")
        contenido.append("• Zona intermedia (n-5 a n-8): r_i = 1.0 + 0.1*(i-n+4)")
        contenido.append("• Pisos inferiores (1 a n-9): r_i = 0.5")
        contenido.append("")
        
        # Resultados
        contenido.append("RESULTADOS:")
        contenido.append("-" * 11)
        contenido.append(f"{'Piso':<6} | {'Factor':<8} | {'Criterio':<20}")
        contenido.append("-" * 50)
        
        for i in range(n, 0, -1):  # De arriba hacia abajo
            factor = calcular_factor_reduccion(i, n)
            
            if i >= n - 4:
                criterio = "Piso superior"
            elif i >= n - 8:
                criterio = "Zona intermedia"
            else:
                criterio = "Piso inferior"
            
            contenido.append(f"{i:<6} | {factor:<8.3f} | {criterio:<20}")
        
        contenido.append("")
        contenido.append("="*60)
        contenido.append("⚠️  DISCLAIMER: Verificar siempre la aplicabilidad")
        contenido.append("de los resultados con un profesional calificado.")
        
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


def mostrar_ayuda():
    """Muestra ventana de ayuda"""
    ayuda_window = tk.Toplevel(root)
    ayuda_window.title("Ayuda")
    ayuda_window.geometry("600x400")
    
    # Buscar y configurar icono también en ventana de ayuda
    buscar_y_cargar_icono(ayuda_window)
    
    help_text = """
CALCULADORA DE FACTOR DE REDUCCIÓN DE CARGA VIVA

ALGORITMO:
• Pisos superiores (n-4 a n): r = 1.0
• Zona intermedia (n-5 a n-8): r = 1.0 + 0.1*(i-n+4)
• Pisos inferiores (1 a n-9): r = 0.5

USO:
1. Ingrese número de pisos
2. Presione "Calcular"
3. Use "Exportar TXT" para generar reporte
4. Seleccione carpeta de destino

⚠️ IMPORTANTE:
Verificar siempre la aplicabilidad de los resultados
con un profesional calificado.
"""
    
    text_widget = tk.Text(ayuda_window, wrap=tk.WORD, padx=20, pady=20)
    text_widget.pack(fill=tk.BOTH, expand=True)
    text_widget.insert(tk.END, help_text)
    text_widget.config(state=tk.DISABLED)


# Mostrar disclaimer inicial (REMOVIDO - reemplazado por splash screen)
# def mostrar_disclaimer():
#     result = messagebox.askokcancel(
#         "⚠️ DISCLAIMER IMPORTANTE", 
#         "Es responsabilidad del usuario verificar que los datos "
#         "generados por este software son correctos.\n\n"
#         "¿Acepta continuar bajo su responsabilidad?"
#     )
#     return result


# Mostrar splash screen primero
mostrar_splash_screen()

# Crear ventana principal
root = tk.Tk()
root.title("Calculadora de Factor de Reducción v2.0")
root.geometry("600x550")

# Buscar y configurar icono principal - REEMPLAZA LA PLUMILLA
print("\n🔍 Configurando icono principal...")
icono_cargado = buscar_y_cargar_icono(root)

if icono_cargado:
    print("🎉 ¡Icono personalizado cargado! La plumilla ha sido reemplazada.")
else:
    print("🖼️ Se mantiene icono predeterminado (plumilla) de tkinter.")

# Crear menú
menubar = Menu(root)
root.config(menu=menubar)

# Menú Archivo
file_menu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="📁 Archivo", menu=file_menu)
file_menu.add_command(label="📄 Exportar TXT", command=exportar_a_txt)
file_menu.add_separator()
file_menu.add_command(label="❌ Salir", command=root.quit)

# Menú Ayuda
help_menu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="❓ Ayuda", menu=help_menu)
help_menu.add_command(label="📖 Cómo usar", command=mostrar_ayuda)

# Frame principal
main_frame = ttk.Frame(root, padding="15")
main_frame.pack(fill=tk.BOTH, expand=True)

# Título
title_label = ttk.Label(main_frame, text="Calculadora de Factor de Reducción v2.0", 
                       font=("Arial", 14, "bold"))
title_label.pack(pady=(0, 20))

# Frame para input
input_frame = ttk.Frame(main_frame)
input_frame.pack(fill=tk.X, pady=(0, 20))

ttk.Label(input_frame, text="Número de pisos:").pack(side=tk.LEFT)
entry_pisos = ttk.Entry(input_frame, width=10)
entry_pisos.pack(side=tk.LEFT, padx=(5, 10))
entry_pisos.insert(0, "10")

ttk.Button(input_frame, text="Calcular", command=calcular_y_mostrar).pack(side=tk.LEFT, padx=(0, 5))
ttk.Button(input_frame, text="Exportar TXT", command=exportar_a_txt).pack(side=tk.LEFT)

# Tabla de resultados
columns = ('Piso', 'Factor', 'Criterio')
tree = ttk.Treeview(main_frame, columns=columns, show='headings', height=12)

for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=120, anchor='center')

tree.pack(fill=tk.BOTH, expand=True, pady=(0, 15))

# Scrollbar
scrollbar = ttk.Scrollbar(tree, orient=tk.VERTICAL, command=tree.yview)
tree.configure(yscrollcommand=scrollbar.set)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Información
info_label = ttk.Label(main_frame, 
                      text="⚠️ Verificar siempre los resultados con un profesional calificado",
                      font=("Arial", 9), foreground="red")
info_label.pack(pady=(10, 0))

# Calcular automáticamente
calcular_y_mostrar()

# Ejecutar aplicación
root.mainloop()