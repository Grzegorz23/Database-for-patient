import sqlite3
con = sqlite3.connect('Przychodnia.db')
con.row_factory = sqlite3.Row
cur = con.cursor()

def manu(self):
    b=0
    powstanie_tabeli(0)
    while(b==0):
        x=opcje(0)
        if x == '1':
            dodaj(0)
        elif x == '2':
            usun(0)
        elif x == '3':
            wypisywanie_pacjentow(0)
        elif x == '4':
            cur.execute("DROP TABLE IF EXISTS pacjent")
        elif x=='5':
            wybor_pacjenta(0)
        elif x == '6':
            b=1

def dodaj(self,a=[]):
    a.append(input("Pdaj imie pacjenta:\n"))
    a.append(input("Podaj nazwisko:\n"))
    a.append(input("Podaj pesel:\n"))
    a.append(input("Podaj date:\n"))
    a.append(input("Podaj rodzaj badania:\n"))
    a.append(input("Zdjecie analogowe czy cyfrowe:\n"))
    a.append(input("Jaki gabinet:\n"))
    cur.execute('INSERT INTO pacjent VALUES(Null,?,?,?,?,?,?,?);', (a[0], a[1], a[2], a[3], a[4], a[5], a[6]))
    con.commit()
#cur.execute("DROP TABLE IF EXISTS pacjent")
def powstanie_tabeli(self):
    cur.execute("""CREATE TABLE IF NOT EXISTS pacjent (
                id_pacjenta INTEGER PRIMARY KEY AUTOINCREMENT,
                imie TEXT,
                nazwisko TEXT,
                pesel int,
                data int,
                rodzaj_badania TEXT,
                analog_cyfr TEXT,
                gabinet int)""")
def manu_2(self):
    x = input("Wybierz czy chcesz znalesc pacjenta po:\n1. Imieniu\n2. Nazwisku\n3. Peselu\n4. Dacie\n")
    return x
def wybor_pacjenta(self):
    x=manu_2(0)
    if x == "1":
        z = input("Podaj imie:\n")
        cur.execute("""SELECT * FROM pacjent WHERE imie = ?;""",(z,))
        p = cur.fetchall()
        for i in p:
            print((i['id_pacjenta'], i['imie'], i['nazwisko'], i['pesel'], i['data'], i['rodzaj_badania'], i['analog_cyfr'], i['gabinet']))
        if len(p)==0:
            print("Nie ma takiego pacjenta")

    elif x == "2":
        z = input("Podaj nazwisko:\n")
        cur.execute("""SELECT * FROM pacjent WHERE nazwisko=?;""", (z,))
        p = cur.fetchall()
        for i in p:
            print(i['id_pacjenta'], i['imie'], i['nazwisko'], i['pesel'], i['data'], i['rodzaj_badania'],
                  i['analog_cyfr'], i['gabinet'])
        if len(p)==0:
            print("Nie ma takiego pacjenta")

    elif x == "3":
        z = input("Podaj pesel:\n")
        cur.execute("""SELECT * FROM pacjent WHERE pesel=?;""", (z,))
        p = cur.fetchall()
        for i in p:
            print(i['id_pacjenta'], i['imie'], i['nazwisko'], i['pesel'], i['data'], i['rodzaj_badania'],
                  i['analog_cyfr'], i['gabinet'])
        if len(p)==0:
            print("Nie ma takiego pacjenta")

    elif x == "4":
        z = input("Podaj date:\n")
        cur.execute("""SELECT * FROM pacjent WHERE data=?;""", (z,))
        p = cur.fetchall()
        for i in p:
            print(i['id_pacjenta'], i['imie'], i['nazwisko'], i['pesel'], i['data'], i['rodzaj_badania'],
                  i['analog_cyfr'], i['gabinet'])
        if len(p)==0:
            print("Nie ma takiego pacjenta")
def usun(self):
    a = input("Podaj id pacjenta ktorego chcesz usunac")
    cur.execute('DELETE FROM pacjent WHERE id_pacjenta=?;', (a))
    con.commit()
def wypisywanie_pacjentow(self):
    cur.execute(
        """SELECT pacjent.id_pacjenta,imie,nazwisko,pesel,data,rodzaj_badania,analog_cyfr,gabinet FROM pacjent""")
    p = cur.fetchall()
    for i in p:
        print(i['id_pacjenta'], i['imie'], i['nazwisko'], i['pesel'], i['data'], i['rodzaj_badania'], i['analog_cyfr'],
              i['gabinet'])
    print()
def opcje(self):
    a=input("Co chcesz zrobic:\n1. Dodac pacjenta\n2. Usunac pacjenta\n3. Wglad w pacjentow\n4. Skasowac baze\n5. Wybor pacjenta\n6. Koniec\n")
    return a
manu(0)




