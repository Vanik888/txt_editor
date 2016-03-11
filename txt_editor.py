from tkinter import Tk, Button, Text, Scrollbar, filedialog, Frame


def quit(ev):
    global root
    root.destroy()


def load_file(ev):
    fn = filedialog.Open(root, filetypes=[('*.txt files', '.txt'),
                                          ('*.xml files', '.xml'),
                                          ('all', '*')]).show()
    if fn == '':
        return
    textbox.delete('1.0', 'end')
    textbox.insert('1.0', open(fn, 'rt').read())


def save_file(ev):
    fn = filedialog.SaveAs(root, filetypes=[('*.txt files', '.txt'),
                                            ('all', '*')]).show()
    if fn == '':
        return
    if not fn.endswith('.txt'):
        fn+='.txt'
    open(fn, 'wt').write(textbox.get('1.0', 'end'))


root = Tk()

panel_frame = Frame(root, height=60, bg='gray')
text_frame = Frame(root, height=360, width=600)

panel_frame.pack(side='top', fill='x')
text_frame.pack(side='bottom', fill='both', expand=1)

textbox = Text(text_frame, font='Arial 14', wrap='word')
scrollbar = Scrollbar(text_frame)

scrollbar['command'] = textbox.yview
textbox['yscrollcommand'] = scrollbar.set

textbox.pack(side='left', fill='both', expand=1)
scrollbar.pack(sid='right', fill='y')

load_btn = Button(panel_frame, text='Load')
save_btn = Button(panel_frame, text='Save')
quit_btn = Button(panel_frame, text='Quit')

load_btn.bind('<Button-1>', load_file)
save_btn.bind('<Button-1>', save_file)
quit_btn.bind('<Button-1>', quit)

load_btn.place(x=10, y=10, width=40, height=40)
save_btn.place(x=60, y=10, width=40, height=40)
quit_btn.place(x=110, y=10, width=40, height=40)

root.mainloop()
