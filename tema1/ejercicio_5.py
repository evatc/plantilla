import math

def es_primo(numero: int) -> bool:
    """Determina si un número es primo."""
    assert numero >= 0,  """tiene que ser positivo o cero"""
    if numero < 2:
        return False  # 0 y 1 no son primos
    else:
        raiz = math.isqrt(numero)  # Raíz cuadrada entera
        for i in range(2, raiz + 1):  # Revisar hasta la raíz cuadrada
            if numero % i == 0:
                return False  # Si es divisible, no es primo

    return True  # Si no encontró divisores, es primo


##############################
#          TESTS             #
##############################

def test_es_primo():
    numero1 = es_primo(5)
    numero2 = es_primo(6)
    numero3 = es_primo(0)
    assert numero1 == True
    assert numero2 == False
    assert numero3 == False

