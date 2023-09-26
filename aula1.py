import time
import pandas as pd
import pyautogui


def abrir_navegador():
    pyautogui.press('win')
    pyautogui.write('Chrome')
    pyautogui.press('enter')
    time.sleep(3)  # tempo para o navegador abrir


def acessar_site(link):
    pyautogui.write(link)
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(5)  # tempo para o site carregar


def fazer_login(x, y, email, senha):
    pyautogui.click(x=x, y=y)
    pyautogui.write(email)
    pyautogui.press('tab')
    pyautogui.write(senha)
    pyautogui.press('tab')
    pyautogui.press('enter')
    time.sleep(3)  # tempo para login


def cadastrar_produtos(tabela):
    for linha in tabela.index:
        pyautogui.click(x=-896, y=295)

        for coluna in tabela.columns:
            valor = tabela.loc[linha, coluna]
            if not pd.isna(valor):
                pyautogui.write(str(valor))
            pyautogui.press('tab')

        pyautogui.press('enter')
        pyautogui.scroll(5000)


def main():
    link = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'
    email = 'entrar@gmail.com'
    senha = '12345'

    abrir_navegador()
    acessar_site(link)
    fazer_login(x=-780, y=413, email=email, senha=senha)

    tabela = pd.read_csv('produtos.csv')
    cadastrar_produtos(tabela)


if __name__ == "__main__":
    main()
