def escrever_arquivo(valor: str, tipo: int, operador: str) -> bool:
    root = 'arquivos/'
    arquivo = ''
    if tipo == 0:
        arquivo = open(f'{root}list_marketplace.txt', operador)
    elif tipo == 1:
        arquivo = open(f'{root}list_category.txt', operador)
    try:
        arquivo.write(str(valor)+';\n')
        return True
    except Exception as e:
        return False
    finally:
        arquivo.close()
