#1- renkleri fontları düzenle, icon bul 2-text dosyası ve fotoğrafları uygulamanın içine göm 3-tanım veya kelime uzun olunca pencerenin dışına taşıyor(hem ana sayfa hem tüm kelimelerin bulunduğu yer için geçerli) 4- lexicondaki kelimeler aşağıda kalıyor güncelleme yapılınca scrollbar değişimi algılamıyor. 5- randomizer update almıyor eski sözlüğe göre işlem yapıyor 6- app az kelimeyle açılırsa lexicondaki scrollbar çalışmıyor.
import random
from random import choice
from cgitb import text
from tkinter import *
import tkinter as tk                
from tkinter import LEFT, Frame, font as tkfont
from turtle import left, title, width 
from tkinter.ttk import *
import os
import time

current_path = os.path.dirname(os.path.realpath(__file__))

def dict_func():
    olex = {}
    with open(current_path + "\dictionary.txt", "r") as f:
        lines = f.readlines()
    if len(lines) > 0:
        for line in lines:
            key, val = line.split(':')
            olex[key] = val.strip('\n')
    return olex


class SampleApp(tk.Tk):
    
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title_font = tkfont.Font(family='Helvetica', size=18,  slant="italic")
        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}
        for F in (StartPage, Menu1, Add_ChangeWord, RemoveWord, Lexicon, Randomizer):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")
        
    def show_frame(self, page_name):
        '''Show a frame for the given page name'''        

        frame = self.frames[page_name]
        frame.tkraise()
        


class StartPage(tk.Frame):
      
    def __init__(self, parent, controller):
        
        tk.Frame.__init__(self, parent)
        self.controller = controller
        buttonM = tk.Button(self,bg="#4C6793",activebackground='#4C6793', text="///",fg="white",
                            command=lambda: controller.show_frame("Menu1"))
        
        buttonM.pack(side=RIGHT,anchor='n')
        
        label = tk.Label(self, text="OLEX",fg="white",bg="#256D85", font=controller.title_font)
        label.pack(anchor='center',expand=1)

        StartPage.configure(self,bg="#256D85")
        
    
        word_var=tk.StringVar()
        tk.Entry(self,bg='#06283D',textvariable = word_var,fg="white",width = 20, font=("Helvetica 15 bold")).pack(anchor='center',expand=1)
        
        
        def getdict():
            olex = dict_func()
            word = word_var.get()
            if word in olex.keys():
                meaning.config(text=olex[word])
            else:
                meaning.config(text='Not found!',bg="#256D85")

            word_var.set("")
            
        self.photo = PhotoImage(file = r"C:\Users\extre\Desktop\Python\ProjectOlex\icons8-search-50.png").subsample(2, 2)
        buttonE = tk.Button(self, image=self.photo, compound="left",bg="#4C6793",activebackground='#4C6793', command=getdict)
        buttonE.pack(anchor='n',expand=1)
        meaning = tk.Label(self, text='',bg="#256D85",fg="white", font=("Helvetica 24"))
        meaning.pack()

                
