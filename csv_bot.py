import pyautogui
import time
import pandas as pd

pyautogui.PAUSE = 1.5

def csv_bot_filler():

    pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
    pyautogui.press("return")
    time.sleep(3)

    # Passo 2: login
    # selecting email field
    pyautogui.press("tab")
    pyautogui.write("pythonimpressionador@gmail.com")
    pyautogui.press("tab") # Going to next field
    # Selecting password field
    pyautogui.write("123456")
    pyautogui.press("enter")
    time.sleep(3)

    # Passo 3: Import database to register products
    tabela = pd.read_csv("tables/produtos.csv")
    print(tabela)
    # Passo 4: Register products
    for linha in tabela.index:
        pyautogui.click(x=536, y=312) # Clicking in the register button 
        # If needed, use get_cursor_position.py to get the coordinates of the button and plae on the above line
        pyautogui.write(str(tabela.loc[linha, "codigo"]))
        pyautogui.press("tab") # Label
        pyautogui.write(str(tabela.loc[linha, "marca"]))
        pyautogui.press("tab") # type
        pyautogui.write(str(tabela.loc[linha, "tipo"]))
        pyautogui.press("tab") # category
        pyautogui.write(str(tabela.loc[linha, "categoria"]))
        pyautogui.press("tab") # price
        pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
        pyautogui.press("tab") # cost
        pyautogui.write(str(tabela.loc[linha, "custo"]))
        pyautogui.press("tab") # obs
        obs = tabela.loc[linha, "obs"]
        if not pd.isna(obs):
            pyautogui.write(str(tabela.loc[linha, "obs"]))
        pyautogui.press("tab")
        
        pyautogui.press("enter")
        
        pyautogui.scroll(5000)
        