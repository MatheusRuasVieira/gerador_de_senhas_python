# 🔒 Gerador de Senhas Seguras em Python

![Status](https://img.shields.io/badge/status-concluído-brightgreen)

Um script de console interativo que gera senhas fortes e customizáveis. Este projeto foi desenvolvido como uma forma prática de aplicar e solidificar conceitos fundamentais da linguagem Python, como manipulação de strings, laços de repetição, condicionais e tratamento de exceções.

---

## ✨ Funcionalidades Principais

* **Comprimento Customizável:** Permite ao usuário definir o tamanho exato da senha (com um **mínimo de 8 caracteres** para garantir a segurança).
* **Conjunto de Caracteres Flexível:** O usuário pode escolher incluir:
    * Letras Maiúsculas
    * Números
    * Símbolos Especiais
* **Garantia de Complexidade:** O algoritmo assegura que, se um tipo de caractere for selecionado, pelo menos um caractere daquele tipo estará presente na senha final, evitando resultados fracos por puro acaso.
* **Robustez:** Valida a entrada do usuário em loop, garantindo que apenas valores válidos (números inteiros, >= 8) sejam aceitos sem que o programa encerre.

---

## 🛠️ Tecnologias Utilizadas

* **Python 3:** Linguagem principal do projeto.
* **Biblioteca `random`:** Utilizada para toda a lógica de sorteio e aleatoriedade dos caracteres.
* **Biblioteca `string`:** Usada para obter de forma eficiente os conjuntos de caracteres (maiúsculas, minúsculas, números e símbolos).

---

## 🚀 Como Executar o Projeto

Para rodar este projeto na sua máquina, siga os passos abaixo:

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/MatheusRuasVieira/gerador_de_senhas_python.git
    ```

2.  **Navegue até a pasta do projeto:**
    ```bash
    cd gerador_de_senhas_python
    ```

3.  **Execute o script:**
    ```bash
    python gerador_de_senhas.py
    ```
O programa irá iniciar no seu terminal e fazer as perguntas para gerar a senha.

---

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.