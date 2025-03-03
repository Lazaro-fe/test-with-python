import os
os.system("clear")

# Solicitando dados ao Usuário 

primeira_nota = float(input("Digite sua primeira nota : "))
segunda_nota = float(input("Digite sua segunda nota : "))
qualitativo = float(input("Digite sua qualitativo nota : "))

media_escolar = (primeira_nota + segunda_nota + qualitativo) / 3

# Exibindo os dados na tela

print()
print(f"Nota do Teste : {primeira_nota}")
print(f"Nota do Prova : {segunda_nota}")
print(f"Nota do Qualitativo : {qualitativo}")
print(f"Média escolar : {media_escolar:.2f}")