valorHamburguer = float(input())
quantidadeHamburguer = int(input())
valorBebida = float(input())
quantidadeBebida = int(input())
valorPago = float(input())

valor_total_hamburgueres = valorHamburguer * quantidadeHamburguer
valor_total_bebida = valorBebida * quantidadeBebida
preco_total = valor_total_bebida + valor_total_hamburgueres
troco = valorPago - preco_total

print(f"O preço final do pedido é R$ {preco_total:.2f}. Seu troco é R$ {troco:.2f}.")

