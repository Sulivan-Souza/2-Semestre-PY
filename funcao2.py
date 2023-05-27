def consumo(km, litros):
    if km <= 0:
        return -999
    if litros <= 0:
        return -998
    return km / litros

km = float(input("Digite a quantidade de km percorridos: "))
litros = float(input("Digite a quantidade de litros usados: "))
print("Consumo: %.2f" % consumo(km, litros))
