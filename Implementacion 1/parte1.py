

from subprocess import call

#instalamos las ultimas actualizaciones y clonamos nuestro repositorio para probar la aplicacion

call(["sudo apt-get update"], shell=True)
call(["sudo apt install python3-pip"], shell=True) 
call(["git clone https://github.com/Nerio-Messino/Repositorio_Instancias.git"], shell=True)


#instalamos las cosas necesarias de la carpeta requirements.txt y actualizamos 

call(["pip3 install urllib3"], shell=True)
call(["pip3 install flask_bootstrap"], shell=True)
call(["pip3 install chardet"], shell=True)
call(["pip3 install -r Repositorio_Instancias/bookinfo/src/productpage/requirements.txt"],shell=True) 
call(["pip3 install --upgrade requests"], shell=True)#Nos pide que algunas versiones se actualizen a la mas nueva
call(["sudo apt-get update"], shell=True)



#Modificar Group number
fin = open("Repositorio_Instancias/bookinfo/src/productpage/productpage_monolith.py",'r')
fout = open("Repositorio_Instancias/bookinfo/src/productpage/productpage_monolith2.py",'w')

for line in fin:

#     |--------NOTA TEORICA---------------------------------------------------------------------------------------------|
#     |	os.getenv() does not raise an exception, but returns None					            						|
#     |	os.environ.get() similarly returns None							                                                |
#     |	os.environ[] raises an exception if the environmental variable does not exist	               			        |
#     |-----------------------------------------------------------------------------------------------------------------|

	if "reviewsHostname = "+r'"'+"reviews"+r'"'+" if (os.environ.get("+r'"'+"REVIEWS_HOSTNAME"+r'"'+") is None) else os.environ.get("+r'"'+"REVIEWS_HOSTNAME"+r'"'+")" in line :
	#r, raw para poner caracteres tal cual
		fout.write(line+ "\nos.environ['GROUP_NUMBER']="+r'"'+"Grupo 03"+r'"'+" \n")
		#Lo que hace es sacar del entorno la variable group number y se sustituye por Equipo 02. Para modifcar sacandola del entorno es \os.environ[]
	#reviewsHostname = "reviews" if (os.environ.get("REVIEWS_HOSTNAME") is None) else os.environ.get("REVIEWS_HOSTNAME"), linea 62 de github, no tiene sentido cambiar ni el service, ni el detail ni el rating
	elif "'title': 'The Comedy of Errors'," in line :
		fout.write("'title': 'The Comedy of Errors ' + os.environ['GROUP_NUMBER'],")
		#OJO QUE NO SE SI TENEMOS QUE USAR LO DEL RAW
		#Tenemos que cambiar el nombre del autor????Si, para hacer el titulo del equipo
	elif "'author': book['authors'][0]," in line :
			fout.write(line + "        'equipo' : os.environ['GROUP_NUMBER'],\n")		
	else:
		fout.write(line)
fin.close()
fout.close()

call(["sudo cp Repositorio_Instancias/bookinfo/src/productpage/productpage_monolith2.py Repositorio_Instancias/bookinfo/src/productpage/productpage_monolith.py"], shell= True)
call(["sudo rm Repositorio_Instancias/bookinfo/src/productpage/productpage_monolith2.py"], shell= True)

#-------------------------------------------------------------------------------
call(["sudo python3 Repositorio_Instancias/bookinfo/src/productpage/productpage_monolith.py 9080"],shell=True)
