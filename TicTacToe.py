jogo = [
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
]


def main():
    player = 1

    explicacao()
    print("=" * 50)
    while True:
        if player == 1:
            peca = "X"
        else:
            peca = "O"

        imprimirJogo()

        while True:
            opcao = input(
                "\nPlayer %d(%s),Em qual posição do tabuleiro voce deseja jogar? "
                % (player, peca))
            try:
                opcao = int(opcao)
            except ValueError:
                print("Opção Inválida")
                continue
            else:
                if opcao in range(1, 10) and verificaJogada(opcao):
                    break
                print("Opção inválida, escolha uma posição vazia entre 1 e 9.")

        jogo[opcao - 1] = peca
        _, venceu = confereSeVenceu(player)
        if venceu:
            break
        if player == 1:
            player = 2
        else:
            player = 1

    imprimirJogo()
    print("Parabéns Player %d, Você venceu!!!" % player)


def explicacao():
    print(" 1 | 2 | 3 \n-----------\n 4 | 5 | 6 \n-----------\n 7 | 8 | 9 ")


def imprimirJogo():
    print(
        " %s | %s | %s \n-----------\n %s | %s | %s \n-----------\n %s | %s | %s"
        % (
            jogo[0],
            jogo[1],
            jogo[2],
            jogo[3],
            jogo[4],
            jogo[5],
            jogo[6],
            jogo[7],
            jogo[8],
        ))


def verificaJogada(choice):
    if jogo[choice - 1] == " ":
        return True
    return False


def confereSeVenceu(player):
    if player == 1:
        if jogo[0] == "X" and jogo[1] == "X" and jogo[2] == "X":
            return 1, True
        if jogo[3] == "X" and jogo[4] == "X" and jogo[5] == "X":
            return 1, True
        if jogo[6] == "X" and jogo[7] == "X" and jogo[8] == "X":
            return 1, True
        if jogo[0] == "X" and jogo[3] == "X" and jogo[6] == "X":
            return 1, True
        if jogo[1] == "X" and jogo[4] == "X" and jogo[7] == "X":
            return 1, True
        if jogo[2] == "X" and jogo[5] == "X" and jogo[8] == "X":
            return 1, True
        if jogo[0] == "X" and jogo[4] == "X" and jogo[8] == "X":
            return 1, True
        if jogo[2] == "X" and jogo[4] == "X" and jogo[6] == "X":
            return 1, True

    elif player == 2:
        if jogo[0] == "O" and jogo[1] == "O" and jogo[2] == "O":
            return 2, True
        if jogo[3] == "O" and jogo[4] == "O" and jogo[5] == "O":
            return 2, True
        if jogo[6] == "O" and jogo[7] == "O" and jogo[8] == "O":
            return 2, True
        if jogo[0] == "O" and jogo[3] == "O" and jogo[6] == "O":
            return 2, True
        if jogo[1] == "O" and jogo[4] == "O" and jogo[7] == "O":
            return 2, True
        if jogo[2] == "O" and jogo[5] == "O" and jogo[8] == "O":
            return 2, True
        if jogo[0] == "O" and jogo[4] == "O" and jogo[8] == "O":
            return 2, True
        if jogo[2] == "O" and jogo[4] == "O" and jogo[6] == "O":
            return 2, True

    return 0, False


main()
