from pywinauto import Application, keyboard
from time import sleep

app = Application().start('notepad.exe')
app.UntlitedNotepad.Edit.type_keys("Olá, como vai você?", with_spaces = True)
sleep(3)
keyboard.send_keys('{ENTER}')
app.UntlitedNotepad.type_keys("\nEstou testando esse processo com o Python.", with_spaces = True)
sleep(3)
keyboard.send_keys('{ENTER}')
app.UntlitedNotepad.menu_select("Arquivo->Salvar como...")
sleep(3)
keyboard.send_keys('{ENTER}')
app.Dialog.edit1.set_edit_text("Minha nota")
sleep(3)
app.Dialog.Salvar.click()

