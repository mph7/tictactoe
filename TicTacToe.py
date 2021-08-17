jogo = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',]
jogador = True ##True == 1, False == 2
def main():
    global XO, jogador
    player = 1
    
   
        
    explicacao()
    print('=' * 50)
    while True:
        if player == 1:
            peca = 'X'
        else:
            peca = 'O'
            
        imprimirJogo()
        
        while True:
            opcao = input('\nPlayer %d(%s),Em qual posição do tabuleiro voce deseja jogar? ' % (player, peca))
            try:
                opcao = int(opcao)
            except:
                print('Opção Inválida')
                continue
            else:
                if opcao in range(1, 10) and verificaJogada(opcao):
                    break
                print('Opção inválida, escolha uma posição vazia entre 1 e 9.')
        
        jogo[opcao-1] = peca
        winner, venceu = confereSeVenceu(player)
        if venceu:
            break
        if player == 1:
            player = 2
        else:
            player = 1


                
    imprimirJogo()
    print('Parabéns Player %d, Você venceu!!!' % player)

def explicacao():
    print(' 1 | 2 | 3 \n-----------\n 4 | 5 | 6 \n-----------\n 7 | 8 | 9 ')


def imprimirJogo():
    print(' %s | %s | %s \n-----------\n %s | %s | %s \n-----------\n %s | %s | %s' % \
          (jogo[0], jogo[1], jogo[2], jogo[3], jogo[4], jogo[5], jogo[6], \
           jogo[7], jogo[8], ))




def verificaJogada(choice):
    if jogo[choice-1] == ' ':
        return True
    return False

def confereSeVenceu(player):
    winnerPlayer = 0
    if player == 1:
        if 'X' == jogo[0] and 'X' == jogo[1] and 'X' == jogo[2]:
            return 1, True
        elif 'X' == jogo[3] and 'X' == jogo[4] and 'X' == jogo[5]:
            return 1, True
        elif 'X' == jogo[6] and 'X' == jogo[7] and 'X' == jogo[8]:
            return 1, True
        elif 'X' == jogo[0] and 'X' == jogo[3] and 'X' == jogo[6]:
            return 1, True
        elif 'X' == jogo[1] and 'X' == jogo[4] and 'X' == jogo[7]:
            return 1, True
        elif 'X' == jogo[2] and 'X' == jogo[5] and 'X' == jogo[8]:
            return 1, True
        elif 'X' == jogo[0] and 'X' == jogo[4] and 'X' == jogo[8]:
            return 1, True
        elif 'X' == jogo[2] and 'X' == jogo[4] and 'X' == jogo[6]:
            return 1, True

    elif player == 2:
        if 'O' == jogo[0] and 'O' == jogo[1] and 'O' == jogo[2]:
            return 2, True
        elif 'O' == jogo[3] and 'O' == jogo[4] and 'O' == jogo[5]:
            return 2, True
        elif 'O' == jogo[6] and 'O' == jogo[7] and 'O' == jogo[8]:
            return 2, True
        elif 'O' == jogo[0] and 'O' == jogo[3] and 'O' == jogo[6]:
            return 2, True
        elif 'O' == jogo[1] and 'O' == jogo[4] and 'O' == jogo[7]:
            return 2, True
        elif 'O' == jogo[2] and 'O' == jogo[5] and 'O' == jogo[8]:
            return 2, True
        elif 'O' == jogo[0] and 'O' == jogo[4] and 'O' == jogo[8]:
            return 2, True
        elif 'O' == jogo[2] and 'O' == jogo[4] and 'O' == jogo[6]:
            return 2, True
    
    return 0, False







main()
