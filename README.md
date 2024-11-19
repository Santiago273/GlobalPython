# Proyecto ADN
## Participantes

- Ezequiel Alarcon

## Descripción

El programa permite realizar las siguientes operaciones sobre una matriz de ADN representada por cadenas de texto:

1. **Detección de mutaciones**: El programa permite verificar si el ADN tiene mutaciones horizontales, verticales o diagonales.
2. **Mutación del ADN**: Se pueden realizar mutaciones en el ADN utilizando dos tipos de mutadores: **Radiación** y **Virus**.
3. **Sanación del ADN**: El ADN puede ser "sanado", restaurándolo a su estado original si ha sido mutado.

## Instrucciones

El programa solicitará al usuario que elija una de las siguientes opciones:

1. **Detectar mutaciones (D)**: Detecta si hay mutaciones horizontales, verticales o diagonales.
2. **Mutar el ADN (M)**: Se solicita al usuario la base nitrogenada para realizar la mutación (A, T, C, G) y el tipo de mutador (Radiación o Virus).
3. **Sanar el ADN (S)**: Si el ADN ha sido mutado, se restaurará a su versión original.
4. **Salir (X)**: Sale del programa.

## Caso de ejemplo

Entrada
El programa inicializa un ADN con el siguiente valor:

AGATCA
GATTCA
CAACAT
GAGCTA
ATTGCG
CTGTTC

El programa le pedirá al usuario que ingrese una de las siguientes opciones:

1. Detectar mutaciones (D): Detecta si hay mutaciones horizontales, verticales o diagonales.
2. Mutar el ADN (M): Se solicita al usuario la base nitrogenada para realizar la mutación (A, T, C, G) y el tipo de   mutador (Radiación o Virus).
3. Sanar el ADN (S): Si el ADN ha sido mutado, se restaurará a su versión original.
4. Salir (X): Sale del programa.

## Ejemplo de ejecución:

ADN ACTUAL:
AGATCA
GATTCA
CAACAT
GAGCTA
ATTGCG
CTGTTC

¿Desea detectar mutaciones (D), mutar el ADN (M), sanarlo (S) o salir (X)? M
Ingrese la base nitrogenada para la mutación (A, T, C, G): T
¿Desea realizar una mutación por Radiación (R) o Virus (V)? R
Ingrese la fila inicial para la mutación: 1
Ingrese la columna inicial para la mutación: 3
¿Horizontal (H) o Vertical (V)? H
ADN después de la mutación:
AGATCA
GATTTC
CAACAT
GAGCTA
ATTGCG
CTGTTC

¿Desea detectar mutaciones (D), mutar el ADN (M), sanarlo (S) o salir (X)? S
ADN después de sanar:
AGATCA
GATTCA
CAACAT
GAGCTA
ATTGCG
CTGTTC

## Output esperado

1. Si el ADN es mutado, se muestra el ADN después de la mutación.
2. Si el ADN es sanado, se muestra el ADN restaurado a su estado original.