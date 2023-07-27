def main():
    n = int(input())
 
    total = 0
 
    for i in range(1, n + 1):
        pedido = input().split(" ")
        nome = pedido[0]
        valor = float(pedido[1])
        total += valor
    desconto = input()

    if desconto == "10%":
        total_com_desconto = total - ( (total / 100) * 10)
    elif desconto == "20%":
        total_com_desconto = total - ( (total / 100) * 20)
    
    print(f"Valor total: {total_com_desconto:.2f}")
 
 
 
 
if __name__ == "__main__":
    main()