if __name__ == '__main__':
    parada = False
    while not parada:
        valor = int(input("Informe um número inteiro positivo: "))
        if valor < 0:
            parada = True
        else:
            mult = 1
            n = valor
            while n > 0:
                mult = mult * n
                n = n - 1
            print("O fatorial de {} é {}".format(valor, mult))
            