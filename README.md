# Calculadora de Factor de Reducción de Carga Viva

## Descripción
Este proyecto implementa un algoritmo para calcular factores de reducción de carga viva en edificios según el número de pisos.

## Algoritmo Implementado
Para un edificio de **n** pisos, el factor de reducción **r_i** para el piso **i** se calcula según:

- **Pisos superiores** (i = n-4 a i = n): `r_i = 1.0` (5 pisos superiores)
- **Zona intermedia** (i = n-5 a i = n-8): `r_i = 1.0 + 0.1*(i - n + 4)` (4 pisos)
- **Pisos inferiores** (i = 1 a i = n-9): `r_i = 0.5` (resto de pisos)

## Archivos

### `version_simple.py`
Versión básica con interfaz profesional:
- **Splash screen con disclaimer de responsabilidad**
- **Icono personalizado (si está disponible)**
- **Menú ribbon con ayuda integrada**
- Interfaz simple pero profesional con tkinter
- Cálculo automático
- Tabla de resultados clara
- **Selector de carpeta para exportar TXT**
- **Exportación a archivo TXT con reporte completo**
- **Recomendado para uso general**

### `reduccion_carga_viva.py`
Versión completa con funcionalidades avanzadas:
- **Todas las funcionalidades de la versión simple PLUS:**
- **Splash screen profesional más detallado**
- **Ayuda avanzada con documentación completa**
- Interfaz más elaborada y profesional
- **Selector de carpeta para ambas exportaciones**
- Exportación a CSV y TXT
- **Reporte TXT detallado con estadísticas avanzadas**
- Información detallada del criterio aplicado
- **Validaciones y manejo robusto de errores**

## Requisitos
- Python 3.7 o superior
- tkinter (incluido por defecto en Python)
- pandas (solo para la versión completa)

## Instalación
```bash
# Instalar pandas (solo para versión completa)
pip install pandas
```

## Configuración del Icono

Para usar el icono personalizado:
1. Asegúrese de que el archivo `LOGO 4D-ROTULO.ico` esté en `E:\PROYECTOS PYTHON\`
2. Si no se encuentra, la aplicación usará el icono predeterminado de Windows
3. El icono se aplica tanto a la ventana principal como a ventanas de ayuda

## Funcionalidades de Seguridad

### Disclaimer de Responsabilidad:
- **Aparece obligatoriamente** al iniciar cualquier versión
- **Recordatorio importante**: Verificar siempre la aplicabilidad
- **Responsabilidad del usuario**: Validar con profesional calificado
- **Auto-cierre**: Se cierra automáticamente después de algunos segundos

### Validaciones Implementadas:
- Verificación de números válidos
- Control de permisos de escritura
- Manejo de errores en exportación
- Selección de carpeta válida

## Uso

### Ejecutar versión simple:
```bash
python version_simple.py
```

### Ejecutar versión completa:
```bash
python reduccion_carga_viva.py
```

## 📊 **Nuevo Formato de Reporte TXT v2.0**

### ✨ **Mejoras Implementadas:**
- ✅ **Tabla ASCII profesional** idéntica a la ventana principal
- ✅ **Bordes estructurados** con caracteres Unicode para mejor presentación
- ✅ **Columnas organizadas**: Piso | Factor | Criterio | Observaciones
- ✅ **Ecuaciones matemáticas detalladas** con símbolos apropiados
- ✅ **Referencias normativas** completas y actualizadas
- ✅ **Variables explicadas** con definiciones claras
- ✅ **Disclaimer profesional** expandido con responsabilidades específicas

### 📐 **Ecuaciones Incluidas:**
1. **Pisos Superiores**: `r_i = 1.0` (para i ≥ n-4)
2. **Zona Intermedia**: `r_i = 1.0 + 0.1 × (i - n + 4)` (para n-8 ≤ i < n-4)  
3. **Pisos Inferiores**: `r_i = 0.5` (para i < n-8)

### 📚 **Referencias Normativas Incluidas:**
- Código de Construcción vigente
- Norma de Diseño Sísmico y Cargas
- Reglamento de Construcciones locales
- ASCE 7 - Minimum Design Loads (referencia internacional)
- Normas técnicas de ingeniería estructural

### 📋 **Variables Definidas:**
- **n**: Número total de pisos del edificio
- **i**: Número del piso analizado (1 = planta baja)
- **r_i**: Factor de reducción para el piso i

## Ejemplo de Uso
1. **Al iniciar**: Se muestra splash screen con disclaimer importante
2. **Interfaz principal**: Ingrese el número de pisos del edificio
3. **Cálculo**: Haga clic en "Calcular" (o automático)
4. **Resultados**: Observe los factores en la tabla organizada
5. **Exportar TXT**: 
   - Haga clic en "Exportar TXT"
   - **Seleccione la carpeta destino**
   - Reporte completo se guarda automáticamente
6. **Ayuda**: Use el menú "📚 Ayuda" para información detallada
7. (Versión completa) **Exportar CSV** con selección de carpeta

## 🆕 Nuevas Funcionalidades v2.0

### 🚀 Mejoras de Interfaz:
- **Splash Screen**: Pantalla inicial con disclaimer de responsabilidad
- **Icono Personalizado**: Soporte para LOGO 4D-ROTULO.ico
- **Menú Ribbon**: Navegación profesional con pestañas organizadas
- **Ayuda Integrada**: Documentación completa desde la aplicación

### 📁 Exportación Mejorada:
- **Selector de Carpeta**: Elige dónde guardar tus reportes
- **Nombres Únicos**: Timestamps automáticos evitan sobrescritura
- **Múltiples Formatos**: TXT detallado y CSV para análisis

### ⚖️ Responsabilidad Profesional:
- **Disclaimer Prominente**: Recordatorio de verificación independiente
- **Documentación Clara**: Limitaciones y responsabilidades explicadas
- **Uso Profesional**: Herramienta de apoyo, no substituto de criterio ingenieril

## Características de los Reportes TXT

### Versión Simple:
- **Splash con disclaimer** al iniciar
- **Selector de carpeta** para elegir ubicación
- Información del algoritmo utilizado detallada
- Tabla completa con factores y cálculos paso a paso
- Fecha y hora de generación
- **Menú de ayuda integrado**
- Formato legible para impresión
- **Timestamps únicos** para evitar sobrescritura

### Versión Completa:
- **Todo lo de la versión simple PLUS:**
- **Splash screen profesional** más elaborado
- **Ayuda avanzada** con documentación técnica completa
- Resumen estadístico completo y detallado
- Análisis de distribución de factores por categorías
- Información técnica detallada con justificaciones
- **Manejo robusto de errores** y validaciones
- **Exportación dual** (TXT y CSV) con selector de carpeta
- Formato profesional para documentación técnica

## Ejemplo de Resultados
Para un edificio de 10 pisos:
```
Piso 10: r = 1.000 (Piso superior)
Piso  9: r = 1.000 (Piso superior) 
Piso  8: r = 1.000 (Piso superior)
Piso  7: r = 1.000 (Piso superior)
Piso  6: r = 1.000 (Piso superior)
Piso  5: r = 0.900 (Zona intermedia)
Piso  4: r = 0.800 (Zona intermedia)
Piso  3: r = 0.700 (Zona intermedia)
Piso  2: r = 0.600 (Zona intermedia)
Piso  1: r = 0.500 (Piso inferior)
```