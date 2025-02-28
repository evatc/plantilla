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
    if(len(candidatos) % 2 == 0):
        if candidato[0] > candidato[1]:
            maximo = candidato[0]
            minimo = candidato[1]
        else:
            maximo = candidato[1]
            minimo = candidato[0]
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

