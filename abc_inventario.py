import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 🔹 1. Creación de la matriz con al menos 25 materiales
materiales = [
    {"Código": "ADH-LOR001", "Concepto": "LORD 406-19 BLANCO", "Unidad": "L", "Costo_Unitario": 982, "Consumo_Anual": 42016},
    {"Código": "ADH-RES002", "Concepto": "RESISTOL 5000 AMARILLO", "Unidad": "L", "Costo_Unitario": 1060, "Consumo_Anual": 15643},
    {"Código": "ADH-SIL003", "Concepto": "SILICON SISTA SELLADO NEGRO", "Unidad": "L", "Costo_Unitario": 44, "Consumo_Anual": 320648},
    {"Código": "VYL-LON007", "Concepto": "LONA PANAGRAPHICS III 3.2M", "Unidad": "M", "Costo_Unitario": 651, "Consumo_Anual": 8513},
    {"Código": "IMP-TEL003", "Concepto": "TELA SARGA", "Unidad": "M2", "Costo_Unitario": 280, "Consumo_Anual": 4678},
    {"Código": "MAD-MDF001", "Concepto": "MDF DE 3MM", "Unidad": "PZA", "Costo_Unitario": 88.16, "Consumo_Anual": 13547},
    {"Código": "PLA-PVC002", "Concepto": "PVCEL BLANCO 3MM", "Unidad": "PZA", "Costo_Unitario": 370, "Consumo_Anual": 348},
    {"Código": "ILU-LED012", "Concepto": "LED GLOBAL LUX MINI BLANCO", "Unidad": "PZA", "Costo_Unitario": 14.57, "Consumo_Anual": 8216},
    {"Código": "MET-LAM002", "Concepto": "LÁMINA DE ALUMINIO CAL.14", "Unidad": "PZA", "Costo_Unitario": 1974.78, "Consumo_Anual": 403},
    {"Código": "IMP-VIN022", "Concepto": "WALL GRAPHICS LAMINADO", "Unidad": "M2", "Costo_Unitario": 466, "Consumo_Anual": 2468},
    {"Código": "ADH-LOK001", "Concepto": "PEGAMENTO LOKWELD 500", "Unidad": "L", "Costo_Unitario": 17285.42, "Consumo_Anual": 257},
    {"Código": "PLA-ACR021", "Concepto": "ACRÍLICO CRISTAL 9MM", "Unidad": "PZA", "Costo_Unitario": 4626, "Consumo_Anual": 951},
    {"Código": "IMP-EST002", "Concepto": "ESTIRENO DE 100PTS", "Unidad": "M2", "Costo_Unitario": 945, "Consumo_Anual": 2459},
    {"Código": "IMP-COR001", "Concepto": "COROPLAST 4MM", "Unidad": "M2", "Costo_Unitario": 355, "Consumo_Anual": 4687},
    {"Código": "VYL-LON005", "Concepto": "LONA PANAGRAPHICS III 1.5M", "Unidad": "M", "Costo_Unitario": 310, "Consumo_Anual": 6412},
    {"Código": "ILU-TAQ001", "Concepto": "TAQUETE PLÁSTICO", "Unidad": "PZA", "Costo_Unitario": 63, "Consumo_Anual": 30126},
    {"Código": "MAD-LAM002", "Concepto": "LAMINADO FASHION GREY", "Unidad": "PZA", "Costo_Unitario": 33.32, "Consumo_Anual": 412},
    {"Código": "PLA-ACR034", "Concepto": "ACRÍLICO ROJO L123 3MM", "Unidad": "PZA", "Costo_Unitario": 97.75, "Consumo_Anual": 543},
    {"Código": "MET-PIJ004", "Concepto": "PIJA AUTORROSCANTE 1/4 X 2", "Unidad": "PZA", "Costo_Unitario": 72.70, "Consumo_Anual": 2598},
    {"Código": "ILU-TUB001", "Concepto": "TUBO CONDUIT 1/2\"", "Unidad": "PZA", "Costo_Unitario": 55.96, "Consumo_Anual": 12348},
    {"Código": "EMP-POL004", "Concepto": "POLYSTRECH ROLLO PLAYO", "Unidad": "PZA", "Costo_Unitario": 135, "Consumo_Anual": 2478},
    {"Código": "IMP-VIN018", "Concepto": "FLOOR GRAPHICS 1440DPIS", "Unidad": "M2", "Costo_Unitario": 350, "Consumo_Anual": 357},
    {"Código": "ILU-LED008", "Concepto": "LED GE ROJO 145º", "Unidad": "PZA", "Costo_Unitario": 58, "Consumo_Anual": 8412},
]

# 🔹 2. Convertir a DataFrame y calcular costos totales
df = pd.DataFrame(materiales)
df["Importe_Total"] = df["Costo_Unitario"] * df["Consumo_Anual"]

# 🔹 3. Ordenar materiales de mayor a menor por costo total
df = df.sort_values(by="Importe_Total", ascending=False).reset_index(drop=True)

# 🔹 4. Calcular porcentaje del costo total y acumulado
df["Porcentaje_Individual"] = (df["Importe_Total"] / df["Importe_Total"].sum()) * 100
df["Porcentaje_Acumulado"] = df["Porcentaje_Individual"].cumsum()

# 🔹 5. Asignar clasificación ABC
def clasificar_abc(porcentaje):
    if porcentaje <= 80:
        return "A"
    elif porcentaje <= 95:
        return "B"
    else:
        return "C"

df["Clasificación"] = df["Porcentaje_Acumulado"].apply(clasificar_abc)

# 🔹 6. Exportar la matriz mejorada a Excel
df.to_excel("Matriz_ABC.xlsx", index=False)

# 🔹 7. Mostrar el DataFrame completo
print(df)

from fpdf import FPDF

# Crear PDF
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()
pdf.set_font("Arial", style='', size=10)

# Título
pdf.set_font("Arial", style='B', size=16)
pdf.cell(200, 10, "Clasificación ABC de Inventarios", ln=True, align='C')

# Espacio
pdf.ln(10)

# Agregar tabla con los primeros 25 materiales
pdf.set_font("Arial", size=8)
for i in range(min(25, len(df))):  # Máximo 25 filas para que quepa en la página
    row = df.iloc[i]
    pdf.cell(40, 5, row["Código"], border=1)
    pdf.cell(60, 5, row["Concepto"], border=1)
    pdf.cell(20, 5, row["Unidad"], border=1)
    pdf.cell(25, 5, f"${row['Costo_Unitario']:.2f}", border=1)
    pdf.cell(25, 5, str(row["Consumo_Anual"]), border=1)
    pdf.cell(25, 5, f"${row['Importe_Total']:.2f}", border=1)
    pdf.cell(15, 5, row["Clasificación"], border=1)
    pdf.ln()

# Guardar el PDF
pdf.output("Matriz_ABC.pdf")
print("PDF generado con éxito.")
