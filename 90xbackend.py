import sqlite3

def connect():
        conn = sqlite3.connect("books.db")
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, city text, state text, log integer, lat integer)")
        conn.commit()
        conn.close()
        
def insert(city, state, log, lat):
        conn = sqlite3.connect("books.db")
        cur = conn.cursor()
        cur.execute("INSERT INTO book VALUES (NULL,?,?,?,?)",(city,state,log,lat))
        conn.commit()
        conn.close()
        

def view():
       conn = sqlite3.connect("books.db")
       cur = conn.cursor()
       cur.execute("SELECT * FROM book")
       rows = cur.fetchall()
       conn.close()
       return rows

def search(city='',state='',log='',lat=''):
       conn = sqlite3.connect("books.db")
       cur = conn.cursor()
       cur.execute('SELECT * FROM book WHERE city=? OR state=? OR log=? OR lat=?',(city,state,log,lat))
       rows = cur.fetchall()
       conn.close()
       return rows

def delete(id):
        conn = sqlite3.connect("books.db")
        cur = conn.cursor()
        cur.execute('DELETE FROM book WHERE id=?',(id,))
        conn.commit()
        conn.close()

def update(id,city,state,log,lat):
        conn = sqlite3.connect("books.db")
        cur = conn.cursor()
        cur.execute("UPDATE book SET city=?,state=?,log=?,lat=? WHERE id=?",(city,state,log,lat,id))
        conn.commit()
        conn.close()


connect()

#insert('toledo','ohio',2014,2)
#delete(4)
#update(2,'Cleveland','OH',81.6944,41.4993)
#print(view())
#print(search(author='hbk'))
