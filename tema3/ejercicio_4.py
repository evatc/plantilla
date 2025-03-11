import random

def robot(arrayb :list, arrayc :list) -> any:
    listar = []
    recursiva(arrayb, arrayc, listar)
    return listar


def recursiva(arrayb :list, arrayc :list,arrayr :list) -> any:
    listaizqb = []
    listadchab = []
    listaizqc = []
    listadchac = []
    if(len(arrayb) != 0):
        pivote = arrayb[0]      
        for corcho in arrayc:
            if pivote>corcho:
                listaizqc.append(corcho)
            elif pivote<corcho:
                listadchac.append(corcho)
            else:
                arrayr.append([corcho,pivote])

        pivote = arrayr[-1][0]  #Coge el mismo pivote que en lo anterior, pero coge el corcho para compararlo con las botellas
        for botella in arrayb:
            if pivote>botella:
                listaizqb.append(botella)
            elif pivote<botella:
                listadchab.append(botella)
        recursiva(listaizqb,listaizqc,arrayr)
        recursiva(listadchab,listadchac,arrayr)

    return arrayr
