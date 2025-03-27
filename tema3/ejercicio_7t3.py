def trasponer_matriz(matriz):
    n = len(matriz)
    solucion = []
    for i in range (n): # Crea una matriz cuadrada de 0
        fila = [0]*n
        solucion.append(fila)
    
    def dividir(matriz, solucion, inicio_fila, fin_fila, inicio_columna, fin_columna):
        if inicio_fila == fin_fila and inicio_columna == fin_columna:
            solucion[inicio_columna][inicio_fila] = matriz[inicio_fila][inicio_columna]
        else:
            mitad_fila = (inicio_fila + fin_fila) // 2
            mitad_columna = (inicio_columna + fin_columna) // 2
            
            if inicio_fila <= mitad_fila and inicio_columna <= mitad_columna:
                dividir(matriz, solucion, inicio_fila, mitad_fila, inicio_columna, mitad_columna)
            if inicio_fila <= mitad_fila and mitad_columna + 1 <= fin_columna:
                dividir(matriz, solucion, inicio_fila, mitad_fila, mitad_columna + 1, fin_columna)
            if mitad_fila + 1 <= fin_fila and inicio_columna <= mitad_columna:
                dividir(matriz, solucion, mitad_fila + 1, fin_fila, inicio_columna, mitad_columna)
            if mitad_fila + 1 <= fin_fila and mitad_columna + 1 <= fin_columna:
                dividir(matriz, solucion, mitad_fila + 1, fin_fila, mitad_columna + 1, fin_columna)
    
    dividir(matriz, solucion, 0, n - 1, 0, n - 1)
    return solucion

##############################
#          TESTS             #
##############################

def test_trasponer_matriz():
    matriz = [
    [0, 1, 0],
    [0, 0, 1],
    [1, 0, 1]
    ]
    matriz_traspuesta = trasponer_matriz(matriz)
    assert matriz_traspuesta == [[0,0,1],[1,0,0],[0,1,1]]
    
