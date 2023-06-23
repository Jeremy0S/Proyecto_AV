#@JeremyS
import sympy
import math
import numpy as np
#-----------------------------------------CONJUNTO DE FUNCIONES---------------------------------------

arr = []
vres = []
aux = []

def sumav2(vres,arr,eV):
	for n in range(len(arr)):
		for m in range(eV):
			s = vres[m] + arr[n][m]
			vres[m] = s
	return vres

def iCeros(vres, eV):
	for x in range(eV):
			vres.append(0)
	return vres

def resta(vres,arr,eV):
	for n in range(len(arr)):
		for m in range(eV):
			if n == 0:
				s = vres[m] + arr[n][m]
				vres[m] = s
			else:
				s = vres[m] - arr[n][m]
				vres[m] = s
	return vres

def restaC(vres2,vres,eV):
	j = eV-2
	for x in range(eV):
		if x<j:
			s = vres[0][x] - vres[1][j]
			j = j-1
		if x>j:
			s = vres[0][x+1] - vres[1][j+2]
			j = 2
		if x == 2:
			s = vres[0][x-1] - vres[1][j-2]
		vres2.append(s)
	return vres2

def pInterno(ivector):
	for x in range(len(ivector)):
		s = ivector[x]*ivector[x]
		ivector[x] = s
	return ivector

def pPunto(arr,eV,op):
	s = 0
	if op == 1:
		for y in range(eV):
			s = arr[0][y] * arr[2][y] + s
		return s
	if op == 2:
		for y in range(eV):
			s = arr[0][y] * arr[1][y] + s
		return s
	for x in range(eV):
		s = arr[0][x] * arr[1][x] + s
	return s

def mEscalar(arr, esc):
	m = 0
	for x in range(len(arr)):
		m = arr[x]*esc
		arr[x] = m
	return arr

def mpPunto(arr, vres, eV):
	s=0
	for x in range(eV):
		s = arr[0][x] * arr[1][x]
		vres.append(s)
	s=0
	j=0
	for y in range(eV):
		j = vres[y]
		s = pow(j,2) + s
	s = pow(s,1/2)
	return s

def mVector(arr,op):
	s=0
	for x in range(len(arr)):
		s = arr[x]*arr[x] + s
	s = pow(s,1/2)	
	if op == 0:
		return s
	if op == 1:
		for z in range(len(arr)):
			arr[z] = arr[z],"/",s
		return arr

def mVector2(arr, s, op):
	res = 1
	for x in range(len(arr)):
		for z in range(len(arr[x])):
			s[x] = arr[x][z] * arr[x][z] + s[x]
		s[x] = pow(s[x],1/2)
	if op == 0:
		return s
	if op == 1:
		for y in range(len(s)):
			res = s[y] * res
		return res

def determinante(arr, vres, op):
	vres = [[0] * eV for i in range(len(arr)-1)]
	vres2 = []
	s = 1
	r1 = 0
	r2 = 0
	for v in range(len(arr)-1):
		if v == 0:
			k = 0
		if v == 1:
			k = 2
		j = 0
		 
		for x in range(len(arr[v])):
			j = x
			for y in range(len(arr[v])):
				if j>2:
					j = 0
				if k>2:
					k = 0
				if k<0:
					k = 1
				s = s * arr[j][k]
				if v == 0:
					k = k+1
				if v == 1:
					k = k-1
				j = j+1
			vres[v][x] = s
			if v == 0:
				r1 = s + r1
				k = 0
			if v == 1:
				r2 = s + r2
				k = 2
			s = 1
	s = r1 - r2

	if op == 1:
		return restaC(vres2,vres,len(vres[0]))

	if op == 2:
		s = []
		opt = 0
		restaC(vres2,vres,len(vres[0]))
		return abs(mVector(vres2, opt))

	return s

def tProducto(arr):
	p1 = 0
	p2 = 0
	p1 = pPunto(arr,len(arr[0]),1)
	p2 = pPunto(arr,len(arr[0]),2)
	mEscalar(arr[1],p1)
	mEscalar(arr[2],p2)
	for x in range(len(arr)):
			vres.append(0)
	return resta(vres,reOrd(arr),len(arr))

def reOrd(arr):
	for x in range(len(arr)):
			aux.append(0)
	for z in range(len(arr)-1):
		for x in range(len(arr)):
			aux[x] = arr[z+1][x]
			arr[z][x] = aux[x]
	arr.pop(len(arr)-1)
	return arr

