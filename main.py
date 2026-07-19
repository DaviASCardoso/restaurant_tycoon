import menus
import cardapio
import monetario
import funcionarios
import shutil
from pathlib import Path

BASE = Path(__file__).parent
SAVE = BASE / "database.json"
DEFAULT = BASE / "data" / "database.default.json"

if not SAVE.exists():
    shutil.copy(DEFAULT, SAVE)

itens_cardapio = cardapio.carregar_cardapio()
itens_desbloqueados = [u for u in itens_cardapio if u.desbloqueado]

lista_funcionarios = funcionarios.carregar_funcionarios()
lista_funcionarios_disponiveis = [f for f in lista_funcionarios if f.contratavel and not f.contratado]
lista_funcionarios_contratados = [f for f in lista_funcionarios if f.contratado]

opcoes_tela_inicial = {
    1: "tela_cardapio",
    2: "tela_funcionarios",
    3: "tela_aberto",
    4: "tela_dados",
    5: "sair"
}

while True:
    escolha = menus.tela_inicial(monetario.carregar_saldo())
    tela = opcoes_tela_inicial.get(escolha)
    if tela == "sair":
        print("\nAté mais!")
        cardapio.salvar_cardapio(itens_cardapio)
        funcionarios.salvar_funcionarios(lista_funcionarios)
        break
    elif tela == "tela_cardapio":
        acao, alvo = menus.tela_cardapio(itens_cardapio)

        if acao is menus.AcaoCardapio.VOLTAR:
            continue
        elif acao is menus.AcaoCardapio.SELECIONAR:
            novo_nome, novo_preco = menus.tela_detalhes_item(alvo)
            alvo.nome = novo_nome
            alvo.preco = novo_preco
    elif tela == "tela_funcionarios":
        acao, alvo = menus.tela_funcionarios(lista_funcionarios)
        
        if acao is menus.AcaoFuncionario.SELECIONAR:
            acao, alvo = menus.tela_detalhes_funcionario(alvo)
            
            if acao is menus.AcaoFuncionario.DEMITIR:
                alvo.contratado = False
            elif acao is menus.AcaoFuncionario.VOLTAR:
                continue
        elif acao is menus.AcaoFuncionario.IR_PARA_CONTRATACAO:
            acao, alvo = menus.tela_contratar_funcionarios(lista_funcionarios)
            
            if acao is menus.AcaoFuncionario.CONTRATAR:
                alvo.contratado = True
            elif acao is menus.AcaoFuncionario.VOLTAR:
                continue
        elif acao is menus.AcaoFuncionario.VOLTAR:
            continue
            