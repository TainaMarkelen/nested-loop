if __name__ == '__main__':
    largura = int(input("Informe a largura: "))
    altura = int(input("Informe a altura: "))
    a = 1
    l = 1
    
    while a <= altura:
        while l <= largura:
            if a == altura or l == largura:
                print ("#", end = "")
            elif (a > 1 and l > 1):
                print (" ", end = "")
            else:
                print ("#", end = "")
            l += 1
        a += 1
        print ()
        l = 1