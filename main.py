import menus

opcoes_tela_inicial = {
    1: "tela_cardapio",
    2: "tela_funcionarios",
    3: "tela_aberto",
    4: "tela_dados",
    5: "sair"
}

while True:
    escolha = menus.tela_inicial()
    tela = opcoes_tela_inicial.get(escolha)
    if tela == "sair":
        print("\nAté mais!")
        break
            