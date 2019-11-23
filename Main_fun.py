import sqlite3


con = sqlite3.connect('Przychodnia.db')
con.row_factory = sqlite3.Row
cur = con.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS pacjent (
                id_pacjenta INTEGER PRIMARY KEY AUTOINCREMENT,
                imie TEXT,
                nazwisko TEXT,
                pesel int,
                data int,
                rodzaj_badania TEXT,
                analog_cyfr TEXT,
                gabinet int)""")
def deleta_all_patient():
    cur.execute("DROP TABLE IF EXISTS pacjent")
def add_pacient(list_of_patient_atr):
    cur.execute('INSERT INTO pacjent VALUES(Null,?,?,?,?,?,?,?);',
                (list_of_patient_atr[0],
                 list_of_patient_atr[1],
                 list_of_patient_atr[2],
                 list_of_patient_atr[3],
                 list_of_patient_atr[4],
                 list_of_patient_atr[5],
                 list_of_patient_atr[6]))
    con.commit()
def commit():
    con.commit()
def name_of_patient(name):
    cur.execute("""SELECT * FROM pacjent WHERE imie = ?;""", (name,))
    p = cur.fetchall()
    return p
def id_of_patient(id):
    cur.execute("""SELECT * FROM pacjent WHERE id = ?;""", (id,))
    p = cur.fetchall()
    return p
def surname_of_patient(surname):
    cur.execute("""SELECT * FROM pacjent WHERE nazwisko = ?;""", (surname,))
    p = cur.fetchall()
    return p
def pesel_of_patient(pesel):
    cur.execute("""SELECT * FROM pacjent WHERE pesel = ?;""", (pesel,))
    p = cur.fetchall()
    return p
def delete_patient(id):
    cur.execute('DELETE FROM pacjent WHERE id_pacjenta=?;', (id,))
    con.commit()
def show_all_patient():
    cur.execute(
        """SELECT pacjent.id_pacjenta,imie,nazwisko,pesel,data,rodzaj_badania,analog_cyfr,gabinet FROM pacjent""")
    p = cur.fetchall()
    return p
