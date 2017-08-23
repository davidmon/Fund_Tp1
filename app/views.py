from flask import request, redirect, render_template, url_for, flash
from app import app
import re 
import forms

@app.route('/', methods=['GET','POST'])
def index():
	archivoForm = forms.ArchivoForm(request.form)
	if request.method == 'POST' and archivoForm.validate():
		archivo = archivoForm.nombreArchivo.data
   		valor = re.compile(r'(-?\d+\.\d{1}),{1}\s{1}(-?\d+\.\d{1}),{1}\s{1}(-?\d+\.\d{1})\D+(\d+)')
		archivo = open(archivo,'r')
		texto_pagina = archivo.read()
		lista_coordenadas = valor.findall(texto_pagina)
		archivo.close()
   		informe = open('persona_x.txt','w')
		informe.write('FUNDAMENTOS DE INFORMATICA - TP 1 - Ejercicio 1 \n')
		informe.write('\nNro de puntos\t\t X\t\t Y\t\t Z\n')
		for coord in lista_coordenadas:
			informe.write(coord[3]+'\t\t\t'+coord[0]+'\t\t'+coord[1]+'\t\t'+coord[2]+'\n')
		informe.close()
		return render_template("tabla.html",title='TP3 Resutado', lista_coordenadas= lista_coordenadas)

	return render_template('index.html', title='TP3', form=archivoForm)

if __name__ == '__main__':
	app.run (debug = true, host="0.0.0.0")