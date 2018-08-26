from random import randint

print("Este script genera 500 alumnos para la base de datos del proyecto de la UTU.")
#archivoSentencias = open("Inserts.sql", "w")
lista_inserts = []
lista_sin_codigo = []
inserts = open("inserts.sql","w")

lista_ci = []
lista_nombres = []
lista_apellidos = []
lista_fechaNac = []
lista_tipos = []
lista_telefonos = []
lista_calles = ["Gral. Flores", "Av. Italia", "Luis Alberto de Herrera", "Bulevar Artigas"]
lista_num_calles = []
lista_emails = []
lista_sexos = []

email_opcion = ["@gmail.com","@hotmail.com","@outlook.com"]
tipo_mobil = ["091", "092", "094", "095", "097", "098", "099"]

def generarVerificador(ci):
	ci = str(ci)
	cont = 0
	multiplicador = [2,9,8,7,6,3,4]
	sumatoria = 0
	restar = 0
	codigo_verificador = 0
	for numero in ci:
		mult = multiplicador[cont]
		mult_number = (int(numero) * int(multiplicador[cont]))
		cont+=1
		while mult_number > 10:
			mult_number = mult_number%10;
		sumatoria += mult_number

	restar = sumatoria
	if sumatoria % 10 != 0:
		while restar % 10 != 0:
			restar+=1

	codigo_verificador = (sumatoria - restar) * -1
	lista_ci.append(str(ci)+"-"+str(codigo_verificador))

#*********GENERACION FECHAS NACIMIENTO**********
cont = 0
while len(lista_fechaNac) < 500:
	day = str(randint(1,29))
	month = str(randint(1,12))
	year = str(randint(1980,2001))
	fecha = day+"/"+month+"/"+year
	lista_fechaNac.append(fecha)
	cont+=1

#*********GENERACION DE CEDULAS***************
while len(lista_ci) < 500:
	while True:
		nueva_cedula = randint(3000000, 5999999)
		if nueva_cedula not in lista_sin_codigo:
			lista_sin_codigo.append(nueva_cedula)
			generarVerificador(nueva_cedula)
			break
		else:
			print("ci ya existe")
			input()

#********CARGADO DE NOMBRES Y APELLIDOS*************
for nombre in open("lista_nombres.txt"):
	nombre = nombre.strip('\n')
	persona_separada = nombre.split(' ')
	lista_nombres.append(persona_separada[0])
	lista_sexos.append(persona_separada[1])

for apellido in open("apellidos.txt"):
	apellido.strip("\n")
	lista_apellidos.append(apellido)

#********GENERACION TELEFONOS*******
while len(lista_telefonos) < 500:
	ismobile = randint(0,1)
	numero = ""
	if ismobile == 0:
		numero = "2"
		numero += str(randint(1123009,9786567))
		lista_telefonos.append(str(numero)+'\n')
	else:
		compania = randint(0, 6)
		numero = tipo_mobil[compania]
		numero += str(randint(112000, 978699))
		lista_telefonos.append(str(numero)+'\n')

#********GENERACION NUMERO DE CALLE**********
while len(lista_num_calles) < 500:
	number = randint(1,4000)
	if number not in lista_num_calles:
		bis = randint(1,10)
		if bis == 1:
			number = str(str(number) + "BIS")
		lista_num_calles.append(number)

