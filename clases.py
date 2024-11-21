import random

class Detector:
    adn = []
    def __init__(self, adn):
        self.adn = adn

    def detectarMutanteHorizontal(self, adn):

        for filas in adn:

            contador = 0
            contador1 = 0
            contador2 = 0
            contador3 = 0

            for base in filas:
                if base == 'A':
                    contador += 1
                    if contador >= 4:
                        return True
                elif base == 'T':
                    contador1 += 1
                    if contador1 >= 4:
                        return True
                elif base == 'C':
                    contador2 += 1
                    if contador2 >= 4:
                        return True
                elif base == 'G':
                    contador3 += 1
                    if contador3 >= 4:
                        return True
        return False


    def detectorDeMutantesVertical(self, adn):
        num_columnas = len(adn[0])
        resultado = []

        for j in range(num_columnas):
            conteo = {'A': 0, 'T': 0, 'C': 0, 'G': 0}
            for fila in adn:
                conteo[fila[j]] += 1
            resultado.append(conteo)

        for i, columna in enumerate(resultado):
            if columna['A'] >= 4:
                return True
            elif columna['T'] >= 4:
                return True
            elif columna['C'] >= 4:
                return True
            elif columna['G'] >= 4:
                return True

        return False

    def detectorDeMutantesDiagonal(self, adn):
        n = len(adn)
        diagonal_principal = []
        diagonal_secundaria = []
        conteoPrincipal1 = 0
        conteoPrincipal2 = 0
        conteoPrincipal3 = 0
        conteoPrincipal4 = 0
        conteoSecundario1 = 0
        conteoSecundario2 = 0
        conteoSecundario3 = 0
        conteoSecundario4 = 0

        for i in range(n):
            # Diagonal principal
            diagonal_principal.append(adn[i][i])
            # Diagonal secundaria
            diagonal_secundaria.append(adn[i][n - i - 1])
        for i in diagonal_principal:
            if i == 'A':
                conteoPrincipal1 += 1
                if conteoPrincipal1 >= 4:
                    return True
            elif i == 'T':
                conteoPrincipal2 += 1
                if conteoPrincipal2 >= 4:
                    return True
            elif i == 'C':
                conteoPrincipal3 += 1
                if conteoPrincipal3 >= 4:
                    return True
            elif i == 'G':
                conteoPrincipal4 += 1
                if conteoPrincipal4 >= 4:
                    return True
        for i in diagonal_secundaria:
            if i == 'A':
                conteoSecundario1 += 1
                if conteoSecundario1 >= 4:
                    return True
            elif i == 'T':
                conteoSecundario2 += 1
                if conteoSecundario2 >= 4:
                    return True
            elif i == 'C':
                conteoSecundario3 += 1
                if conteoSecundario3 >= 4:
                    return True
            elif i == 'G':
                conteoSecundario4 += 1
                if conteoSecundario4 >= 4:
                    return True

        return False

    def detectarMutante(self,adn):
        if self.detectorDeMutantesDiagonal(adn) or self.detectorDeMutantesVertical(adn) or self.detectarMutanteHorizontal(adn):
            return True

        return False

class Mutador:
    base_nitrogenada = ""
    cantidad_repetida = 0
    adn = []
    indice = 0

    def __init__(self, base_nitrogenada, cantidad_repedida, adn, indice):
        self.base_nitrogenada = base_nitrogenada
        self.cantidad_repetida = cantidad_repedida
        self.adn = adn
        self.indice = indice


    def crear_mutante(self):
        return


####**Clase Radiacion**
"""Clase hija de Mutador. La radiación solo crea mutantes horizontales y verticales.
Esta clase debe contener:
  - El atributo base_nitrogenada, la cual especificará cuál de las bases se repetirá 4 veces.
  - Por lo menos 2 atributo más que consideren pertinentes. 
Pueden ser los heredados de su clase padre.
  - Método constructor (init) con sus argumentos para definir los atributos 
al instanciar un objeto.
  - Método crear_mutante. Éste debe tener los argumentos base_nitrogenada, 
  posicion_inicial (para saber dónde insertar la mutación) y 
  orientacion_de_la_mutacion (posibles valores: "H" de horizontal o "V" de vertical) 
  y devolver la matriz con las modificaciones pertinentes. 
  Debe incluir manejo de errores (bloques try-except)."""