class Menu1(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        
        
        label = tk.Label(self,bg="#256D85",fg="white", text="Menu", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        
        button1 = tk.Button(self,bg="#256D85",activebackground="#256D85",fg="white", text="Back",
                           command=lambda: controller.show_frame("StartPage"))
        button1.pack()
        
        button2 = tk.Button(self,bg="#256D85",activebackground="#256D85",fg="white", text="Add or Change Word",
                           command=lambda: controller.show_frame("Add_ChangeWord"))
        button2.pack()
        
        button3 = tk.Button(self,bg="#256D85",activebackground="#256D85",fg="white", text="Remove word",
                           command=lambda: controller.show_frame("RemoveWord"))
        button3.pack()
        
        button4 = tk.Button(self,bg="#256D85",activebackground="#256D85",fg="white", text="Lexicon",
                           command=lambda: controller.show_frame("Lexicon"))
        button4.pack()
        
        button5 = tk.Button(self,bg="#256D85",activebackground="#256D85",fg="white", text="Randomizer",
                           command=lambda: controller.show_frame("Randomizer"))
        button5.pack()
        Menu1.configure(self,bg="#256D85")


class Add_ChangeWord(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self,bg="#256D85",fg="white", text="Add or Change Word", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self,bg="#256D85",fg="white",activebackground="#256D85", text="Back",
                           command=lambda: controller.show_frame("Menu1"))
        button.pack()
        key1=tk.StringVar()
        value1=tk.StringVar()
        tk.Entry(self,bg='#06283D',fg="white",textvariable = key1, font=("Helvetica 15 bold")).pack(pady=0)
        tk.Entry(self,bg='#06283D',fg="white",textvariable = value1, font=("Helvetica 15 bold")).pack(pady=50)
        Add_ChangeWord.configure(self,bg="#256D85")   
        
        def add_word():
            olex = dict_func()
            olex[key1.get()]=value1.get()
            print(olex)
            with open(current_path + "/dictionary.txt", "w") as dict_file:
                ins_str = '\n'.join([k+':'+v for k, v in olex.items()])
                dict_file.write(ins_str)
            with open(current_path + "/dictionary.txt") as f:
                for line in f:
                    key, val = line.split(':')
                    olex[key] = val
            key1.set("")
            value1.set("")
        
        
        save_button = tk.Button(self,bg="#256D85",fg="white",activebackground="#256D85", text="save",command=add_word)
        save_button.pack()

        
class RemoveWord(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self,bg="#256D85",fg="white", text="Remove Word", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self,bg="#256D85",fg="white",activebackground="#256D85", text="Back",
                           command=lambda: controller.show_frame("Menu1"))
        button.pack()
        key2 = tk.StringVar()
        tk.Entry(self,bg='#06283D',fg="white",textvariable = key2, font=("Helvetica 15 bold")).pack(pady=0)
        
        RemoveWord.configure(self,bg="#256D85")
        
        def removeword():
            with open(current_path + "/dictionary.txt", "r") as f:
                lines = f.readlines()
            with open(current_path + "/dictionary.txt", "w") as f:
                for line in lines:
                    if line.strip("\n").split(':')[0] != key2.get():
                        f.write(line)
            key2.set("")                        

                    
        remove_button = tk.Button(self,bg="#256D85",fg="white",activebackground="#256D85", text="Remove",command=removeword)
        remove_button.pack()


class Lexicon(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text ="Lexicon",bg="#256D85",fg="white",font=controller.title_font)
        label.pack()
        label3 = tk.Label(self,text='',bg="#256D85",fg="white")
        label3.pack()
        
        button2 = tk.Button(self,bg="#256D85" ,text ="Back",fg="white",
                            command = lambda: controller.show_frame("Menu1"))

        button2.pack()
        
        Lexicon.configure(self,bg="#256D85")
        
        
    
        main_frame = tk.Frame(self)
        main_frame.pack(fill=BOTH,expand=True)
        my_canvas = tk.Canvas(main_frame)
        my_canvas.pack(side=LEFT,fill=BOTH,expand=True)
        my_scrollbar = tk.Scrollbar(main_frame,orient=VERTICAL,command=my_canvas.yview)
        my_scrollbar.pack(side=RIGHT,fill=Y,expand=FALSE)
        my_canvas.configure(yscrollcommand=my_scrollbar.set)
        my_canvas.bind('<Configure>',lambda e:my_canvas.configure(scrollregion=my_canvas.bbox("all")))
        second_frame = tk.Frame(my_canvas)
        
        
        def get_lines2():
            olex = dict_func()
            ins_str = '\n'.join([f'{k:<20} : {v:>40}' for k, v in olex.items()])
            return ins_str
        my_canvas.create_window((0,0),window=second_frame,anchor="nw")
        print(get_lines2())
        lexi = tk.Label(second_frame,font=24, bg="#256D85",fg="white",text=get_lines2())
        lexi.pack()
        
        
        def get_lines():
            olex = dict_func()
            ins_str = '\n'.join([f'{k:<20} : {v:>40}' for k, v in olex.items()])
            lexi.config(text=ins_str)
            lexi.pack()
            my_canvas.create_window((0,0),window=second_frame,anchor="nw")
            
            
        show = tk.Button(self,bg="#256D85" ,text ="Refresh",fg="white",
                            command =get_lines)
        show.pack(side=TOP)


class Randomizer(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text ="Randomizer",bg="#256D85",fg="white",font=controller.title_font)
        label.pack()
        
        Randomizer.configure(self,bg="#256D85")   
        
        
        button = tk.Button(self,bg="#256D85" ,text ="Back",fg="white",
                            command = lambda: controller.show_frame("Menu1"))

        button.pack()

        label_random = tk.Label(self, text ="Cards",bg="#256D85",fg="white",font=controller.title_font)
        label_random.pack()

        label_random2 = tk.Label(self, text ="Meanings",bg="#256D85",fg="white",font=controller.title_font)
        label_random2.pack()
        
        
       


        self.v = ""  
        
        
        self.olength = list(dict_func())
        self.slist = list(range(0,len(self.olength)))
        
        def key_randomizer():
            label_random2.config(text =  "")
            self.control = dict_func()
            length = len(self.control)
            if len(self.olength)  == len(self.control):
                print("if")
                self.randomval = random.sample(self.slist, 1)[0]
                print(self.randomval)
                self.slist.remove(self.randomval)
                print(self.slist)
                print(self.control)
                print(self.olength)
                k = list(self.control.keys())[self.randomval]
                label_random.config(text = k)
                if self.slist == []:
                    self.slist = list(range(0,len(self.olength)))
                    key_randomizer()

            elif len(self.olength)  < len(self.control):
                self.slist = list(range(0,length))
                map(self.slist.append,range(len(self.olength),length))
                self.olength = self.control
                key_randomizer()
              
            elif len(self.olength)  > len(self.control):
                self.slist = list(range(0,length))
                map(self.slist.remove,range(length,len(self.olength),-1))
                self.olength = self.control
                key_randomizer()
               
                
        def show_meaning():
            
            self.v = list(self.control.values())[self.randomval]
            label_random2.config(text =  self.v)
      
            
   
                
            
                 

      
        
        
        show_key = tk.Button(self,bg="#256D85" ,text ="word",fg="white",command=key_randomizer)
        show_key.pack(side=LEFT)
        show_value = tk.Button(self,bg="#256D85" ,text ="meaning",fg="white",command=show_meaning)
        show_value.pack(side=RIGHT)
  


if __name__ == "__main__":
    app = SampleApp()
    app.title('OLEX')
    app.geometry('600x600')
    # app.resizable(height = None, width = None)
    
    app.mainloop()