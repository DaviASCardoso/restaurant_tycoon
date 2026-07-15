import shutil

largura, altura = shutil.get_terminal_size()

def tela_inicial() -> int:
    """
    Exibe a interface da tela inicial.
    
    Retorna:
        int: A escolha do usuário.
    """
    
    while True:
        print("1 - Gerenciar cardápio")
        print("2 - Gerenciar funcionários")
        print("3 - Abrir restaurante")
        print("4 - Gerenciar meus dados")
        print("5 - Sair")
   
        try:
            escolha = int(input("\n>> "))
            
            if escolha >= 1 and escolha <= 5:
                return escolha
            else:
                print("Opção inválida, tente novamente.\n")
                        
        except ValueError:
            print("Por favor, digite apenas números inteiros.\n")
            
def tela_cardapio(itens: list) -> int:
    """
    Exibe a interface do cardápio.
    
    Parâmetros:
        itens (list): Lista dos itens do cardápio.
    
    Retorna:
        int: A escolha do usuário.
    """
    
    while True:
        itens_desbloqueados = [u for u in itens if u.desbloqueado]
        for i in itens_desbloqueados:
            print(str(i))
            
        print(f"{len(itens_desbloqueados) + 1}: Voltar")
        
        try:
            escolha = int(input("\n>> "))
            
            if escolha >= 1 and escolha <= len(itens_desbloqueados) + 1:
                return escolha
            else:
                print("Opção inválida, tente novamente.\n")
                        
        except ValueError:
            print("Por favor, digite apenas números inteiros.\n")
    
def tela_editar_item() -> tuple[str, float]:
    """
    Exibe a tela de edição de item.
    
    Retorna:
        tuple[str, float]: uma tupla contendo:
            - nome (str): O novo nome escolhido pelo usuário.
            - preco (float): O novo valor escolhido pelo usuário.
    """
    
    novo_nome = str(input("Digite o novo nome do item: "))
    
    while True:
        try:
            novo_preco = float(input("Digite o novo preco do item: "))
            break
        except ValueError:
            print("Por favor, digite apenas números.\n")
            
    return novo_nome, novo_preco
