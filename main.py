from gtts import gTTS
from playsound import playsound
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
import os
import ttkthemes as t
#convert the text from given box
def convert_text():
    text=texts_var.get()
    play(text)

def play(text):
    op=gTTS(text)
    op.save('temp.mp3')
    playsound('temp.mp3')
    os.remove('temp.mp3')

def savefile():
    op=gTTS(data)
    op.save('music.mp3')

#upload a file
def upload():
    filetypes = (('Text files', '*.txt'),('All files', '*.*'))
    filename = filedialog.askopenfilename(initialdir = "/",title = "Select a File",filetypes = filetypes)
    #f =filedialog.askopenfile(filetypes=filetypes)
    f = open(filename, "r")
    global data
    data = f.read()
    label_file_explorer.configure(text="File Opened: " + filename)
    file_text.config(state=NORMAL)
    file_text.insert('1.0', data)
    file_text.config(state=DISABLED)
    data=data.replace("\n", " ")
    #print(data)
    #play(data)

def play_after_uploading():
    play(data)
    file_text.clipboard_clear()


#mainwindow
root=t.ThemedTk(theme="arc")
texts_var = StringVar()
save_texts_var = StringVar()
root.geometry("900x600")
root.title("text to speech")

#------TABS-----
TAB_CONTROL = ttk.Notebook(root)
#text input tab
tabHome = ttk.Frame(TAB_CONTROL)
TAB_CONTROL.add(tabHome, text = "Custom Sentence")
#upload file tab
TAB1 = ttk.Frame(TAB_CONTROL)
TAB_CONTROL.add(TAB1, text='Upload file')
TAB_CONTROL.pack(expand=1, fill="both")

#contents of text input tab
text_label = ttk.Label(tabHome, text='Enter your text here :', font=('calibre', 10, 'normal'))
text_entry = ttk.Entry(tabHome, textvariable=texts_var, font=('calibre', 10, 'normal'))
dummy_label2=ttk.Label(tabHome,text="  ")
dummy_label3=ttk.Label(tabHome,text="  ")
dummy_label4=ttk.Label(tabHome,text="  ")
app_sub_btn = ttk.Button(tabHome, text='Submit', command=convert_text)
text_label.grid(row=1, column=1)
text_entry.grid(row=1, column=2)
dummy_label2.grid(row=0, column=0)
dummy_label3.grid(row=2,column=0)
dummy_label4.grid(row=1,column=0)
app_sub_btn.grid(row=3, column=2)

#contents of upload file tab
label_file_explorer = ttk.Label(TAB1,text = "Path goes here",font=('calibre', 10, 'normal'))

#text box
h = Scrollbar(root, orient='horizontal')
h.pack(side=BOTTOM, fill=X)
v = Scrollbar(root, orient='vertical')
v.pack(side=RIGHT, fill=Y)
file_text = Text(TAB1, height=12,wrap=NONE,xscrollcommand=h.set,yscrollcommand=v.set)
file_text.grid(column=0, row=0, sticky='nsew')
file_text.config(state=DISABLED)
h.config(command=file_text.xview)
v.config(command=file_text.yview)
#buttons
upload_file_btn=ttk.Button(TAB1, text='Upload', command=upload)
label_file_explorer.grid(column = 0, row = 1,sticky='w', padx=10, pady=10)
upload_file_btn.grid(column=0, row=2, sticky='w', padx=10, pady=10)
play_file_btn=ttk.Button(TAB1, text='Play', command=play_after_uploading)
play_file_btn.grid(column=0, row=3, sticky='w', padx=10, pady=10)
save_file_btn=ttk.Button(TAB1, text='Save', command=savefile)
save_file_btn.grid(column=0, row=4, sticky='w', padx=10, pady=10)

root.resizable(0,0)
root.mainloop()