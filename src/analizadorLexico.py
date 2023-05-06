import ply.lex as lex
import re
import codecs
import os
import sys


reservadas = ['NUMERO','SERVIR','RECETA','AGREGAR','INGR','TIEMPO','ECC','ESCRIBIR','LEER','UTCL','REPETIR','MIRAR','SEGUIR','COCINAR','MEZCLAR','RETIRAR','USAR','CORTAR']
tokens = reservadas+['TIME','COMILLAS','ALLAVE','CLLAVE','ACORC','CCORC','DELIMITADOR','ID','ASSIGN','DIGITO','APARENT','CPARENT','CMAYOR','AMENOR']



t_ignore = '\t '
t_ASSIGN = r'='
t_APARENT = r'\('
t_CPARENT = r'\)'
t_ALLAVE = r'\{'
t_CLLAVE = r'\}'
t_ACORC = r'\['
t_CCORC = r'\]'
t_AMENOR = r'\<<'
t_CMAYOR = r'\>>'
t_DELIMITADOR = r'\;'
t_COMILLAS = r'\"'



def t_ID(t):
	r'[a-zA-Z_][a-zA-Z0-9_]*'
	if t.value.upper() in reservadas:
		t.value = t.value.upper()
		#reservadas.get(t.value,'ID')
		t.type = t.value

	return t

def t_newline(t):
	r'\n+'
	t.lexer.lineno += len(t.value)

#dsfjksdlgjklsdgjsdgslxcvjlk-,.
def t_COMMENT(t):
	r'\#.*'
	pass

def t_TIME(t):
	r'[1-9][0-9]*s'
	return t

def t_DIGITO(t):
	r'\d+'
	t.value = int(t.value)
	return t



def t_error(t):
	print "caracter ilegal '%s'" % t.value[0]
	t.lexer.skip(1)

#def buscarFicheros(directorio):
# 	ficheros = []
#	numArchivo = ''
# 	respuesta = False
# 	cont = 1

# 	for base, dirs, files in os.walk(directorio):
# 		ficheros.append(files)
# 	for file in files:
# 		print str(cont)+". "+file
# 		cont = cont+1

# 	while respuesta == False:
# 		numArchivo = raw_input('\nNumero del test: ')
# 		for file in files:
# 			if file == files[int(numArchivo)-1]:
# 				respuesta = True
# 				break

# 	print "Has escogido \"%s\" \n" %files[int(numArchivo)-1]

# 	return files[int(numArchivo)-1]

#directorio = '/home/dev/Documentos/analizador version 3/test/'
#archivo = buscarFicheros(directorio)
#test = directorio+archivo
#fp = codecs.open(test,"r","utf-8")
#cadena = fp.read()
#fp.close()

analizador = lex.lex()

#analizador.input(cadena)

#while True:
# 	tok = analizador.token()
# 	if not tok : break
# 	print tok


