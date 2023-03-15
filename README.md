# QR
## Generador de códigos QR

_Este es un proyecto de Python que genera códigos QR a partir de URLs y las agrega a un archivo PDF. Para ello, utiliza la librería qrcode para generar los códigos QR y la librería reportlab para agregarlos al archivo PDF._

### Recomendaciones
Usar Virtual Environment para la instalación de paquetes y contener el aplicativo. Sigue los pasos en https://pypi.org/project/virtualenvwrapper-win/

```
pip install virtualenvwrapper-win
mkvirtualenv -r .\ENV\ENV\requirements.txt qr
workon qr
```

### Requerimientos
_Para utilizar este generador de códigos QR, necesitas tener instalado Python 3.x y las librerías qrcode y reportlab. Puedes instalarlas fácilmente utilizando pip:_

```
pip install qrcode reportlab
```

## Uso

_Para generar los códigos QR, simplemente debes ejecutar el archivo generador_qr.py y se creará un archivo PDF con los códigos QR correspondientes a las URLs que se encuentran en el diccionario urls_imagenes. También puedes especificar el tamaño de los códigos QR y el nombre del archivo PDF resultante._

```
python generador_qr.py
```


## Personalización

_Si deseas agregar tus propias URLs y personalizar los parámetros de generación de los códigos QR, simplemente modifica el diccionario urls_imagenes en el archivo generador_qr.py. También puedes cambiar el tamaño de los códigos QR y el nombre del archivo PDF resultante._

## Contribuciones

_Si deseas contribuir a este proyecto, puedes hacerlo abriendo un issue o un pull request en GitHub. ¡Toda ayuda es bienvenida!_

## Autor

_Este generador de códigos QR fue desarrollado por Felipe Alejandro Tosse._
