def inverso(n: int) -> str:
    assert n >= 0, """El número debe ser mayor a 0"""
    numero = str(n)  # Convert the number to string
    if len(numero) == 1:
        return numero
    else:
        # Recursive call to invert the rest of the string and append the first digit at the end
        return inverso(int(numero[1:])) + numero[0]



##############################
#          TESTS             #
##############################

def test_inverso():
    numero1 = inverso(627)
    assert numero1 == str(726)