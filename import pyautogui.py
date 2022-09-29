import pyautogui
import time 
#caixa de pesquisa
pesquisar = pyautogui.prompt(text="", title="Digite o nome do canal")
#abrir chrome
tes = pyautogui.locateCenterOnScreen(r'chrome.png')
print(tes)
pyautogui.moveTo(tes)
pyautogui.click()
time.sleep(1)
#caixa de pesquisa
pesquisar = pyautogui.prompt(text="", title="Digite o nome do canal")
# abrir nova guia
time.sleep(1)
pyautogui.moveTo(1585, 16)
pyautogui.click()
pyautogui.hotkey('ctrl', 't')

#pesquisar youtube

pyautogui.write("www.youtube.com", interval=0.050)
pyautogui.press('enter')
time.sleep(1)
btn_pesquisar = pyautogui.locateCenterOnScreen("pesquisar2.png", confidence=0.9)
pyautogui.moveTo(btn_pesquisar, 1)
pyautogui.click()
pyautogui.write(pesquisar)
pyautogui.press('enter')
