
estoque_atual = {}
print("=== CADASTRO DO ESTOQUE INICIAL ===")
print("Digite pelo menos 8 produtos e suas quantidades.\n")

while len(estoque_atual) < 8:
    produto = input("Nome do produto: ").strip().lower()
    quantidade = int(input(f"Quantidade inicial de {produto}: "))
    estoque_atual[produto] = quantidade

print("\nEstoque inicial cadastrado com sucesso!\n")


movimentacoes_dia = [
    ("canetas", "saída", 25),
    ("cadernos", "entrada", 10),
    ("borrachas", "saída", 50),
    ("lapis", "saída", 40),
    ("marcadores", "entrada", 30),
    ("pastas", "saída", 10),
    ("reguas", "saída", 40),
    ("canetas", "entrada", 50),
    ("borrachas", "entrada", 15),
    ("marcadores", "saída", 60),
    ("cadernos", "saída", 30),
    ("pastas", "entrada", 25),
    ("apontadores", "entrada", 40),  
    ("colas", "entrada", 60)         
]


for produto, tipo, quantidade in movimentacoes_dia:
    if produto not in estoque_atual and tipo == "entrada":
        estoque_atual[produto] = 0  

    if tipo == "entrada":
        estoque_atual[produto] += quantidade
    elif tipo == "saída":
        estoque_atual[produto] -= quantidade
        if estoque_atual[produto] < 0:
            estoque_atual[produto] = 0  


produtos_baixo = [p for p, q in estoque_atual.items() if q <= 50]


print("\n=== RELATÓRIO FINAL DE ESTOQUE ===")
for produto, quantidade in estoque_atual.items():
    print(f"{produto.capitalize()}: {quantidade} unidades")

print("\n=== PRODUTOS QUE PRECISAM DE REPOSIÇÃO (<=50) ===")
if produtos_baixo:
    for p in produtos_baixo:
        print(f"- {p.capitalize()} ({estoque_atual[p]} unidades)")
else:
    print("Nenhum produto precisa de reposição.")
