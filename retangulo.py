if __name__ == '__main__':
    largura = int(input("Informe a largura: "))
    altura = int(input("Informe a altura: "))
    a = 1
    l = 1
    
    while a <= altura:
        while l <= largura:
            print ("#", end = "")
            l += 1
        a += 1
        print ()
        l = 1