import webbrowser
from flaskAPI import Util;
from database import Funcs;
import os

if __name__ == "__main__":
    # MontaBD
    funcs = Funcs()
    funcs.montaTabelas()

    # abrir página web
    diretorio_atual = os.path.dirname(__file__)
    caminho_arquivo = os.path.join(diretorio_atual, 'index.html')
    webbrowser.open(f'file://{caminho_arquivo}')

    # monta API
    Util.buildAPI()