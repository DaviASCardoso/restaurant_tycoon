import json

class Funcionario():
    def __init__(self, id: int, nome: str, sexo: str, idade: int, salario: float, funcao: str, contratavel: bool, contratado: bool = False):
        self.id = id
        self.nome = nome
        self.sexo = sexo
        self.idade = idade
        self.salario = salario
        self.funcao = funcao
        self.contratavel = contratavel
        self.contratado = contratado
        
    def __str__(self):
        return f"{self.id}: {self.nome} - {self.funcao} (R$ {self.salario:.2f})"
    
    def para_dicionario(self) -> dict:
        return {
            "id": self.id,
            "nome": self.nome,
            "sexo": self.sexo,
            "idade": self.idade,
            "salario": self.salario,
            "funcao": self.funcao,
            "contratavel": self.contratavel,
            "contratado": self.contratado
        }
        
def carregar_funcionarios() -> list:
    """
    Carrega a lista de funcionários do banco de dados.
    
    Retorna:
        list: Lista de funcionários.
    """
    
    with open("database.json", "r", encoding="utf-8") as arquivo:
        dados_completos = json.load(arquivo)
    
    lista_dic = dados_completos["funcionarios"]
    lista_obj = []
    
    for dados_funcionario in lista_dic:
        novo_objeto = Funcionario(**dados_funcionario)
        lista_obj.append(novo_objeto)
        
    return lista_obj

def salvar_funcionários(funcionarios: list) -> None:
    """
    Salva a lista de funcionários no banco de dados.
    
    Parâmetros:
        funcionarios (list): Lista de funcionários alterada que se 
        deseja salvar.
    """

    with open("database.json", encoding="utf-8") as f:
        dados = json.load(f)
    
    funcionarios_dict = []
    
    for i in funcionarios:
        funcionarios_dict.append(i.para_dicionario())
    
    dados["funcionarios"] = funcionarios_dict
        
    with open("database.json", "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=2)