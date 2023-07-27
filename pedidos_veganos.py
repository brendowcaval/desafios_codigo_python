numPedidos = int(input())
pedidos = []

for i in range(1, numPedidos + 1):
    prato = input()
    calorias = int(input())
    ehVegano = input()

    ehVegano = "Vegano" if ehVegano == "s" else "Nao-vegano"

    pedidos.append(f"Pedido {i}: {prato} ({ehVegano}) - {calorias} calorias")

for pedido in pedidos:
    print(pedido)

