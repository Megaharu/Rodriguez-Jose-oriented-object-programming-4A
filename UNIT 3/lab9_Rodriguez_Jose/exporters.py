import csv
import json
import decimal
import datetime
from fpdf import FPDF

class Exportador:
    def export(self, datos, ruta_archivo):
        raise NotImplementedError("Este método debe ser implementado por la subclase.")

class ExportadorTXT(Exportador):
    def export(self, datos, ruta_archivo):
        with open(ruta_archivo, 'w', encoding='utf-8') as file:
            file.write("--- REPORTE DE PRODUCTOS ---\n")
            for producto in datos:
                file.write(f"ID: {producto['id']} | Nombre: {producto['name']} | Precio: ${producto['price']} | Stock: {producto['stock']}\n")
        print(f"Archivo TXT generado en: {ruta_archivo}")

class ExportadorCSV(Exportador):
    def export(self, datos, ruta_archivo):
        with open(ruta_archivo, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "Nombre", "Descripción", "Categoría", "Precio", "Stock", "Fecha de Creación"])
            for p in datos:
                writer.writerow([p['id'], p['name'], p['description'], p['category'], p['price'], p['stock'], p['created_at']])
        print(f"Archivo CSV generado en: {ruta_archivo}")

class ExportadorJSON(Exportador):
    def export(self, datos, ruta_archivo):
        def default_converter(o):
            if isinstance(o, (datetime.datetime, datetime.date, decimal.Decimal)):
                return str(o)
                
        with open(ruta_archivo, 'w', encoding='utf-8') as file:
            json.dump(datos, file, indent=4, default=default_converter)
        print(f"Archivo JSON generado en: {ruta_archivo}")

class ExportadorPDF(Exportador):
    def export(self, datos, ruta_archivo):
        pdf = FPDF()
        pdf.add_page()
        
        pdf.set_font("Arial", 'B', 16)
        pdf.cell(200, 10, txt="Reporte de Inventario de Productos", ln=True, align='C')
        pdf.ln(10)
        
        pdf.set_font("Arial", size=12)
        for producto in datos:
            texto_linea = f"ID: {producto['id']} - Producto: {producto['name']} - Precio: ${producto['price']} - Stock: {producto['stock']}"
            pdf.cell(200, 10, txt=texto_linea, ln=True)
            
        pdf.output(ruta_archivo)
        print(f"Archivo PDF generado en: {ruta_archivo}")