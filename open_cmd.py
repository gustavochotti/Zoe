from pywinauto import Application, keyboard
from time import sleep
import pyautogui

app = Application().start(r'c:\WINDOWS\System32\cmd.exe /k', create_new_console=True, wait_for_idle=False)
sleep(1)
pyautogui.write('sfc/scannow', interval=0.10)
pyautogui.press('enter')
