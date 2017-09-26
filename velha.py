def initTabuleiro():
    marcador = "X"
    lista = [" "," "," "," "," "," "," "," "," "]
    print("7 | 8 | 9")
    print("-------------")
    print("4 | 5 | 6")
    print("-------------")
    print("1 | 2 | 3")  
    return lista

def tabuleiro():
    print(" {l[7]} | {l[8]} | {l[9]}".format(l = lista))
    print("-------------")
    print(" {l[4]} | {l[5]} | {l[6]}".format(l = lista))
    print("-------------")
    print(" {l[1]} | {l[2]} | {l[3]}".format(l = lista))

def jogada():
    if marcador = "X":
        print("Jogador 1 escolha uma posição:")
    else:
        print("Jogador 2 escolha uma posição:")
    
    posicao = input()     
    
    if marcador = "X":
        marcador = "O"
    else:
        marcador= "X"
    
    return posicao


def checkfull():
    i = 0
    while i < 9:
        if lista[i] == " ":
            return False
    return True

def coluna():
    for i in range(3):
        if lista[i] != " " and (lista[i] == lista[i+3] and lista[i+3] == lista[i+6]):
            return True
    return False

def linha():
    for i in range(7):
        if i%3 == 0:
            if lista[i] != " " and (lista[i] == lista[i+1] and lista[i+1] == lista[i+2]):
                return True
    return False

def diagonal():
    if lista[4] != " " and (lista[0] == lista[4] and lista[4] == lista[8]) or (lista[2] == lista[4] and lista[4] == lista[6]):
        return True
    return False

def verificar():
    if diagonal() or linha() or coluna():
        return True
    else:
        return False

def main():
    marcador = initTabuleiro()
    lista = []
    fim = False
   
    while fim:
        jog = jogada()
        if lista[jog] == " ":
            lista[jog] = marcador
                if verificar():
                    if marcador = "X":
                        print("Jogador 1 Venceu!")
                    else:
                        print("Jogador 2 Venceu!")
                    fim = True
            if checkfull():
                print("Empate")
                fim = True
            
        else:
            print("Escolha outra posição:") 
    

main()
