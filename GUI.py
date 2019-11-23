from tkinter import *
import tkinter.messagebox
import tkinter.ttk as ttk
#from tkinter.ttk import *
import Main_fun



class PodstawoweManu (ttk.Frame):

    def __init__(self, master=None):
        ttk.Frame.__init__(self, master)

        self.master = master
        self.master.maxsize(400, 260)
        self.master.minsize(400, 260)
        self.master.title("Pacjenci")

        self.pack(fill=BOTH, expand=True)


        self.layout()
    def layout(self):
        global root_01
        title = ttk.Label(self, text="Pancjenci:", style="title.TLabel")
        title.place(x=0, y=0)
        Option_to_do = ["Dodaj pacjenta",
                "Usun pacjenta",
                "Wszyscy pacjenci",
                "Wybór pacjenta",
                "Skasowac baze",
                "Koniec"]
        funkcion = ["addpc",
                    "delpc",
                    "allpc",
                    "selectpc",
                    "dellall",
                    "root_01.destroy"]
        layout_counter = 50
        for i in range(len(Option_to_do)):
            label_01 = ttk.Label(self, text = "{}:".format(Option_to_do[i]), style="label_01.TLabel")
            label_01.place(x=0, y=layout_counter)
            layout_counter+=35
        button_01 = ttk.Button(self, text=Option_to_do[0], style="TButton", command=addpc)
        button_01.place(x=200, y=50)
        button_02 = ttk.Button(self, text=Option_to_do[1], style="TButton", command=delpc)
        button_02.place(x=200, y=85)
        button_03 = ttk.Button(self, text=Option_to_do[2], style="TButton", command=allpc)
        button_03.place(x=200, y=120)
        button_04 = ttk.Button(self, text=Option_to_do[3], style="TButton", command=selectpc)
        button_04.place(x=200, y=155)
        button_05 = ttk.Button(self, text=Option_to_do[4], style="TButton", command=self.dellall)
        button_05.place(x=200, y=190)
        button_06 = ttk.Button(self, text=Option_to_do[5], style="TButton", command=root_01.destroy)
        button_06.place(x=200, y=225)


        # ----------- STYLES ------------
        style = ttk.Style()
        style.configure("TFrame",
                        background="#607D8B"
                        )
        style.configure("title.TLabel",
                        background="#455A64",
                        foreground="#42A5F5",
                        font="Arial 20 bold",
                        width=500,
                        padding=5,
                        )
        style.configure("label_01.TLabel",
                        background="#455A64",
                        foreground="#42A5F5",
                        font="Arial 10 bold",
                        width=500,
                        padding=5
                        )
        style.configure("TButton",
                        relief="flat",
                        background="#455A64",
                        foreground="#455A64",
                        width=30)
        style.map("TButton",
                 foreground=[('pressed', 'blue'), ('active', 'blue')],
                 background=[('pressed', '!disabled', 'black'), ('active', 'white')]
                 )
    """
        self.label_1 = Label(self.window, text="Dodaj pacjenta:")
        self.label_2 = Label(self.window, text="Usun pacjenta:")
        self.label_3 = Label(self.window, text="Wszyscy pacjenci:")
        self.label_4 = Label(self.window, text="Wybór pacjenta:")
        self.label_5 = Label(self.window, text="Skasowac baze:")
        self.label_6 = Label(self.window, text="Koniec:")

        self.button_1 = Button(self.window, text = "Dodaj pacjenta",height = 1, width = 15,command=self.dodajpacjenta)
        self.button_2 = Button(self.window, text = "Usun pacjenta",height = 1, width = 15,command=self.usunpacjenta)
        self.button_3 = Button(self.window, text = "Wszyscy pacjenci",height = 1, width = 15,command=self.wszyscypacjenci)
        self.button_4 = Button(self.window, text = "Wybór pacjenta",height = 1, width = 15,command=self.wyborpacjenta)
        self.button_5 = Button(self.window, text = "Skasowac baze",height = 1, width = 15,command=self.skasowac)
        #****** Wyskakujace okno czy napewno******
        self.button_6 = Button(self.window, text = "Koniec",height = 1, width = 15,command=self.window.quit)

        self.label_1.grid(row=0, sticky=NSEW)
        self.label_2.grid(row=1, sticky=N+S+E+W)
        self.label_3.grid(row=2, sticky=N+S+E+W)
        self.label_4.grid(row=3, sticky=N+S+E+W)
        self.label_5.grid(row=4, sticky=N+S+E+W)
        self.label_6.grid(row=5, sticky=N+S+E+W)

        self.button_1.grid(row=0, column=1,sticky=N+S+E+W)
        self.button_2.grid(row=1, column=1,sticky=N+S+E+W)
        self.button_3.grid(row=2, column=1,sticky=N+S+E+W)
        self.button_4.grid(row=3, column=1,sticky=N+S+E+W)
        self.button_5.grid(row=4, column=1,sticky=N+S+E+W)
        self.button_6.grid(row=5, column=1,sticky=N+S+E+W)

    """
    def dodajpacjenta(self):
        addpc()
    def usunpacjenta(self):
        self.usun_pacjenta = UsunPacjenta(self.window)
    def wszyscypacjenci(self):
        self.wszyscy_pacjenci = WszyscyPacjenci(self.window)
    def wyborpacjenta(self):
        self.wybor_pacjenta = WyborPacjenta(self.window)
    def dellall(self):
        answer = tkinter.messagebox.askquestion('','Czy na pewno chcesz skasowac baze!')
        if answer == 'yes':
            Main_fun.deleta_all_patient()

    def loop(self):
        self.window.mainloop()

