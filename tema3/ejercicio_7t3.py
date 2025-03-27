def invertir_callejero(callejero):
    n = len(callejero)
    nuevo_callejero = [[0] * n for _ in range(n)]
    
    def dividir_y_vencer(callejero, nuevo_callejero, inicio_fila, fin_fila, inicio_columna, fin_columna):
        if inicio_fila == fin_fila and inicio_columna == fin_columna:
            nuevo_callejero[inicio_columna][inicio_fila] = callejero[inicio_fila][inicio_columna]
        else:
            mitad_fila = (inicio_fila + fin_fila) // 2
            mitad_columna = (inicio_columna + fin_columna) // 2
            
            if inicio_fila <= mitad_fila and inicio_columna <= mitad_columna:
                dividir_y_vencer(callejero, nuevo_callejero, inicio_fila, mitad_fila, inicio_columna, mitad_columna)
            if inicio_fila <= mitad_fila and mitad_columna + 1 <= fin_columna:
                dividir_y_vencer(callejero, nuevo_callejero, inicio_fila, mitad_fila, mitad_columna + 1, fin_columna)
            if mitad_fila + 1 <= fin_fila and inicio_columna <= mitad_columna:
                dividir_y_vencer(callejero, nuevo_callejero, mitad_fila + 1, fin_fila, inicio_columna, mitad_columna)
            if mitad_fila + 1 <= fin_fila and mitad_columna + 1 <= fin_columna:
                dividir_y_vencer(callejero, nuevo_callejero, mitad_fila + 1, fin_fila, mitad_columna + 1, fin_columna)
    
    dividir_y_vencer(callejero, nuevo_callejero, 0, n - 1, 0, n - 1)
    return nuevo_callejero

# Ejemplo de uso
callejero = [
    [0, 1, 0],
    [0, 0, 1],
    [1, 0, 0]
]

nuevo_callejero = invertir_callejero(callejero)
for fila in nuevo_callejero:
    print(fila)
    