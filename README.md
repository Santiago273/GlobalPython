# Proyecto ADN
## Participantes

- Ezequiel Alarcon
- Vera Santiago
- Cornejo Tadeo
- Flores Leandro

## Descripción

El programa implementa un conjunto de funcionalidades para la detección, manipulación y restauración de ADN representado como una matriz de cadenas de texto. Las principales características incluyen:

**Ingreso de ADN**: Permite al usuario ingresar una matriz de ADN fila por fila (cada fila es una cadena de 6 bases: A, T, C, G).  
**Detección de mutaciones**: Verifica si el ADN contiene mutaciones horizontales, verticales o diagonales.  
**Mutación del ADN**: Realiza modificaciones en el ADN utilizando dos tipos de mutadores: Radiación y Virus.  
**Sanación del ADN**: Restaura el ADN a su estado original si este ha sido alterado.

## Instrucciones

El programa presenta un menú interactivo que permite al usuario elegir entre las siguientes opciones:

1. **Ingresar un nuevo ADN (I)**: Permite cargar una nueva matriz de ADN ingresando fila por fila. Cada fila debe tener exactamente 6 bases nitrogenadas válidas (A, T, C, G).  
2. **Detectar mutaciones (D)**: Determina si el ADN tiene mutaciones.  
3. **Mutar el ADN (M)**:  
   - Solicita la base nitrogenada (A, T, C, G).  
   - Permite elegir entre mutaciones por Radiación (horizontales o verticales) o Virus (diagonales).  
4. **Sanar el ADN (S)**: Si el ADN fue mutado, lo restaura a su versión inicial.  
5. **Salir (X)**: Termina el programa.

## Caso de ejemplo

Ejemplo de ADN inicial:  
El ADN se representa como una matriz de cadenas de texto:

AGATCA
GATTCA
CAACAT
GAGCTA
ATTGCG
CTGTTC


El programa le pedirá al usuario que ingrese una de las siguientes opciones:

1. Ingresar un nuevo ADN (I): Carga una nueva matriz fila por fila.
2. Detectar mutaciones (D): Detecta si hay mutaciones horizontales, verticales o diagonales.
3. Mutar el ADN (M): Solicita al usuario la base nitrogenada para realizar la mutación (A, T, C, G) y el tipo de mutador (Radiación o Virus).
4. Sanar el ADN (S): Si el ADN ha sido mutado, se restaurará a su versión original.
5. Salir (X): Sale del programa.

## Ejemplo de ejecución:

ADN ACTUAL:
AGATCA
GATTCA
CAACAT
GAGCTA
ATTGCG
CTGTTC

## Ingreso de ADN

Entrada:

I
Fila 1: AGATCA
Fila 2: GATTCA
Fila 3: CAACAT
Fila 4: GAGCTA
Fila 5: ATTGCG
Fila 6: CTGTTC

Salida:

ADN ingresado con éxito:
AGATCA
GATTCA
CAACAT
GAGCTA
ATTGCG
CTGTTC


## Detección de mutaciones

Entrada: D

Salida: "No se ha detectado ninguna mutación en el ADN."

## Mutación del ADN

Entrada:

M
Ingrese la base nitrogenada: A
¿Desea realizar una mutación por Radiación (R) o Virus (V)? R
Ingrese el índice para la mutación: 2
¿Horizontal (H) o Vertical (V)? H

Salida:
ADN después de la mutación:
AGATCA
AAAACA
CAACAT
GAGCTA
ATTGCG
CTGTTC

## Sanación del ADN

Entrada: S
Salida:

ADN después de sanar:
AGATCA
GATTCA
CAACAT
GAGCTA
ATTGCG
CTGTTC

Clases principales
- Detector
    Contiene métodos para detectar mutaciones en las tres direcciones (horizontal, vertical y diagonal).

- Radiación
    Clase hija de Mutador que realiza mutaciones horizontales o verticales.

- Virus
    Clase hija de Mutador que realiza mutaciones diagonales.

- Sanador
    Clase responsable de restaurar el ADN a su estado original si este ha sido alterado.

## Output esperado

1. Si el ADN es mutado, se muestra el ADN después de la mutación.
2. Si el ADN es sanado, se muestra el ADN restaurado a su estado original.