def eFun(fEv, f, p):
	x, y, z = sympy.symbols('x y z', real=True)
	t = sympy.symbols('t')
	sym = [x, y, z, t]

	if len(p) == 1:
		fEv = f.subs(t, p[0])
	if len(p) == 2:
		fEv = f.subs(sym[0], p[0]).subs(sym[1], p[1])
	if len(p) == 3:
		fEv = f.subs(sym[0], p[0]).subs(sym[1], p[1]).subs(sym[2], p[2])

	return fEv

def dFun(dF, p, f):
	x, y, z = sympy.symbols('x y z', real=True)
	t = sympy.symbols('t')
	sym = [x, y, z, t]

	for i in range(len(p)):
		if len(p) == 1:
			dF.append(f.diff(sym[3]).subs(t,p[0]))
		if len(p) == 2:
			dF.append(f.diff(sym[i]).subs(x,p[0]).subs(y,p[1]))
		if len(p) == 3:
			dF.append(f.diff(sym[i]).subs(x,p[0]).subs(y,p[1]).subs(z,p[2]))

	return dF

def fGrad(dF, f, op):
	x, y, z = sympy.symbols('x y z', real=True)
	sym = [x, y, z]

	for i in range(len(dF)):
		if op == 1:
			f = dF[i]
		dF[i] = f.diff(sym[i])
	return dF

def fRot(fT, dF):
	x1 = len(dF) - 1
	x2 = 0

	for x in range(len(dF)):	
			x2 = x+1
			if x1>len(dF)-1:
				x1 = 0
			if x2>len(dF)-1:
				x2 = 0
			fT[x] = dF[x1].diff(sym[x2]) - dF[x2].diff(sym[x1])
			x1 = x1 + 1
	return fT

def fDf(Df, dF):
	Df = [[0] * len(dF) for i in range(len(dF))]
	x, y, z = sympy.symbols('x y z', real=True)
	sym = [x, y, z]

	for i in range(len(dF)):
		for j in range(len(dF)):
			Df[i][j] = dF[i].diff(sym[j])

	print("\nEl Df de la funcion es: \n")

	for x in range(len(dF)):
			print(Df[x])

	return 0


#-------------------------------------------MENU DE OPCIONES-------------------------------------

print("\nCalculadora de OPERACIONES VECTORIALES\n")

print("1. Operaciones con 1 vector de tamano n")
print("2. Operaciones con n vectores de tamano m")
print("3. Operaciones con 2 vectores de tamano n")
print("4. Operaciones con 2 vectores de tamano 3")
print("5. Operaciones con 3 vectores de tamano 3\n")

print("Calculo Diferencial e Integral Vectorial\n")

print("6. Operaciones con curvas ya definidas")
print("7. Operaciones con funciones de R3->R ya definidas")
print("8. Operaciones con funciones de R3->R3 ya definidas\n")

op = int(input("Escriba el numero de la operacion que desea realizar: "))

#-------------------------------------------OPCION 1-------------------------------------

if (op == 1):

	nV = 1
	eV = int(input("Ingrese el numero de elementos del vector: "))

	for x in range(eV):
			arr.append(0)

	print("\nIngrese los valores del vector: \n")
	for m in range(eV):
		arr[m] = int(input("Valor: "))

	print("\nVector: ",arr)

	print("\n- Operaciones disponibles:\n 1. Multiplicacion por un escalar\n 2. Producto Interno\n 3. Vector Unitario\n")
	op1 = int(input("Escriba el numero de la operacion que desea realizar: "))

	if op1 == 1:
		esc = int(input("\nIngrese el escalar: "))
		print("\nEl vector resultante es: ",mEscalar(arr,esc))

	if op1 == 2:
		print("\nEl producto interno del vector es: ",pInterno(arr))

	if op1 == 3:
		opt = 1
		for x in range(eV):
			vres.append(0)
		print("\nEl vector unitario es: ", mVector(arr,opt))

#-------------------------------------------OPCION 2-------------------------------------

if (op == 2):

	nV = int(input("\nIngrese el numero de vectores: "))
	eV = int(input("Ingrese el numero de elementos de los vectores: "))

	arr = [[0] * eV for i in range(nV)]

	for n in range(nV):
		print("\nIngrese los valores del vector ",n+1,": \n")
		for m in range(eV):
			arr[n][m] = int(input("Valor: "))

	print("\n")

	for z in range(nV):
		print("Vector ",z+1,": ",arr[z])

	print("\n- Operaciones disponibles:\n  \n  1. Suma de Vectores\n  2. Resta de vectores\n")
	op2 = int(input("Escriba el numero de la operacion que desea realizar: "))

	if op2 == 1:
		print("\nEl vector resultante es: ",sumav2(iCeros(vres, eV),arr,eV))

	if op2 == 2:
		print("\nEl vector resultante es: ",resta(iCeros(vres, eV),arr,eV))