class DodawaniePacjentow(ttk.Frame):

    def __init__(self, master=None):
        ttk.Frame.__init__(self, master)

        self.master = master
        self.master.maxsize(400, 285)
        self.master.minsize(400, 285)
        self.master.title("Dodawanie pacjentow")

        self.pack(fill=BOTH, expand=True)

        self.layout()

    def layout(self):
        title = ttk.Label(self, text="Dane pacjenta:", style="title.TLabel")
        title.place(x=0, y=0)

        label_list = ["Podaj Imie",
                      "Podaj Nazwisko",
                      "Podaj Pesel",
                      "Podaj Date",
                      "Podaj rodzaj badania",
                      "Jakie zdjecie",
                      "Podaj gabinet"]
        layout_counter = 50
        for i in label_list:
            label_01 = ttk.Label(self, text="{}:".format(i), style="label_01.TLabel")
            enrty_01 = ttk.Entry(self,width=35)
            label_01.place(x=0, y=layout_counter)
            enrty_01.place(x=160,y=layout_counter)
            layout_counter +=30
        button_1 = ttk.Button(self, text="OK", style="TButton")
        button_1.place(x=0,y=layout_counter)
        # ----------- STYLES ------------
        style = ttk.Style()
        style.configure("TFrame",
                        background="#607D8B"
                        )
        style.configure("title.TLabel",
                        background="#455A64",
                        foreground="#42A5F5",
                        font="Arial 20 bold",
                        width=500,
                        padding=5,
                        )
        style.configure("label_01.TLabel",
                        background="#455A64",
                        foreground="#42A5F5",
                        font="Arial 10 bold",
                        width=500,
                        padding=5
                        )
        style.configure("TButton",
                        relief="flat",
                        background="#455A64",
                        foreground="#455A64",
                        width=65)
        style.map("TButton",
                  foreground=[('pressed', 'blue'), ('active', 'blue')],
                  background=[('pressed', '!disabled', 'black'), ('active', 'white')]
                  )
    """
        self.label_1 = Label(frame_2,text="Podaj Imie")
        self.label_2 = Label(frame_2,text="Podaj Nazwisko")
        self.label_3 = Label(frame_2,text="Podaj Pesel")
        self.label_4 = Label(frame_2,text="Podaj Date")
        self.label_5 = Label(frame_2,text="Podaj rodzaj badania")
        self.label_6 = Label(frame_2,text="Jakie zdjecie")
        self.label_7 = Label(frame_2,text="Podaj gabinet")

        self.entry_1 = Entry(frame_2, width = 20)
        self.entry_2 = Entry(frame_2, width = 20)
        self.entry_3 = Entry(frame_2, width = 20)
        self.entry_4 = Entry(frame_2, width = 20)
        self.entry_5 = Entry(frame_2, width = 20)
        self.entry_6 = Entry(frame_2, width = 20)
        self.entry_7 = Entry(frame_2, width = 20)

        #self.button_1 = Button(frame_2, text="Analog", height = 1, width = 7)
        #self.button_2 = Button(frame_2, text="Cyfrowka", height = 1, width = 7)
        self.button_3 = Button(frame_2, text="OK", width=20,command=self.dodawanie)


        self.label_1.grid(row=0, sticky=W)
        self.label_2.grid(row=1, sticky=W)
        self.label_3.grid(row=2, sticky=W)
        self.label_4.grid(row=3, sticky=W)
        self.label_5.grid(row=4, sticky=W)
        self.label_6.grid(row=5, sticky=W)
        self.label_7.grid(row=6, sticky=W)

        self.entry_1.grid(row=0, column=1, columnspan=2)
        self.entry_2.grid(row=1, column=1, columnspan=2)
        self.entry_3.grid(row=2, column=1, columnspan=2)
        self.entry_4.grid(row=3, column=1, columnspan=2)
        self.entry_5.grid(row=4, column=1, columnspan=2)
        self.entry_6.grid(row=5, column=1, columnspan=2)
        self.entry_7.grid(row=6, column=1, columnspan=2)

        #self.button_1.grid(row=4,column=1)
        #self.button_2.grid(row=4,column=2)
        self.button_3.grid(row=7, columnspan=3)
    """
    def dodawanie(self):
        patient_atr=[]
        patient_atr.append(self.entry_1.get())
        patient_atr.append(self.entry_2.get())
        patient_atr.append(self.entry_3.get())
        patient_atr.append(self.entry_4.get())
        patient_atr.append(self.entry_5.get())
        patient_atr.append(self.entry_6.get())
        patient_atr.append(self.entry_7.get())

        Main_fun.add_pacient(patient_atr)
        self.master.destroy()
