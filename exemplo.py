# SUBALGORITMOS
"""

"""

# procedimentos
def saudacao() -> None:
    print("Aoba")

def saudacao2(nome: str) -> None:
    print(f"Aoba {nome}")

def saudacao3(nome: str, hora: int) -> None:
    if hora  < 12:
        msg = "Bom dia"
    elif hora  < 18:
        msg = "Boa tarde"
    else:
        msg = "Boa noite"

    print(f"{msg} {nome}")

# funções
from math import sqrt
raiz = sqrt(25)

def raiz_quadrada(n: int) -> int:
    resp = n ** (1/2)
    return resp

# programa principal
saudacao()

nm = "erick"
saudacao2("erick")
saudacao2(nm)

saudacao3(nm, 11)

print(raiz)
print(raiz_quadrada(81))