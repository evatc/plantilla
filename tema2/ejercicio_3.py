def mejor_candidato(candidatos :list) -> any:
    """ Devuelve el mejor candidato """
    return [candidatos[0],candidatos[1]]

def es_completable(solucion :list, candidato :any) -> any:
    """ Comprueba si se puede llegar a la solución usando ese candidato """
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
        if(len(candidatos) % 2 == 0):
            if candidatos[0] > candidatos[1]:
                maximo = candidatos[0]
                minimo = candidatos[1]
            else:
                maximo = candidatos[1]
                minimo = candidatos[0]
            candidatos = candidatos[2:]
        else:
            maximo = candidatos[0]
            minimo = candidatos[0]
            candidatos = candidatos[1:]

        solucion = [minimo,maximo]
        
        while len(candidatos) > 0:
            c = mejor_candidato(candidatos)
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