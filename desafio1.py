"""
    FAZER UM PROCEDIMENTO QUE PEGUE DOIS NUMEROS POR PARAMENTRO E EXIBA 
    OS NUMEROS DO INTERVALO

    EX.: intervalo(2,9)
    >> 2 3 4 5 6 7 8 9
"""

def intervalo(n1, n2):
    for i in range(n1, n2 + 1):
        print(i, "", end="")

intervalo(2, 11)