import tkinter as tk           							# Importamos el modulo Tkinter para manejo de ventana
from tkinter import *    							# Carga módulo tk (widgets estándar)
from tkinter import ttk  							# Carga ttk (para widgets nuevos 8.5+)
from pandastable import Table, TableModel					# Se instala pip3 install pandastable para el manejo de tablas dentro de las ventanas.
import pandas as pd								# Se importa las librerias para manejar pandas para manejo de dataframe
import sys									# Se importa las librerias de sys

df_call_todos = pd.read_csv('1_Call_Center/Call_Center_1999_DataSet.csv', sep=';', thousands=",")	# Se cargan en un dataframe el contenido de los datos que vienen del archivo .csv
df_call_center = df_call_todos["vru.line"]    					# Se crea un dataframe con la columna vru.line

def funcion():
    reporte = tk.Tk()								# Se crea una ventana para mostrar el reporte
    reporte.geometry('950x350')							# Se indica el tamaño inicial de la ventana
    reporte.title("Reporte")							# Se indica el titulo para la ventana del reporte
    indices = listbox.curselection()						# Regresa una tupla, en la posicion [0] se encuentra el indice
    seleccion = ", ".join(listbox.get(i) for i in indices)			# Se obtiene la selección del listbox
    if seleccion != '':								# Si selecciono algo se realiza un reporte con lo seleccionado
      df_seleccionado = df_call_todos[df_call_todos['vru.line'] == seleccion]	# Se hace un filtro del dataframe completo con el dato seleccionado.
    else:									# Si no se selecciona ningun dato, entonces se asume que se desea mostrar todo el dataframe
      seleccion = 'All'								# Por defecto todo el dataframe
      df_seleccionado = df_call_todos						# No se aplica filtro
    dimension = df_seleccionado.shape						# Se obtiene el tamaño del dataframe solo para mostrarlo
    etiqueta_valor = Label(reporte, text="Valor")				# Se crea una etiqueta donde se colocará la informacion del dato seleccionado y de la dimensión del dataframe
    etiqueta_valor.grid(column=2, row=5, sticky=(W,E))				# Ubicacion de la etiqueta para mostra la información.
    etiqueta_valor.config(text=seleccion + ' ' + str(dimension))		# Se concatena la información que se desea mostrar en la etiqueta.
    etiqueta_valor.pack() 							# Se crea la etiqueta.
    frame_reporte = tk.Frame(reporte)						# Se grea la ventana para el reporte
    frame_reporte.pack(fill='both', expand=True)				# Se le indica la configuración de la ventana
    pt = Table(frame_reporte, dataframe=df_seleccionado)			# Se le pasa el dataframe a la ventana del reporte
    pt.show()									# Se muestra el reporte.
    
    boton_salir = ttk.Button(reporte, text='Cerrar', command=reporte.destroy).pack(side=BOTTOM)	# Boton que permite cerrar una ventana

root = tk.Tk()									# Define la ventana seleccion de la aplicación
root.configure(bg = 'beige')							# Color de fondo de la ventana
root.title("Seleccione")							# Titulo de la ventana
root.geometry('350x320')							# Tamaño inicial de la ventana
frame_lista = tk.Frame()							# Marco para contener el listbox y la barra de desplazamiento.
listbox = tk.Listbox(selectmode=tk.EXTENDED)					# Se crea el listado del listbox
scrollbar = tk.Scrollbar(frame_lista, orient=tk.VERTICAL)			# Crear una barra de deslizamiento con orientación vertical.
listbox = tk.Listbox(frame_lista, 						# Vincularla con la lista.
		     yscrollcommand=scrollbar.set, 				# Se activa el scrollbar
		     selectforeground="#ffffff",				# Se indica el color de la seleccion del scrollbar
                     selectbackground="#00aa00",				# Se indica el color del botom
                     selectborderwidth=5)					# Se indica el grosor del borde.
scrollbar.config(command=listbox.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)					# Ubicarla a la derecha.
listbox.pack()                     						# Hacemos los pack() del boton y el Listbox
frame_lista.pack()		   						# Hacemos los pack() del frame
plist = df_call_center.unique().tolist()					# Del dataframecon toda la columna vru.line, solo de deja un unico valor de la lista
for item in plist: 								# Insertamos los items en un Listbox
	listbox.insert(END,item)						# Se va creando la lista del listbox
boton_reporte = tk.Button(root, text="Reporte", command=funcion)		# Se crea un boton que envia al usuario a la ventana de reporte
boton_reporte.pack()								# Hacemos los pack() del frame
ttk.Button(root, text='Salir', command=quit).pack(side=BOTTOM)			# Se crea el boton para salir de la ejecución del programa
root.mainloop()
root.destroy()