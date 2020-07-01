import sqlite3

class Database:
    def __init__(self):
        self.conn=sqlite3.connect("books.db")
        self.cur=self.conn.cursor()
        self.cur.execute("create table if not exists book (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)" )
        self.conn.commit()
        
    



    def insert(self,title,author,year,isbn):
 
        self.cur.execute("insert into book values (NULL,?,?,?,?)",(title,author,year,isbn) )
        self.conn.commit()
       

    def view(self):

        self.cur.execute("select * from book")
        rows=self.cur.fetchall()
        
        return rows

    def search(self,title="", author="", year="", isbn=""):

        self.cur.execute("select * from book where title =? or author =? or year = ? or isbn=?",(title, author, year, isbn))
        rows=self.cur.fetchall()
       
        return rows

    def delete(self,id):

        self.cur.execute("delete from book where id = ?",(id,))
        self.conn.commit()
        

    def update(self,title,author,year,isbn,id):

        self.cur.execute("Update book set title=?, author=?, year=?, isbn=? where id =?",(title,author,year,isbn,id))
        self.conn.commit()
        
    def __del__():
        self.conn.close()

    


#connect()
#insert("the nature","nich smith","1947","4535628")
#delete(5)
#print(search(author="nicholas "))
#update(6,"the new title","the new author","the new year","the new isbn")
#print( view())


