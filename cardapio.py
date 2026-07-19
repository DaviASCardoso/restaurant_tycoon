import json

class ItemCardapio():
    def __init__(self, nome, preco, ingredientes, tempo_preparo, id, categoria, desbloqueado=False):
        self.nome = nome
        self.preco = preco
        self.ingredientes = ingredientes
        self.tempo_preparo = tempo_preparo
        self.desbloqueado = desbloqueado
        self.id = id
        self.categoria = categoria
        
    def __str__(self):
        return f"{self.nome} - R$ {self.preco:.2f} (Preapro: {self.tempo_preparo}m)"
    
    def para_dicionario(self) -> dict:
        return {
            "id": self.id,
            "nome": self.nome,
            "preco": self.preco,
            "ingredientes": self.ingredientes,
            "tempo_preparo": self.tempo_preparo,
            "desbloqueado": self.desbloqueado,
            "categoria": self.categoria
        }
            
def carregar_cardapio() -> list:
    """
    Carrega o cardápio do banco de dados.
    
    Retorna:
        list: Conteúdo do cardápio.
    """
    
    with open("database.json", "r", encoding="utf-8") as arquivo:
        dados_completos = json.load(arquivo)
    
    lista_dic = dados_completos["cardapio"]
    lista_obj = []
    
    for dados_item in lista_dic:
        novo_objeto = ItemCardapio(**dados_item)
        lista_obj.append(novo_objeto)
        
    return lista_obj

def salvar_cardapio(cardapio: list) -> None:
    """
    Salva o cardápio no banco de dados.
    
    Parâmetros:
        cardapio (list): Cardápio alterado que se deseja salvar.
    """

    with open("database.json", encoding="utf-8") as f:
        dados = json.load(f)
    
    cardapio_dict = []
    
    for i in cardapio:
        cardapio_dict.append(i.para_dicionario())
    
    dados["cardapio"] = cardapio_dict
        
    with open("database.json", "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=2)