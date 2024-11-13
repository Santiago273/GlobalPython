import clases
adn=["TGATCA", "GGTTCA", "CATCAT", "GAGTTA", "ATTGCG", "CTGGTC"]

#Instancia de la clase Detector
miAdn = clases.Detector(adn)

#Instacia de la clase Radiacion
miRaiactivo = clases.Radiacion('A',4,adn,'H',2)

#Instancia de la clase Virus
miVirus = clases.Virus('A',4,adn, 2)

#Detector de mutante
print(miAdn.detectarMutante(adn))

#Creacion de mutante Radiactivo
print(miRaiactivo.crear_mutante('A', 1))

#Creacion de mutante con Virus
print(miVirus.crear_mutante('C'))




