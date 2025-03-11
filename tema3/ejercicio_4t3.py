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
    if(len(arrayb) != 0 and len(arrayc) != 0):
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
