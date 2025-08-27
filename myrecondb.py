import argparse
import json

DB_FILE = "recondb.json"

def carregar_dados():
    """Carrega os dados do arquivo JSON ou retorna uma lista vazia."""
    try:
        with open(DB_FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        # para o caso do arquivo existir mas estiver vazio ou corrompido
        return []

def salvar_dados(dados):
    """Salva a lista de dados no arquivo JSON."""
    with open(DB_FILE, 'w') as f:
        json.dump(dados, f, indent=4)

def adicionar_alvo(args):
    """Adiciona um novo alvo ao banco de dados."""
    dados = carregar_dados()

    novo_alvo = {
        'ip': args.ip,
        'portas': args.portas.split(',') if args.portas else [],
        'notas': args.notas if args.notas else ""
    }

    dados.append(novo_alvo)

    salvar_dados(dados)
    print(f"[+] Alvo {args.ip} adicionado com sucesso!")

def listar_alvos(args):
    """Lista todos os alvos salvos no banco de dados."""
    dados = carregar_dados()

    if not dados:
        print("[-] Nenhum alvo cadastrado.")
        return 
    
    print("\n--- LISTA DE ALVOS ---")
    for i, alvo in enumerate(dados, 1):
        print(f"----------------------------------")
        print(f"Alvo #{i}: {alvo.get('ip')}")
        portas_str = ', '.join(alvo.get('portas', []))
        print(f" Portas: {portas_str}")
        print(f" Notas: {alvo.get('notas')}")
    print(f"----------------------------------")

def main():
    """Função principal que configura o argparse e executa o programa."""
    parser = argparse.ArgumentParser(description="MyReconDB - Banco de Dados de Reconhecimento")
    subparsers = parser.add_subparsers(dest='command', required=True, help='Comandos disponíveis')

    parser_add = subparsers.add_parser('add', help='Adicionar um novo alvo')
    parser_add.add_argument('--ip', required=True, help='Endereço IP do alvo')
    parser_add.add_argument('--portas', help='Portas separadas por vírgula')
    parser_add.add_argument('--notas', help='Anotações sobre o alvo')
    parser_add.set_defaults(func=adicionar_alvo)

    parser_list = subparsers.add_parser('list', help='Listar todos os alvos salvos')
    parser_list.set_defaults(func=listar_alvos)

    args = parser.parse_args()

    args.func(args)

if __name__ == '__main__':
    main()