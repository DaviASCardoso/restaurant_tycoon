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
        funcionarios.salvar_funcionários(lista_funcionarios)
        break
    elif tela == "tela_cardapio":
        escolha = menus.tela_cardapio(itens_cardapio)
        item = next((obj for obj in itens_cardapio if obj.id == escolha), None)

        if escolha == (len(itens_desbloqueados) + 1):
            continue
        else:
            novo_nome, novo_preco = menus.tela_editar_item()
            item.nome = novo_nome
            item.preco = novo_preco
    elif tela == "tela_funcionarios":
        escolha = menus.tela_funcionarios(lista_funcionarios)
        funcionario = next((obj for obj in lista_funcionarios if obj.id == escolha), None)
        
        if escolha == (len(lista_funcionarios_contratados) + 2):
            continue
        elif escolha == (len(lista_funcionarios_contratados) + 1):
            escolha = menus.tela_contratar_funcionarios(lista_funcionarios)
            if escolha is None:
                continue
            funcionario = next((obj for obj in lista_funcionarios if obj.id == escolha), None)
            if funcionario is None:
                continue
            funcionario.contratado = True
        else:
            funcionario = next((obj for obj in lista_funcionarios if obj.id == escolha), None)
            if funcionario is None:
                continue
            demitir = menus.tela_detalhes_funcionario(lista_funcionarios, escolha)
            funcionario.contratado = not demitir