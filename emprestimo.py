def analisar_credito(renda, parcela):
    if renda > 2000 and parcela <= 0.3 * renda:
        return "Aprovado"
    elif renda <= 2000:
        return "Negado: Renda insuficiente"
    else:
        return "Negado: Parcela alta"


r = float(input("Renda: "))
p = float(input("Parcela: "))


resultado = analisar_credito(r, p)
print(resultado)