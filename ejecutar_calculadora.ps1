# Script de PowerShell para ejecutar la calculadora
# Configuración de encoding
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8

# Obtener directorio del script
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path

Write-Host "🚀 Iniciando Calculadora Factor Reducción NSR-10 B.5.4.2" -ForegroundColor Green
Write-Host "📁 Directorio: $scriptDir" -ForegroundColor Yellow
Write-Host ""

# Cambiar al directorio correcto
Set-Location -Path $scriptDir

# Lista de archivos a intentar ejecutar (en orden de preferencia)
$archivos = @(
    "calculadora_estable.py",
    "calculadora_simple.py", 
    "calculadora_limpia.py"
)

$ejecutado = $false

foreach ($archivo in $archivos) {
    if (Test-Path $archivo) {
        Write-Host "▶️ Ejecutando: $archivo" -ForegroundColor Cyan
        try {
            # Ejecutar Python con el archivo
            python $archivo
            $ejecutado = $true
            break
        }
        catch {
            Write-Host "❌ Error al ejecutar $archivo" -ForegroundColor Red
            Write-Host $_.Exception.Message -ForegroundColor Red
            continue
        }
    }
    else {
        Write-Host "⚠️ No encontrado: $archivo" -ForegroundColor Yellow
    }
}

if (-not $ejecutado) {
    Write-Host ""
    Write-Host "❌ No se pudo ejecutar ninguna versión de la calculadora" -ForegroundColor Red
    Write-Host ""
    Write-Host "🔧 Diagnóstico:" -ForegroundColor Yellow
    Write-Host "   • Verificando Python..."
    try {
        python --version
    }
    catch {
        Write-Host "   ❌ Python no está instalado o no está en el PATH" -ForegroundColor Red
    }
    
    Write-Host "   • Archivos disponibles:"
    Get-ChildItem -Name "*.py" | ForEach-Object { Write-Host "     📄 $_" -ForegroundColor Cyan }
    
    Write-Host ""
    Write-Host "💡 Soluciones:" -ForegroundColor Green
    Write-Host "   1. Instalar Python desde python.org"
    Write-Host "   2. Ejecutar desde Explorador de Windows (doble clic en calculadora_estable.py)"
    Write-Host "   3. Abrir PowerShell aquí y ejecutar: python calculadora_estable.py"
}

Write-Host ""
Write-Host "✅ Script finalizado. Presiona cualquier tecla para salir..." -ForegroundColor Green
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")