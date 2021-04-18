import os
print("************************************")
print("*Renombrar archivos automaticamente*")
print("************************************ \n")
nombre = input("Ingrese el nombre desea asignar: ")

ubicacion = input("Ingresa la ubicacion de los archivos: ") 
os.chdir(ubicacion)
i=1
for file in os.listdir():
     src=file
     dst=nombre+str(i)+".jpg"
     os.rename(src,dst)
     i+=1
print("Tus archivos han sido renombrados exitosamente.")
