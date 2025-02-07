# Algoritmia y Complejidad Curso 2024-25
# Esqueleto de trabajo en Python

import sys
import mylib
import ejercicio_5


def main(args :list[str]) -> bool:
    print(ejercicio_5.es_primo(5))


if __name__ == '__main__': # Si este modulo es el principal
    if '--test' in sys.argv: # Si existe "--test" en la linea de argumentos
        import pytest
        import glob
        pytest.main( sys.argv[2:] + # Le pasamos el resto de argumentos (launch.json)
            glob.glob("**/*.py", recursive=True) ) # Ruta de los archivos para buscar los tests
    else:
        main(sys.argv) # Ejecutamos el programa principal
