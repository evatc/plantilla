def robot(lbotellas :list, lcorchos :list) -> any:
    resultado = []
    def recursiva(lbotellas :list, lcorchos :list,resultado :list) -> any:
        listaizqb = []
        listadchab = []
        listaizqc = []
        listadchac = []
        assert len(lbotellas) == len(lcorchos)  # Comprueba que lbotellas y lcorchos tengan el mismo número de elementos
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