class WyborPacjenta:

    def __init__(self,parent):

        self.master = Toplevel(parent)
        self.master.title('Program')
        self.master.resizable(0, 0)

        frame = Frame(self.master)
        frame.pack()

        self.label_1 = Label(frame,text="Po czym chcesz szukac pacjenta")

        self.button_1 = Button(frame,text="ID",width=20,command=self.id)
        self.button_2 = Button(frame, text="Imie", width=20,command=self.imie)
        self.button_3 = Button(frame, text="Nazwisko", width=20,command=self.nazwisko)
        self.button_4 = Button(frame, text="Pesel", width=20,command=self.pesel)

        self.label_1.grid(row=0)
        self.button_1.grid(row=1)
        self.button_2.grid(row=2)
        self.button_3.grid(row=3)
        self.button_4.grid(row=4)

    def id(self):
        self.i_d = ID(self.master)
        Main_fun.commit()
        #self.master.destroy()
    def imie(self):
        self.imie = Imie(self.master)
        Main_fun.commit()
        #self.master.destroy()
    def nazwisko(self):
        self.nazwisko = Imie(self.master)
        Main_fun.commit()
        #self.master.destroy()
    def pesel(self):
        self.pesel= Pesel(self.master)
        Main_fun.commit()
        #self.master.destroy()
class Imie:

    def __init__(self,parent):

        self.master = Toplevel(parent)
        self.master.title('Program')
        self.master.resizable(0, 0)

        frame = Frame(self.master)
        frame.pack()

        self.label=Label(frame,text="Podaj imie")

        self.enter=Entry(frame)

        self.button=Button(frame,text="OK",width=20,command=self.wyswietl_imie)

        self.label.grid(row=0)

        self.enter.grid(row=0,column=1)

        self.button.grid(row=1,columnspan=2)

    def wyswietl_imie(self):
        name_entry_get = self.enter.get()
        patient_data = Main_fun.name_of_patient(name_entry_get)
        Wyswietlacz(self.master,patient_data)
        Main_fun.commit()
        #self.master.destroy()
class ID:

    def __init__(self,parent):

        self.master = Toplevel(parent)
        self.master.title('Program')
        self.master.resizable(0, 0)
        frame = Frame(self.master)
        frame.pack()

        self.label=Label(frame,text="Podaj ID")

        self.enter=Entry(frame)

        self.button=Button(frame,text="OK",width=20,command=self.wyswietl_id)

        self.label.grid(row=0)

        self.enter.grid(row=0,column=1)

        self.button.grid(row=1,columnspan=2)

    def wyswietl_id(self):
        name_entry_get = self.enter.get()
        patient_data = Main_fun.id_of_patient(name_entry_get)

        Wyswietlacz(self.master, patient_data)
        Main_fun.commit()
        #self.master.destroy()
class Nazwisko:

    def __init__(self,parent):
        self.master = Toplevel(parent)
        self.master.title('Program')
        self.master.resizable(0, 0)
        frame = Frame(self.master)
        frame.pack()

        self.label=Label(frame,text="Podaj nazwisko")

        self.enter=Entry(frame)

        self.button=Button(frame,text="OK",width=20,command=self.wyswietl_nazwisko)

        self.label.grid(row=0)

        self.enter.grid(row=0,column=1)

        self.button.grid(row=1,columnspan=2)
    def wyswietl_nazwisko(self):
        surname_entry_get = self.enter.get()
        patient_data=Main_fun.surname_of_patient(surname_entry_get)

        Wyswietlacz(self.master,patient_data)

        Main_fun.commit()
        #self.master.destroy()
