#!/usr/bin/env python3
"""
Generar ejemplo con la nota importante incluida
"""
from datetime import datetime

def generar_reporte_con_nota(n_pisos):
    """Genera ejemplo del reporte con nota importante"""
    
    def calcular_factor(piso, total_pisos):
        if piso >= total_pisos - 4:
            return 1.0
        elif piso >= total_pisos - 8:
            return 1.0 + 0.1 * (piso - total_pisos + 4)
        else:
            return 0.5
    
    contenido = [
        "=" * 60,
        "         REPORTE DE FACTORES DE REDUCCIÓN",
        "              DE CARGA VIVA",
        "=" * 60,
        f"Fecha: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}",
        f"Número de pisos del edificio: {n_pisos}",
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
    for i in range(n_pisos, 0, -1):
        factor = calcular_factor(i, n_pisos)
        if i >= n_pisos - 4:
            criterio = "Piso superior"
            calculo = "r = 1.0"
        elif i >= n_pisos - 8:
            criterio = "Zona intermedia"
            calculo = f"r = 1.0+0.1*({i}-{n_pisos}+4) = {factor:.3f}"
        else:
            criterio = "Piso inferior"
            calculo = "r = 0.5"
        
        linea = f"{i:<7}| {factor:<9.3f}| {criterio:<21}| {calculo}"
        contenido.append(linea)
    
    # NOTA IMPORTANTE
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
    
    return '\n'.join(contenido)

if __name__ == "__main__":
    # Generar ejemplo
    reporte = generar_reporte_con_nota(8)
    
    print("REPORTE CON NOTA IMPORTANTE:")
    print("=" * 80)
    print(reporte)
    
    # Guardar archivo de ejemplo
    with open("ejemplo_con_nota_importante.txt", 'w', encoding='utf-8') as f:
        f.write(reporte)
    
    print("\n✅ Ejemplo guardado en: ejemplo_con_nota_importante.txt")
    print("📝 La nota importante ahora está incluida en todos los reportes")
    print("⚠️  Especifica claramente: SOLO para columnas y cimentaciones")