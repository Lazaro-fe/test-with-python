# Limpeza do Terminal
import os
os.system("clear")
os.system('cls'if os.name == 'nt' else 'clear')

# Solicitando Dados ao Usuário

nome_do_usuario = input("Informe seu nome completo : ")
serie_escolar = input("Digite sua série escolar : ")
nota_do_teste = float(input("Digite sua nota do teste : "))
nota_da_prova = float(input("Digite sua nota da prova : "))
nota_do_qualitativo = float(input("Digite sua nota do qualitativo : "))

media_escolar = (nota_do_teste + nota_da_prova + nota_do_qualitativo) / 3
os.system('cls'if os.name == 'nt' else 'clear')

# Exibindo resulotados

print()
print(f"Nome completo da pessoa : {nome_do_usuario}")
print(f"Série escolar : {serie_escolar}")
print(f"Nota do Teste : {nota_do_teste}")
print(f"Nota da Prova : {nota_da_prova}")
print(f"Nota do qualitativo : {nota_do_qualitativo}")
print(f"Nota da Média : {media_escolar:.2f}")