import pyautogui
import time
import pandas as pd

pyautogui.PAUSE = 1.5

def csv_bot_filler():

    pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
    pyautogui.press("return")
    time.sleep(3)

    # Passo 2: Fazer login
    # selecionar o campo de email
    pyautogui.press("tab")
    pyautogui.write("pythonimpressionador@gmail.com")
    pyautogui.press("tab") # passando pro próximo campo
    # selecionar o campo de senha
    pyautogui.write("123456")
    pyautogui.press("enter")
    time.sleep(3)

    # Passo 3: Importar a base de produtos pra cadastrar
    tabela = pd.read_csv("tables/produtos.csv")
    print(tabela)
    # Passo 4: Cadastrar um produto
    for linha in tabela.index:
        pyautogui.click(x=536, y=312) # clicar no campo de código
        pyautogui.write(str(tabela.loc[linha, "codigo"]))
        pyautogui.press("tab") # marca
        pyautogui.write(str(tabela.loc[linha, "marca"]))
        pyautogui.press("tab") # tipo
        pyautogui.write(str(tabela.loc[linha, "tipo"]))
        pyautogui.press("tab") # categoria
        pyautogui.write(str(tabela.loc[linha, "categoria"]))
        pyautogui.press("tab") # preço unitário
        pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
        pyautogui.press("tab") # custo
        pyautogui.write(str(tabela.loc[linha, "custo"]))
        pyautogui.press("tab") # observações
        obs = tabela.loc[linha, "obs"]
        if not pd.isna(obs):
            pyautogui.write(str(tabela.loc[linha, "obs"]))
        pyautogui.press("tab")
        pyautogui.press("enter")
        pyautogui.scroll(5000)
        