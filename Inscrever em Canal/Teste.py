
from tkinter import messagebox
from PIL import Image
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
import selenium
import pyautogui
import time





#abrir chrome
'''tes = pyautogui.locateCenterOnScreen(r'chrome.png', confidence=0.9)
print("coord chrome: ",tes)
pyautogui.moveTo(tes)
pyautogui.click()'''
driver = webdriver.Chrome()
#caixa de pesquisa
pesquisar = pyautogui.prompt(text="", title="Digite o nome do canal")
# abrir nova guia
time.sleep(1)
pyautogui.moveTo(700, 26)
pyautogui.click()
pyautogui.hotkey('ctrl', 't')

#pesquisar youtube
pyautogui.write("www.youtube.com", interval=0.050)
pyautogui.press('enter')
time.sleep(5)
btn_pesquisar = pyautogui.locateCenterOnScreen(r"pesquisar.png", confidence=0.9)
print("coord barra: ",btn_pesquisar)
pyautogui.moveTo(btn_pesquisar)
pyautogui.click()
pyautogui.write(pesquisar, interval=0.025)
pyautogui.press('enter')
url = pesquisar.replace(" ", "+")
print(url)
time.sleep(2)

#acessar canal
'''
driver.find_element(By.XPATH, '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-channel-renderer/div/div[2]/a/div[1]/ytd-channel-name/div/div/yt-formatted-string').click()
logo = pyautogui.locateCenterOnScreen(r"logocanaldark.png", confidence=0.9)
logo = pyautogui.locateCenterOnScreen(elem)
print("coord logo:",elem)
pyautogui.moveTo(elem)
pyautogui.click()
time.sleep(5)'''
ver = pyautogui.locateCenterOnScreen(r'Verificado.png', confidence=0.9)
print("coord ver:", ver)
pyautogui.moveTo(ver, duration=0.3)
pyautogui.click()
time.sleep(2)

#se inscrever
btn_inscrever = pyautogui.locateCenterOnScreen(r"inscrever.png", confidence=0.9)
print("coord inscrever:",btn_inscrever)
pyautogui.moveTo(btn_inscrever)
pyautogui.click()
time.sleep(1)
pyautogui.alert(text='Inscrito com Sucesso!', title='Inscrição Concluída', button='OK')

