# BarionBet - Simulação de Roleta em Python

Este projeto consiste em uma simulação de um jogo de roleta de cassino, desenvolvido inteiramente em Python e projetado para ser executado em um ambiente de terminal (CLI).

O objetivo é replicar as mecânicas centrais da roleta europeia (com um único zero), permitindo que o usuário gerencie um saldo virtual, realize diferentes tipos de apostas e acompanhe os resultados gerados aleatoriamente.

## Funcionalidades Principais

* **Saldo Virtual:** O jogador inicia com um saldo fixo de fundos virtuais para realizar suas apostas.
* **Sistema de Apostas:** Implementação de um menu de apostas claro e interativo.
* **Geração Aleatória:** Utilização da biblioteca `random` do Python para simular o giro da roleta, garantindo resultados imprevisíveis (números de 0 a 49).
* **Validação de Saldo:** O sistema verifica se o jogador possui fundos suficientes antes de aceitar uma aposta.
* **Cálculo de Pagamentos:** O saldo do jogador é atualizado automaticamente com base no resultado e no tipo de aposta realizada.

## Tipos de Apostas Implementadas

O sistema atualmente suporta as seguintes opções de aposta:

1.  **Apostas Externas (Pagamento 1:1)**
    * **Vermelho ou Preto:** O jogador aposta na cor do número sorteado.
    * **Par ou Ímpar:** O jogador aposta se o número será par ou ímpar (o 0 não é considerado nenhum dos dois).
    * **Baixo (1-18) ou Alto (19-36):** O jogador aposta se o número estará na metade inferior ou superior.

2.  **Apostas Internas (Pagamento 35:1)**
    * **Pleno (Número Específico):** O jogador aposta em um único número (incluindo o 0).

*Nota: Em todas as apostas externas, se o resultado for 0, o jogador perde a aposta.*

## Tecnologias Utilizadas

* **Python 3.x:** Linguagem principal do projeto.
* **Biblioteca `random`:** Essencial para a geração dos resultados da roleta.
* **Biblioteca `rich` (Opcional):** Utilizada para a formatação da interface no terminal, aplicando cores e painéis para uma experiência de usuário mais clara e organizada.
* **Biblioteca `os`:** Utilizada para limpar a tela do terminal, melhorando a legibilidade entre as rodadas.

## Como Executar o Projeto

### Pré-requisitos

* Python 3.8 ou superior.
* `pip` (Gerenciador de pacotes do Python).

### Instalação

1.  Clone este repositório para sua máquina local:
    ```bash
    git clone [https://github.com/seu-usuario/nome-do-repositorio.git](https://github.com/seu-usuario/nome-do-repositorio.git)
    cd nome-do-repositorio
    ```

2.  (Opcional, se estiver usando `rich`) Instale as dependências:
    ```bash
    pip install rich
    ```

### Execução

Para iniciar o programa, execute o script principal através do seu terminal:

```bash
python nome_do_arquivo.py