class Radiacion(Mutador):
    orientacion = ''

    def __init__(self, base_nitrogenada, cantidad_repedida, adn, orientacion, indice, max_mutaciones=10):
        super().__init__(base_nitrogenada, cantidad_repedida,adn, indice)
        self.orientacion = orientacion
        self.max_mutaciones = max_mutaciones

    def crear_semilla_horizontal(self, base, ind):
        miAdn = self.adn

        if not isinstance(miAdn, list):
            raise TypeError("miAdn debe ser una lista")
        if not isinstance(base, str) or len(base) != 1:
            raise ValueError("base debe ser un string de un solo caracter")
        if ind < 0 or ind >= len(miAdn):
            raise IndexError("El índice ind está fuera de rango")

        try:
            fila = list(miAdn[ind])  # Convertimos la fila en una lista mutable
            cantidad = self.cantidad_repetida

            for i in range(min(cantidad, len(fila))):  # Modificamos hasta `cantidad` elementos
                fila[i] = base

            miAdn[ind] = "".join(fila)  # Convertimos de nuevo la lista a string
            return miAdn
        except IndexError as e:
            print(f"Se ha producido un error de índice: {e}")
            return None

    def crear_semilla_vertical(self, base, ind):
        miAdn = self.adn
        cantidad = self.cantidad_repetida

        if not isinstance(miAdn, list):
            raise TypeError("miAdn debe ser una lista")
        if not isinstance(base, str) or len(base) != 1:
            raise ValueError("base debe ser un string de un solo caracter")
        if ind < 0 or ind >= len(miAdn[0]):
            raise IndexError("El índice ind está fuera de rango")
        try:
            for i in range(min(cantidad, len(miAdn))):  # Modificamos hasta `cantidad` filas
                fila = list(miAdn[i])  # Convertimos la fila en una lista mutable
                fila[ind] = base  # Cambiamos el carácter en la posición de la columna
                miAdn[i] = "".join(fila)  # Convertimos de nuevo la lista a string
            return miAdn
        except IndexError:
            print("Se ha producido un error de índice. Verifica los datos de entrada.")

    def crear_mutante(self, base_nitrogenada, posicion_inicial):
        ori = self.orientacion
        if ori == 'H':
            return self.crear_semilla_horizontal(base_nitrogenada, posicion_inicial-1)
        elif ori == 'V':
            return self.crear_semilla_vertical(base_nitrogenada, posicion_inicial-1)

""""**Clase Virus
 Clase hija de Mutador. Los virus solo crean mutantes diagonales.Esta clase debe contener:
 - El atributo base_nitrogenada, la cual especificará cuál de las bases se repetirá 4 veces.
 - Por lo menos 2 atributos más que consideren pertinentes. Pueden ser los heredados de su clase padre.
 - Método constructor (init) con sus argumentos para definir los atributos al instanciar un objeto.
 - Método crear_mutante. Éste debe tener los argumentos base_nitrogenada y posicion_inicial 
 (para saber dónde insertar la mutación) y devolver la matriz con las modificaciones pertinentes. 
 Debe incluir manejo de errores (bloques try-except)."""


class Virus(Mutador):

    def __init__(self, base_nitrogenada, cantidad_repedida, adn, indice, num_max_mutaciones=10):
        super().__init__(base_nitrogenada, cantidad_repedida, adn, indice)
        self.num_max_mutaciones = num_max_mutaciones
        self.contador_mutaciones = 0


    def crear_semilla_diagonal(self, base):
        miAdn = self.adn
        cantidad = self.cantidad_repetida

        if not isinstance(miAdn, list):
            raise TypeError("miAdn debe ser una lista")
        if not isinstance(base, str) or len(base) != 1:
            raise ValueError("base debe ser un string de un solo caracter")
        if cantidad > len(miAdn):
            raise ValueError("cantidad no puede ser mayor que el tamaño de miAdn")

        try:
            for i in range(len(miAdn)):
                secuencia = base
                miAdn[i] = list(miAdn[i])
                miAdn[i][i] = "".join(secuencia)
                miAdn[i] = "".join(miAdn[i])
            return miAdn
        except IndexError:
            print("Se ha producido un error de índice. Verifica los datos de entrada.")
            return None

    def crear_mutante(self, base_nitrogenada):

        return self.crear_semilla_diagonal(base_nitrogenada)



"""**Clase Sanador**
Debe contener:
  - Por lo menos 2 atributos que consideren pertinentes.
  - Método constructor (init) con sus argumentos para definir los atributos al instanciar un objeto.
  - Método sanar_mutantes, encargado de sanar cualquier tipo de mutación. Éste debe tener como argumento la matriz de ADN, revisar si existen mutaciones y, si las hay, generar aleatoriamente un ADN completamente nuevo que **no** tenga mutaciones y retornarlo. Consejo: esta clase va a necesitar el método detectar_mutante, que ya lo han definido en otra clase!
"""

class Sanador:
    def __init__(self, ADN:list):
        try:
            self.bases_nitrogenadas = ["A","C","G","T"]
            self.ADN = ADN
            self.detectar_mutantes(self.ADN)
            self.sanar_mutantes(self.ADN)
        except Exception:
            pass

    def detectar_mutantes(self, ADN:list):
        detector = Detector(ADN)
        return True if detector.detectarMutante(ADN) == True else False
    
    def sanar_mutantes(self,ADN:list):
        if self.detectar_mutantes(ADN) == True:
            while self.detectar_mutantes(ADN) == True:
                for i in range(0, 6):
                    palabra = list(ADN[i])
                    for j in range(len(palabra)):
                        palabra[j] = random.choice(self.bases_nitrogenadas)
                    palabra = ''.join(palabra)
                    ADN[i] = palabra
                self.ADN = ADN
                self.detectar_mutantes(ADN)
        return self.ADN