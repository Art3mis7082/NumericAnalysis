#Fecha de creación: 9 de febrero de 2026
#Tema: Errores de redondeo y truncamiento
#Nombre: Almaraz García Beatriz

#from numpy import arange
#for i in arange(4,2,-0.5): 
#    print(i)


R=3.14159265359

#4 decimales

VR=3.1416
VT=3.1415

EA_R=abs(VR-R)
EA_T=abs(VT-R)

print((f"EA_Redondeado={EA_R} [U] EA_Truncado={EA_T} [U]"))
print("-------------------------------")

ER_R = abs((VR-R)/R)
ER_T = abs((VT-R)/R)

print((f"ER_Redondeado={ER_R}  ER_Truncado={ER_T}"))
print("-------------------------------")

EP_R = abs((VR-R)/R)*100
EP_T = abs((VT-R)/R)*100

print((f"EP_Redondeado={EP_R} %  EP_Truncado={EP_T} %"))
print("-------------------------------")
