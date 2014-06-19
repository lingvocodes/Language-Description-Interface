from Tkinter import *
import tkFileDialog
import ttk
import re
import codecs

name = 0


  
#############################################
def textw():

    def LoadFile():
        fn = tkFileDialog.Open(root, filetypes = [('*.txt files', '.txt')]).show()
        if fn == '':
            return
        
        textbox.delete('1.0', 'end') 
        textbox.insert('1.0', open(fn, 'rt').read())
        
    
    def SaveFile():
        fn = tkFileDialog.SaveAs(root, filetypes = [('*.txt files', '.txt')]).show()
        if fn == '':
            return
        if not fn.endswith(".txt"):
            fn+=".txt"
        t = []
        t.append(textbox.get('1.0', 'end'))
        
        open(fn, 'wt')
        f = codecs.open(fn,'w','utf-8')
        for i in t:
            f.write(i)
        f.close()

    def ins2(evt):
        w = evt.widget
        i = []
        index = int(w.curselection()[0])
        i.append(w.get(index))
        for s in i:
            textbox.insert('end',s)

    def ins(evt):
        w = evt.widget
        i = []
        d = {0: '̀', 1: '́', 2:'̂', 3: '̄', 4:'̊', 5:'̌', 6:'̕', 7:'̯', 8:'̣', 9: '̦', 10: '̥', 11:'̬', 12:'̨', 13:'ͅ', 14:'҃', 15: '̏', 16: '̋', 17: '͡'}
        index = int(w.curselection()[0])
        i.append(d.get(index))
        for s in i:
            textbox.insert('end',s)



    root = Tk()


    textFrame = Frame(root, height = 340, width = 600)

    textFrame.pack(side = 'bottom', fill = 'both', expand = 1)

    textbox = Text(textFrame, font='Arial 14', wrap='word')
    scrollbar = Scrollbar(textFrame)

    scrollbar['command'] = textbox.yview
    textbox['yscrollcommand'] = scrollbar.set

    textbox.pack(side = 'left', fill = 'both', expand = 1)
    scrollbar.pack(side = 'right', fill = 'y')



    rframe = Frame(textFrame, height = 340, width = 75, bg = 'gray',bd=5)
    rframe.pack(side = 'right', fill = 'y')

    Lb2 = Listbox(rframe, height = 20)
    Lb2.insert(1, " ̀ ")
    Lb2.insert(2, " ́ ")
    Lb2.insert(3, " ̂")
    Lb2.insert(4, " ̄")
    Lb2.insert(5, " ̊")
    Lb2.insert(6, " ̌")
    Lb2.insert(7, " ̕")
    Lb2.insert(8, " ̯")
    Lb2.insert(9, ' ̣')
    Lb2.insert(10, ' ̦')
    Lb2.insert(11, ' ̥')
    Lb2.insert(12, ' ̬')
    Lb2.insert(13, ' ̨')
    Lb2.insert(14, ' ͅ')
    Lb2.insert(15, ' ҃')
    Lb2.insert(16, ' ̏')
    Lb2.insert(17, ' ̋')
    Lb2.insert(18, ' ͡')


    
 

    Lb2.pack(side = 'left', expand = 1)
    Lb2.bind("<<ListboxSelect>>", ins)

    MB = Menu(root)
    
    MN = Menu(MB)
    MN.add_command(label=u"Сохранить", command= SaveFile)
    MN.add_command(label=u"Загрузить", command= LoadFile)
    MN.add_command(label = u'Выход', command = root.destroy)
    MB.add_cascade(label=u"Файл", menu=MN)

    root.config(menu=MB)


    root.mainloop()

####################################################################
textboxes = []

