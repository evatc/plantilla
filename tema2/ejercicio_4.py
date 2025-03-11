U = 0
V = 1
PESO = 2

def ordena_aristas(aristas :list) -> list:
    """ Ordena las aristas por peso de menor a mayor """
    peso = lambda arista: arista[PESO]
    return sorted(aristas, key=peso)

def find(conjuntos :list, u :int) -> set:
    """ Devuelve el conjunto al que pertenece un nodo """
    for conjunto in conjuntos:
        if u in conjunto:
            return conjunto
    return None

def union(conjuntos :list, arista :tuple) -> None:
    """ Actualiza los conjuntos """
    set_u = find(conjuntos, arista[U])
    set_v = find(conjuntos, arista[V])
    if set_u != set_v:
        conjuntos.remove(set_u)
        conjuntos.remove(set_v)
        conjuntos.append(set_u.union(set_v))

def is_bucle(conjuntos :list, arista :tuple) -> bool:
    """ Hay un bucle si los nodos pertenecen al mismo conjunto (algoritmo union-find) """
    set_u = find(conjuntos, arista[U])
    set_v = find(conjuntos, arista[V])
    return set_u == set_v

def kruskal(aristas :list, conjuntos :list) -> list:
    """ Algoritmo de Kruskal """
    aristas = ordena_aristas(aristas)
    solucion = []
    for arista in aristas:
        if not is_bucle(conjuntos, arista):
            solucion.append(arista)
            union(conjuntos, arista)
    return solucion

def sumar(lista: list) -> float:
    cont = 0
    for i in lista:
        cont += i[2]
    return cont

##############################
#          TESTS             #
##############################

def test_sumar():
    nodos = [{'Sevilla'}, {'Madrid'}, {'Barcelona'}, {'Cuenca'}, {'Valencia'}]
    aristas = []
    aristas.append(('Sevilla', 'Madrid', 7))
    aristas.append(('Madrid', 'Barcelona', 5))
    aristas.append(('Madrid', 'Cuenca', 2))
    aristas.append(('Barcelona', 'Valencia', 4))
    aristas.append(('Cuenca', 'Valencia', 3))
    arbol_expansion_minima = kruskal(aristas, nodos)
    resultado = sumar(arbol_expansion_minima)
    assert resultado == 16
