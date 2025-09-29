import requests
import json
 
URL = 'https://uselessfacts.jsph.pl/api/v2/facts/random'
 
def main():
    while True:
        print('1 - Ver um fato novo')
        print('2 - Sair')
       
        try:
            opcao = int(input('Escolha uma opcao: '))
        except ValueError:
            print('Opção Inválida, digite 1 ou 2')
            continue  # Continua o loop se a opção for inválida
           
        if opcao == 1:
            verFatoNovo()
        elif opcao == 2:
            print('Saindo...')
            break  # Sai do loop e termina o programa
        else:
            print('Opção inválida, digite 1 ou 2')
 
def verFatoNovo():
    try:
        resposta = requests.get(URL)
   
        if resposta.status_code == 200:
            fato = resposta.json()
            print('Fato> ', fato['text'])
        else:
            print(f'Erro ao acessar o servidor. Status code: {resposta.status_code}')
            print('Mostrando fato de backup...')
            fatoLocal()
    except:
        print(f'Erro ao acessar a API')
        print('Mostrando fato de backup...')
        fatoLocal()
 
def fatoLocal():
    try:
        with open('arquivo_backup.json', 'r') as arquivo:
            fato = json.load(arquivo)
            print('Fato (backup): ', fato['text'])
    except FileNotFoundError:
        print('Arquivo backup não encontrado')
    except json.JSONDecodeError:
        print('Erro ao ler o conteúdo do arquivo backup')
    except Exception as e:
        print(f'Erro desconhecido ao ler o backup: {e}')
 
if __name__ == '__main__':
    main()
 
