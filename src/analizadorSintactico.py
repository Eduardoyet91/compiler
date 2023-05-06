import ply.yacc as yacc
import os
import codecs
import re
from analizadorLexico import tokens
from sys import stdin
from analizadorSemantico import *


precedence = (
	('right','ID'),	
	('left','MEZCLAR','CORTAR'),
	('left','APARENT','CPARENT'),
	)

def p_program(p):
	'''program : declaracion'''
	print "programa"
	p[0] = program(p[1],"programa")

def p_declaracion(p):
	'''declaracion : list DELIMITADOR'''
	print "declaracion"
	p[0] = declaracion(p[1],delimitador(p[2]),"Declaracion")


def p_list1(p):
	'''list : INGR ID'''
	print "content ID"
	p[0] = list1(ingr(p[1]),id(p[2]),"list")

def p_list2(p):
	'''list : NUMERO ID'''
	print "content ID"
	p[0] = list2(numero(p[1]),id(p[2]),"list")

def p_list3(p):
	'''list : list DELIMITADOR INGR ID'''
	print "content1 LIST ; ID"
	p[0] = list3(p[1],delimitador(p[2]),ingr(p[3]),id(p[4]),"list")

def p_list4(p):
	'''list : list DELIMITADOR NUMERO ID'''
	print "content1 LIST ; ID"
	p[0] = list3(p[1],delimitador(p[2]),numero(p[3]),id(p[4]),"list")

def p_type1(p):
	'''type : INGR'''
	print "content ID"
	p[0] = type1(ingr(p[1]),"type1")

def p_type2(p):
	'''type : NUMERO'''
	print "content ID"
	p[0] = type2(numero(p[1]),"type2")

def p_asignacion(p):
	'''asignacion : ID ASSIGN DIGITO'''
	print "content ID"
	p[0] = asignacion(id(p[1]),assing(p[2]),digito(p[3]),"asignacion")


def p_error(p):
	print "Error de sintaxis ", p
	#print "Error en la linea "+str(p.lineno)

def p_empty(p):
	'''empty :'''
	pass

def buscarFicheros(directorio):
	ficheros = []
	numArchivo = ''
	respuesta = False
	cont = 1

	for base, dirs, files in os.walk(directorio):
		ficheros.append(files)

	for file in files:
		print str(cont)+". "+file
		cont = cont+1

	while respuesta == False:
		numArchivo = raw_input('\nNumero del test: ')
		for file in files:
			if file == files[int(numArchivo)-1]:
				respuesta = True
				break

	print "Has escogido \"%s\" \n" %files[int(numArchivo)-1]

	return files[int(numArchivo)-1]

def traducir(result):
	graphFile = open('graphviztrhee.vz','w')
	graphFile.write(result.traducir())
	graphFile.close()
	print "El programa traducido se guardo en \"graphviztrhee.vz\""

directorio = '/home/dev/Documentos/analizador version 3/test/'
archivo = buscarFicheros(directorio)
test = directorio+archivo
fp = codecs.open(test,"r","utf-8")
cadena = fp.read()
fp.close()

parser = yacc.yacc()
result = yacc.parse(cadena)

#result.imprimir(" ")
#print result.traducir()
traducir(result)



#print result















