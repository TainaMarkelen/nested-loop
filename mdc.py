if __name__ == '__main__':
    n = 1
    while n > 0:
        n = int(input("Informe um número inteiro positivo: "))
        
        i = 2
        divisor = 0
        while i <= n:
            if n % i == 0:
                divisor = i
            i += 1
                    