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
            return (False,cont)              #devuelve false si tenemos que cambiar la lista de pista y devuelve la posición en la que tenemos q cambiarlo
    return (bool,cont)


def voraz(candidatos :list) -> list:
    pistas = 0
    lista = []
    if(len(candidatos) > 0):
        candidatos = sorted(candidatos)      #ordenamos la lista según la hora de entrada 
        lista.append(candidatos[0])
        candidatos.remove(candidatos[0])
        pistas = 1
        while len(candidatos) > 0:
            c = mejor_candidato(candidatos)
            candidatos.remove(c)
            comp = es_completable(lista, c)
            if (comp[0]):                       #suma una pista y añade el horario de la pista
                pistas += 1
                lista.append(c)
            else:                               #cambia la lista por el nuevo horario
                lista[comp[1]] = c

    return pistas












