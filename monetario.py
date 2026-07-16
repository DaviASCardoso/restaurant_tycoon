import json

def carregar_saldo() -> float:
    """
    Carrega o saldo atual do jogador.
    
    Retorna:
        float: O saldo atual do jogador.
    """
    
    with open("database.json", "r", encoding="utf-8") as arquivo:
        dados_completos = json.load(arquivo)
        
    return dados_completos["saldo"]

def movimentar(valor: float) -> None:
    """
    Movimenta um valor no saldo do jogador.
    
    Parâmetros:
        valor (float): O valor a ser movimentado. 
    """
    
    with open("database.json", "r", encoding="utf-8") as arquivo:
        dados_completos = json.load(arquivo)

    novo_saldo = carregar_saldo() + valor
    dados_completos["saldo"] = novo_saldo

    with open("database.json", "w", encoding="utf-8") as arquivo:
        json.dump(dados_completos, arquivo, ensure_ascii=False, indent=2)