# Limpeza do Terminal
import os
os.system("clear")

# Solicitando dados ao Usuário

valor = int(input("Digite o valor da compra : "))
print()

print("""

============================ TIPO DE PAGAMENTO ============================
      
      1-            À vista
      2-            À prazo

""")
print()

escolha = int(input("Digite a forma de Pagamento : "))
print()

match escolha:

    case 1:
        print("--- à vista ---")
        print()
        desconto = (10/100)
        valor_descontado = (valor * desconto)
        total = (valor - valor_descontado)
        print()
        print(f"O valor foi de : {valor} Reais")
        print()
        print(f"Com o desconto de 10% foi de {valor_descontado}")
        print(f"O valor total foi de {total:.1f} Reais")
    
    case 2 :
        print("--- à prazo ---")
        print()
        parcelas = int(input("Digite a quantidade de parcelas : "))
        print()

        if parcelas >= 1 and parcelas <= 6:
            valor_parcelado = (valor/parcelas)
            print(f"O valor foi de : {valor} Reais")
            print()
            print(f"A parcela foi dividida em {parcelas} vezes")
            print()
            print(f"O valor à ser pago a cada mês é de : {valor_parcelado:.1f}")
            print()
        else:
            print("--- Quantidade de parcelas invalida ---")
    case _:
        print("--- OPERAÇÃO INVÁLIDA ---")