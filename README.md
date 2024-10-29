# Inventory Management System

## Descrição

Este projeto é um sistema de gerenciamento de estoque desenvolvido em Python, utilizando a biblioteca PyQt5 para a interface gráfica e SQLite para armazenamento de dados. O objetivo é fornecer uma solução simples e eficaz para gerenciar produtos em estoque, permitindo que os usuários adicionem, visualizem e organizem os itens.

## Funcionalidades

- **Adição de Produtos:** Interface para adicionar novos produtos ao estoque.
- **Listagem de Produtos:** Visualização dos produtos cadastrados em uma tabela.
- **Persistência de Dados:** Os dados são armazenados em um banco de dados SQLite (`inventory.db`).
- **Criação Automática de Tabelas:** A tabela `products` é criada automaticamente se não existir.

## Tecnologias Utilizadas

- **Python:** Linguagem de programação principal.
- **PyQt5:** Biblioteca para a criação de interfaces gráficas.
- **SQLite:** Sistema de gerenciamento de banco de dados leve e integrado.

## Requisitos

Para rodar este projeto, você precisa ter o Python instalado, além das bibliotecas listadas em `requirements.txt`. Para instalá-las, execute:
    ```bash
    pip install -r requirements.txt

## Como executar

1. Certifique-se de que todas as dependências estão instaladas.
2. Navegue até a pasta src onde o inventory_app.py está localizado.
3. Execute o seguinte comando no terminal:
    ```bash
    python inventory_app.py
4. A interface do sistema de gerenciamento de estoque será aberta, permitindo que você adicione e visualize produtos.


