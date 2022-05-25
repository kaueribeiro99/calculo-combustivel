from calculo import Calculo


def main():
    print(
        """
        Esta aplicação tem como finalidade demonstrar os valores que serão gastos 
        com combustível durante uma viagem, com base no consumo do seu veículo, e 
        com a distância determinada por você!
        """
    )

    print("Os combustíveis disponíveis para este cálculo são:")
    print("\t° Álcool")
    print("\t° Díesel")
    print("\t° Gasolina")

    print(" ")

    try:
        distancia = float(input("Digite a distância em quilômetros a ser percorrida: "))
        consumo = float(input("Digite o consumo de combustível do veículo (Km/l): "))
        calculo = Calculo()
        print(
            calculo.calcular_gasto(distancia, consumo)
        )
    except ValueError as erro:
        print("O valor recebido não é valido"), erro


if __name__ == "__main__":
    main()
