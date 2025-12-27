#!/bin/bash
# 🚀 SCRIPT PARA SUBIR A GITHUB - EJECUTAR DESPUÉS DE CREAR EL REPO

echo "🔄 Subiendo calculadora NSR-10 a GitHub..."

# Verificar estado
echo "📊 Estado del repositorio:"
git status

# Hacer el push
echo "🚀 Subiendo archivos..."
git push -u origin main

echo "✅ ¡Listo! Tu proyecto está en:"
echo "🔗 https://github.com/jorgeh2000/calculadora-factor-reduccion-nsr10"

echo ""
echo "📦 El ejecutable estará disponible en:"
echo "🔗 https://github.com/jorgeh2000/calculadora-factor-reduccion-nsr10/blob/main/dist/CalculadoraFactorReduccion_NSR10_v2.2_FINAL.exe"

pause