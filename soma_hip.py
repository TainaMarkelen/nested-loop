def eh_hipotenusa(n):
    x = 2
    y = 2
    hip = 0
    é_hip = False
    
    while x < n:
        while y < n and not é_hip:
            if n ** 2 == (x ** 2 + (y ** 2)):
                é_hip = True
            y += 1
        x += 1
        y = 2
    if é_hip:
        hip = n
    return hip
        
def soma_hipotenusa ():
    n = int(input("Informe um número inteiro positivo: "))
    soma = 0
    while n > 0:
        if (eh_hipotenusa(n)) > 0:
            soma += (eh_hipotenusa(n))
        n = n - 1
    return soma
    
if __name__ == '__main__':
    soma_hipotenusa()