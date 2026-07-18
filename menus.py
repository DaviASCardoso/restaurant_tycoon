from enum import Enum, auto
from collections import namedtuple
from funcionarios import Funcionario

EntradaMenu = namedtuple("EntradaMenu", ["acao", "alvo", "rotulo"])

class AcaoFuncionario(Enum):
    SELECIONAR = auto()
    CONTRATAR = auto()
    DEMITIR = auto()
    VOLTAR = auto()
    IR_PARA_CONTRATACAO = auto()

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

def tela_funcionarios(funcionarios: list) -> tuple[AcaoFuncionario, Funcionario | None]:
    """
    Exibe a tela de gerenciamento de funcionários.
    
    Parâmetros:
        funcionarios (list): Lista de funcionarios.
        
    Retorna:
        tuple[AcaoFuncionario, Funcionario | None]: uma tupla contendo:
            - AcaoFuncionario: Ação (Ex.: SELECIONAR, VOLTAR).
            - Funcionario | None: Objeto Funcionario como alvo quando 
            a ação pedir um, ou None quando a ação não pede alvo.
    """
    while True:
        funcionarios_contratados = [u for u in funcionarios if u.contratado]
        entradas = []
        for f in funcionarios_contratados:
            entradas.append(EntradaMenu(AcaoFuncionario.SELECIONAR, f, str(f)))
                        
        entradas.append(EntradaMenu(AcaoFuncionario.IR_PARA_CONTRATACAO, None, "Contratar mais funcionários"))
        entradas.append(EntradaMenu(AcaoFuncionario.VOLTAR, None, "Voltar"))

        for pos, entrada in enumerate(entradas, 1):
            print(f"{pos}: {entrada.rotulo}")
        
        try:
            escolha = int(input("\n>> "))
            
            if escolha >= 1 and escolha <= len(entradas):
                entrada = entradas[escolha - 1]
                return entrada.acao, entrada.alvo
            else:
                print("Opção inválida, tente novamente.\n")
                        
        except ValueError:
            print("Por favor, digite apenas números inteiros.\n")
            
def tela_contratar_funcionarios(funcionarios: list) -> tuple[AcaoFuncionario, Funcionario | None]:
    """
    Exibe a tela de contratação de funcionários.
    
    Parâmetros:
        funcionarios (list): Lista de funcionarios.
        
    Retorna:
        tuple[AcaoFuncionario, Funcionario | None]: Uma tupla contendo:
            - AcaoFuncionario: Ação (Ex.: CONTRATAR, VOLTAR).
            - Funcionario | None: Objeto Funcionario como alvo quando 
            a ação pedir um, ou None quando a ação não pede alvo.
    """
    
    while True:
        funcionarios_disponiveis = [f for f in funcionarios if f.contratavel and not f.contratado]
        
        if not funcionarios_disponiveis:
            print("Não existem funcionários disponíveis para contratação.\n")
            return AcaoFuncionario.VOLTAR, None
        
        entradas = []
        for f in funcionarios_disponiveis:
            entradas.append(EntradaMenu(AcaoFuncionario.CONTRATAR, f, str(f)))

        entradas.append(EntradaMenu(AcaoFuncionario.VOLTAR, None, "Voltar"))

        for pos, entrada in enumerate(entradas, 1):
            print(f"{pos}: {entrada.rotulo}")

        try:
            escolha = int(input("\n>> "))
            
            if escolha >= 1 and escolha <= len(entradas):
                entrada = entradas[escolha - 1]
                return entrada.acao, entrada.alvo
            else:
                print("Opção inválida, tente novamente.\n")
                        
        except ValueError:
            print("Por favor, digite apenas números inteiros.\n")
            
def tela_detalhes_funcionario(funcionario: Funcionario) -> tuple[AcaoFuncionario, Funcionario | None]:
    """
    Exibe a tela de detalhes de um funcionário.
    
    Parâmetros:
        funcionario (Funcionario): Funcionario que se deseja exibir
        os detalhes
        
    Retorna:
        tuple[AcaoFuncionario, Funcionario | None]: Uma tupla contendo:
            - AcaoFuncionario: Ação. Neste caso, sempre DEMITIR ou
            VOLTAR.
            - Funcionario | None: Alvo da ação ou None a depender da 
            ação.
    """
    
    while True:
        print(f"{funcionario.nome} - {funcionario.funcao}")
        print(f"Salário: R$ {funcionario.salario:.2f}")
        print(f"Idade: {funcionario.idade}")
        
        escolha = input("Deseja demitir esse funcionário (S/N): ")
        
        if escolha.upper() in ("S", "SIM"):
            return AcaoFuncionario.DEMITIR, funcionario
        elif escolha.upper() in ("N", "NAO", "NÃO"):
            return AcaoFuncionario.VOLTAR, None
        else:
            print("Opção inválida, tente novamente.\n")