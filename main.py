import menus
import cardapio
import shutil
from pathlib import Path

BASE = Path(__file__).parent
SAVE = BASE / "database.json"
DEFAULT = BASE / "data" / "database.default.json"

if not SAVE.exists():
    shutil.copy(DEFAULT, SAVE)

itens_cardapio = cardapio.carregar_cardapio()
itens_desbloqueados = [u for u in itens_cardapio if u.desbloqueado]

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
        cardapio.salvar_cardapio(itens_cardapio)
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
            itens_cardapio[escolha-1] = item
            