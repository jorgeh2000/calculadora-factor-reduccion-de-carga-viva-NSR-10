#!/usr/bin/env python3
"""
Vista previa del nuevo formato de reporte TXT
"""

from datetime import datetime

def calcular_factor(i, n):
    if i >= n - 4:
        return 1.0
    elif i >= n - 8:
        return 1.0 + 0.1 * (i - n + 4)
    else:
        return 0.5

# Generar ejemplo de reporte con 10 pisos
n = 10
contenido = []
contenido.append("╔" + "═"*70 + "╗")
contenido.append("║" + "REPORTE DE FACTORES DE REDUCCIÓN DE CARGA VIVA".center(70) + "║")
contenido.append("╚" + "═"*70 + "╝")
contenido.append("")
contenido.append(f"📅 Fecha de generación: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
contenido.append(f"🏢 Número de pisos del edificio: {n}")
contenido.append("")
contenido.append("TABLA DE RESULTADOS:")
contenido.append("┌" + "─"*6 + "┬" + "─"*10 + "┬" + "─"*20 + "┬" + "─"*25 + "┐")
contenido.append(f"│{'Piso':^6}│{'Factor':^10}│{'Criterio':^20}│{'Observaciones':^25}│")
contenido.append("├" + "─"*6 + "┼" + "─"*10 + "┼" + "─"*20 + "┼" + "─"*25 + "┤")

for i in range(n, 0, -1):
    factor = calcular_factor(i, n)
    if i >= n - 4:
        criterio = "Superior"
        observacion = "Sin reducción"
    elif i >= n - 8:
        criterio = "Intermedio"
        observacion = f"r = 1.0+0.1*({i}-{n}+4)"
    else:
        criterio = "Inferior"
        observacion = "Reducción máxima"
    
    contenido.append(f"│{i:^6}│{factor:^10.3f}│{criterio:^20}│{observacion:^25}│")

contenido.append("└" + "─"*6 + "┴" + "─"*10 + "┴" + "─"*20 + "┴" + "─"*25 + "┘")
contenido.append("")
contenido.append("📐 ECUACIONES UTILIZADAS:")
contenido.append("• Pisos superiores: r_i = 1.0")
contenido.append("• Zona intermedia: r_i = 1.0 + 0.1 × (i - n + 4)")
contenido.append("• Pisos inferiores: r_i = 0.5")
contenido.append("")
contenido.append("📚 REFERENCIAS NORMATIVAS:")
contenido.append("• Código de Construcción vigente")
contenido.append("• ASCE 7 - Minimum Design Loads")
contenido.append("• Normas técnicas de ingeniería estructural")

print("🎯 VISTA PREVIA DEL NUEVO FORMATO DE REPORTE:")
print("═" * 72)
for linea in contenido:
    print(linea)
print("")
print("✅ El archivo TXT ahora incluye:")
print("   📊 Tabla formateada igual a la ventana principal")
print("   📐 Ecuaciones detalladas del algoritmo")
print("   📚 Referencias normativas completas")
print("   ⚠️  Disclaimer profesional expandido")