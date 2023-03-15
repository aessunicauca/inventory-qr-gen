import segno
import io
from PIL import Image
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

def insert_newlines(string, every=64):
    return '\n'.join(string[i:i+every] for i in range(0, len(string), every))

# Función para generar QR y agregarlo al PDF
def generar_qr(url, micro=False):
    if micro: # Only supports < 21 alphanumeric, symbols require extra char size
        qr = segno.make_micro(url)
    else:
        qr = segno.make(url)
    out = io.BytesIO()
    qr.save(out, scale=5, kind='png')
    out.seek(0)
    img = Image.open(out)

    return img

def generar_sticker_small(url, owner, qr_size, pdf, x, y, micro=False):
    img = generar_qr(url, micro)
    pdf.drawInlineImage(img, x, y + 7, qr_size, qr_size)
    pdf.setFont("Helvetica-Bold", 7, leading = None)
    pdf.drawString(x, y + 7, owner)

def generar_sticker_large(url, title, message, qr_size, pdf, x, y, sticker_width, sticker_height, micro=False):
    img = generar_qr(url, micro)
    pdf.drawInlineImage(img, x, y + sticker_height - qr_size, qr_size, qr_size)

    pdf.setFont("Helvetica-Bold", 7, leading = None)
    pdf.drawString(x + 10, y + sticker_height - qr_size - 7, "AESS")

    _title = insert_newlines(str(title).upper(), 16)[0:33]
    t = pdf.beginText()
    t.setFont("Helvetica-Bold", 10, leading = None)
    t.setTextOrigin(x + qr_size, y + sticker_height - 16)
    t.textLines(_title)
    pdf.drawText(t)

    _offset = 0
    if "\n" in _title:
        _offset = 14
    m = pdf.beginText()
    m.setFont("Helvetica", 10, leading = None)
    m.setTextOrigin(x + qr_size, y + sticker_height - 27 - _offset)
    m.textLines(insert_newlines(str(message).upper(), 16)[0:33])
    pdf.drawText(m)

def generar_pagina_small(df):
    # Parámetros de entrada
    qr_size = 55  # Tamaño del QR (en celdas)
    sticker_width = qr_size + 2
    sticker_height = qr_size + 6
    x_start = 20  # Coordenada x de inicio
    y_start = 710  # Coordenada y de inicio
    x = x_start
    y = y_start

    # Crear el archivo PDF y generar QR para cada URL en el diccionario
    pdf_small = canvas.Canvas("stickers_small.pdf", pagesize=letter)
    for i in range(df.shape[0]):
        if df["type"][i] == "small":
            generar_sticker_small(df["url"][i], str(df["owner"][i]), qr_size, pdf_small, x, y, micro=False)
            x += sticker_width  # Avanzar en la coordenada x
            if x > 570:  # Saltar a la siguiente línea si se llega al límite de la página
                x = x_start
                y -= sticker_height
                if y < 20:  # Crear una nueva página si se llega al límite de la página
                    pdf_small.showPage()
                    y = y_start
    pdf_small.save()

def generar_pagina_large(df):
    # Parámetros de entrada
    qr_size = 70  # Tamaño del QR (en celdas)
    sticker_width = 180
    sticker_height = 90
    x_start = 20  # Coordenada x de inicio
    y_start = 660  # Coordenada y de inicio
    x = x_start
    y = y_start

    pdf_large = canvas.Canvas("stickers_large.pdf", pagesize=letter)
    for i in range(df.shape[0]):
        if df["type"][i] == "large":
            generar_sticker_large(df["url"][i], df["title"][i], df["message"][i], qr_size, pdf_large, x, y, sticker_width, sticker_height, micro=False)
            x += sticker_width  # Avanzar en la coordenada x
            if x > 520:  # Saltar a la siguiente línea si se llega al límite de la página
                x = x_start
                y -= sticker_height
                if y < 20:  # Crear una nueva página si se llega al límite de la página
                    pdf_large.showPage()
                    y = y_start
    pdf_large.save()