# Restaurant Tycoon - Simulador de hamburgueria
Esse é um jogo que simula o gerenciamento de uma hamburgueria completamente pelo terminal, usando recursos de TUI. O objetivo do projeto é aplicar os conhecimentos demonstrados no livro Pense em Python ([Leia aqui](https://github.com/PenseAllen/PensePython2e)).

# Requisitos Técnicos
Uma lista de recursos técnicos do Python que terei que usar no jogo como forma de aplicação do livro. Obs.: A lista foi gerada usando IA para arbitrariedade.

1. **Arquitetura Modular:** Separação obrigatória do código em pelo menos 5 arquivos `.py`;
2. **Programação Orientada a Objetos (POO):** Uso de herança com uma classe mãe e classes filhas com atributos e comportamentos específicos.
3. **Persistência de Dados:** Salvamento automático e carregamento do estado do jogo utilizando arquivos no formato JSON.
4. **Estruturas de Dados Aninhadas:** Uso de dicionários complexos para mapear o cardápio e os ingredientes exatos de cada receita.
5. **Motor de Simulação Baseado em Tempo:** Loop secundário que simula a passagem das horas (12:00 às 14:00) em intervalos de 5 minutos utilizando pausas controladas com `time.sleep`.
6. **Sistema de Eventos Aleatórios:** Algoritmo baseado na biblioteca `random` com pelo menos 6 eventos imprevisíveis que alteram os preços ou a mecânica do dia atual.
7. **Interface Blindada contra Falhas:** Implementação rigorosa de blocos `try/except` em todas as entradas de dados do menu para impedir o fechamento inesperado do programa por digitação incorreta.

# Implementação dos Requisitos Técnicos
Registros de como e onde os Requisitos Técnicos foram implementados.

1. (Arquitetura Modular): `main.py`, `menus.py`, `cardapio.py`, `funcionarios.py` e `monetario.py`;
2. (POO): Classes para itens do cardápio, para funcionários e para ações de menus, que herda de Enum;
3. (Persistência de Dados): Dados armazenados em JSON, com default;
4. (Estruturas de Dados Aninhadas): Armazenamento de dados de forma aninhada para os itens do cardápio.