def slov():

    def AddS():
        k = u'-lexeme \r\n lex: \r\n stem: \r\n paradigm: \r\n'
        textbox.insert('end',k)

    def LBAdd():
        m = Tk()
        e = Entry(m)
        e.pack()
        e.focus_set()
        def insl():
            Lb.insert('end', e.get())
        b = Button(m, text= u"Вставить", width=10, command=insl)
        b.pack()
    
    def LoadFile2():
        global name
        global textboxes
        name += 1
     
        page = []
        fn = tkFileDialog.Open(root3, filetypes = [('*.txt files', '.txt')]).show()
        if fn == '':
            return
 

        k = re.findall('-lexeme',open(fn, 'rt').read())
        m = len(k)

        
        for name in range(1,m+1):
            notes = ttk.Frame(root3)
            note.add(notes, text ='Лекс. %s' % name)
            page.append(notes)

            lframe = Frame(notes, height = 340, width = 60, bg = 'gray')
            lframe.pack(side = 'left', fill = 'y')
            rframe = Frame(notes, height = 340, width = 75, bg = 'gray',bd=5)
            rframe.pack(side = 'right', fill = 'y')

            Lb = Listbox(lframe, height = 30)
           

            Lb.pack(side = 'right', expand = 1)
            Lb.bind("<<ListboxSelect>>", ins2)
            
            Lb2 = Listbox(rframe, height = 20)
            Lb2.insert(1, " ̀ ")
            Lb2.insert(2, " ́ ")
            Lb2.insert(3, " ̂")
            Lb2.insert(4, " ̄")
            Lb2.insert(5, " ̊")
            Lb2.insert(6, " ̌")
            Lb2.insert(7, " ̕")
            Lb2.insert(8, " ̯")
            Lb2.insert(9, ' ̣')
            Lb2.insert(10, ' ̦')
            Lb2.insert(11, ' ̥')
            Lb2.insert(12, ' ̬')
            Lb2.insert(13, ' ̨')
            Lb2.insert(14, ' ͅ')
            Lb2.insert(15, ' ҃')
            Lb2.insert(16, ' ̏')
            Lb2.insert(17, ' ̋')
            Lb2.insert(18, ' ͡')
            Lb2.pack(side = 'left', expand = 1)
            Lb2.bind("<<ListboxSelect>>", ins)

        f = codecs.open(fn, 'r', 'utf-8-sig')
        text = f.read()
        f.close()
        textf = []
        text = re.findall(u'(-lexeme[^\r\n]*\r?\n(?: [^\r\n]*\r?\n)*)',
                              text, flags=re.U|re.DOTALL)
        for k in text:
            textf.append(k)


        for i in range(m):
            textbox = Text(page[i], font='Curier 14', wrap='word')
            textboxes.append(textbox)
            textbox.pack(fill='both', expand=True)
            
            scrollbar2 = Scrollbar(textbox)
            scrollbar2['command'] = textbox.yview
            textbox['yscrollcommand'] = scrollbar2.set

            textbox.pack(side = 'left', fill = 'both', expand = 1)
            scrollbar2.pack(side = 'right', fill = 'y')
            textbox.insert('1.0', textf[i])
            

        return name, textboxes


    def ins2(evt):
        w = evt.widget
        i = []
        index = int(w.curselection()[0])
        i.append(w.get(index))
        for s in i:
            textbox.insert('end',s)

    def ins(evt):
        w = evt.widget
        i = []
        d = {0: '̀', 1: '́', 2:'̂', 3: '̄', 4:'̊', 5:'̌', 6:'̕', 7:'̯', 8:'̣', 9: '̦', 10: '̥', 11:'̬', 12:'̨', 13:'ͅ', 14:'҃', 15: '̏', 16: '̋', 17: '͡'}
        index = int(w.curselection()[0])
        i.append(d.get(index))
        for s in i:
            textbox.insert('end',s)
            
    def SaveFile2():
            global v
            global text
            global textboxes
            fn = tkFileDialog.SaveAs(root3, filetypes = [('*.txt files', '.txt')]).show()
            if fn == '':
                return
            if not fn.endswith(".txt"):
                fn+=".txt"
            t = []
            for textbox in textboxes:
                t.append(textbox.get('1.0', 'end'))
            f = codecs.open(fn,'w','utf-8')
            for w in t:
                for s in w:
                    f.write(s)
            f.close()



    def AddN():
        global textboxes
        global name
        
        notes = ttk.Frame(root3)
        notes.pack(side = "right")
        name += 1       

        lframe = Frame(notes, height = 340, width = 75, bg = 'gray',bd=5)
        lframe.pack(side = 'left', fill = 'y')
        rframe = Frame(notes, height = 340, width = 75, bg = 'gray',bd=5)
        rframe.pack(side = 'right', fill = 'y')

        textboxn = Text(notes, font='Curier 14', wrap='word')
        scrollbar3 = Scrollbar(textboxn)
    
        scrollbar3['command'] = textboxn.yview
        textboxn['yscrollcommand'] = scrollbar3.set

        textboxn.pack(side = 'left', fill = 'both', expand = 1)
        scrollbar3.pack(side = 'right', fill = 'y')                  

        Lb = Listbox(lframe, height = 30)
        Lb.pack(side = 'right', expand = 1)
        Lb.bind("<<ListboxSelect>>", ins2)

        Lb2 = Listbox(rframe, height = 20)
        Lb2.insert(1, " ̀ ")
        Lb2.insert(2, " ́ ")
        Lb2.insert(3, " ̂")
        Lb2.insert(4, " ̄")
        Lb2.insert(5, " ̊")
        Lb2.insert(6, " ̌")
        Lb2.insert(7, " ̕")
        Lb2.insert(8, " ̯")
        Lb2.insert(9, ' ̣')
        Lb2.insert(10, ' ̦')
        Lb2.insert(11, ' ̥')
        Lb2.insert(12, ' ̬')
        Lb2.insert(13, ' ̨')
        Lb2.insert(14, ' ͅ')
        Lb2.insert(15, ' ҃')
        Lb2.insert(16, ' ̏')
        Lb2.insert(17, ' ̋')
        Lb2.insert(18, ' ͡')
        Lb2.pack(side = 'left', expand = 1)
        Lb2.bind("<<ListboxSelect>>", ins)
        note.add(notes, text ='Лекс.%s' % name)
        textboxes.append(textbox)
       
        return name, textboxes

    

    root3 = ttk.Tkinter.Tk()
    root3.title(u'Графический интерфейс')
    root3.geometry('1000x750+100+100')
    root3.resizable(True, True)
    
    note = ttk.Notebook(root3, height = 30, width = 60)
    note.pack(side = 'top', fill = 'both',expand = True)    

    notes = ttk.Frame(root3)
    notes.pack(side = "right", fill = 'both',expand=True)

    lframe = Frame(notes, height = 340, width = 75, bg = 'gray',bd=5)
    lframe.pack(side = 'left', fill = 'y')
    rframe = Frame(notes, height = 340, width = 75, bg = 'gray',bd=5)
    rframe.pack(side = 'right', fill = 'y')
    
    textbox = Text(notes, font='Arial 14', wrap='word')
    scrollbar3 = Scrollbar(textbox)
    
    scrollbar3['command'] = textbox.yview
    textbox['yscrollcommand'] = scrollbar3.set

    textbox.pack(side = 'left', fill = 'both', expand = 1)
    scrollbar3.pack(side = 'right', fill = 'y')                   

    Lb = Listbox(lframe, height = 30)
    Lb.pack(side = 'right', expand = 1)
    Lb.bind("<<ListboxSelect>>", ins2)

    Lb2 = Listbox(rframe, height = 20)
    Lb2.insert(1, " ̀ ")
    Lb2.insert(2, " ́ ")
    Lb2.insert(3, " ̂")
    Lb2.insert(4, " ̄")
    Lb2.insert(5, " ̊")
    Lb2.insert(6, " ̌")
    Lb2.insert(7, " ̕")
    Lb2.insert(8, " ̯")
    Lb2.insert(9, ' ̣')
    Lb2.insert(10, ' ̦')
    Lb2.insert(11, ' ̥')
    Lb2.insert(12, ' ̬')
    Lb2.insert(13, ' ̨')
    Lb2.insert(14, ' ͅ')
    Lb2.insert(15, ' ҃')
    Lb2.insert(16, ' ̏')
    Lb2.insert(17, ' ̋')
    Lb2.insert(18, ' ͡')
    Lb2.pack(side = 'left', expand = 1)
    Lb2.bind("<<ListboxSelect>>", ins)
    note.add(notes, text ='Главная вкладка')
       
    MB = Menu(root3)
    MN = Menu(MB)
    MN.add_command(label=u"Сохранить", command= SaveFile2)
    MN.add_command(label=u"Загрузить", command= LoadFile2)
    MN.add_command(label = u'Выход', command = root3.destroy)
    MB.add_cascade(label=u"Файл", menu=MN)
    MB.add_command(label = u"Добавить вкладку", command = AddN)
    MB.add_command(label = u"Вставить шаблон", command = AddS)
    MB.add_command(label = u"+", command = LBAdd)
    root3.config(menu=MB)
    
    textboxes.append(textbox)
    return name, textboxes


   


