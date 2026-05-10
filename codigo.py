# Programa de automatização usando PyAutoGUI
import pyautogui
import time
import pandas as pd

pyautogui.PAUSE = 0.8

# Link do sistema
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

# Abrir o navegador Chrome
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# Esperar o Chrome abrir
time.sleep(2)

# Digitar o link
pyautogui.write(link)
pyautogui.press("enter")

# Pausa maior para carregar o site
time.sleep(5)

# Fazer login
pyautogui.click(x=903, y=461)

pyautogui.write("emailparaestudos@gmail.com")
pyautogui.press("tab")  # Passa para o próximo campo
pyautogui.write("Senha teste!")
pyautogui.press("tab")
pyautogui.press("enter")

# Esperar carregamento
time.sleep(5)

# Importar a base de dados
tabela = pd.read_csv("produtos.csv")

print(tabela)

# Cadastrar produtos
for linha in tabela.index:

    # Clicar no campo código
    pyautogui.click(x=908, y=323)

    # Código
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")

    # Marca
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")

    # Tipo
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")

    # Categoria
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")

    # Preço
    pyautogui.write(str(tabela.loc[linha, "preco"]))
    pyautogui.press("tab")

    # Custo
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")

    # Observações
    obs = tabela.loc[linha, "obs"]

    if not pd.isna(obs):
        pyautogui.write(str(obs))

    pyautogui.press("tab")
    pyautogui.press("enter")  # Cadastra o produto

    # Voltar para o topo
    pyautogui.scroll(10000)