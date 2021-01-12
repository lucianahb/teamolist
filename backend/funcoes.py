import datetime as datetime
import sys
sys.path.append('.')


def escrever_arquivo(valor: str, tipo: int, operador: str) -> bool:
    root = 'backend/arquivos/'
    arquivo = ''
    if tipo == 0:
        arquivo = open(f'{root}list_marketplace.txt', operador)
    elif tipo == 1:
        arquivo = open(f'{root}list_produto.txt', operador)
    try:
        arquivo.write(str(valor)+'%\n')
        return True
    except Exception as e:
        return False
    finally:
        arquivo.close()


def log(valor: str):
    root = 'backend/arquivos/'
    arquivo = open(f'{root}log.txt', 'a')
    data = datetime.datetime.now()
    arquivo.write(data.strftime(
        f"%d/%m/%Y às %H:%M:%S => Acesso a função {valor}\n"))
    arquivo.close()
