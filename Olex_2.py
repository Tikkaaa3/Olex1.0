#1- renkleri fontları düzenle, icon bul 2-text dosyası ve fotoğrafları uygulamanın içine göm 3-tanım veya kelime uzun olunca pencerenin dışına taşıyor(just Lexicon için geçerli) 4- lexicondaki kelimeler aşağıda kalıyor güncelleme yapılınca scrollbar değişimi algılamıyor.  6- app az kelimeyle açılırsa lexicondaki scrollbar çalışmıyor. 7- enter tuşuna entrylerin fonksiyonlarını atadım, butonlar çalışmıyor şimdide.(aynı fonksiyonu iki kere yazıp birinin içine event yazmayıp onu butona atarsak çözülüyor ama daha hızlı bir çözüm var mıdır ki?) 8- search kısmında guess sistemi olmalı 9- örnek cümle eklemesi güzel olur.
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


import customtkinter

customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"



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
        buttonM = customtkinter.CTkButton(self, text="///",fg_color=("#111111", "#111111"),hover_color="#222222",bg_color=("#111111", "#111111"), border_width=0.9,border_color="white", text_color=("white", "white"),command=lambda: controller.show_frame("Menu1"),width=30,height=30)
        
        buttonM.pack(side=RIGHT,anchor='n',pady=5,padx=5)
        
        

        label = customtkinter.CTkLabel(self , fg_color=("#111111", "#111111"),font=("Lato",40), text=" OLEX",text_color="white",width = 60, height = 30)
        label.pack(anchor='center',expand=1)

        StartPage.configure(self,bg="#111111")
        
    
        word_var=tk.StringVar()
        entry1 = customtkinter.CTkEntry(self,text_color=("black", "white"),fg_color="#111111",border_color="white",placeholder_text="...",placeholder_text_color="white",width=250)
        #entry1.get(textvariable = word_var)
        entry1.pack(anchor='center',expand=False,pady=10)
        
        
        def getdict(event):
            olex = dict_func()
           # word = word_var.get()
            word = entry1.get()
            if word in olex.keys():
                meaning.configure(text=olex[word])
                word1.configure(text=word+":")
            else:
                meaning.configure(text='Not found!')
                word1.configure(text='')

           
            entry1.delete(0,len(entry1.get()))

        def getdict2():
            olex = dict_func()
           # word = word_var.get()
            word = entry1.get()
            if word in olex.keys():
                meaning.configure(text=olex[word])
                word1.configure(text=word+":")
            else:
                meaning.configure(text='Not found!')
                word1.configure(text='')

           
            entry1.delete(0,len(entry1.get()))
        
        entry1.bind("<Return>",getdict)    
        
        buttonE = customtkinter.CTkButton(self,text="Search",hover_color="#222222",fg_color="transparent", border_width=1, text_color=("white", "white"),border_color="white", compound="left", command=getdict2)
        buttonE.pack(anchor='n',expand=1)
        word1 = customtkinter.CTkLabel(self,font=("Lato", 30), text="")
        word1.pack()
        meaning = tk.Message(self, text='',bg="#111111",fg="white", font=("Lato", 18), aspect=600)
        meaning.pack()

                
