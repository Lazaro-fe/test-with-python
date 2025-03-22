# Limpeza do Terminal
import os
os.system('clear')

# Solicitando dados ao Usuário

nome = input("Digite seu nome : ")
idade = float(input("Digite sua idade : "))

# Processamento 

if idade < 16 :
    print("Voto Facultativo! (= )")
elif idade <= 18 :
    print("Voto Opcional! (= )")
elif idade <= 65 : 
    print("É obrigado a votar! (= )")
else :
    print("Não é obrigado a votar!")