class Pesel:

    def __init__(self,parent):
        self.master = Toplevel(parent)
        self.master.title('Program')
        self.master.resizable(0, 0)

        frame = Frame(self.master)
        frame.pack()

        self.label=Label(frame,text="Podaj Pesel")

        self.enter=Entry(frame)

        self.button=Button(frame,text="OK",width=20,command=self.wyswietl_pesel)

        self.label.grid(row=0)

        self.enter.grid(row=0,column=1)

        self.button.grid(row=1,columnspan=2)

    def wyswietl_pesel(self):
        pesel_entry_get= self.enter.get()

        patient_data=Main_fun.pesel_of_patient(pesel_entry_get)

        b = Wyswietlacz(self.master,patient_data)
        Main_fun.commit()
        #self.master.destroy()
class UsunPacjenta:

    def __init__(self,parent):
        self.master = Toplevel(parent)
        self.master.title('Program')
        self.master.resizable(0, 0)
        frame =Frame(self.master)
        frame.pack()

        self.lable=Label(frame,text="Podaj ID pacjenta ktorego chcesz usunac")

        self.button=Button(frame,text="OK",width=20,command=self.usun)
        self.entry=Entry(frame)

        self.lable.grid(row=0)
        self.button.grid(row=1,columnspan=2)
        self.entry.grid(row=0,column=1)

    def usun(self):
        id_entry_get = self.entry.get()
        Main_fun.delete_patient(id_entry_get)
        self.master.destroy()
class WszyscyPacjenci:

    def __init__(self,parent):
        self.master = Toplevel(parent)
        self.master.title('Program')
        self.master.geometry('400x300')
        self.master.resizable(0, 0)
        frame = Frame(self.master)
        frame.pack(fill=BOTH,expand=1)

        listbox=Listbox(frame)
        """
        tv=tree(frame)
        tv['colums']=('Id','Imie','Nazwisko','Pesel','Data','Rodzaj badania','analog/cyfra','Gabinet')

        tv.heading('Id',text='Id')
        tv.column('Id',anchor='center',width=100)

        tv.heading('Imie', text='Imie')
        tv.column('Imie', anchor='center', width=100)

        tv.heading('Nazwisko', text='Nazwisko')
        tv.column('Nazwisko', anchor='center', width=100)

        tv.heading('Pesel', text='Pesel')
        tv.column('Pesel', anchor='center', width=100)

        tv.heading('Data', text='Data')
        tv.column('Data', anchor='center', width=100)

        tv.heading('Rodzaj badania', text='Rodzaj badania')
        tv.column('Rodzaj badania', anchor='center', width=100)

        tv.heading('analog/cyfra', text='analog/cyfra')
        tv.column('analog/cyfra', anchor='center', width=100)

        tv.heading('Gabinet', text='Gabinet')
        tv.column('Gabinet', anchor='center', width=100)
        """
        scrollbar =Scrollbar(frame)
        scrollbar.pack(side=RIGHT,fill=Y)
        listbox.pack(fill=BOTH,expand=1)

        all_patient_data=Main_fun.show_all_patient()



        for i in all_patient_data:
            listbox.insert(END, (i['id_pacjenta'], i['imie'], i['nazwisko'], i['pesel'], i['data'], i['rodzaj_badania'],
                  i['analog_cyfr'],
                  i['gabinet']))
class Wyswietlacz:
    def __init__(self,parent,napis):
        self.master = Toplevel(parent)
        self.master.title('Program')
        self.master.geometry('400x300')
        self.master.resizable(0, 0)
        frame = Frame(self.master)
        frame.pack(fill=BOTH,expand=1)

        self.listbox=Listbox(frame)

        self.scrollbar =Scrollbar(frame)
        self.scrollbar.pack(side=RIGHT,fill=Y)
        self.listbox.pack(fill=BOTH,expand=1)

        if len(napis)==0:
            self.listbox.insert(END,"Niema takiego pacjenta")
        else:
            for i in napis:
                self.listbox.insert(END,(i['id_pacjenta'], i['imie'], i['nazwisko'], i['pesel'], i['data'], i['rodzaj_badania'],
                     i['analog_cyfr'], i['gabinet']))


def main():
    global root_01
    root_01 = Tk()

    app_01 = PodstawoweManu(root_01)
    root_01.mainloop()

def addpc():
    global root_01
    root_01.destroy()
    root_02 = Tk()
    app_02 = DodawaniePacjentow(root_02)
    root_02.mainloop()
def delpc():
    global root_01
    root_01.destroy()
    root_03 = Tk()
    app_03 = UsunPacjenta(root_03)
    root_03.mainloop()
def allpc():
    global root_01
    root_01.destroy()
    root_04 = Tk()
    app_04 = WszyscyPacjenci(root_04)
    root_04.mainloop()
def selectpc():
    global root_01
    root_01.destroy()
    root_05 = Tk()
    app_05 = WyborPacjenta(root_05)
    root_05.mainloop()
if __name__ == "__main__":
    main()





