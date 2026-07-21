import json

def dados_existem() -> bool:
    """Verifica se os dados do usuário existem no banco de dados.

    Returns:
        bool: True se existirem, False se não.
    """

    with open("database.json", encoding="utf-8") as f:
        dados = json.load(f)

    if "username" in dados and "restaurant_name" in dados:
        return True
    else:
        return False

def atualizar_dados(username: str, restaurant_name: str) -> None:
    """Atualiza o nome de usuário e o nome do restaurante no banco de dados.

    Args:
        username (str): Novo nome de usuário
        restaurant_name (str): Novo nome do restaurante
    """

    with open("database.json", encoding="utf-8") as f:
        dados = json.load(f)

    dados["username"] = username
    dados["restaurant_name"] = restaurant_name

    with open("database.json", "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=2)