def n_rainhas(n):
    """Retorna (quantidade_de_solucoes, quantidade_de_passos)."""
    tabuleiro = [-1] * n
    solucoes = 0
    passos = 0

    def seguro(linha, coluna):
        nonlocal passos
        for linha_anterior in range(linha):
            passos += 1
            coluna_anterior = tabuleiro[linha_anterior]

            # mesma coluna ou mesma diagonal
            if coluna_anterior == coluna:
                return False
            if abs(coluna_anterior - coluna) == abs(linha_anterior - linha):
                return False

        return True

    def buscar(linha):
        nonlocal solucoes, passos
        passos += 1  # chamada recursiva

        if linha == n:
            solucoes += 1
            return

        for coluna in range(n):
            if seguro(linha, coluna):
                tabuleiro[linha] = coluna
                buscar(linha + 1)
                tabuleiro[linha] = -1

    if n < 1:
        return 0, passos

    buscar(0)
    return solucoes, passos


if __name__ == "__main__":
    while True:
        n = int(input("\nDigite n: "))

        solucoes, passos = n_rainhas(n)

        print(f"Soluções: {solucoes}")
        print(f"Passos: {passos}")

        continuar = input(
            "\nDeseja testar outro valor de n? (s/n): "
        ).lower()

        if continuar != "s":
            print("\nPrograma encerrado.")
            input("Pressione ENTER para fechar...")
            break
