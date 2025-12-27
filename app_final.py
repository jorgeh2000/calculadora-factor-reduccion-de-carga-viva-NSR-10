import tkinter as tk
from tkinter import ttk, messagebox, filedialog, Menu
from datetime import datetime
import os


def buscar_y_cargar_icono(ventana):
    """Busca el icono en múltiples ubicaciones y lo carga"""
    posibles_rutas = [
        "E:\\PROYECTOS PYTHON\\LOGO 4D-ROTULO.ico",
        os.path.join(os.path.dirname(__file__), "LOGO 4D-ROTULO.ico"),
        "LOGO 4D-ROTULO.ico"
    ]
    
    for ruta in posibles_rutas:
        if os.path.exists(ruta):
            try:
                ventana.iconbitmap(ruta)
                return True
            except:
                continue
    return False


def calcular_factor_reduccion(i, n):
    """Calcula el factor de reducción para el piso i de un edificio de n pisos"""
    if i >= n - 4:
        return 1.0
    elif i >= n - 8:
        return 1.0 + 0.1 * (i - n + 4)
    else:
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
        
        if not carpeta_destino:
            return
        
        # Generar contenido del archivo
        contenido = []
        contenido.append("REPORTE DE FACTORES DE REDUCCIÓN DE CARGA VIVA")
        contenido.append("="*60)
        contenido.append("")
        contenido.append(f"Fecha de generación: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
        contenido.append(f"Número de pisos del edificio: {n}")
        contenido.append("")
        
        # Tabla simple con tabulaciones
        contenido.append("TABLA DE RESULTADOS:")
        contenido.append("")
        contenido.append("Piso\tFactor\tCriterio\tObservaciones")
        
        for i in range(n, 0, -1):
            factor = calcular_factor_reduccion(i, n)
            
            if i >= n - 4:
                criterio = "Superior"
                observacion = "Sin reducción"
            elif i >= n - 8:
                criterio = "Intermedio"
                observacion = f"r = 1.0+0.1*({i}-{n}+4) = {factor:.3f}"
            else:
                criterio = "Inferior"
                observacion = "Reducción máxima"
            
            contenido.append(f"{i}\t{factor:.3f}\t{criterio}\t{observacion}")
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
        contenido.append("REFERENCIAS NORMATIVAS:")
        contenido.append("-" * 24)
        contenido.append("• Código de Construcción vigente")
        contenido.append("• Norma de Diseño Sísmico y Cargas")
        contenido.append("• Reglamento de Construcciones locales")
        contenido.append("• ASCE 7 - Minimum Design Loads (referencia internacional)")
        contenido.append("• Normas técnicas de ingeniería estructural")
        contenido.append("")
        contenido.append("VARIABLES UTILIZADAS:")
        contenido.append("-" * 21)
        contenido.append("• n  = Número total de pisos del edificio")
        contenido.append("• i  = Número del piso analizado (1 = planta baja)")
        contenido.append("• r_i = Factor de reducción para el piso i")
        contenido.append("")
        contenido.append("DISCLAIMER PROFESIONAL:")
        contenido.append("-" * 23)
        contenido.append("Es RESPONSABILIDAD del usuario verificar que:")
        contenido.append("• Los factores calculados son aplicables a su proyecto")
        contenido.append("• Se cumplen las normativas locales vigentes")
        contenido.append("• Los resultados son validados por un profesional calificado")
        contenido.append("• Se consideran las condiciones específicas del edificio")
        contenido.append("")
        contenido.append("Consulte SIEMPRE con un ingeniero estructural calificado")
        
        # Guardar archivo
        filename = f"reporte_factores_{n}_pisos_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        filepath = os.path.join(carpeta_destino, filename)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write('\\n'.join(contenido))
        
        messagebox.showinfo("Éxito", f"Reporte exportado exitosamente:\\n{filepath}")
        
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
        for i in range(n, 0, -1):
            factor = calcular_factor_reduccion(i, n)
            
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
    ayuda_window = tk.Toplevel(root)
    ayuda_window.title("Ayuda")
    ayuda_window.geometry("600x400")
    buscar_y_cargar_icono(ayuda_window)
    
    help_text = """
CALCULADORA DE FACTOR DE REDUCCIÓN DE CARGA VIVA v2.0

ALGORITMO:
• Pisos superiores (n-4 a n): r = 1.0
• Zona intermedia (n-5 a n-8): r = 1.0 + 0.1*(i-n+4)
• Pisos inferiores (1 a n-9): r = 0.5

USO:
1. Ingrese número de pisos
2. Presione "Calcular" 
3. Use "Exportar TXT" para generar reporte
4. Seleccione carpeta de destino

FUNCIONALIDADES:
• Cálculo automático
• Exportación con selector de carpeta
• Icono personalizado (reemplaza plumilla)
• Menú de ayuda integrado
• Disclaimer de responsabilidad

⚠️ IMPORTANTE:
Verificar siempre la aplicabilidad de los resultados
con un profesional calificado.
"""
    
    text_widget = tk.Text(ayuda_window, wrap=tk.WORD, padx=20, pady=20)
    text_widget.pack(fill=tk.BOTH, expand=True)
    text_widget.insert(tk.END, help_text)
    text_widget.config(state=tk.DISABLED)


def mostrar_splash():
    """Mostrar splash screen simple"""
    result = messagebox.showinfo(
        "Calculadora Factor de Reducción v2.0",
        "⚠️ DISCLAIMER IMPORTANTE ⚠️\\n\\n" +
        "Es responsabilidad del usuario verificar que los datos\\n" +
        "generados por este software son correctos y aplicables.\\n\\n" +
        "El desarrollador no se hace responsable por errores\\n" +
        "en cálculos o decisiones basadas en los resultados.\\n\\n" +
        "Consulte siempre con un profesional calificado."
    )


# Crear ventana principal
root = tk.Tk()
root.title("Calculadora de Factor de Reducción v2.0")
root.geometry("600x550")

# Configurar icono - REEMPLAZA LA PLUMILLA
icono_cargado = buscar_y_cargar_icono(root)
if icono_cargado:
    print("✅ Icono personalizado cargado - plumilla reemplazada")
else:
    print("ℹ️  Usando icono predeterminado")

# Mostrar splash/disclaimer al inicio
mostrar_splash()

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
help_menu.add_separator()
help_menu.add_command(label="ℹ️ Acerca de", command=lambda: messagebox.showinfo(
    "Acerca de",
    "Calculadora de Factor de Reducción v2.0\\n\\n" +
    "Características:\\n" +
    "• Splash screen con disclaimer\\n" +
    "• Icono personalizado (sin plumilla)\\n" +
    "• Exportación con selector de carpeta\\n" +
    "• Interfaz profesional\\n\\n" +
    "⚠️ Verificar siempre resultados con profesional calificado"
))

# Frame principal
main_frame = ttk.Frame(root, padding="15")
main_frame.pack(fill=tk.BOTH, expand=True)

# Título
title_label = ttk.Label(main_frame, text="🏗️ Calculadora de Factor de Reducción v2.0", 
                       font=("Arial", 14, "bold"))
title_label.pack(pady=(0, 20))

# Frame para input
input_frame = ttk.Frame(main_frame)
input_frame.pack(fill=tk.X, pady=(0, 20))

ttk.Label(input_frame, text="Número de pisos:").pack(side=tk.LEFT)
entry_pisos = ttk.Entry(input_frame, width=10)
entry_pisos.pack(side=tk.LEFT, padx=(5, 10))
entry_pisos.insert(0, "10")

ttk.Button(input_frame, text="🔢 Calcular", command=calcular_y_mostrar).pack(side=tk.LEFT, padx=(0, 5))
ttk.Button(input_frame, text="📄 Exportar TXT", command=exportar_a_txt).pack(side=tk.LEFT)

# Tabla de resultados
columns = ('Piso', 'Factor', 'Criterio')
tree = ttk.Treeview(main_frame, columns=columns, show='headings', height=12)

for col in columns:
    tree.heading(col, text=col)
    if col == 'Piso':
        tree.column(col, width=80, anchor='center')
    elif col == 'Factor':
        tree.column(col, width=100, anchor='center')
    else:
        tree.column(col, width=200, anchor='center')

tree.pack(fill=tk.BOTH, expand=True, pady=(0, 15))

# Información
info_frame = ttk.LabelFrame(main_frame, text="ℹ️ Información", padding="10")
info_frame.pack(fill=tk.X, pady=(10, 0))

info_text = """✅ Splash screen con disclaimer  •  🎨 Icono personalizado (sin plumilla)  •  📁 Selector de carpeta"""
info_label = ttk.Label(info_frame, text=info_text, font=("Arial", 9))
info_label.pack()

disclaimer_label = ttk.Label(info_frame, 
                      text="⚠️ Verificar siempre los resultados con un profesional calificado",
                      font=("Arial", 9), foreground="red")
disclaimer_label.pack(pady=(5, 0))

# Calcular automáticamente
calcular_y_mostrar()

print("🚀 Aplicación iniciada correctamente")
print("📋 Funcionalidades implementadas:")
print("   • Splash screen con disclaimer")
print("   • Icono personalizado (reemplaza plumilla)")  
print("   • Selector de carpeta para exportar")
print("   • Menú ribbon completo")

# Ejecutar aplicación
root.mainloop()