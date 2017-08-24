from wtforms import Form
from wtforms import StringField
from wtforms import validators
import os.path as path
import re

def mivalidacion(form, field):
	if not path.exists(field.data) and len(field.data)>0:
		print field.data
		raise validators.ValidationError('* El archivo no existe. Ingrese un archivo valido!')
	valor = re.compile(r'\w+\.html')
	nombreDelArchivo = valor.findall(field.data)
	if len(nombreDelArchivo)==0:
		raise validators.ValidationError('* El archivo no es un html. Ingrese un archivo valido!')

class ArchivoForm(Form):
	nombreArchivo = StringField('- Ingresar el Nombre del Archivo:', [
		validators.length(min=5, max=50, message='* Nombre no valido. Ingrese una nombre valido!'),
		validators.Required(message='* Este es un campo requerido')
		
		]
		)
