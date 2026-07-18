import shutil

largura, altura = shutil.get_terminal_size()

def tela_inicial(saldo: float) -> int:
    """
    Exibe a interface da tela inicial.
    
    Parâmetros:
        saldo (float): O saldo atual a ser exibido.
    
    Retorna:
        int: A escolha do usuário.
    """
    
    while True:
        print(f"Saldo: R$ {saldo:.2f}\n")
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

def tela_funcionarios(funcionarios: list) -> int:
    """
    Exibe a tela de gerenciamento de funcionários.
    
    Parâmetros:
        funcionarios (list): Lista de funcionarios.
        
    Retorna:
        int: A escolha do usuário.
    """
    while True:
        funcionarios_contratados = [u for u in funcionarios if u.contratado]
        for i in funcionarios_contratados:
            print(str(i))
            
        print(f"{len(funcionarios_contratados) + 1}: Contratar mais funcionários")
        print(f"{len(funcionarios_contratados) + 2}: Voltar")
    
        try:
            escolha = int(input("\n>> "))
            
            if escolha >= 1 and escolha <= len(funcionarios_contratados) + 2:
                return escolha
            else:
                print("Opção inválida, tente novamente.\n")
                        
        except ValueError:
            print("Por favor, digite apenas números inteiros.\n")
            
def tela_contratar_funcionarios(funcionarios: list) -> int | None:
    """
    Exibe a tela de contratação de funcionários.
    
    Parâmetros:
        funcionarios (list): Lista de funcionarios.
        
    Retorna:
        int | None: Escolha do usuário, ou None quando não houverem
        funcionários contratáveis.
    """
    
    while True:
        funcionarios_disponiveis = [f for f in funcionarios if f.contratavel and not f.contratado]
        
        if not funcionarios_disponiveis:
            print("Não existem funcionários disponíveis para contratação.\n")
            return None
        
        for i in funcionarios_disponiveis:
            print(str(i))
            
        print(f"{len(funcionarios_disponiveis) + 1}: Voltar")
            
        try:
            escolha = int(input("\n>> "))
            
            if escolha >= 1 and escolha <= len(funcionarios_disponiveis) + 1:
                return escolha
            else:
                print("Opção inválida, tente novamente.\n")
                        
        except ValueError:
            print("Por favor, digite apenas números inteiros.\n")
            
def tela_detalhes_funcionario(funcionarios: list, id: int) -> bool:
    """
    Exibe a tela de detalhes de um funcionário.
    
    Parâmetros:
        funcionarios (list): Lista de funcionários.
        id (int): ID do funcionáio a serem exibidos os detalhes.
        
    Retorna:
        bool: True se o usuário quiser demitir o funcionário, False se
        quiser manter o funcionario contratado.
    """
    
    funcionario = next((obj for obj in funcionarios if obj.id == id), None)
    
    while True:
        print(f"{funcionario.nome} - {funcionario.funcao}")
        print(f"Salário: R$ {funcionario.salario:.2f}")
        print(f"Idade: {funcionario.idade}")
        
        escolha = input("Deseja demitir esse funcionário (S/N): ")
        
        if escolha.upper() in ("S", "SIM"):
            return True
        elif escolha.upper() in ("N", "NAO, NÃO"):
            return False
        else:
            print("Opção inválida, tente novamente.\n")