class Menu1(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        
        label = customtkinter.CTkLabel(self,fg_color=("#111111", "#111111"),font=("Lato",40), text="Menu",text_color="white",width = 60, height = 30)
        label.pack(anchor='n',pady=45)

        
        buttonBack = customtkinter.CTkButton(self,corner_radius=15,hover_color="#222222", text="Back",fg_color=("#111111", "#111111"), border_width=0.2, text_color=("white", "white"),command=lambda: controller.show_frame("StartPage"),width=30,height=30)
        
        buttonBack.pack(anchor='w',padx=10)

        buttonadd = customtkinter.CTkButton(self,hover_color="#222222", text="Add or Change Word",border_color="white",fg_color=("#111111", "#111111"), border_width=0.7, text_color=("white", "white"),command=lambda: controller.show_frame("Add_ChangeWord"),width=30,height=30)
        
        buttonadd.pack(anchor='n',pady=10)
        
        buttonrem = customtkinter.CTkButton(self,hover_color="#222222", text="      Remove Word      ",border_color="white",fg_color=("#111111", "#111111"), border_width=0.7, text_color=("white", "white"),command=lambda: controller.show_frame("RemoveWord"),width=30,height=30)
        
        buttonrem.pack(anchor='n',pady=10)
        
        buttonlex = customtkinter.CTkButton(self,hover_color="#222222", text="            Lexicon            ",border_color="white",fg_color=("#111111", "#111111"), border_width=0.7, text_color=("white", "white"),command=lambda: controller.show_frame("Lexicon"),width=30,height=30)
        
        buttonlex.pack(anchor='n',pady=10)
        
        buttonran = customtkinter.CTkButton(self,hover_color="#222222", text="        Randomizer        ",border_color="white",fg_color=("#111111", "#111111"), border_width=0.7, text_color=("white", "white"),command=lambda: controller.show_frame("Randomizer"),width=30,height=30)
        
        buttonran.pack(anchor='n',pady=10)
        

        Menu1.configure(self,bg="#111111")


class Add_ChangeWord(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        label = customtkinter.CTkLabel(self,fg_color=("#111111", "#111111"),font=("Lato",40), text="Add or Change Word",text_color="white",width = 60, height = 30)
        label.pack(anchor='n',pady=45)
        
        buttonBack = customtkinter.CTkButton(self,hover_color="#222222", text="Back",fg_color=("#111111", "#111111"),corner_radius=15, border_width=0.2, text_color=("white", "white"),command=lambda: controller.show_frame("Menu1"),width=30,height=30)
        
        buttonBack.pack(anchor='w',padx=10)
        
        
        key1=tk.StringVar()
        value1=tk.StringVar()
        
        entry1 = customtkinter.CTkEntry(self,textvariable = key1,fg_color="#111111",border_color="white",text_color=("black", "white"),placeholder_text="...",placeholder_text_color="white",width=250)
        entry1.pack(anchor='center',expand=False,pady=10)
        
        entry2 = customtkinter.CTkEntry(self,textvariable = value1,fg_color="#111111",border_color="white",text_color=("black", "white"),placeholder_text="...",placeholder_text_color="white",width=250)
        entry2.pack(anchor='center',expand=False,pady=10)
        
        
        Add_ChangeWord.configure(self,bg="#111111")   
        
        def add_word(event):
            olex = dict_func()
            olex[key1.get()]=value1.get()
            
            with open(current_path + "/dictionary.txt", "w") as dict_file:
                ins_str = '\n'.join([k+':'+v for k, v in olex.items()])
                dict_file.write(ins_str)
            with open(current_path + "/dictionary.txt") as f:
                for line in f:
                    
                    key, val = line.split(':')
                    olex[key] = val
            key1.set("")
            value1.set("")
        
        def add_word2():
            olex = dict_func()
            olex[key1.get()]=value1.get()
            
            with open(current_path + "/dictionary.txt", "w") as dict_file:
                ins_str = '\n'.join([k+':'+v for k, v in olex.items()])
                dict_file.write(ins_str)
            with open(current_path + "/dictionary.txt") as f:
                for line in f:
                    
                    key, val = line.split(':')
                    olex[key] = val
            key1.set("")
            value1.set("")
        
        entry1.bind("<Return>",add_word)
        entry2.bind("<Return>",add_word)
        
        buttonadd = customtkinter.CTkButton(self,hover_color="#222222", text="Save",fg_color=("#111111", "#111111"), border_width=0.7,
        text_color=("white", "white"),border_color="white",command=add_word2,width=30,height=30)
        
        buttonadd.pack(anchor='n')
        

        
class RemoveWord(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        label = customtkinter.CTkLabel(self,fg_color=("#111111", "#111111"),font=("Lato",40), text="Remove Word",width = 60, height = 30)
        label.pack(anchor='n',pady=45)
        
        buttonBack = customtkinter.CTkButton(self, hover_color="#222222",text="Back",fg_color=("#111111", "#111111"),corner_radius=15, border_width=0.2, text_color=("white", "white"),command=lambda: controller.show_frame("Menu1"),width=30,height=30)
        
        buttonBack.pack(anchor='w',padx=10)

        
        key2 = tk.StringVar()
        
        entry1 = customtkinter.CTkEntry(self,textvariable = key2,fg_color="#111111",border_color="white",text_color=("black", "white"),width=250)
        entry1.pack(anchor='center',expand=False,pady=10)
        
        
        RemoveWord.configure(self,bg="#111111")
        
        def removeword(event):
            with open(current_path + "/dictionary.txt", "r") as f:
                lines = f.readlines()
            with open(current_path + "/dictionary.txt", "w") as f:
                for line in lines:
                    if line.strip("\n").split(':')[0] != key2.get():
                        f.write(line)
            key2.set("")                        

        def removeword2():
            with open(current_path + "/dictionary.txt", "r") as f:
                lines = f.readlines()
            with open(current_path + "/dictionary.txt", "w") as f:
                for line in lines:
                    if line.strip("\n").split(':')[0] != key2.get():
                        f.write(line)
            key2.set("")                        

        entry1.bind("<Return>",removeword)
        
        
        
        buttonRemove = customtkinter.CTkButton(self,hover_color="#222222", text="Remove",fg_color=("#111111", "#111111"),border_color="white", border_width=0.7, text_color=("white", "white"),command=removeword2,width=30,height=30)
        
        buttonRemove.pack(anchor='n')

        


class Lexicon(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        label = customtkinter.CTkLabel(self,fg_color=("#111111", "#111111"),font=("Lato",40), text="Lexicon",text_color="white",width = 60, height = 30)
        label.pack(anchor='n')
        
        
        
        
        # label3 = tk.Message(self,text='',bg="#256D85",fg="white") ne işe yarıyordu bu?? (sildim hiçbir şey değişmedi gibi..)
        # label3.pack()
        
        buttonBack = customtkinter.CTkButton(self,hover_color="#222222", text="Back",fg_color=("#111111", "#111111"),corner_radius=15,border_color="white", border_width=0.2, text_color=("white", "white"),command=lambda: controller.show_frame("Menu1"),width=30,height=30)
        
        buttonBack.pack(anchor='w',padx=10)
        
        Lexicon.configure(self,bg="#111111")
        
        
    
        main_frame = tk.Frame(self,bg="#111111")
        main_frame.pack(fill=BOTH,expand=True)
        my_canvas = tk.Canvas(main_frame,bg="#111111")
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
        
        lexi = tk.Message(second_frame,font=24, bg="#111111",fg="white",text=get_lines2())
        lexi.pack()
        
        
        def get_lines():
            olex = dict_func()
            ins_str = '\n'.join([f'{k:<20} : {v:>40}' for k, v in olex.items()])
            lexi.configure(text=ins_str)
            lexi.pack()
            my_canvas.create_window((0,0),window=second_frame,anchor="nw")
            
            
        buttonRef = customtkinter.CTkButton(self, hover_color="#222222",text="Refresh",fg_color=("#111111", "#111111"),border_color="white", border_width=0.7, text_color=("white", "white"),command=get_lines,width=30,height=30)
        
        buttonRef.pack(anchor='n',pady=10)


class Randomizer(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        label = customtkinter.CTkLabel(self,fg_color=("#111111", "#111111"),font=("Lato",40), text="Randomizer",width = 60, height = 30)
        label.pack(anchor='n',pady=45)
        
        buttonBack = customtkinter.CTkButton(self,hover_color="#222222", text="Back",fg_color=("#111111", "#111111"),border_color="white",corner_radius=15, border_width=0.2, text_color=("white", "white"),command=lambda: controller.show_frame("Menu1"),width=30,height=30)
        
        buttonBack.pack(anchor='w',padx=10)

        Randomizer.configure(self,bg="#111111")   
        
        label_random = customtkinter.CTkLabel(self,fg_color=("#111111", "#111111"),font=("Lato", 32), text="Cards",width = 60, height = 30)
        label_random.pack(anchor='n')
        
        label_random2 = tk.Message(self,font=("Lato",18), text='Meaning',bg="#111111",fg="white", aspect=600)
        label_random2.pack()
        
        
       


        self.v = ""  
        
        
        self.olength = list(dict_func())
        self.slist = list(range(0,len(self.olength)))
        
        def key_randomizer():
            if len(self.olength) == 1:
                self.slist.append(0) 
            label_random2.configure(text =  "")
            self.control = dict_func()
            length = len(self.control)
            if len(self.olength)  == len(self.control):
                
                self.randomval = random.sample(self.slist, 1)[0]
                
                self.slist.remove(self.randomval)
                
                k = list(self.control.keys())[self.randomval]
                label_random.configure(text = k)
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
            label_random2.configure(text =  self.v)
      

        show_key = customtkinter.CTkButton(self,hover_color="#222222", text="   Word   ",fg_color=("#111111", "#111111"),border_color="white", border_width=0.7, text_color=("white", "white"),command=key_randomizer,width=30,height=30)
        
        show_key.pack(anchor='center',side=LEFT,padx=10)    
        
        show_value = customtkinter.CTkButton(self, hover_color="#222222",text="Meaning",fg_color=("#111111", "#111111"),border_color="white", border_width=0.7, text_color=("white", "white"),command=show_meaning,width=30,height=30)
        
        show_value.pack(anchor='center',side=RIGHT,padx=10)

  


if __name__ == "__main__":
    app = SampleApp()
    app.title("")
    app.geometry('600x600')
    app.iconbitmap(current_path + "/Lexi.ico")
    # app.resizable(height = None, width = None)
    
    app.mainloop()