class Persona():
	ci=""
	p_nombre=""
	s_nombre = ""
	p_apellido = ""
	s_apellido = ""
	tipo = ""
	telefono = ""
	dir_calle = ""
	dir_numero = ""
	grado = ""
	email = ""
	sexo = ""
	fecha_nac = ""
	hace_proyecto = ""
	baja = ""

	def __init__(self,ci,pnombre,snombre,pape,sape,tipo,telefono,dir_calle,dir_numero,grado,nota_final_proyecto,email,sexo,fecha_nac,hace_proyecto,baja):
		self.ci = ci.split("-")
		self.p_nombre = pnombre
		self.s_nombre = snombre
		self.p_apellido = pape
		self.s_apellido = sape
		self.tipo = tipo
		self.telefono = telefono
		self.dir_calle = dir_calle
		self.dir_numero = dir_numero
		self.grado = grado
		self.nota_final_proyecto = nota_final_proyecto
		self.email = email
		self.sexo = sexo
		self.fecha_nac = fecha_nac
		self.hace_proyecto = hace_proyecto
		self.baja = baja
	
	def ToInsert(self):
		sentencia = "INSERT INTO persona (ci, p_nombre, s_nombre, p_apellido, s_apellido, tipo, telefono, dir_calle, dir_numero, grado, nota_final_proyecto, email, sexo, fecha_nac, hace_proyecto, baja)\n"
		if self.s_nombre == "NULL":
			agrega = 'VALUES ({}{}, "{}", {}, "{}", "{}", "{}", "{}", "{}", "{}", {}, {}, "{}", "{}", {}, "{}", "{}");\n'.format(self.ci[0],self.ci[1],self.p_nombre,self.s_nombre,self.p_apellido,self.s_apellido,self.tipo,self.telefono,self.dir_calle,self.dir_numero,self.grado,self.nota_final_proyecto,self.email,self.sexo,self.fecha_nac,self.hace_proyecto,self.baja)
		else:
			agrega = 'VALUES ({}{}, "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", {}, {}, "{}", "{}", {}, "{}", "{}");\n'.format(self.ci[0],self.ci[1],self.p_nombre,self.s_nombre,self.p_apellido,self.s_apellido,self.tipo,self.telefono,self.dir_calle,self.dir_numero,self.grado,self.nota_final_proyecto,self.email,self.sexo,self.fecha_nac,self.hace_proyecto,self.baja)
		
		sentencia+=agrega
		lista_inserts.append(sentencia)
		#archivoSentencias.write(sentencia)

cont = 0
for ci in lista_ci:
	tieneSnom = randint(0,10)
	if 0 <= tieneSnom >= 3:
		snombre = lista_nombres[randint(0,len(lista_nombres)-1)]
	else:
		snombre = "NULL"
		pnombre = lista_nombres[cont]
		pape = lista_apellidos[randint(0,len(lista_apellidos)-1)].strip("\n")
		sape = lista_apellidos[randint(0,len(lista_apellidos)-1)].strip("\n")
		tipo = "Alumno"
		telefono = lista_telefonos[cont].strip("\n")
		dir_calle = lista_calles[randint(0,len(lista_calles)-1)]
		dir_numero = str(lista_num_calles[cont]).strip("\n")
		email = str(pnombre+pape)+str(email_opcion[randint(0,2)])
		fecha_nac = lista_fechaNac[cont]
		while email in lista_emails:
			email = pnombre+pape+str(randint(0,100))+str(email_opcion[randint(0,2)])
			
		lista_emails.append(email)
		sexo = lista_sexos[cont]
		if tipo == "Alumno":
			grado = "NULL"
			hace_proyecto = randint(0,10)
			if 0 <= hace_proyecto <= 2:
				hace_proyecto = "t"
				notaFinalP = "NULL"	
			else:
				hace_proyecto = "f"
				notaFinalP = randint(8,12)

		baja = "f"
		
		PERSONA = Persona(ci,pnombre,snombre,pape,sape,tipo,telefono,dir_calle,dir_numero,grado,notaFinalP,email,sexo,fecha_nac,hace_proyecto,baja)
		PERSONA.ToInsert()
		cont+=1
		
input("Mostrar Lista Inserts >")
for insert in lista_inserts:
	print(insert)
	inserts.write(insert)
#INSERT INTO persona (ci, p_nombre, s_nombre, p_apellido, s_apellido, tipo, telefono, dir_calle, dir_numero, grado, nota_final_proyecto, email, sexo, baja)
#VALUES (47911800, "Martin", " " ,"Kasamajeu" , "del Pino" ,"Alumno", "092228484", "Camino de los granjeros", "4860","" ,"","martin@casamayou.net", "O", "f");
