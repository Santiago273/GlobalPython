from clases import *

def mostrar_ADN(matriz):
    for fila in matriz:
        print(" ".join(fila))
    print()

def main():
    matriz_ADN_Original = ["AGATCA", "GATTCA", "CAACAT", "GAGCTA", "ATTGCG", "CTGTTC"]
    matriz_ADN = ["AGATCA", "GATTCA", "CAACAT", "GAGCTA", "ATTGCG", "CTGTTC"]
    mutado = False  # Variable para verificar si se hizo una mutación

    print("ADN ACTUAL: ")
    mostrar_ADN(matriz_ADN)

    while True:
        opcion = input("¿Desea detectar mutaciones (D), mutar el ADN (M), sanarlo (S) o salir (X)? ").upper()
        
        if opcion == "D":
            detector = Detector(matriz_ADN)
            if detector.detectarMutante(matriz_ADN):
                print("Se ha detectado una mutación en el ADN.")
            else:
                print("No se ha detectado ninguna mutación en el ADN.")
        
        elif opcion == "M":
            cantidadRepetida = 4
            base_valida = False
            while not base_valida:
                try:
                    base = input("Ingrese la base nitrogenada para la mutación (A, T, C, G): ").upper()
                    if base not in "ATCG":
                        raise ValueError(f"La base '{base}' no es válida. Solo se permiten A, T, C, G.")
                    base_valida = True 
                except ValueError as e:
                    print(f"Error: {e}. Intente nuevamente.")
            tipo_valido = False
            while not tipo_valido:
                try:
                    tipo_mutador = input("¿Desea realizar una mutación por Radiación (R) o Virus (V)? ").upper()
                    if tipo_mutador not in "RV":
                        raise ValueError(f"El tipo mutador '{tipo_mutador}' no es válido. Solo se permiten R o V.")
                    tipo_valido = True 
                except ValueError as e:
                    print(f"Error: {e}. Intente nuevamente.")
            
            if tipo_mutador == "R":
                indRadiacion = int(input("Ingrese el indice para la mutación:"))
                orientacion = input("¿Horizontal (H) o Vertical (V)? ").upper()
                mutador = Radiacion(base,cantidadRepetida,matriz_ADN,orientacion,indRadiacion)
                matriz_ADN = mutador.crear_mutante(base, indRadiacion)
            
            elif tipo_mutador == "V":
                indVirus =  int(input("Ingrese le indice para la mutacion"))
                mutador = Virus(base,cantidadRepetida,matriz_ADN,indVirus)
                matriz_ADN = mutador.crear_mutante(base)
            
            mutado = True  # Cambia el valor ya que se ha realizado una mutación
            print("ADN después de la mutación:")
            mostrar_ADN(matriz_ADN)
        
        elif opcion == "S":
            if mutado:
                sanador = Sanador(matriz_ADN_Original)
                matriz_ADN = sanador.sanar_mutantes(matriz_ADN)
                print("ADN después de sanar:")
                mostrar_ADN(matriz_ADN)
                mutado = False  # Resetea el valor después de sanar
            else:
                print("No se ha realizado ninguna mutación para sanar.")
        
        elif opcion == "X":
            print("Saliendo del programa.")
            break
        
        else:
            print("Ingrese una de las opciones dadas anteriormente.")

if __name__ == "__main__":
    main()

#adn = ["AGATCA", "GATTCA", "CAACAT", "GAGCTA", "ATTGCG", "CTGTTC"]

#miadn = Radiacion("A",4,adn,"H",6)
#print(miadn.crear_semilla_horizontal("A",5))
