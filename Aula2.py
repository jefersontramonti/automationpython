# Passo a passo do projeto:
# passo 1: Entrar no sistema da Empresa
# passo 2: fazer login
# passo 3: importar a base de dados de produtos
# passo 4: cadastrar roduto
# passo 5: repetir o cadastro para cada produto
import pandas
import pyautogui
import time
import pandas as pd

# Abrir o navegador
pyautogui.press('win')
pyautogui.write('Chrome')
pyautogui.press('enter')

# Aguardar o navegador abrir
time.sleep(3)

# Digitar a url do site e pressionar enter
link = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'
pyautogui.write(link)
time.sleep(2)
pyautogui.press('enter')

# Aguardar o navegador abrir
time.sleep(5)

# Fazer login
pyautogui.click(x=-780, y=413)
pyautogui.write('entrar@gmail.com')
pyautogui.press('tab')
pyautogui.write('12345')
pyautogui.press('tab')
pyautogui.press('enter')

time.sleep(3)

# tabela recebe os valores do csv
tabela = pandas.read_csv('produtos.csv')

for linha in tabela.index:
    pyautogui.click(x=-896, y=295)

    codigo = tabela.loc[linha, 'codigo']

    # preencher os campos
    pyautogui.write(str(codigo))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'marca']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'tipo']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'categoria']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'preco_unitario']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'custo']))
    pyautogui.press('tab')

    obs = tabela.loc[linha, 'obs']
    if not pandas.isna(obs):
        pyautogui.write(str(obs))

    pyautogui.press('tab')
    pyautogui.press('enter')

    pyautogui.scroll(5000)
