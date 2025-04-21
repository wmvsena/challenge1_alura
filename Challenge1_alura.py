import pandas as pd

url = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science/refs/heads/main/base-de-dados-challenge-1/loja_1.csv"
url2 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science/refs/heads/main/base-de-dados-challenge-1/loja_2.csv"
url3 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science/refs/heads/main/base-de-dados-challenge-1/loja_3.csv"
url4 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science/refs/heads/main/base-de-dados-challenge-1/loja_4.csv"

loja = pd.read_csv(url)
loja2 = pd.read_csv(url2)
loja3 = pd.read_csv(url3)
loja4 = pd.read_csv(url4)

loja.head()
#
# Faturamento por loja
faturamento_loja = loja['Preço'].sum()
faturamento_loja2 = loja2['Preço'].sum()
faturamento_loja3 = loja3['Preço'].sum()
faturamento_loja4 = loja4['Preço'].sum()

print(f'Loja 01: R$ {faturamento_loja:,.2f}')
print(f'Loja 02: R$ {faturamento_loja2:,.2f}')
print(f'Loja 03: R$ {faturamento_loja3:,.2f}')
print(f'Loja 04: R$ {faturamento_loja4:,.2f}')

#Grafico de Barras do Faturamento
import matplotlib.pyplot as plt


lojas = ['Loja 1', 'Loja 2', 'Loja 3', 'Loja 4']
faturamentos = [faturamento_loja, faturamento_loja2, faturamento_loja3, faturamento_loja4]


plt.figure(figsize=(8, 5))
barras = plt.bar(lojas, faturamentos, color='skyblue')
plt.bar(lojas, faturamentos, color='skyblue')
plt.title('Faturamento por Loja - Gráfico de Barras')
plt.ylabel('Faturamento (R$)')
plt.xlabel('Lojas')
plt.grid(axis='y', linestyle='--', alpha=0.7)
for barra, valor in zip(barras, faturamentos):
    plt.text(barra.get_x() + barra.get_width() / 2, 
             barra.get_height() + 20000,  
             f'R$ {valor:,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.'),
             ha='center', va='bottom', fontsize=9, fontweight='bold')
plt.tight_layout()
plt.show()

#Vendas por Categoria
from collections import Counter
quantidade_categoria = Counter(loja['Categoria do Produto'])
quantidade_categoria2 = Counter(loja2['Categoria do Produto'])
quantidade_categoria3 = Counter(loja3['Categoria do Produto'])
quantidade_categoria4 = Counter(loja4['Categoria do Produto'])

categorias_ordenadas = sorted(quantidade_categoria.items(), key=lambda x: x[1], reverse=True)
categorias_ordenadas2 = sorted(quantidade_categoria2.items(), key=lambda x: x[1], reverse=True)
categorias_ordenadas3 = sorted(quantidade_categoria3.items(), key=lambda x: x[1], reverse=True)
categorias_ordenadas4 = sorted(quantidade_categoria4.items(), key=lambda x: x[1], reverse=True)

print("Quantidade de vendas por categoria Loja 01:\n")

print("Categoria".ljust(26) + "Quantidade")
print("-" * 40)

for categoria, quantidade in categorias_ordenadas:
  print(f"{categoria.ljust(21)} {str(quantidade).rjust(7)} vendas")

print("\n" * 1)
print("Quantidade de vendas por categoria Loja 02:\n")

print("Categoria".ljust(26) + "Quantidade")
print("-" * 40)

for categoria, quantidade in categorias_ordenadas2:
  print(f"{categoria.ljust(21)} {str(quantidade).rjust(7)} vendas")

print("\n" * 1)

print("Quantidade de vendas por categoria Loja 03:\n")

print("Categoria".ljust(26) + "Quantidade")
print("-" * 40)

for categoria, quantidade in categorias_ordenadas3:
  print(f"{categoria.ljust(21)} {str(quantidade).rjust(7)} vendas")

print("\n" * 1)

print("Quantidade de vendas por categoria Loja 04:\n")

print("Categoria".ljust(26) + "Quantidade")
print("-" * 40)

for categoria, quantidade in categorias_ordenadas4:
  print(f"{categoria.ljust(21)} {str(quantidade).rjust(7)} vendas")

print("\n" * 1)

#Grafico de Pizza por Categoria
#Loja 02
plt.figure(figsize=(6, 6))
plt.pie(list(quantidade_categoria.values()), labels=list(quantidade_categoria.keys()), autopct='%1.1f%%', startangle=140, 
        colors=['#66b3ff','#99ff99','#ffcc99','#ff9999'])  
plt.title('Quantidade de Vendas por Categoria (Loja 01)') 
plt.tight_layout()
plt.show()

print("\n" * 2)

#Loja 02
plt.figure(figsize=(6, 6))
plt.pie(list(quantidade_categoria2.values()), labels=list(quantidade_categoria2.keys()), autopct='%1.1f%%', startangle=140, 
        colors=['#66b3ff','#99ff99','#ffcc99','#ff9999'])  
plt.title('Quantidade de Vendas por Categoria (Loja 02)')
plt.tight_layout()
plt.show()

print("\n" * 2)

# Loja 03
plt.figure(figsize=(6, 6))
plt.pie(list(quantidade_categoria3.values()), labels=list(quantidade_categoria3.keys()), autopct='%1.1f%%', startangle=140, 
        colors=['#66b3ff','#99ff99','#ffcc99','#ff9999'])  
