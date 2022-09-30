from tkinter import messagebox
from PIL import ImageGrab
import pyautogui
import time




#abrir chrome
tes = pyautogui.locateCenterOnScreen(r'chrome.png', confidence=0.7)
print("coord chrome: ",tes)
pyautogui.moveTo(tes, duration=0.3)
pyautogui.click()
time.sleep(0.5)
#caixa de pesquisa
pesquisar = pyautogui.prompt(text="", title="Digite o nome do canal")
# abrir nova guia1111111111111111111111
time.sleep(1)
pyautogui.click(556,22)
pyautogui.hotkey('ctrl', 't')

#pesquisar youtube
pyautogui.write("www.youtube.com", interval=0.050)
pyautogui.press('enter')
time.sleep(3.5)
btn_pesquisar = pyautogui.locateCenterOnScreen(r"pesquisar.png", confidence=0.9)
print("coord barra: ",btn_pesquisar)
pyautogui.moveTo(btn_pesquisar, duration=0.3)
pyautogui.click()
pyautogui.write(pesquisar, interval=0.025)
pyautogui.press('enter')
time.sleep(2)

#acessar canal usando o selo de verificado como referencia
ver = pyautogui.locateCenterOnScreen(r'Verificado.png', confidence=0.9)
print("coord ver:", ver)
pyautogui.moveTo(ver, duration=0.3)
pyautogui.click()
time.sleep(2)

#se inscrever
btn_inscrever = pyautogui.locateCenterOnScreen(r"inscrever.png", confidence=0.9)
print("coord inscrever:",btn_inscrever)
pyautogui.moveTo(btn_inscrever, duration=0.3)
pyautogui.click()
time.sleep(1)
pyautogui.alert(text='Inscrito com Sucesso!', title='Inscrição Concluída', button='OK')


