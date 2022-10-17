import os


lista_productos= []

def agregar_productos(elementos):
	lista_productos.append(elementos)
	print("Producto Agregado exitosamente")
	print("Tiene", len(lista_productos), "elementos en sus lista")

def mostrar_productos():
	print("Seleccionaste los siguientes productos: ")
	for elementos in lista_productos:
		print(elementos)
	
def mostrar_ayuda():
	print("Bienvenido, Que producto deseas agregar a tu lista de mercado: " )
	print("******En caso de solicitar Ayuda, Ingresa 'AYUDA'******")
	print("******Ingresa 'TERMINADO' cuando termines tu lista de mercado******")
	print("******Ingresa 'MOSTRAR' para listar los productos seleccionados hasta el momento ******")
	print("******Ingresa 'ElIMINAR' para borrar el ultimo elemento de su lista ******")

def borrar_elementos():
	del lista_productos[(len(lista_productos)-1)]
	print("El elemento fue eliminado de la lista")
	print("Tiene", len(lista_productos), "elementos en sus lista")


mostrar_ayuda()
while True:

	nuevo_item= input("> ").upper()
	if nuevo_item == "AYUDA":
		mostrar_ayuda()
		continue
	elif nuevo_item == "TERMINADO":
		break
	elif nuevo_item == "MOSTRAR":
		mostrar_productos()
		continue
	elif nuevo_item == "ELIMINAR":
		borrar_elementos()
		continue
	agregar_productos(nuevo_item)

mostrar_productos()
	


