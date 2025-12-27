# 🏗️ Calculadora de Factor de Reducción de Carga Viva NSR-10
**Versión 2.2 FINAL - Diciembre 2025**

## 📋 Descripción

Esta aplicación calcula los factores de reducción de carga viva según la norma colombiana NSR-10, sección B.5.4.2. Desarrollada específicamente para ingenieros estructurales que requieren determinar los factores de reducción aplicables en el diseño de columnas y cimentaciones.

## ⚠️ LIMITACIONES CRÍTICAS

### 🔴 APLICACIÓN ESPECÍFICA
Los factores calculados **APLICAN ÚNICAMENTE** para:
- ✅ **COLUMNAS**
- ✅ **CIMENTACIONES** (zapatas, pilotes, etc.)
- ✅ **EDIFICIOS DE 5 PISOS O MÁS**

### ❌ NO APLICABLE PARA:
- Vigas
- Losas
- Muros estructurales
- **Edificios de menos de 5 pisos**
- Otros elementos estructurales

## 🚨 Validaciones de Seguridad Implementadas

1. **Validación de altura del edificio**: La aplicación detecta automáticamente si el edificio tiene menos de 5 pisos y muestra advertencias críticas.

2. **Advertencias en interfaz**: Nota visible permanente en la aplicación sobre las limitaciones de uso.

3. **Advertencias en reportes**: Cada reporte TXT incluye secciones específicas sobre aplicabilidad y limitaciones.

4. **Mensajes de alerta**: Diálogos de advertencia cuando se intenta usar la aplicación fuera de su alcance.

## 🧮 Algoritmo NSR-10 B.5.4.2

Para un edificio de 'n' pisos, el factor de reducción r_i para el piso 'i' se calcula como:

### Pisos superiores (i = n-4 a i = n):
```
r_i = 1.0
```
*Aplicado a los 5 pisos superiores*

### Zona intermedia (i = n-5 a i = n-8):
```
r_i = 1.0 + 0.1 × (i - n + 4)
```

### Pisos inferiores (i = 1 a i = n-9):
```
r_i = 0.5
```

## 🖥️ Características de la Aplicación

- **Interfaz gráfica intuitiva** con tkinter
- **Tabla de resultados** con cálculos detallados por piso
- **Exportación profesional** a archivos TXT con formato estructurado
- **Validaciones automáticas** de entrada
- **Icono corporativo** 4D-ROTULO integrado
- **Reportes profesionales** con toda la información técnica y legal

## 📁 Archivos del Proyecto

- `calculadora_estable.py` - Versión principal de producción
- `calculadora_simple.py` - Versión alternativa con características adicionales
- `calculadora_limpia.py` - Versión mínima para compatibilidad
- `dist/CalculadoraFactorReduccion_NSR10_v2.2_FINAL.exe` - Ejecutable final (11 MB)
- `LOGO 4D-ROTULO.ico` - Icono corporativo

## 🚀 Uso del Ejecutable

1. Ejecute `CalculadoraFactorReduccion_NSR10_v2.2_FINAL.exe`
2. Ingrese el número de pisos del edificio (**mínimo 5**)
3. Haga clic en "Calcular Factores"
4. Revise los resultados en la tabla
5. Use "Exportar a TXT" para generar reportes profesionales

## ⚖️ Responsabilidad Profesional

Esta herramienta es una **ayuda de cálculo** que implementa estrictamente lo establecido en NSR-10 B.5.4.2. El usuario es responsable de:

- Verificar la aplicabilidad de la norma a su proyecto específico
- Confirmar que el edificio cumple los requisitos (≥5 pisos)
- Aplicar los factores únicamente en columnas y cimentaciones
- Realizar las validaciones profesionales correspondientes

## 📜 Referencia Normativa

**NSR-10 (Reglamento Colombiano de Construcción Sismo Resistente)**
- Título B: Cargas
- Capítulo B.5: Cargas Vivas
- Sección B.5.4.2: Factor de Reducción de Carga Viva

## 🏢 Información Corporativa

**Desarrollado por:** 4D ROTULO  
**Versión:** 2.2 FINAL  
**Fecha:** Diciembre 2025  
**Lenguaje:** Python 3.13  
**Framework:** Tkinter  

## 🔧 Desarrollo Técnico

### Requisitos para desarrolladores:
- Python 3.13+
- tkinter (incluido con Python)
- PyInstaller 6.16.0+ (para compilación)

### Estructura del código:
```
calculadora_estable.py
├── Funciones principales
│   ├── calcular_factor() - Implementa NSR-10 B.5.4.2
│   ├── calcular() - Maneja GUI y validaciones
│   └── exportar() - Genera reportes TXT
├── Interfaz GUI
│   ├── Widgets de entrada y resultados
│   ├── Tabla de factores
│   └── Botones de acción
└── Validaciones de seguridad
    ├── Verificación de altura mínima
    ├── Mensajes de advertencia
    └── Notas de aplicabilidad
```

## 📞 Soporte

Para consultas técnicas sobre la implementación de la norma NSR-10 B.5.4.2 o el uso apropiado de esta herramienta, consulte con un ingeniero estructural certificado.

---

**⚠️ IMPORTANTE:** Esta aplicación es una herramienta de cálculo que debe usarse bajo supervisión profesional. Los factores de reducción deben aplicarse únicamente según las limitaciones establecidas en la norma NSR-10 B.5.4.2.