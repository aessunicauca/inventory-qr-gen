import segno
import io
from PIL import Image
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter


# Función para generar QR y agregarlo al PDF
def generar_qr(url, qr_size, pdf, x, y, micro=False):
    if micro: # Only supports < 21 alphanumeric, symbols require extra char size
        qr = segno.make_micro(url)
    else:
        qr = segno.make(url)
    out = io.BytesIO()
    qr.save(out, scale=5, kind='png')
    out.seek(0)
    img = Image.open(out)
    pdf.drawInlineImage(img, x, y, qr_size, qr_size)

def generar_pagina(df):
    # Parámetros de entrada
    qr_size = 30  # Tamaño del QR (en celdas)
    x_start = 20  # Coordenada x de inicio
    y_start = 740  # Coordenada y de inicio
    x = x_start
    y = y_start

    # Crear el archivo PDF y generar QR para cada URL en el diccionario
    pdf_small = canvas.Canvas("stickers_small.pdf", pagesize=letter)
    pdf_large = canvas.Canvas("stickers_large.pdf", pagesize=letter)
    for i in range(df.shape[0]):
        generar_qr(df["url"][i], qr_size, pdf_small, x, y, micro=False)
        x += qr_size  # Avanzar en la coordenada x
        if x > 580:  # Saltar a la siguiente línea si se llega al límite de la página
            x = x_start
            y -= qr_size
            if y < 20:  # Crear una nueva página si se llega al límite de la página
                pdf_small.showPage()
                y = y_start
    pdf_small.save()