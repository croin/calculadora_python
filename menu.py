# -*- coding: utf-8 -*-
from funciones.suma import suma

import sys

def menu():
	opcion = -1

	operacion = {1:suma}

	while opcion != 5:
		opcion = int(raw_input("""escoja una opción
		1)suma (+)
		5)Salir
		:"""))
		
		operacion[opcion]()

	sys.exit()