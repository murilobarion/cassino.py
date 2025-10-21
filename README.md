# BarionBet: Simulador de Caça-Níquel em Python

Este projeto é uma simulação de uma máquina caça-níquel (slot machine) desenvolvida em Python. O jogo é executado inteiramente no terminal (CLI) e utiliza a biblioteca `rich` para criar uma interface de usuário visualmente agradável e organizada.

O objetivo principal é oferecer uma experiência de cassino virtual onde o jogador gerencia um saldo inicial, realiza apostas e testa a sorte em uma máquina de três rolos.

## Funcionalidades Principais

* **Saldo Virtual:** O jogador inicia o jogo com um saldo fixo de $1000.
* **Interface Gráfica no Terminal:** Utiliza painéis (`Panel`) da biblioteca `rich` para estruturar o menu principal, o saldo e as seções do jogo.
* **Animação de Giro:** Simula o giro dos rolos com uma animação de terminal, utilizando `print(..., end="\r", flush=True)` por 50 iterações para criar suspense antes de revelar o resultado.
* **Lógica de Símbolos:** Utiliza uma lista de 5 símbolos (`"🍒", "🔔", "💰", "🍋", "💩"`) sorteados aleatoriamente pela biblioteca `random`.
* **Sistema de Pagamento:**
    * **Jackpot (10x):** Concedido ao obter três símbolos `💰`.
    * **Prêmio (3x):** Concedido ao obter três símbolos idênticos (exceto o Jackpot).
    * **Perda:** Ocorre em todas as outras combinações.
* **Validação de Apostas:** O sistema impede que o jogador prossiga em duas condições:
    1.  Se o saldo do jogador for `0` (zero).
    2.  Se o valor da aposta (`valor_aposta`) for maior que o saldo (`saldo`) disponível.

## Tecnologias Utilizadas

* **Python 3.x:** Linguagem principal do projeto.
* **Biblioteca `rich`:** Utilizada para toda a formatação da interface, incluindo `print` colorido, estilos (`bold`) e componentes `Panel`.
* **Biblioteca `random`:** Essencial para a geração dos resultados da animação e do resultado final.
* **Biblioteca `time`:** Usada para criar pausas (`time.sleep`) e controlar a velocidade da animação, melhorando a experiência do usuário.
* **Biblioteca `os`:** Utilizada para a função `limpar_tela()`, que limpa o console entre as jogadas.

## Como Executar o Projeto

### Pré-requisitos

* Python 3.8 ou superior.
* `pip` (Gerenciador de pacotes do Python).

### Instalação

1.  Clone este repositório para sua máquina local:
    ```bash
    git clone [https://github.com/murilobarion/cassino.py.git](https://github.com/murilobarion/cassino.py.git)
    cd cassino.py
    ```

2.  Instale a biblioteca `rich`:
    ```bash
    pip install rich
    ```

### Execução

Para iniciar o programa, execute o script principal através do seu terminal:

```bash
# Se o seu arquivo se chama 'cassino.py'
python cassino.py
