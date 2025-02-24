# matriz_ABC
# 📊 Clasificación ABC de Inventarios

Este proyecto genera una **matriz de clasificación ABC de materiales** utilizando **Python**.  
El código calcula los costos totales de los materiales, asigna la clasificación **A, B o C** según el método **Pareto (80/20)** y exporta los resultados en **Excel (`.xlsx`) y PDF (`.pdf`)**.  

## 📌 Requisitos
Antes de ejecutar el código, asegúrate de tener instalado:
- **Python 3.x** ([Descargar aquí](https://www.python.org/downloads/))
- **Librerías necesarias** (instalar con `pip`)

## 🔹 Instalación de Librerías
Abre **CMD o PowerShell** y ejecuta:
```powershell
pip install pandas matplotlib seaborn fpdf openpyxl
```

## 🚀 Cómo Ejecutar el Código
1. **Descarga el archivo `clasificacion_abc.py`** o crea uno y copia el código.  
2. **Guarda el archivo** en una carpeta fácil de encontrar, como el Escritorio.  
3. **Abre CMD o PowerShell** y navega a la carpeta:
   ```powershell
   cd C:\Users\TuUsuario\Desktop
   ```
   *(Reemplaza `TuUsuario` con tu usuario en Windows).*
4. **Ejecuta el script** con:
   ```powershell
   python clasificacion_abc.py
   ```

## 📂 Archivos Generados
Después de ejecutar el código, se generarán estos archivos en la misma carpeta:

| Archivo | Descripción |
|---------|------------|
| `Matriz_ABC.xlsx` | Tabla con la clasificación ABC en formato Excel. |
| `Matriz_ABC.pdf` | Documento PDF con la tabla de materiales y clasificación ABC. |

## 📤 Cómo Compartir los Resultados
Puedes compartir los archivos generados de las siguientes maneras:
✅ **Correo Electrónico**: Adjunta los archivos `.xlsx` y `.pdf`.  
✅ **Google Drive**: Súbelos y comparte el enlace.  
✅ **Impresión**: Si se requiere en físico, imprime el PDF.  

## 📌 Explicación de la Clasificación ABC
La clasificación **ABC** se basa en el **principio de Pareto (80/20)**:
- **Categoría A**: Materiales de alto valor, representan **el 80% del costo total** pero solo **el 20% del inventario**.  
- **Categoría B**: Materiales intermedios, representan **el 15% del costo total** y **el 15% del inventario**.  
- **Categoría C**: Materiales de bajo valor, representan **solo el 5% del costo total**, pero **el 65% del inventario**.  

### 📊 **Plan de Control de Inventarios**
| Categoría | Frecuencia de Revisión | Nivel de Control |
|-----------|-----------------------|------------------|
| **A** | Semanal | Control estricto, pedidos just-in-time. |
| **B** | Mensual | Stock de seguridad moderado. |
| **C** | Trimestral | Baja inversión, evitar sobreinventario. |

## 📞 Soporte
Si tienes problemas al ejecutar el código, verifica que Python esté instalado y que las librerías necesarias estén correctamente instaladas.  
Si el problema persiste, contáctame y te ayudaré. 
Pepe73@gmail.com
jose.santiago40@my.unitec.edu.mx  

