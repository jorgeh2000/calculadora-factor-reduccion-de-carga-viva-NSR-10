#!/usr/bin/env python3
"""
Creador de icono de prueba para la aplicación
"""

import os
from PIL import Image, ImageDraw, ImageFont

def crear_icono_4d():
    """Crea un icono de prueba con el texto '4D'"""
    try:
        # Crear imagen de 64x64 píxeles
        img = Image.new('RGBA', (64, 64), (44, 62, 80, 255))  # Color azul oscuro
        draw = ImageDraw.Draw(img)
        
        # Dibujar borde
        draw.rectangle([2, 2, 61, 61], outline=(255, 255, 255, 255), width=2)
        
        # Intentar cargar una fuente, si no usar la predeterminada
        try:
            font = ImageFont.truetype("arial.ttf", 24)
        except:
            try:
                font = ImageFont.truetype("Arial", 24)
            except:
                font = ImageFont.load_default()
        
        # Dibujar texto "4D"
        text = "4D"
        bbox = draw.textbbox((0, 0), text, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        
        x = (64 - text_width) // 2
        y = (64 - text_height) // 2 - 2
        
        draw.text((x, y), text, fill=(255, 255, 255, 255), font=font)
        
        # Guardar como .ico
        icono_path = "LOGO 4D-ROTULO.ico"
        img.save(icono_path, format='ICO', sizes=[(32,32), (64,64)])
        
        print(f"✅ Icono creado: {icono_path}")
        print(f"📁 Ubicación: {os.path.abspath(icono_path)}")
        return True
        
    except ImportError:
        print("❌ PIL (Pillow) no está instalado")
        print("💡 Instalar con: pip install Pillow")
        return False
    except Exception as e:
        print(f"❌ Error creando icono: {e}")
        return False

def crear_icono_simple():
    """Crea un icono básico usando solo Python estándar"""
    try:
        # Crear datos de icono ICO básico (16x16)
        # Header ICO
        ico_data = bytearray()
        ico_data.extend([0, 0])  # Reserved
        ico_data.extend([1, 0])  # Type: ICO
        ico_data.extend([1, 0])  # Number of images
        
        # Image directory
        ico_data.extend([16])    # Width
        ico_data.extend([16])    # Height
        ico_data.extend([0])     # Color palette
        ico_data.extend([0])     # Reserved
        ico_data.extend([1, 0])  # Color planes
        ico_data.extend([1, 0])  # Bits per pixel
        ico_data.extend([40, 1, 0, 0])  # Size of image data
        ico_data.extend([22, 0, 0, 0])  # Offset to image data
        
        # BMP header (simplificado)
        bmp_data = bytearray([40, 0, 0, 0,  # Size of header
                             16, 0, 0, 0,  # Width
                             32, 0, 0, 0,  # Height (double for ICO)
                             1, 0,         # Planes
                             1, 0,         # Bits per pixel
                             0, 0, 0, 0,   # Compression
                             64, 0, 0, 0,  # Image size
                             0, 0, 0, 0,   # X pixels per meter
                             0, 0, 0, 0,   # Y pixels per meter
                             2, 0, 0, 0,   # Colors used
                             0, 0, 0, 0])  # Important colors
        
        # Color table (blanco y azul)
        color_table = bytearray([0, 0, 0, 0,        # Negro
                                255, 255, 255, 0])   # Blanco
        
        # Datos de imagen (patrón simple)
        image_data = bytearray([0xFF, 0xFF] * 16)  # Imagen blanca simple
        mask_data = bytearray([0x00, 0x00] * 16)   # Sin máscara
        
        ico_data.extend(bmp_data)
        ico_data.extend(color_table)
        ico_data.extend(image_data)
        ico_data.extend(mask_data)
        
        # Guardar archivo
        with open("LOGO 4D-ROTULO.ico", "wb") as f:
            f.write(ico_data)
        
        print("✅ Icono básico creado: LOGO 4D-ROTULO.ico")
        return True
        
    except Exception as e:
        print(f"❌ Error creando icono básico: {e}")
        return False

if __name__ == "__main__":
    print("🎨 CREADOR DE ICONO 4D-ROTULO")
    print("=" * 40)
    
    # Verificar si ya existe
    if os.path.exists("LOGO 4D-ROTULO.ico"):
        print("ℹ️  El archivo LOGO 4D-ROTULO.ico ya existe")
        print("   No se creará uno nuevo")
        exit()
    
    print("Intentando crear icono con PIL...")
    if crear_icono_4d():
        print("🎉 ¡Icono creado exitosamente!")
    else:
        print("\nIntentando crear icono básico...")
        if crear_icono_simple():
            print("🎉 ¡Icono básico creado!")
        else:
            print("❌ No se pudo crear ningún icono")
    
    print("\n📋 SIGUIENTES PASOS:")
    print("1. Ejecutar la aplicación para probar el icono")
    print("2. Si desea un icono personalizado, reemplazar el archivo")
    print("3. El icono debe ser formato .ico para compatibilidad")