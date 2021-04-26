import pandas as pd
df=pd.DataFrame()

for i in range(5000):
	opcion = input("Menu Registros\n\n1)-Press 1 para Insertar Alumno:\n2)-Press 2 para Guardar Datos y Salir:")

	if opcion =="1":

		menu = input("Press Enter Para Ingresar Usuario:")

		Nombre = input("Nombre:")
		Apellidos = input("Apellidos:")
		Edad = input("Edad:")
		Grado = input("Grado:")
		Grupo = input("Grupo:")
		Correo = input("Correo:")


		data = {'Nombre':Nombre, 'Apellidos':Apellidos, 'Edad':Edad, 'Grado':Grado, 'Grupo':Grupo,'Correo electronico':Correo}
		df = df.append(data, ignore_index=True)

	elif opcion=="2":
		print("Acaba de finalizar Datos Guardados Correctamente!!")
		break

	else: 
		print("Digite una opcion")

df.to_csv('datos_alumno.csv')








	










#opc2 = input("b) Para Guardar datos y salir:"














#opc2 = input("b) Para Guardar datos y salir:"






