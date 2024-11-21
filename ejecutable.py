from clases import *

def mostrar_ADN(matriz):
    for fila in matriz:
        print(" ".join(fila))
    print()

def ingresar_ADN():
    print("Ingrese el ADN fila por fila (una cadena de 6 bases: A, T, C, G):")
    matriz = []
    while len(matriz) < 6:
        fila = input(f"Fila {len(matriz) + 1}: ").strip().upper()
        if len(fila) == 6 and all(base in "ATCG" for base in fila):
            matriz.append(list(fila))  # Guardar como lista de caracteres para mutabilidad
        else:
            print("Error: La fila debe contener exactamente 6 bases válidas (A, T, C, G).")
    
    detector = Detector(matriz)
    es_mutante = detector.detectarMutante(matriz)
    if es_mutante:
        print("--------------------------------")
        print("El ADN ingresado tiene mutaciones. Procediendo a sanarlo...")
        sanador = Sanador(matriz)
        matriz = sanador.sanar_mutantes(matriz)
        print("ADN sanado correctamente.")
    return matriz



def main():
    matriz_ADN = []

    while True:
        # Se le pide al usuario que ingrese un ADN si no hay uno cargado
        if not matriz_ADN:
            print("No hay ADN cargado. Por favor, ingrese uno.")
            matriz_ADN = ingresar_ADN()
        
        print("--------------------------------")
        print("ADN ACTUAL:")
        mostrar_ADN(matriz_ADN)    
        
        opcion = input("¿Desea ingresar un nuevo ADN (I), detectar mutaciones (D), mutar el ADN (M), sanarlo (S) o salir (X)? ").upper()
        
        if opcion == "I":
            matriz_ADN = ingresar_ADN()
        
        elif opcion == "D":
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
                indRadiacion = int(input("Ingrese el índice para la mutación: "))
                orientacion = input("¿Horizontal (H) o Vertical (V)? ").upper()
                mutador = Radiacion(base, cantidadRepetida, matriz_ADN, orientacion, indRadiacion)
                matriz_ADN = mutador.crear_mutante(base, indRadiacion)
            
            elif tipo_mutador == "V":
                indVirus = int(input("Ingrese el índice para la mutación: "))
                mutador = Virus(base, cantidadRepetida, matriz_ADN, indVirus)
                matriz_ADN = mutador.crear_mutante(base)
            
            mutado = True  # Cambia el valor ya que se ha realizado una mutación
            print("ADN después de la mutación:")
            mostrar_ADN(matriz_ADN)
        
        elif opcion == "S":
            sanador = Sanador(matriz_ADN)  # Usamos el nuevo Sanador sin depender de ADN original
            matriz_ADN = sanador.sanar_mutantes(matriz_ADN)
            print("ADN después de sanar:")
            mostrar_ADN(matriz_ADN)
            mutado = False  # Resetea el valor después de sanar
        
        elif opcion == "X":
            print("Saliendo del programa.")
            break
        
        else:
            print("Ingrese una de las opciones dadas anteriormente.")

if __name__ == "__main__":
    main()