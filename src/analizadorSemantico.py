txt = " "
cont = 0
def incremetarContador():
	global cont
	cont +=1
	return "%d" %cont

class Nodo():
	pass

class Null(Nodo):
	def __init__(self):
		self.type = 'void'

	def traducir(self):
		global txt
		id = incremetarContador()
		txt += id+"[label= "+"nodo_nulo"+"]"+"\n\t"

		return id

class program(Nodo):
	def __init__(self,son1,name):
		self.name = name
		self.son1 = son1


	def traducir(self):
		global txt
		id = incremetarContador()

		son1 = self.son1.traducir()

		txt += id +"[label= "+self.name+"]"+"\n\t"

		txt += id +"->"+son1+"\n\t"

		return "digraph G {\n\t"+txt+"}"

class declaracion(Nodo):
	def __init__(self,son1,son2,name):
		self.name = name
		self.son1 = son1
		self.son2 = son2
			
	def traducir(self):
		global txt
		id = incremetarContador()

		if type(self.son1) == type(tuple()):
			son1 = self.son1[0].traducir()
		else:
			son1 = self.son1.traducir()

		if type(self.son2) == type(tuple()):
			son2 = self.son2[0].traducir()
		else:
			son2 = self.son2.traducir()

		

		txt += id + "[label= "+self.name+"]"+"\n\t"
		txt += id + " -> " + son1 + "\n\t"
		txt += id + " -> " + son2 + "\n\t"
		
	

		return id

class list1(Nodo):
	def __init__(self,son1,son2,name):
		self.name = name
		self.son1 = son1
		self.son2 = son2


	def traducir(self):
		global txt
		id = incremetarContador()

		if type(self.son1) == type(tuple()):
			son1 = self.son1[0].traducir()
		else:
			son1 = self.son1.traducir()

		if type(self.son2) == type(tuple()):
			son2 = self.son2[0].traducir()
		else:
			son2 = self.son2.traducir()

		#son1 = self.son1.traducir()

		txt += id +"[label= "+self.name+"]"+"\n\t"
		txt += id +"->"+son1+"\n\t"
		txt += id +"->"+son2+"\n\t"

		return id

class list2(Nodo):
	def __init__(self,son1,son2,name):
		self.name = name
		self.son1 = son1
		self.son2 = son2


	def traducir(self):
		global txt
		id = incremetarContador()

		if type(self.son1) == type(tuple()):
			son1 = self.son1[0].traducir()
		else:
			son1 = self.son1.traducir()

		if type(self.son2) == type(tuple()):
			son2 = self.son2[0].traducir()
		else:
			son2 = self.son2.traducir()

		#son1 = self.son1.traducir()

		txt += id +"[label= "+self.name+"]"+"\n\t"
		txt += id +"->"+son1+"\n\t"
		txt += id +"->"+son2+"\n\t"

		return id


class list3(Nodo):
	def __init__(self,son1,son2,son3,son4,name):
		self.name = name
		self.son1 = son1
		self.son2 = son2
		self.son3 = son3
		self.son4 = son4

			
	def traducir(self):
		global txt
		id = incremetarContador()

		son1 = self.son1.traducir()
		son2 = self.son2.traducir()
		son3 = self.son3.traducir()
		son4 = self.son4.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"
		txt += id + " -> " + son1 + "\n\t"
		txt += id + " -> " + son2 + "\n\t"
		txt += id + " -> " + son3 + "\n\t"
		txt += id + " -> " + son4 + "\n\t"

		return id

class list4(Nodo):
	def __init__(self,son1,son2,son3,son4,name):
		self.name = name
		self.son1 = son1
		self.son2 = son2
		self.son3 = son3
		self.son4 = son4


			
	def traducir(self):
		global txt
		id = incremetarContador()

		son1 = self.son1.traducir()
		son2 = self.son2.traducir()
		son3 = self.son3.traducir()
		son4 = self.son4.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"
		txt += id + " -> " + son1 + "\n\t"
		txt += id + " -> " + son2 + "\n\t"
		txt += id + " -> " + son3 + "\n\t"
		txt += id + " -> " + son4 + "\n\t"

		return id

class type1(Nodo):
	def __init__(self,son1,name):
		self.name = name
		self.son1 = son1

	def traducir(self):
		global txt
		id = incremetarContador()

		son1 = self.son1.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"
		txt += id + " -> " + son1 + "\n\t"

		return id

class type2(Nodo):
	def __init__(self,son1,name):
		self.name = name
		self.son1 = son1
	

	def traducir(self):
		global txt
		id = incremetarContador()

		son1 = self.son1.traducir()
		

		txt += id + "[label= "+self.name+"]"+"\n\t"
		txt += id + " -> " + son1 + "\n\t"
		

		return id



class asignacion(Nodo):
	def __init__(self,son1,son2,son3,name):
		self.name = name
		self.son1 = son1
		self.son2 = son2
		self.son3 = son3


	def traducir(self):
		global txt
		id = incremetarContador()
		
		txt += id + "[label= \""+self.name+"\"]"+"\n\t"

		return id



class numero(Nodo):
	def __init__(self,name):
		self.name = name

	
			
	def traducir(self):
		global txt
		id = incremetarContador()
		txt += id + "[label= "+str(self.name)+"]"+"\n\t"

		return id

class digito(Nodo):
	def __init__(self,name):
		self.name = name

			
	def traducir(self):
		global txt
		id = incremetarContador()
		txt += id + "[label= "+str(self.name)+"]"+"\n\t"

		return id

class assing(Nodo):
	def __init__(self,name):
		self.name = name

			
	def traducir(self):
		global txt
		id = incremetarContador()
		txt += id + "[label= "+str(self.name)+"]"+"\n\t"

		return id

class id(Nodo):
	def __init__(self,name):
		self.name = name

			
	def traducir(self):
		global txt
		id = incremetarContador()
		txt += id + "[label= "+self.name+"]"+"\n\t"

		return id

class delimitador(Nodo):
	def __init__(self,name):
		self.name = name


			
	def traducir(self):
		global txt
		id = incremetarContador()
		txt += id + "[label= "+self.name+"]"+"\n\t"

		return id

class ingr(Nodo):
	def __init__(self,name):
		self.name = name

			
	def traducir(self):
		global txt
		id = incremetarContador()
		txt += id + "[label= "+self.name+"]"+"\n\t"

		return id


# class empty(Nodo):
# 	def __init__(self,name):
# 		pass

