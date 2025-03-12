def mejor_candidato(candidatos :list) -> any:
    return [candidatos[0],candidatos[1]]

def es_completable(solucion :list, candidato :any) -> any:
    # Comprueba si c es mejor candidato que solución,y si lo es, lo cambia 
    if candidato[0] > candidato[1]:
        candidatomax = candidato[0]
        candidatomin = candidato[1]
    else:
        candidatomax = candidato[1]
        candidatomin = candidato[0]
    if(candidatomax > solucion[1]):
        solucion[1] = candidatomax
    if(candidatomin < solucion[0]):
        solucion[0] = candidatomin
    return solucion

def voraz(candidatos :list) -> list:
    solucion = []
    if(len(candidatos) != 0):
        # Si la longitud de la lista es par coge los dos primeros elementos y pone al mayor como máximo y al menor como mínimo
        if(len(candidatos) % 2 == 0):            
            if candidatos[0] > candidatos[1]:
                maximo = candidatos[0]
                minimo = candidatos[1]
            else:
                maximo = candidatos[1]
                minimo = candidatos[0]
            candidatos = candidatos[2:]  # Borra los dos primeros elementos de la lista candidatos
        # Si la longitud de la lista es impar y pone el primer elemento de la lista como máximo y como mínimo
        else:
            maximo = candidatos[0]
            minimo = candidatos[0]
            candidatos = candidatos[1:] # Borra el primer elemento de la lista candidatos

        solucion = [minimo,maximo]
        
        while len(candidatos) > 0:
            c = mejor_candidato(candidatos) # c es los dos nuevos primeros elementos de la lista candidatos
            candidatos.remove(c[0])
            candidatos.remove(c[1])
            es_completable(solucion, c)
    return solucion

##############################
#          TESTS             #
##############################

def test_voraz():
    lista1 = voraz([1,3,2])
    lista2 = voraz([5,1,3,2,4,6])
    lista3 = voraz([])
    assert lista1 == [1, 3]
    assert lista2 == [1, 6]
    assert lista3 == []