#-------------------------------------------OPCION 3-------------------------------------

if (op == 3):

	nV = 2
	eV = int(input("\nIngrese el numero de elementos de los vectores: "))

	arr = [[0] * eV for i in range(nV)]

	for n in range(nV):
		print("\nIngrese los valores del vector ",n+1,": \n")
		for m in range(eV):
			arr[n][m] = int(input("Valor: "))

	print("\n")

	for z in range(nV):
		print("Vector ",z+1,": ",arr[z])

	print("\n- Operaciones disponibles: \n 1. Producto Punto\n 2. Modulo del producto Punto\n 3. Angulo entre vectores\n")
	op2 = int(input("Escriba el numero de la operacion que desea realizar: "))

	if op2 == 1:
		print("\nEl producto punto de los vectores es: ",pPunto(arr,eV,0))

	if op2 == 2:
		print("\nEl modulo del producto punto es: ","{:.2f}".format(mpPunto(arr,vres,eV)))

	if op2 == 3:
		s = []
		ppv = 0
		mppv = 0
		op = 1
		ppv = pPunto(arr,eV,0)
		mppv = mVector2(arr,iCeros(s,len(arr)),op)

		print("\nEl angulo entre los vectores es: ","{:.2f}".format(math.degrees(math.acos(ppv/mppv))),"°")

#-------------------------------------------OPCION 4-------------------------------------

if (op == 4):

	nV = 3
	eV = 3

	arr = [[1] * eV for i in range(nV)]

	for n in range(nV-1):
		print("\nIngrese los valores del vector ",n+1,": \n")
		for m in range(eV):
			arr[n+1][m] = int(input("Valor: "))

	print("\n")

	for z in range(nV-1):
		print("Vector ",z+1,": ",arr[z+1])

	print("\n- Operaciones disponibles:\n  1. Producto Cruz\n  2. Volumen del Paralelogramo\n")
	op3 = int(input("Escriba el numero de la operacion que desea realizar: "))

	if op3 == 1:
		op = 1
		vres = [[0] * eV for i in range(nV-1)]
		print("\nEl producto cruz es: ",determinante(arr,vres,op))

	if op3 == 2:
		op = 2
		print("\nEl volumen del paralelogramo es de: ","{:.2f}".format(determinante(arr,vres,op)), "Unidades cuadradas")

#-------------------------------------------OPCION 5-------------------------------------

if (op == 5):

	nV = 3
	eV = 3

	arr = [[0] * eV for i in range(nV)]

	for n in range(nV):
		print("\nIngrese los valores del vector ",n+1,": \n")
		for m in range(eV):
			arr[n][m] = int(input("Valor: "))

	print("\n")

	for z in range(nV):
		print("Vector ",z+1,": ",arr[z])

	print("\n- Operaciones disponibles:\n  1. Triple Producto Escalar\n  2. Volumen de un Paralelepipedo\n  3. Triple Producto Vectorial\n")
	op4 = int(input("Escriba el numero de la operacion que desea realizar: "))

	if op4 == 1:
		print("\nEl triple producto escalar es: ",determinante(arr,vres,0))

	if op4 == 2:
		print("\nEl volumen del paralelepipedo es de: ",abs(determinante(arr,vres,0)), "Unidades cubicas")

	if op4 == 3:
		print("\nEl triple producto vectorial de la forma V1x(V2xV3) es: ",tProducto(arr))

#-------------------------------------------OPCION 6-------------------------------------

if (op == 6):

	t = sympy.symbols('t')
	f = [t**2, 3*t**4, t]
	f2 = t**2
	p = [2]
	rEv = []
	fAux = []
	fE = 0
	sym = ['x', 'y', 'z']

	print("\nSe trabaja con la curva c(t): ",f)

	print("\n- Operaciones disponibles con la curva:\n\n  1. Vector Tangente a la Curva\n  2. Ecuaciones parametricas de la recta tangente en un punto\n  3. Aceleracion del vector velocidad de la curva\n")
	op2 = int(input("Escriba el numero de la operacion que desea realizar: "))

	if op2 == 1:
		for x in range(len(f)):
			f[x] = f[x].diff(t)

		print("\nEl Vector Tangente a la curva es: ",f)

	if op2 == 2:

		for x in range(len(f)):
			dFun(fAux, p, f[x])

		mEscalar(fAux, t)
		iCeros(rEv, len(f))

		for x in range(len(f)):
			rEv[x] = eFun(fE, f[x], p)

		print("\nLas ecuaciones parametricas de la recta tangente evaluada en un punto son : \n")
		for x in range(len(f)):
			print(" ",sym[x], " = ",rEv[x], " + ", fAux[x]) 

	if op2 == 3:
		for x in range(len(f)):
			f[x] = f[x].diff(t,t)

		print("\nLa aceleracion del vector velocidad es: ",f)

