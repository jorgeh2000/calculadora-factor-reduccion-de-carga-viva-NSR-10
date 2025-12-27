import tkinter as tk
from tkinter import ttk, messagebox, filedialog, Menu
import pandas as pd
from datetime import datetime
import os


class FactorReduccionGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora de Factor de Reducción de Carga Viva v2.0")
        self.root.geometry("850x700")
        
        # Configurar icono
        try:
            self.root.iconbitmap("E:\\PROYECTOS PYTHON\\LOGO 4D-ROTULO.ico")
        except:
            pass  # Si no se encuentra el icono, usar el predeterminado
        
        # Variables
        self.num_pisos = tk.IntVar(value=10)
        
        self.crear_menu()
        self.crear_widgets()
    
    def crear_menu(self):
        """Crear menú ribbon"""
        menubar = Menu(self.root)
        self.root.config(menu=menubar)
        
        # Menú Archivo
        file_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="📁 Archivo", menu=file_menu)
        file_menu.add_command(label="📤 Exportar TXT", command=self.exportar_txt)
        file_menu.add_command(label="📊 Exportar CSV", command=self.exportar_csv)
        file_menu.add_separator()
        file_menu.add_command(label="❌ Salir", command=self.root.quit)
        
        # Menú Ayuda
        help_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="📚 Ayuda", menu=help_menu)
        help_menu.add_command(label="📖 Funcionalidad y Uso", command=self.mostrar_ayuda)
        help_menu.add_separator()
        help_menu.add_command(label="ℹ️ Acerca de", command=self.mostrar_acerca_de)
    
    def mostrar_ayuda(self):
        """Muestra ventana de ayuda detallada"""
        ayuda_window = tk.Toplevel(self.root)
        ayuda_window.title("Ayuda y Funcionalidad Avanzada")
        ayuda_window.geometry("800x600")
        ayuda_window.configure(bg='white')
        
        # Configurar icono
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
        
        # Contenido de ayuda avanzada
        help_text = """
🏗️ CALCULADORA AVANZADA DE FACTOR DE REDUCCIÓN DE CARGA VIVA

📋 FUNCIONALIDADES AVANZADAS:
• Cálculos automáticos con validaciones
• Exportación en múltiples formatos (TXT y CSV)
• Reportes detallados con estadísticas
• Selección libre de carpeta destino
• Interfaz profesional con tablas organizadas

📐 ALGORITMO TÉCNICO:
Para un edificio de 'n' pisos:

1. PISOS SUPERIORES (i = n-4 hasta i = n):
   • Factor: r_i = 1.0
   • Aplicación: 5 pisos más altos
   • Justificación: Carga viva completa en niveles superiores

2. ZONA INTERMEDIA (i = n-5 hasta i = n-8):
   • Factor: r_i = 1.0 + 0.1 × (i - n + 4)
   • Aplicación: Siguientes 4 pisos hacia abajo
   • Justificación: Reducción progresiva según distancia del techo

3. PISOS INFERIORES (i = 1 hasta i = n-9):
   • Factor: r_i = 0.5
   • Aplicación: Resto de pisos hacia la base
   • Justificación: Máxima reducción en niveles de cimentación

🎯 USO PASO A PASO:
1. 🔢 Ingrese número total de pisos
2. 📊 Presione "Calcular Factores" (automático)
3. 👀 Revise resultados en tabla organizada
4. 📤 Use "Exportar TXT" para reporte completo
5. 📊 Use "Exportar CSV" para análisis de datos
6. 📁 Seleccione carpeta de destino

📊 REPORTES GENERADOS:

📋 REPORTE TXT:
• Algoritmo explicado paso a paso
• Tabla detallada con fórmulas aplicadas
• Resumen estadístico completo
• Conteo por categorías de pisos
• Factor máximo, mínimo y promedio
• Formato profesional para documentación

📈 REPORTE CSV:
• Datos estructurados para análisis
• Compatible con Excel y herramientas de análisis
• Fácil importación a otros sistemas

🔍 VALIDACIONES IMPLEMENTADAS:
• Número de pisos mayor a cero
• Valores numéricos válidos
• Verificación de permisos de escritura
• Control de errores en exportación

💾 CARACTERÍSTICAS TÉCNICAS:
• Interfaz responsiva con tkinter
• Codificación UTF-8 para caracteres especiales
• Timestamps únicos para evitar sobrescritura
• Manejo robusto de excepciones

⚠️ RESPONSABILIDAD PROFESIONAL:
Este software es una HERRAMIENTA DE APOYO al cálculo.
• Verificar aplicabilidad según normativas locales
• Validar resultados con ingeniero estructural
• Considerar condiciones particulares del proyecto
• Revisar códigos de construcción vigentes

📞 SOPORTE TÉCNICO:
Para consultas sobre interpretación de resultados o 
aplicación en proyectos específicos, consulte con 
profesionales calificados en ingeniería estructural.
"""
        
        text_label = tk.Label(scrollable_frame, text=help_text, 
                             font=("Arial", 11), justify='left', 
                             bg='white', padx=25, pady=25)
        text_label.pack(fill=tk.BOTH, expand=True)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
    
    def mostrar_acerca_de(self):
        """Muestra información acerca de la aplicación"""
        messagebox.showinfo(
            "Acerca de", 
            "Calculadora de Factor de Reducción de Carga Viva v2.0\n\n" +
            "Versión Profesional con funcionalidades avanzadas\n\n" +
            "Características:\n" +
            "• Cálculos automáticos\n" +
            "• Exportación TXT y CSV\n" +
            "• Reportes con estadísticas\n" +
            "• Interfaz profesional\n\n" +
            "⚠️ Verificar siempre la aplicabilidad de los resultados\n" +
            "según las normativas locales vigentes."
        )
    
    def crear_widgets(self):
        # Frame principal
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configurar grid
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        
        # Título
        title_label = ttk.Label(main_frame, text="Factor de Reducción de Carga Viva", 
                               font=("Arial", 16, "bold"))
        title_label.grid(row=0, column=0, columnspan=3, pady=(0, 20))
        
        # Input para número de pisos
        ttk.Label(main_frame, text="Número de pisos (n):").grid(row=1, column=0, sticky=tk.W, pady=5)
        pisos_entry = ttk.Entry(main_frame, textvariable=self.num_pisos, width=10)
        pisos_entry.grid(row=1, column=1, sticky=tk.W, padx=(10, 0), pady=5)
        
        # Botón calcular
        calc_btn = ttk.Button(main_frame, text="Calcular Factores", command=self.calcular_factores)
        calc_btn.grid(row=1, column=2, padx=(10, 0), pady=5)
        
        # Frame para la tabla
        table_frame = ttk.LabelFrame(main_frame, text="Factores de Reducción por Piso", padding="10")
        table_frame.grid(row=2, column=0, columnspan=3, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(20, 0))
        main_frame.rowconfigure(2, weight=1)
        
        # Treeview para mostrar resultados
        self.tree = ttk.Treeview(table_frame, columns=('Factor', 'Criterio'), show='tree headings')
        self.tree.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configurar columnas
        self.tree.column('#0', width=100, anchor='center')
        self.tree.column('Factor', width=150, anchor='center')
        self.tree.column('Criterio', width=400, anchor='w')
        
        # Encabezados
        self.tree.heading('#0', text='Piso')
        self.tree.heading('Factor', text='Factor (r_i)')
        self.tree.heading('Criterio', text='Criterio Aplicado')
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(table_frame, orient=tk.VERTICAL, command=self.tree.yview)
        scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))
        self.tree.configure(yscrollcommand=scrollbar.set)
        
        # Configurar grid del table_frame
        table_frame.columnconfigure(0, weight=1)
        table_frame.rowconfigure(0, weight=1)
        
        # Frame para información del algoritmo
        info_frame = ttk.LabelFrame(main_frame, text="Algoritmo", padding="10")
        info_frame.grid(row=3, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(10, 0))
        
        # Texto explicativo
        info_text = """Algoritmo de Factor de Reducción:
• Pisos n-4 a n (5 pisos superiores): r_i = 1.0
• Pisos n-5 a n-8 (4 pisos): r_i = 1.0 + 0.1*(i - n + 4)
• Pisos 1 a n-9 (resto): r_i = 0.5"""
        
        info_label = ttk.Label(info_frame, text=info_text, justify=tk.LEFT)
        info_label.grid(row=0, column=0, sticky=tk.W)
        
        # Botones de exportación
        export_frame = ttk.Frame(main_frame)
        export_frame.grid(row=4, column=0, columnspan=3, pady=(10, 0), sticky=tk.W)
        
        ttk.Button(export_frame, text="Exportar CSV", command=self.exportar_csv).pack(side=tk.LEFT)
        ttk.Button(export_frame, text="Exportar TXT", command=self.exportar_txt).pack(side=tk.LEFT, padx=(10, 0))
        
        # Calcular automáticamente al inicio
        self.calcular_factores()
    
    def calcular_factor_reduccion(self, i, n):
        """
        Calcula el factor de reducción para el piso i de un edificio de n pisos
        
        Args:
            i: número del piso (1 = planta baja)
            n: número total de pisos
        
        Returns:
            tuple: (factor_reduccion, criterio_aplicado)
        """
        if i >= n - 4:  # Los 5 pisos superiores (n-4 a n)
            return 1.0, f"Piso superior (i >= n-4): r_i = 1.0"
        elif i >= n - 8:  # Pisos n-5 a n-8 (4 pisos)
            factor = 1.0 + 0.1 * (i - n + 4)
            return factor, f"Zona intermedia (n-8 <= i < n-4): r_i = 1.0 + 0.1*(i-n+4) = 1.0 + 0.1*({i}-{n}+4)"
        else:  # Pisos 1 a n-9
            return 0.5, f"Piso inferior (i < n-8): r_i = 0.5"
    
    def calcular_factores(self):
        try:
            n = self.num_pisos.get()
            
            if n < 1:
                messagebox.showerror("Error", "El número de pisos debe ser mayor a 0")
                return
            
            # Limpiar tabla
            for item in self.tree.get_children():
                self.tree.delete(item)
            
            # Calcular factores para cada piso
            self.resultados = []
            for i in range(n, 0, -1):  # De arriba hacia abajo
                factor, criterio = self.calcular_factor_reduccion(i, n)
                self.resultados.append({
                    'Piso': i,
                    'Factor': factor,
                    'Criterio': criterio
                })
                
                # Insertar en la tabla
                self.tree.insert('', 'end', 
                               text=f'{i}',
                               values=(f'{factor:.3f}', criterio))
            
        except Exception as e:
            messagebox.showerror("Error", f"Error en el cálculo: {str(e)}")
    
    def exportar_csv(self):
        try:
            if not hasattr(self, 'resultados') or not self.resultados:
                messagebox.showwarning("Advertencia", "No hay resultados para exportar")
                return
            
            # Selector de carpeta
            carpeta_destino = filedialog.askdirectory(
                title="Seleccionar carpeta para guardar el archivo CSV",
                initialdir="e:\\PROYECTOS PYTHON\\SCRIPTS\\REDUCCION DE CARGA VIVA"
            )
            
            if not carpeta_destino:  # Usuario canceló
                return
            
            df = pd.DataFrame(self.resultados)
            filename = f"factores_reduccion_{self.num_pisos.get()}_pisos_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
            filepath = os.path.join(carpeta_destino, filename)
            
            df.to_csv(filepath, index=False, encoding='utf-8-sig')
            messagebox.showinfo("Éxito", f"Archivo CSV exportado exitosamente:\n{filepath}")
            
        except Exception as e:
            messagebox.showerror("Error", f"Error al exportar CSV: {str(e)}")
    
    def exportar_txt(self):
        try:
            if not hasattr(self, 'resultados') or not self.resultados:
                messagebox.showwarning("Advertencia", "No hay resultados para exportar")
                return
            
            # Selector de carpeta
            carpeta_destino = filedialog.askdirectory(
                title="Seleccionar carpeta para guardar el reporte TXT",
                initialdir="e:\\PROYECTOS PYTHON\\SCRIPTS\\REDUCCION DE CARGA VIVA"
            )
            
            if not carpeta_destino:  # Usuario canceló
                return
            
            n = self.num_pisos.get()
            
            # Generar contenido del archivo
            contenido = []
            contenido.append("="*70)
            contenido.append("           REPORTE DE FACTORES DE REDUCCIÓN")
            contenido.append("                   DE CARGA VIVA")
            contenido.append("="*70)
            contenido.append(f"Fecha de generación: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
            contenido.append(f"Número de pisos del edificio: {n}")
            contenido.append("")
            
            # Algoritmo detallado
            contenido.append("ALGORITMO UTILIZADO:")
            contenido.append("-" * 20)
            contenido.append("Para un edificio de 'n' pisos, el factor de reducción r_i")
            contenido.append("para el piso 'i' se calcula aplicando las siguientes reglas:")
            contenido.append("")
            contenido.append("1. PISOS SUPERIORES (i = n-4 a i = n):")
            contenido.append("   • Se aplica a los 5 pisos más altos del edificio")
            contenido.append("   • Factor de reducción: r_i = 1.0")
            contenido.append("   • Justificación: Carga completa en niveles superiores")
            contenido.append("")
            contenido.append("2. ZONA INTERMEDIA (i = n-5 a i = n-8):")
            contenido.append("   • Se aplica a los siguientes 4 pisos")
            contenido.append("   • Factor de reducción: r_i = 1.0 + 0.1*(i - n + 4)")
            contenido.append("   • Justificación: Reducción gradual según altura")
            contenido.append("")
            contenido.append("3. PISOS INFERIORES (i = 1 a i = n-9):")
            contenido.append("   • Se aplica al resto de pisos hacia abajo")
            contenido.append("   • Factor de reducción: r_i = 0.5")
            contenido.append("   • Justificación: Máxima reducción en niveles inferiores")
            contenido.append("")
            
            # Resultados detallados
            contenido.append("RESULTADOS CALCULADOS:")
            contenido.append("-" * 22)
            contenido.append(f"{'Piso':<6} | {'Factor':<8} | {'Categoria':<18} | {'Fórmula Aplicada':<30}")
            contenido.append("-" * 70)
            
            for resultado in self.resultados:
                piso = resultado['Piso']
                factor = resultado['Factor']
                
                # Determinar categoría y fórmula
                if piso >= n - 4:
                    categoria = "Piso Superior"
                    formula = "r = 1.0"
                elif piso >= n - 8:
                    categoria = "Zona Intermedia"
                    formula = f"r = 1.0+0.1*({piso}-{n}+4) = {factor:.3f}"
                else:
                    categoria = "Piso Inferior"
                    formula = "r = 0.5"
                
                contenido.append(f"{piso:<6} | {factor:<8.3f} | {categoria:<18} | {formula:<30}")
            
            # Resumen estadístico
            factores = [r['Factor'] for r in self.resultados]
            contenido.append("")
            contenido.append("RESUMEN ESTADÍSTICO:")
            contenido.append("-" * 19)
            contenido.append(f"Factor máximo: {max(factores):.3f}")
            contenido.append(f"Factor mínimo: {min(factores):.3f}")
            contenido.append(f"Factor promedio: {sum(factores)/len(factores):.3f}")
            contenido.append(f"Pisos con factor 1.0: {sum(1 for f in factores if f == 1.0)}")
            contenido.append(f"Pisos con factor 0.5: {sum(1 for f in factores if f == 0.5)}")
            contenido.append(f"Pisos con factor variable: {sum(1 for f in factores if 0.5 < f < 1.0)}")
            
            contenido.append("")
            contenido.append("="*70)
            contenido.append("Reporte generado por: Calculadora de Factor de Reducción v2.0")
            contenido.append("Desarrollado para análisis de carga viva en edificaciones")
            
            # Guardar archivo
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            filename = f"reporte_detallado_{n}_pisos_{timestamp}.txt"
            filepath = os.path.join(carpeta_destino, filename)
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write('\n'.join(contenido))
            
            messagebox.showinfo("Éxito", f"Reporte TXT exportado exitosamente:\n{filepath}")
            
        except Exception as e:
            messagebox.showerror("Error", f"Error al exportar TXT: {str(e)}")


def mostrar_splash_screen():
    """Muestra la pantalla de splash con disclaimer profesional"""
    splash = tk.Toplevel()
    splash.title("")
    splash.geometry("600x500")
    splash.configure(bg='#2c3e50')
    splash.resizable(False, False)
    
    # Configurar icono
    try:
        splash.iconbitmap("E:\\PROYECTOS PYTHON\\LOGO 4D-ROTULO.ico")
    except:
        pass
    
    # Frame principal
    main_frame = tk.Frame(splash, bg='#2c3e50', padx=40, pady=40)
    main_frame.pack(fill=tk.BOTH, expand=True)
    
    # Título principal
    title_label = tk.Label(main_frame, text="CALCULADORA PROFESIONAL\nDE FACTOR DE REDUCCIÓN\nDE CARGA VIVA", 
                          font=("Arial", 18, "bold"), fg='white', bg='#2c3e50', justify='center')
    title_label.pack(pady=(0, 10))
    
    # Versión
    version_label = tk.Label(main_frame, text="Versión 2.0 - Edición Profesional", 
                            font=("Arial", 12), fg='#ecf0f1', bg='#2c3e50')
    version_label.pack(pady=(0, 30))
    
    # Disclaimer prominente
    disclaimer_frame = tk.Frame(main_frame, bg='#e74c3c', relief='solid', bd=3)
    disclaimer_frame.pack(fill=tk.X, pady=(0, 20))
    
    disclaimer_title = tk.Label(disclaimer_frame, text="⚠️ RESPONSABILIDAD PROFESIONAL - DISCLAIMER", 
                               font=("Arial", 14, "bold"), fg='white', bg='#e74c3c')
    disclaimer_title.pack(pady=(15, 10))
    
    disclaimer_text = """Es RESPONSABILIDAD EXCLUSIVA del usuario verificar que 
los datos generados por este software son CORRECTOS y 
APLICABLES a su caso específico. 

El desarrollador NO se hace responsable por:
• Errores en cálculos o interpretaciones
• Decisiones basadas en los resultados
• Cumplimiento con normativas locales

Consulte SIEMPRE con un ingeniero estructural calificado."""
    
    disclaimer_label = tk.Label(disclaimer_frame, text=disclaimer_text, 
                               font=("Arial", 11), fg='white', bg='#e74c3c', 
                               justify='left', wraplength=500)
    disclaimer_label.pack(pady=(0, 15), padx=20)
    
    # Botón continuar
    continue_btn = tk.Button(main_frame, text="Acepto y Continuar", 
                            font=("Arial", 14, "bold"), 
                            command=splash.destroy,
                            bg='#27ae60', fg='white', 
                            relief='flat', padx=40, pady=12)
    continue_btn.pack()
    
    # Auto-cerrar después de 6 segundos
    splash.after(6000, splash.destroy)
    
    return splash


def main():
    # Crear ventana principal (oculta inicialmente)
    root = tk.Tk()
    root.withdraw()  # Ocultar mientras se muestra splash
    
    # Mostrar splash screen
    splash = mostrar_splash_screen()
    
    def mostrar_ventana_principal():
        """Mostrar la ventana principal después del splash"""
        root.deiconify()  # Mostrar ventana principal
    
    # Auto mostrar ventana principal después de 6 segundos
    root.after(6000, mostrar_ventana_principal)
    
    # Crear la aplicación
    app = FactorReduccionGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()