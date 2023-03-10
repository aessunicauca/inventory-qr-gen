import qrcode
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

# Diccionario de URLs
urls_imagenes = {
    "imagen1": "https://ejemplo.com/imagen1.jpg",
    "imagen2": "https://ejemplo.com/imagen2.jpg",
    "imagen3": "https://ejemplo.com/imagen3.jpg",
    "imagen4": "https://ejemplo.com/imagen4.jpg",
    "imagen5": "https://ejemplo.com/imagen5.jpg",
    "imagen6": "https://ejemplo.com/imagen6.jpg",
    "imagen7": "https://ejemplo.com/imagen7.jpg",
    "imagen8": "https://ejemplo.com/imagen8.jpg",
    "imagen9": "https://ejemplo.com/imagen9.jpg",
    "imagen10": "https://ejemplo.com/imagen10.jpg",
    "imagen13": "https://ejemplo.com/imagen3.jpg",
    "imagen14": "https://ejemplo.com/imagen4.jpg",
    "imagen15": "https://ejemplo.com/imagen5.jpg",
    "imagen16": "https://ejemplo.com/imagen6.jpg",
    "imagen17": "https://ejemplo.com/imagen7.jpg",
    "imagen18": "https://ejemplo.com/imagen8.jpg",
    "imagen19": "https://ejemplo.com/imagen9.jpg",
    "imagen20": "https://ejemplo.com/imagen10.jpg"
}

# Función para generar QR y agregarlo al PDF
def generar_qr(url, qr_size, pdf, x, y, micro=False):
    if micro:
        qr = qrcode.QRCode(
            version=None,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=1,
            border=0,
            box_aspect_ratio=1,
            fit=True
        )
    else:
        qr = qrcode.QRCode(
            version=None,
            error_correction=qrcode.constants.ERROR_CORRECT_Q,
            box_size=2,
            border=1
        )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    pdf.drawInlineImage(img, x, y, qr_size*4, qr_size*4)

# Parámetros de entrada
qr_size = 10  # Tamaño del QR (en celdas)
filename = "urls_imagenes.pdf"  # Nombre del archivo PDF
x_start = 50  # Coordenada x de inicio
y_start = 50  # Coordenada y de inicio
x = x_start
y = y_start

# Crear el archivo PDF y generar QR para cada URL en el diccionario
pdf = canvas.Canvas(filename, pagesize=letter)
for key, value in urls_imagenes.items():
    generar_qr(value, qr_size, pdf, x, y, micro=False)
    x += qr_size*6  # Avanzar en la coordenada x
    if x > 550:  # Saltar a la siguiente línea si se llega al límite de la página
        x = x_start
        y -= qr_size*6
        if y < 50:  # Crear una nueva página si se llega al límite de la página
            pdf.showPage()
            y = y_start
pdf.save()