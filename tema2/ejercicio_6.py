def mejor_candidato(candidatos :list) -> any:
    """ Devuelve el mejor candidato """
    return candidatos[0]

def es_completable(lista :list, candidato :any) -> any:
    """ Comprueba si se puede llegar a la solución usando ese candidato """
    cont = -1
    bool =  True
    for i in lista:
        cont += 1
        if(candidato[0] >= i[1]): 
            return (False,cont)        # Devuelve false si podemos meterlo en una de las pistas que ya teníamos y devuelve tambien la posición de la lista donde deberiamos meter el nuevo horario
    return (bool,cont)


def voraz(candidatos :list) -> list:
    pistas = 0
    lista = []
    if(len(candidatos) > 0):
        candidatos = sorted(candidatos)      # Ordenamos la lista según la hora de entrada 
        lista.append(candidatos[0])        # Añadimos el primer elemento a la lista 
        candidatos = candidatos[1:]        # Y lo eliminamos de candidatos
        pistas = 1
        while len(candidatos) > 0:
            c = mejor_candidato(candidatos)
            candidatos = candidatos[1:] 
            comp = es_completable(lista, c)
            if (comp[0]):                       # Si comp es verdadero se suma una pista y se añade el horario de la pista a la lista 
                pistas += 1
                lista.append(c)
            else:                               # Si es falso se pone en la lista el nuevo horario
                lista[comp[1]] = c

    return pistas

##############################
#          TESTS             #
##############################

def test_voraz():
    horarios = [(10,12),(9,11),(11,13),(12,14),(11,12)]
    resultado = voraz(horarios)
    assert resultado == 3

    horarios1 = []
    resultado1 = voraz(horarios1)
    assert resultado1 == 0
