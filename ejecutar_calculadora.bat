@echo off
title Calculadora Factor Reduccion NSR-10
echo.
echo =========================================================
echo         CALCULADORA FACTOR REDUCCION CARGA VIVA
echo                     NSR-10 B.5.4.2
echo =========================================================
echo.
echo Cambiando al directorio correcto...
cd /d "%~dp0"
echo Directorio actual: %CD%
echo.
echo Ejecutando calculadora...
echo.
python calculadora_estable.py
if errorlevel 1 (
    echo.
    echo Error con calculadora_estable.py, intentando alternativa...
    python calculadora_simple.py
    if errorlevel 1 (
        echo.
        echo Error con calculadora_simple.py, intentando ultima opcion...
        python calculadora_limpia.py
        if errorlevel 1 (
            echo.
            echo ===========================================
            echo ERROR: No se pudo ejecutar ninguna version
            echo ===========================================
            echo.
            echo Solucion 1: Hacer doble clic en calculadora_estable.py
            echo Solucion 2: Abrir PowerShell aqui y ejecutar:
            echo             python calculadora_estable.py
            echo Solucion 3: Instalar/reinstalar Python
            echo.
            pause
        )
    )
)
echo.
echo Aplicacion finalizada.
pause