import os

renda = 0
parcela = 0
totalEmprestado = 0

def exibir_subtitulo(texto):
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def simularParcelas():
    valorEmprestimo = float(input("Digite o valor para empréstimo: "))
    parcelas = float(input("Digite o numero de parcelas: "))
    
    valor_com_juros = valorEmprestimo * (1 + (0.02 * parcelas))
    valor_parcela = valor_com_juros / parcelas
    
    print("-" * 30)
    print(f"VALOR DA PARCELA: R$ {valor_parcela:>10.2f}")
    print(f"TOTAL COM JUROS:  R$ {valor_com_juros:>10.2f}")
    print("-" * 30)

def verificaNome():
    while True:
        nomeCliente = input("Digite seu nome: ")
       
        if nomeCliente.replace(" ", "").isalpha(): 
            return nomeCliente
        else:
            os.system('cls')
            print("Erro: O nome deve conter apenas letras!")

def analiseBancaria():
    nomeCliente = verificaNome()
    try:
        renda = float(input("Renda: "))
        parcela = float(input("Parcela desejada: "))
        
        resultado = analisar_credito(renda, parcela)
        print(f"Olá {nomeCliente}, seu resultado: {resultado}")

        if resultado == "Aprovado":
            exibir_subtitulo("SIMULAÇÃO: Aprovado")
            simularParcelas()
        else:
            print("Infelizmente não podemos seguir com a simulação agora.")
        
        
    except ValueError:
        print("\nERRO: Por favor, use apenas números e ponto para valores (ex: 2500.50).")

    
def analisar_credito(renda, parcela):
    try:
        if renda > 2000 and parcela <= 0.3 * renda:
            return "Aprovado"
        elif renda <= 2000:
            return "Negado: Renda insuficiente"
        else:
            return "Negado: Parcela alta"
    except ValueError:
        print("\nERRO: Por favor, use apenas números e ponto para valores (ex: 2500.50).")
def deseja_continuar():
    continuar = input("\nDeseja atender outro cliente? (S/N): ").upper()
    return continuar == 'S' 

def main():
    while True:
        exibir_subtitulo("EMPRÉSTIMO BANCÁRIO")
        analiseBancaria()
        
        if not deseja_continuar():
            os.system('cls')
            print("Sistema encerrado. Até logo!")
            break
        

  

if __name__ == "__main__":
    main()  