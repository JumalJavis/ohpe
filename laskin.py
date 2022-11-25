# tähän tulee laskin
luku = 0
print("luku on 0.")
while True:
    operaattori = input("Anna operaattori(tyhjä lopettaa): ")
    if operaattori == "":
        break
    if operaattori[0] == "+":
        luku = luku + float(operaattori[1:])
    elif operaattori[0] == "-":
        luku = luku - float(operaattori[1:])
    elif operaattori[0] == "*":
        luku = luku * float(operaattori[1:])
    else:
        luku = luku / float(operaattori[1:])
    print("Luku on "+ str(luku)+".")

print("Kiitos ja moi!")
    
