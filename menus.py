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
            
