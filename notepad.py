import tkinter

# Função para chamar o notepad:
def notepad():
    from notepad import notepad
    notepad()

def newfile():
    text_area.delete(1.0, 'end')

def save():
    container = text_area.get(1.0, 'end')
    file = open('notepad.txt', 'w')
    file.write(container)
    file.close()

def Open():
    file = open('notepad.txt', 'r')
    container = file.read()
    text_area.insert(1.0, container)

def update_font():
    size = spin_size.get()
    font = spin_font.get()
    text_area.config(font=f'{font} {size}')

window = tkinter.Tk()
window.title('Notepad')
window.geometry('720x480')
window.configure(background='black')
#window.minsize(width=720, height=480)

frame = tkinter.Frame(window, bg='#3C3F41', height=30)
frame.pack(fill='x')

font_text = tkinter.Label(frame, bg='#3C3F41', fg= 'white', text=' Font:  ')
font_text.pack(side='left')

spin_font = tkinter.Spinbox(frame, bg='#3C3F41', fg='white', values=('Arial', 'Verdana', 'Roman', 'Courier'))
spin_font.pack(side='left')

font_size = tkinter.Label(frame, bg='#3C3F41', fg='white', text=' Font size: ')
font_size.pack(side='left')

spin_size = tkinter.Spinbox(frame, bg='#3C3F41', fg='white', from_=0, to=60)
spin_size.pack(side='left')

button_update = tkinter.Button(frame, bg='#3C3F41', fg='white', text='Change', command=update_font)
button_update.pack(side='left')

text_area = tkinter.Text(window, bg='#2B2B2B', fg='white', font='Arial 12', width=720, height=480)
text_area.pack()

main_menu = tkinter.Menu(window)

file_menu = tkinter.Menu(main_menu, tearoff=0)
file_menu.add_command(label='New', command=newfile)
file_menu.add_command(label='Save', command=save)
file_menu.add_command(label='Open', command=Open)
file_menu.add_command(label='Exit', command=window.quit)

main_menu.add_cascade(label='File', menu=file_menu)
window.config(menu=main_menu)

window.mainloop()
