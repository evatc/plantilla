# Algoritmia y Complejidad Curso 2024-25
# Esqueleto de trabajo en Python

import sys
import mylib
import tema1.ejercicio_8
import tema1.ejercicio_5
import tema2.ejercicio_3
import tema2.ejercicio_4
import tema2.ejercicio_6
import tema3.ejercicio_4

def main(args :list[str]) -> bool:
    #print(tema1.ejercicio_5.es_primo(5))
    #print(tema1.ejercicio_8.inverso(627))
    #print(tema2.ejercicio_3.voraz([1,3,2]))
    """nodos = [{'Sevilla'}, {'Madrid'}, {'Barcelona'}, {'Cuenca'}, {'Valencia'}]
    aristas = []
    aristas.append(('Sevilla', 'Madrid', 7))
    aristas.append(('Madrid', 'Barcelona', 5))
    aristas.append(('Madrid', 'Cuenca', 2))
    aristas.append(('Barcelona', 'Valencia', 4))
    aristas.append(('Cuenca', 'Valencia', 3))
    arbol_expansion_minima = tema2.ejercicio_4.kruskal(aristas, nodos)
    for arista in arbol_expansion_minima:
        print(arista)
    print("El coste total es: " + str(tema2.ejercicio_4.sumar(arbol_expansion_minima)))
    print("El número de pistas necesario es de " + str(tema2.ejercicio_6.voraz([(10,12),(9,11),(11,13),(12,14),(11,12)])))"""
    print(tema3.ejercicio_4.robot([10,15,5,7],[5,10,7,15]))

if __name__ == '__main__': # Si este modulo es el principal
    if '--test' in sys.argv: # Si existe "--test" en la linea de argumentos
        import pytest
        import glob
        pytest.main( sys.argv[2:] + # Le pasamos el resto de argumentos (launch.json)
            glob.glob("**/*.py", recursive=True) ) # Ruta de los archivos para buscar los tests
    else:
        main(sys.argv) # Ejecutamos el programa principal
