def n_primos (n):
    i = 2
    resto = 1
    quantidade = 0
    primo = True
    while n > 1:
        while i < n and primo:  
            resto = n % i
            i += 1
            if resto == 0:
                primo = False
        if primo:
            quantidade += 1
        n = n - 1
        i = 2
        primo = True
    return quantidade
    
if __name__ == '__main__':
    n = int(input("Digite um número inteiro maior que 2: "))
    n_primos(n)
