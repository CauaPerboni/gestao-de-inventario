import csv
import sqlite3
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def generate_report(db_file, report_file):
    connection = sqlite3.connect(db_file)
    cursor = connection.cursor()
    
    cursor.execute('SELECT * FROM products')
    products = cursor.fetchall()

    with open(report_file + '.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Product ID', 'Name', 'Description', 'Quantity', 'Price', 'Min Stock'])
        writer.writerows(products)

    c = canvas.Canvas(report_file + '.pdf', pagesize=letter)
    c.drawString(100, 750, "Relatório de Estoque")
    
    y = 700
    for product in products:
        c.drawString(100, y, str(product))
        y -= 20

    c.save()
    connection.close()