plt.title('Quantidade de Vendas por Categoria (Loja 03)') 
plt.tight_layout()
plt.show()


print("\n" * 2)

# Loja 04
plt.figure(figsize=(6, 6))
plt.pie(list(quantidade_categoria4.values()), labels=list(quantidade_categoria4.keys()), autopct='%1.1f%%', startangle=140, 
        colors=['#66b3ff','#99ff99','#ffcc99','#ff9999'])  
plt.title('Quantidade de Vendas por Categoria (Loja 04)') 
plt.tight_layout()
plt.show()

# Média de Avaliação das Lojas
from collections import Counter
avaliacao = Counter(loja['Avaliação da compra'].tolist())
avaliacao = Counter(loja2['Avaliação da compra'].tolist())
avaliacao = Counter(loja3['Avaliação da compra'].tolist())
avaliacao = Counter(loja4['Avaliação da compra'].tolist())

def media_avaliacao(loja):
  avaliacoes = loja['Avaliação da compra'].tolist()
  return sum(avaliacoes) / len(avaliacoes) if avaliacoes else 0

print(f'Média de avaliação da Loja 01:  {media_avaliacao(loja):.2f}')
print(f'Média de avaliação da Loja 02:  {media_avaliacao(loja2):.2f}')
print(f'Média de avaliação da Loja 03:  {media_avaliacao(loja3):.2f}')
print(f'Média de avaliação da Loja 04:  {media_avaliacao(loja4):.2f}')

#Grafico da avaliacão por loja
import matplotlib.pyplot as plt

lojas = ['Loja 1', 'Loja 2', 'Loja 3', 'Loja 4']


medias = [media_avaliacao(loja), media_avaliacao(loja2),
          media_avaliacao(loja3), media_avaliacao(loja4)]


plt.figure(figsize=(8, 5))
plt.plot(lojas, medias, marker='o', color='purple', linewidth=2, linestyle='-')
plt.title('Média de Avaliação por Loja')
plt.xlabel('Lojas')
plt.ylabel('Média de Avaliação')
plt.ylim(0, 5)
plt.grid(True, linestyle='--', alpha=0.5)

# Adiciona os valores em cima dos pontos
for i, media in enumerate(medias):
    plt.text(lojas[i], media + 0.1, f'{media:.2f}', ha='center', fontsize=9)

plt.tight_layout()
plt.show()

# Produtos Mais e Menos Vendidos
from collections import Counter

# Supondo que você já tenha os dados carregados:
quantidade_produtos = Counter(loja['Produto'])
quantidade_produtos2 = Counter(loja2['Produto'])
quantidade_produtos3 = Counter(loja3['Produto'])
quantidade_produtos4 = Counter(loja4['Produto'])

# Função para encontrar mais e menos vendidos
def exibir_mais_menos_vendidos(nome_loja, contador):
    if not contador:
        print(f"{nome_loja}: Sem dados de vendas.")
        return

    mais_vendido = contador.most_common(1)[0]
    menos_vendido = min(contador.items(), key=lambda x: x[1])

    print(f"\n📊 {nome_loja}")
    print(f"➡️  Produto mais vendido: {mais_vendido[0]} ({mais_vendido[1]} vendas)")
    print(f"⬅️  Produto menos vendido: {menos_vendido[0]} ({menos_vendido[1]} vendas)")

# Exibindo para cada loja
exibir_mais_menos_vendidos("Loja 1", quantidade_produtos)
exibir_mais_menos_vendidos("Loja 2", quantidade_produtos2)
exibir_mais_menos_vendidos("Loja 3", quantidade_produtos3)
exibir_mais_menos_vendidos("Loja 4", quantidade_produtos4)

# Frete Médio por Loja
from collections import Counter
avaliacao = Counter(loja['Frete'].tolist())
avaliacao = Counter(loja2['Frete'].tolist())
avaliacao = Counter(loja3['Frete'].tolist())
avaliacao = Counter(loja4['Frete'].tolist())

def media_frete(loja):
  fretes = loja['Frete'].tolist()
  return sum(fretes) / len(fretes) if fretes else 0

print(f'Média de frete da Loja 01:  {media_frete(loja):.2f}')
print(f'Média de frete da Loja 02:  {media_frete(loja2):.2f}')
print(f'Média de frete da Loja 03:  {media_frete(loja3):.2f}')
print(f'Média de frete da Loja 04:  {media_frete(loja4):.2f}')

# Grafico media do frete por loja
lojas = ['Loja 1', 'Loja 2', 'Loja 3', 'Loja 4']

medias = [media_frete(loja), media_frete(loja2),
          media_frete(loja3), media_frete(loja4)]

# Gráfico de área
plt.figure(figsize=(8, 5))
plt.scatter(lojas, medias, color='darkorange', s=100)
#plt.fill_between(lojas, medias, color='skyblue', alpha=0.5)
plt.plot(lojas, medias, marker='o', color='blue', linewidth=2)

plt.title('Média de Frete por Loja')
plt.xlabel('Lojas')
plt.ylabel('Valor Médio do Frete (R$)')
plt.grid(True, linestyle='--', alpha=0.6)

# Mostra os valores no gráfico
for i, media in enumerate(medias):
    plt.text(lojas[i], media + 0.1, f'R${media:.2f}', ha='center')

plt.tight_layout()
plt.show()