#-------------------------------------------OPCION 7-------------------------------------

if (op == 7):

	x, y, z = sympy.symbols('x y z', real=True)
	#f = 3*x*y + z**2 -4
	f = x**2 + y**4 +5*x*y
	#p = [1,1,1]
	p = [1,2]
	dF = []
	v = [1,3,5]
	fT = []
	fEv = 0

	if len(p) == 3:
		dF2 = [x - p[0], y - p[1], z - p[2]]
	else:
		dF2 = [x - p[0], y - p[1]]

	print("\nSe trabaja con funcion f: ",f)

	print("\n- Operaciones disponibles con la funcion vectorial:\n  \n  1. Gradiente de la Funcion\n  2. Plano Tangente a la funcion R3->R3 \n  3. Plano Tangente a la funcion R2->R3\n  4. Mayor tasa de cambio de la funcion\n  5. Tasa de cambio en direccion de un vector\n")
	op2 = int(input("Escriba el numero de la operacion que desea realizar: "))

	if op2 == 1:
		print("\nEl gradiente de la funcion es: ",fGrad(iCeros(dF, len(p)), f, 0))

	if op2 == 2:
		fT = [dFun(dF,p,f), dF2]
		print("El plano tangente a la funcion es: ",pPunto(fT, len(dF), 0)," = 0")

	if op2 == 3:
		fT = [dFun(dF,p,f), dF2]
		print("El plano tangente a la funcion es z = ", eFun(fEv,f,p) + pPunto(fT, len(dF2), 0))

	if op2 == 4:
		print("\nLa funcion crece mas rapido en la direccion: ",dFun(dF,p,f))

	if op2 == 5:
		fT = [dFun(dF,p,f), v]
		print("\nLa tasa de cambio de la funcion f(x,y,z) en direccion del vector: ",v," es: ",pPunto(fT, len(v), 0))

#-------------------------------------------OPCION 8-------------------------------------

if (op == 8):

	x, y, z = sympy.symbols('x y z', real=True)
	sym = [x, y, z] 
	dF = [3*x*y, 4*z*x**2, 5*z**3]
	c = [3*t**2, 4*t, t**3]
	f = 0
	p = [1,1,1]
	v = [1,3,5]
	fT = []
	x1 = len(dF) - 1
	x2 = 0
	Df = []

	#REGLA DE LA CADENA
	#dF[1] = dF[1].diff(x).subs(x,t+t**2)
	#dF[1] = dF[1].diff(t).subs(z,t)

	print("\nSe trabaja con funcion f: ",dF)

	print("\n- Operaciones disponibles con la funcion vectorial:\n  \n  1. Divergencia de la Funcion\n  2. Rotacional de la funcion\n  3. Df de una funcion\n  4. Regla de la cadena\n")
	op2 = int(input("Escriba el numero de la operacion que desea realizar: "))

	if op2 == 1:
		print("\nLa divergencia de la funcion es: ",fGrad(dF, f, 1))

	if op2 == 2:
		print("\nEl rotacional de la funcion es: ",fRot(iCeros(fT,len(dF)), dF))

	if op2 == 3:
		fDf(Df, dF)

	if op2 == 4:
		pass
		

#-------------------------------------------OPCION 9-------------------------------------

#--------------------------------------------------------------------------------

"""
#METODO PARA LLENAR LOS VECTORES CON 0's CON LAS DIMENSIONES DADAS POR EL USUARIO
arr = [[0] * eV for i in range(nV)]

#ESTRUCTURA PARA LLENAR DE 0's UN VECTOR VACIO CON LA DIMENSION DADA POR EL USUSARIO
for x in range(eV):
	suma.append(0)

#ESTRUCTURA QUE LLENA LOS VECTORES CON LOS DATOS DADOS POR EL USUARIO
for n in range(nV):
	print("Ingrese los valores del vector ",n+1,": \n")
	for m in range(eV):
		arr[n][m] = int(input("Valor: "))
		print(arr[n])

for z in range(nV):
	print("Vector ",z+1,": ",arr[z])

print("\nEl vector resultante es: ",sumav2(suma,arr,eV))
print("\nEl producto interno es: ",pInterno(suma))
"""