###################################################################################################################################

def gramm():
    global n
    n = 0
    global p1
    def LBAdd():
        m = Tk()
        e = Entry(m)
        e.pack()
        e.focus_set()
        def insl():
            Lb.insert('end', e.get())
        b = Button(m, text= U"Вставить", width=10, command=insl)
        b.pack()
        
    def LoadFile3():

        global name

        global textboxes


        page = []
        fn = tkFileDialog.Open(root4, filetypes = [('*.txt files', '.txt')]).show()
        if fn == '':
            return
 
        k = re.findall('-paradigm',open(fn, 'rt').read())
        m = len(k)

        
        for name in range(1,m+1):
            notes = ttk.Frame(root4)
            note.add(notes, text ='Парад. %s' % name)
            page.append(notes)

            lframe = Frame(notes, height = 340, width = 60, bg = 'gray')
            lframe.pack(side = 'left', fill = 'y')
            rframe = Frame(notes, height = 340, width = 75, bg = 'gray',bd=5)
            rframe.pack(side = 'right', fill = 'y')

            Lb = Listbox(lframe, height = 30)
           
            Lb.pack(side = 'right', expand = 1)
            Lb.bind("<<ListboxSelect>>", ins2)
            
            Lb2 = Listbox(rframe, height = 20)
            Lb2.insert(1, " ̀ ")
            Lb2.insert(2, " ́ ")
            Lb2.insert(3, " ̂")
            Lb2.insert(4, " ̄")
            Lb2.insert(5, " ̊")
            Lb2.insert(6, " ̌")
            Lb2.insert(7, " ̕")
            Lb2.insert(8, " ̯")
            Lb2.insert(9, ' ̣')
            Lb2.insert(10, ' ̦')
            Lb2.insert(11, ' ̥')
            Lb2.insert(12, ' ̬')
            Lb2.insert(13, ' ̨')
            Lb2.insert(14, ' ͅ')
            Lb2.insert(15, ' ҃')
            Lb2.insert(16, ' ̏')
            Lb2.insert(17, ' ̋')
            Lb2.insert(18, ' ͡')
            Lb2.pack(side = 'left', expand = 1)
            Lb2.bind("<<ListboxSelect>>", ins)

        f = codecs.open(fn, 'r', 'utf-8-sig')
        text = f.read()
        f.close()
        textf = []
        text = re.findall(u'(-paradigm[^\r\n]*\r?\n(?: [^\r\n]*\r?\n)*)', text, flags=re.U|re.DOTALL)
            
        for k in text:
            textf.append(k)

        for i in range(m):
            textbox = Text(page[i], font='Curier 14', wrap='word')
            textboxes.append(textbox)
            textbox.pack(fill='both', expand=True)

            scrollbar2 = Scrollbar(textbox)
            scrollbar2['command'] = textbox.yview
            textbox['yscrollcommand'] = scrollbar2.set

            textbox.pack(side = 'left', fill = 'both', expand = 1)
            scrollbar2.pack(side = 'right', fill = 'y')         
            
            textbox.insert('1.0', textf[i])
            

        return name
   
    def SaveFile3():

        global textboxes
        fn = tkFileDialog.SaveAs(root4, filetypes = [('*.txt files', '.txt')]).show()
        if fn == '':
            return
        if not fn.endswith(".txt"):
            fn+=".txt"
        t = []
        for textbox in textboxes:
            t.append(textbox.get('1.0', 'end'))
        f = codecs.open(fn,'w','utf-8')
        for w in t:
            for s in w:
                f.write(s)
        f.close()


    def ins2(evt):
         
        w = evt.widget
        i = []
        index = int(w.curselection()[0])
        i.append(w.get(index))
        for s in i:
            textbox.insert('end',s)

    def ins(evt):
         
        w = evt.widget
        i = []
        d = {0: '̀', 1: '́', 2:'̂', 3: '̄', 4:'̊', 5:'̌', 6:'̕', 7:'̯', 8:'̣', 9: '̦', 10: '̥', 11:'̬', 12:'̨', 13:'ͅ', 14:'҃', 15: '̏', 16: '̋', 17: '͡'}
        index = int(w.curselection()[0])
        i.append(d.get(index))
        for s in i:
            textbox.insert('end',s)


    def AddN():
        global textboxes
        global name
        global v
        global text
        global p
        notes = ttk.Frame(root4)
        notes.pack(side = "right", fill = 'both',expand=True)

        name += 1       
        lframe = Frame(notes, height = 340, width = 75, bg = 'gray',bd=5)
        lframe.pack(side = 'left', fill = 'y')
        rframe = Frame(notes, height = 340, width = 75, bg = 'gray',bd=5)
        rframe.pack(side = 'right', fill = 'y')

        textbox = Text(notes, font='Curier 14', wrap='word')
        scrollbar3 = Scrollbar(textbox)
        scrollbar3['command'] = textbox.yview
        textbox['yscrollcommand'] = scrollbar3.set
        textbox.pack(side = 'left', fill = 'both', expand = 1)
        scrollbar3.pack(side = 'right', fill = 'y')

        MB = Menu(root4)
        MN = Menu(MB)
        MN.add_command(label=u"Сохранить", command= SaveFile3)
        MN.add_command(label=u"Загрузить", command= LoadFile3)
        MN.add_command(label = u'Выход', command = root4.destroy)
        MB.add_cascade(label=u"Файл", menu=MN)

        MB.add_command(label = u"Добавить вкладку", command = AddN)
        MB.add_command(label = u"+", command = LBAdd)
        root4.config(menu=MB)                    
            
        Lb = Listbox(lframe, height = 30)
        Lb.pack(side = 'right', expand = 1)
        Lb.insert(1, "-paradigm:")
        Lb.insert(2, " -flex: ")
        Lb.insert(3, "  gramm: ")
        Lb.bind("<<ListboxSelect>>", ins2)

        Lb2 = Listbox(rframe, height = 20)
        Lb2.insert(1, " ̀ ")
        Lb2.insert(2, " ́ ")
        Lb2.insert(3, " ̂")
        Lb2.insert(4, " ̄")
        Lb2.insert(5, " ̊")
        Lb2.insert(6, " ̌")
        Lb2.insert(7, " ̕")
        Lb2.insert(8, " ̯")
        Lb2.insert(9, ' ̣')
        Lb2.insert(10, ' ̦')
        Lb2.insert(11, ' ̥')
        Lb2.insert(12, ' ̬')
        Lb2.insert(13, ' ̨')
        Lb2.insert(14, ' ͅ')
        Lb2.insert(15, ' ҃')
        Lb2.insert(16, ' ̏')
        Lb2.insert(17, ' ̋')
        Lb2.insert(18, ' ͡')
        Lb2.pack(side = 'left', expand = 1)
        Lb2.bind("<<ListboxSelect>>", ins)
        note.add(notes, text ='Парад.%s' % name)
        textboxes.append(textbox)
        
       
        return name, textboxes


    root4 = ttk.Tkinter.Tk()
    root4.title(u'Графический интерфейс')
    root4.geometry('1000x750+100+100')
    root4.resizable(True, True)
      
    note = ttk.Notebook(root4, height = 30, width = 60)
    note.pack(side = 'top', fill = 'both',expand = True)    

    notes = ttk.Frame(root4)
    notes.pack(side = "right", fill = 'both',expand=True)

    lframe = Frame(notes, height = 340, width = 75, bg = 'gray',bd=5)
    lframe.pack(side = 'left', fill = 'y')
    rframe = Frame(notes, height = 340, width = 75, bg = 'gray',bd=5)
    rframe.pack(side = 'right', fill = 'y')
    
    textbox = Text(notes, font='Arial 14', wrap='word')
    scrollbar3 = Scrollbar(textbox)   

    scrollbar3['command'] = textbox.yview
    textbox['yscrollcommand'] = scrollbar3.set

    textbox.pack(side = 'left', fill = 'both', expand = 1)
    scrollbar3.pack(side = 'right', fill = 'y')                               

    Lb = Listbox(lframe, height = 30)
    Lb.pack(side = 'right', expand = 1)
    Lb.insert(1, "-paradigm:")
    Lb.insert(2, " -flex: ")
    Lb.insert(3, "  gramm: ")
    Lb.bind("<<ListboxSelect>>", ins2)

    Lb2 = Listbox(rframe, height = 20)
    Lb2.insert(1, " ̀ ")
    Lb2.insert(2, " ́ ")
    Lb2.insert(3, " ̂")
    Lb2.insert(4, " ̄")
    Lb2.insert(5, " ̊")
    Lb2.insert(6, " ̌")
    Lb2.insert(7, " ̕")
    Lb2.insert(8, " ̯")
    Lb2.insert(9, ' ̣')
    Lb2.insert(10, ' ̦')
    Lb2.insert(11, ' ̥')
    Lb2.insert(12, ' ̬')
    Lb2.insert(13, ' ̨')
    Lb2.insert(14, ' ͅ')
    Lb2.insert(15, ' ҃')
    Lb2.insert(16, ' ̏')
    Lb2.insert(17, ' ̋')
    Lb2.insert(18, ' ͡')
    Lb2.pack(side = 'left', expand = 1)
    Lb2.bind("<<ListboxSelect>>", ins)
    note.add(notes, text ='Главная вкладка')
        
    MB = Menu(root4)
    MN = Menu(MB)
    MN.add_command(label=u"Сохранить", command= SaveFile3)
    MN.add_command(label=u"Загрузить", command= LoadFile3)
    MN.add_command(label = u'Выход', command = root4.destroy)
    MB.add_cascade(label=u"Файл", menu=MN)
    MB.add_command(label = u"Добавить вкладку", command = AddN)
    MB.add_command(label = u"+", command = LBAdd)
    root4.config(menu=MB)
    
    textboxes.append(textbox)
    
    root4.mainloop()
    
    return textboxes






root2=Tk()
root2.title(u'Графический интерфейс')
root2.geometry('300x200+100+100')
root2.resizable(True, True)


button = Button(root2, bg="white", text=u"Текст", command =textw)
button.pack()
button2 = Button(root2, bg="white", text=u"Словарь", command =slov)
button2.pack()
button3 = Button(root2, bg="white", text=u"Грамматика", command =gramm)
button3.pack()
button4 = Button (root2,bg='red', fg = 'white', text = u'Выход', command =root2.destroy)
button4.pack()
root2.mainloop()



