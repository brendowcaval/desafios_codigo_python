nomeRestaurante = input()
tempoEstimadoEntrega = int(input())


if tempoEstimadoEntrega <= 4:
    print("Esse tempo estimado de entrega não é possível!")
else:
    print(f"O restaurante {nomeRestaurante} entrega em {tempoEstimadoEntrega} minutos.")

