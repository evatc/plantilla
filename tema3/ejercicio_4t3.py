def robot(lbotellas :list, lcorchos :list) -> any:
    assert len(lbotellas) == len(lcorchos)  # Comprueba que lbotellas y lcorchos tengan el mismo número de elementos
    resultado = []
    def recursiva(lbotellas :list, lcorchos :list,resultado :list) -> any:
        listaizqb = []
        listadchab = []
        listaizqc = []
        listadchac = []
        if(len(lbotellas) != 0 and len(lcorchos) != 0):
            pivote = lbotellas[0]      
            for corcho in lcorchos:
                if pivote>corcho:
                    listaizqc.append(corcho)
                elif pivote<corcho:
                    listadchac.append(corcho)
                else:
                    resultado.append([corcho,pivote])

            pivote = resultado[-1][0]  #Coge el mismo pivote que en lo anterior, pero coge el corcho para compararlo con las botellas
            for botella in lbotellas:
                if pivote>botella:
                    listaizqb.append(botella)
                elif pivote<botella:
                    listadchab.append(botella)
            recursiva(listaizqb,listaizqc,resultado)
            recursiva(listadchab,listadchac,resultado)

        return resultado
    return recursiva(lbotellas, lcorchos, resultado)



##############################
#          TESTS             #
##############################

def test_robot():
    botellas = [10,15,5,7]
    corchos = [5,10,7,15]
    resultado = robot(botellas,corchos)
    assert resultado == [[10, 10], [5, 5], [7, 7], [15, 15]]

    botellas1 = []
    corchos1 = [3,2]
    resultado1 = robot(botellas1, corchos1)
    assert resultado1 == []

    botellas2 = [3,2]
    corchos2 = []
    resultado2 = robot(botellas2,corchos2)
    assert resultado2 == []



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
