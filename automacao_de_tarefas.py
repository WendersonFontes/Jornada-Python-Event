import pyautogui
import time

pyautogui.PAUSE = 0.5

pyautogui.press("win")

pyautogui.press("chrome")

pyautogui.press("enter")

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")

pyautogui.press("enter")

time.sleep(3)


pyautogui.click(x=751, y=470)

pyautogui.write("pythonimpressionador@gmail.com")

pyautogui.press("tab")

pyautogui.press("tab")

pyautogui.write("minha senha")

pyautogui.click(x=946,y=676)
time.sleep(3)

import pandas
tabela = pandas.read_csv("produtos.csv")
print(tabela)


for linha in tabela.index:
    pyautogui.click(x=725, y=323)
    # codigo
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(codigo)
    pyautogui.press("tab")
    # marca
    pyautogui.write(tabela.loc[linha, "marca"])
    pyautogui.press("tab)")
    # tipo
    pyautogui.write(tabela.loc[linha, "tipo"])
    pyautogui.press("tab)")
    # categoria
    pyautogui.write(tabela.loc[linha, "categoria"])
    pyautogui.press("tab)")
    # preco
    pyautogui.write(tabela.loc[linha, "preco"])
    pyautogui.press("tab)")
    # custo
    pyautogui.write(tabela.loc[linha, "custo"])
    pyautogui.press("tab)")
    # obs
    pyautogui.write(tabela.loc[linha, "obs"])
    # enviar o produto
    pyautogui.write("tab")
    pyautogui.press("enter)")

    pyautogui.scroll(5000)
