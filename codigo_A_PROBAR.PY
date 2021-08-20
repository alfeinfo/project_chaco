#CANT. ???  CANT. RESP. **PORCENTAJE con elif

preguntas = int(input("Ingrese total de preguntas"))
print("Total de preguntas>>>", preguntas)

correctas = int(input("Ingrese cantidad de respuestas correctas"))
print("Total de respuestas correctas>>>", correctas)

porcentaje = correctas * 100 / preguntas
if (porcentaje >=90):
	print("EXELENTE")
elif (porcentaje >=90):
	print("EXELENTE")
elif (porcentaje >= 70):
		print("BUENO")
elif (porcentaje >= 60):

	print("Aprovaste paro volve a repasar todo 3 veces, sabe")
else:
	print("no che no aprovaste")

----------------------------------------------------------

#EDAD DE 1 PERSONA E INFORME ++  --

a = input("Ingrese edad de la persona")
a = int(a)
print()

if (a >18):
	print("Usted es mayor muchacho")
else:
	print("Vallan  a buscar a los tutores pues es menor de edad")
	


--------------------------------------------------------------

#VALIDACIÓN DE USUARIO

valido=False
vocal="AEIOU"
caract_esp= "*#$%&@"
while not valido:
  usuario=input("Ingrese su Nombre de Usuario \n min 8 carct. max 15 caract. \n Una vocal mayusc.\n Un caract. esp.: \n")
  cont_caract=0
  ctrl_vocal= False
  ctrl_esp= False
  for x in usuario:
    cont_caract+=1
    for y in vocal:
      if x==y :
        ctrl_vocal=True
        break
    for z in caract_esp:
      if x==z:
        ctrl_esp=True
        break
  if cont_caract < 8:
      print("El usuario debe contener como min 8 caracteres")
  elif cont_caract > 15:
      print("El usuario debe contener como max 15 caracteres")
  elif ctrl_vocal==False:
      print("El usuario debe contener una vocal mayuscula")
  elif ctrl_esp== False:
      print("El usuario debe contener un caracter especial")
  else:
      print ("Usuario valido")
      valido=True