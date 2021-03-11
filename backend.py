import sqlite3

def connect():
    conn = sqlite3.connect("ms.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS movies(id INTEGER PRIMARY KEY, title text UNIQUE NOT NULL,director text NOT NULL,year INTEGER NOT NULL,imdb float NOT NULL)")
    #cur.execute("drop table movies")
    conn.commit()
    conn.close()

def insert(title,director,year,imdb):
    try:
        conn = sqlite3.connect("ms.db")
        cur = conn.cursor()
        cur.execute("insert into movies values(NULL,?,?,?,?)",(title,director,year,imdb))    
        conn.commit()
        conn.close()
    except:
        pass

def view():
    conn = sqlite3.connect("ms.db")
    cur = conn.cursor()
    cur.execute("select * from movies")
    rows = cur.fetchall()
    conn.close()
    return rows

def search(title="",director="",year="",imdb=""):
    conn = sqlite3.connect("ms.db")
    cur = conn.cursor()
    cur.execute("select * from movies where title=? or director=? or year=? or imdb=?",(title,director,year,imdb))
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn = sqlite3.connect("ms.db")
    cur = conn.cursor()
    cur.execute("delete from movies where id=?",(id,))
    conn.commit()
    conn.close()

def update(id,title,director,year,imdb):
    conn = sqlite3.connect("ms.db")
    cur = conn.cursor()
    cur.execute("update movies set title=?, director=?, year=?, imdb=? where id=?",(title,director,year,imdb,id))
    conn.commit()
    conn.close()


connect()
#insert("Ant man","Sam reimi",2016,7)
#delete(1)
#update(2,"shahryar","tayeb",2017,21365489) 
#print(view())
#print(search(year=2018))
