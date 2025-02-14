nombre= input("registre su nombre")
apellido= input("registre su apellido")
edad= int(input("registre su edad"))
if(edad<=3):
 print("bebe")
elif(edad>=4 and edad<=8):
 print("niño")
elif(edad>=9 and edad<=11):
 print("preadolescente")
elif(edad>=12 and edad<=18):
 print("adolescente") 
elif(edad>=19 and edad<=30):
 print("adulto joven")
elif(edad>=31 and edad<=59):
 print("adulto")
else: 
 print("adulto mayor")