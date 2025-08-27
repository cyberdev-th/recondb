# MyReconDB

Uma simples ferramenta de linha de comando (CLI) para gerenciar dados de reconhecimento de alvos durante testes de invasão (pentests). Este projeto foi desenvolvido como um exercício prático para consolidar os conceitos fundamentais de Python abordados no livro "Python for Security and Networking".

## Funcionalidades

* Adicionar novos alvos com IP, portas de interesse e anotações.
* Listar todos os alvos salvos de forma organizada no terminal.
* Persistir (salvar) os dados em um arquivo local `recondb.json`.

## Requisitos

* Python 3.10+

Nenhuma biblioteca externa é necessária, apenas módulos da biblioteca padrão do Python (`argparse`, `json`).

## Instalação e Preparação

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/SEU_USUARIO/MyReconDB.git](https://github.com/SEU_USUARIO/MyReconDB.git)
    ```
    *(Lembre-se de trocar `SEU_USUARIO` pelo seu nome de usuário no GitHub)*

2.  **Navegue até a pasta do projeto:**
    ```bash
    cd MyReconDB
    ```

3.  **Crie e ative um ambiente virtual:**
    ```bash
    # Cria o ambiente
    python -m venv venv

    # Ativa o ambiente (Windows)
    .\venv\Scripts\activate

    # Ativa o ambiente (Linux/macOS)
    source venv/bin/activate
    ```

## Como Usar

### Adicionando um Novo Alvo

Use o comando `add` com os parâmetros `--ip` (obrigatório), `--portas` e `--notas`.

```bash
python myrecondb.py add --ip 192.168.1.1 --portas 80,443 --notas "Servidor Web Principal"
```
```bash
python myrecondb.py add --ip 192.168.1.50 --portas 22 --notas "Servidor SSH, tentar credenciais padrao"
```

### Listando os Alvos Salvos

Use o comando `list` para ver todos os alvos no banco de dados.

```bash
python myrecondb.py list
```
**Saída de Exemplo:**
```
--- LISTA DE ALVOS ---
----------------------------------
Alvo #1: 192.168.1.1
  Portas: 80, 443
  Notas: Servidor Web Principal
----------------------------------
Alvo #2: 192.168.1.50
  Portas: 22
  Notas: Servidor SSH, tentar credenciais padrao
----------------------------------
```

### Obtendo Ajuda

Para ver todos os comandos e opções disponíveis, use `-h`.

```bash
python myrecondb.py -h
```