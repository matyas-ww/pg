import math

def je_prvocislo(cislo):
    if cislo <= 1:
        return False
    elif cislo in (2, 3):
        return True
    elif cislo % 2 == 0 or cislo % 3 == 0:
        return False
    for i in range(5, int(math.sqrt(cislo)) + 1, 2):
        if cislo % i == 0:
            return False
    return True  

def vrat_prvocisla(maximum):
    prvocisla = []
    for n in range(2, maximum + 1):
        if je_prvocislo(n):
            prvocisla.append(n)
    return prvocisla


if __name__ == "__main__":
    cislo = int(input("Zadej maximum: "))
    prvocisla = vrat_prvocisla(cislo)
    print(prvocisla)
    print(je_prvocislo(cislo))