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