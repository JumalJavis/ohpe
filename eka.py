# Tästä lähtee ensimmäinen demotehtävä

numero1 = int(input("Anna luku 1: "))
numero2 = int(input("Anna luku 2: "))
numero3 = int(input("Anna luku 3: "))

if numero1<numero2 and numero1<numero3:
    print("Pienin luku oli " + str(numero1) + ".")
elif numero2<numero1 and numero2<numero3:
    print("Pienin luku oli " + str(numero2) + ".")
else:
    print("Pienin luku oli " + str(numero3) + ".")


